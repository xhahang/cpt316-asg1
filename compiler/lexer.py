import re

# define tokens following COMPY Language Specification
TOKEN_SPECIFICATION =[
    ('IDENTIFIER', r'[a-z]'),
    ('NUMBER', r'\d+'),
    ('OPERATOR', r'[+\-*/]'),
    ('ASSIGNMENT', r'='),
    ('PARENTHESES', r'[\(\)]'),
    ('TERMINATOR', r';'),
    ('SKIP', r'[ \t\n]+'),
    ('INVALID', r'.'),
]

# Custom error class
class LexicalError(Exception):
    pass

# lexical analyzer
def lexer(code):
  tokens = [] # hold token type, token value and position
  invalid_tokens = [] # hold token value and position

  # regex to match tokens
  token_regex = '|'.join(f'(?P<{token_type}>{pattern})' for token_type, pattern in TOKEN_SPECIFICATION)

  print("\nLEXICAL ANALYSIS")
  print("-" * 45)
  print(f"{'Token Type':<15} | {'Token Value':<12}")
  print("-" * 45)

  # tokenize input
  # use finditer() to find all matches in input code at once
  for match in re.finditer(token_regex, code):
    token_type = match.lastgroup
    token_value = match.group()
    position = match.start()

    if token_type == 'SKIP':
        continue

    # We want to print all tokens in token stream including invalid ones
    print(f"{token_type:<15} | {token_value:^12}")

    # but colllect valid tokens only
    if token_type != 'INVALID':
        tokens.append((token_type, token_value, position))
    else:
        invalid_tokens.append((token_value, position))

  print("-" * 45)
  print("\nTOKEN COUNT SUMMARY (Valid Tokens Only)")
  print("-" * 45)
  print(f"{'Token Type':<15} | {'Count'}")
  print("-" * 45)

  #token counts
  counts = {}
  total = 0
  for token_type, _,_ in tokens:
      counts[token_type] = counts.get(token_type, 0) + 1
      total += 1
  for k, v in counts.items():
      print(f"{k:<15} | {v}")
  print("-" * 45)
  print(f"{'TOTAL':<15} | {total}")
  print("-" * 45)

  # Raise lexical error when there is invalid token
  if invalid_tokens:
    print(f"\nTOTAL INVALID TOKENS: {len(invalid_tokens)}")
    for token_value, position in invalid_tokens:
      print(f"LexicalError at position {position+1}: invalid character '{token_value}'")
    raise LexicalError("PARSING STOPPED DUE TO LEXICAL ERROR.")

  print("\nLexical analysis completed successfully!")
  return tokens