from lex import *

def main():
    input = "+- \"This is a string\" # This is a comment!\n */"
    lexer = Lexer(input)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()