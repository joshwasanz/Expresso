from frontend.lexer import tokenize

def Expresso():
    print("\n🍵 Expresso v0.1")

    while True:
        input_str = input("-> ")

        if not input_str or "exit" in input_str:
            exit(1)

        response = tokenize(input_str)
        n = len(response) - 1
        print(response[:n])

Expresso()