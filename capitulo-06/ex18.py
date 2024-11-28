frase = list(input("Digite uma frase: "))
lista_de_caracteres = [char for char in frase if char != ' ']

print("Lista de Caracteres = ", lista_de_caracteres)

char_dict = {}
counter = 0

for index, char in enumerate(lista_de_caracteres):
    if char in char_dict:
        char_dict[char].append(index)
    else:
        char_dict[char] = [index]

print(char_dict)
