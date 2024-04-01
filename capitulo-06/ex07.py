pilha = []

expressão = list(input("Digite a expressão com parenteses: "))

index = 0

while index < len(expressão):
    if expressão[index] == "(":
        pilha.append(expressão[index])
        index += 1
    else:
        pilha.pop(-1)
        index += 1

if len(pilha) == 0:
    print("Expressão correta - OK")
else:
    print("Expressão incorreta - Erro ")
