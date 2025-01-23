from enum import Enum, auto
from typing import List, Dict

class TokenType(Enum):
    Number = auto()
    Identifier = auto()
    String = auto()
    Let = auto()
    Const = auto()
    Equals = auto()
    OpenParen = auto()
    CloseParen = auto()
    BinaryOperator = auto()
    EOF = auto()

KEYWORDS:Dict[str, TokenType] = {
    "let":TokenType.Let,
    "const":TokenType.Const
}


class Token:
    def __init__(self,value:str,type:TokenType):
        self.value = value
        self.type = type

    def __repr__(self):
        return f"Token (value = '{self.value}', type = {self.type})"
    
#utility functions

def is_alpha(char:str) -> bool:
    return char.isalpha()

def is_skippable(char:str) -> bool:
    return char in (" ", "\n", "\t")

def is_int(char:str) -> bool:
    return char.isdigit()


#main function to tokenize the source code

def tokenize(source_code:str)->List[Token]:
    
    tokens = []
    src = list(source_code)

    while src:
        char = src[0]

        #check single character tokens
        if char == "(":
            tokens.append(Token(src.pop(0), TokenType.OpenParen))
        elif char == ")":
            tokens.append(Token(src.pop(0),TokenType.CloseParen))
        elif char == "=":
            tokens.append(Token(src.pop(0),TokenType.Equals))
        elif char in {"+", "-"}:
            tokens.append(Token(src.pop(0),TokenType.BinaryOperator))
        elif char in {"*", "/","%"}:
            tokens.append(Token(src.pop(0),TokenType.BinaryOperator))

        #check multicharcter tokens 

        elif is_int(char): #numeric literals 
            num = ""

            while src and is_int(src[0]):
                num += src.pop(0)
            tokens.append(Token(num,TokenType.Number))

        elif is_alpha(char):  # identifier or keywords
            ident = ""

            while src and (is_alpha(src[0]) or src[0].isdigit()):
                ident += src.pop(0)
                
                #check if identifers is a reserved keyword
            token_type = KEYWORDS.get(ident,TokenType.Identifier)
            tokens.append(Token(ident,token_type))
        
        elif is_skippable(char):
            src.pop(0)
        
        else:
            print(f"Unrecognized character found in source: {char}")
            exit(1)

    tokens.append(Token("END OF FILE",TokenType.EOF))
    return tokens


if __name__ == "__main__":
    source = "let x = 45"

    for token in tokenize(source):
        print(token)