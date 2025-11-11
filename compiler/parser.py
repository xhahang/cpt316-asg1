class SyntaxError(Exception):
    pass

class Parser:
    def __init__(self,tokens):
        self.tokens = tokens # list of tuples (token type, token value, position)
        self.position = 0

    # return current token the parser is looking at
    def current(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        else:
            return None

    # consume token if it matches expected token type
    def match(self, expected_type=None , expected_value=None):
        token = self.current()
        if token is None:
          if expected_type == 'TERMINATOR':
              raise SyntaxError("SyntaxError at end of input: missing ';'")
          else:
              raise SyntaxError(f"SyntaxError at end of input: missing {expected_value or 'type'}")

        if expected_type and token[0] != expected_type:
            raise SyntaxError(f"SyntaxError at position {token[2]+1}: expected {expected_value or expected_type} before '{token[1]}'")

        if expected_value and token[1] != expected_value:
            raise SyntaxError(f"SyntaxError at position {token[2]+1}: expected '{expected_value}'before '{token[1]}'")
        # advance parser to next token and return matched token
        self.position += 1
        return token

    # Grammar of COMPY Compiler
    # <stmt> → id = <expr> ;
    def stmt(self):
        node ={'type':'stmt', 'children':[]}

        idtoken = self.match('IDENTIFIER')
        node['children'].append({'type': 'id', 'value': idtoken[1], 'pos': idtoken[2]})

        self.match('ASSIGNMENT')
        expr_node = self.expr()
        node['children'].append(expr_node)

        if not self.current() or self.current()[0] != 'TERMINATOR':
            raise SyntaxError("SyntaxError at end of input: missing ';'")
        self.match('TERMINATOR')
        return node

    # <expr> → <term> | <expr> ‘+’ <term> | <expr> ‘-’ <term>
    def expr(self):
        left = self.term()
        while self.current() and self.current()[0] == 'OPERATOR' and self.current()[1] in ('+', '-'):
            optoken = self.match('OPERATOR')
            right = self.term()
            left = {'type': 'binop', 'op': optoken[1], 'left': left, 'right': right, 'pos': optoken[2]}
        return left

    # <term> → <factor> | <term> ‘*’ <factor> | <term> ‘/’ <factor>
    def term(self):
        left = self.factor()
        while self.current() and self.current()[0] == 'OPERATOR' and self.current()[1] in ('*', '/'):
            optoken = self.match('OPERATOR')
            right = self.factor()
            left = {'type': 'binop', 'op': optoken[1], 'left': left, 'right': right, 'pos': optoken[2]}
        return left

    # <factor> → id | int | ( <expr> )
    def factor(self):
        token = self.current()
        if token is None:
            raise SyntaxError("SyntaxError at end of input: unexpected end in factor")

        if token[0] == 'IDENTIFIER':
            self.match('IDENTIFIER')
            return {'type': 'id', 'value': token[1], 'pos': token[2]}
        elif token[0] == 'NUMBER':
            self.match('NUMBER')
            return {'type': 'num', 'value': token[1], 'pos': token[2]}
        elif token[0] == 'PARENTHESES' and token[1] == '(':
            self.match('PARENTHESES', '(')
            expr_node = self.expr()

            if not self.current() or self.current()[0] != 'PARENTHESES' or self.current()[1] != ')':
                next_token = self.current()
                next_char = next_token[1] if next_token else 'end of input'
                raise SyntaxError(f"SyntaxError at position {token[2]+1}: expected ')' before '{next_char}'")
            self.match('PARENTHESES', ')')
            return expr_node
        else:
            raise SyntaxError(f"SyntaxError at position {token[2]+1}: unexpected token '{token[1]}' in factor")
