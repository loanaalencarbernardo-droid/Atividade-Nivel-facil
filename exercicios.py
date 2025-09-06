# Exercícios propostos

# 1. Listas: Crie uma lista com os números de 1 a 5 e imprima cada elemento.
lista_numeros = [1, 2, 3, 4, 5]
print("Lista de números de 1 a 5:")
for num in lista_numeros:
    print(num)

# 2. Condicionais: Peça um número ao usuário e verifique se é positivo, negativo ou zero.
num_usuario = int(input("Digite um número: "))
if num_usuario > 0:
    print("O número é positivo.")
elif num_usuario < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# 3. Laços: Use um loop for para imprimir os números de 1 a 10.
print("Números de 1 a 10:")
for i in range(1, 11):
    print(i)

# 4. Dicionários: Crie um dicionário com nomes e idades de 3 pessoas e imprima cada par.
pessoas = {
    "Ana": 25,
    "Bruno": 30,
    "Carlos": 22
}
print("Nomes e idades:")
for nome, idade in pessoas.items():
    print(f"{nome}: {idade} anos")

# 5. Funções: Crie uma função que recebe dois números e retorna a soma.
def soma(a, b):
    return a + b

print("Soma de 3 + 7 =", soma(3, 7))

# 6. Strings: Peça uma palavra ao usuário e imprima o número de caracteres.
palavra = input("Digite uma palavra: ")
print(f"A palavra '{palavra}' tem {len(palavra)} caracteres.")

# 7. Listas: Crie uma lista com 3 frutas e adicione uma nova fruta.
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")
print("Lista de frutas:", frutas)

# 8. Condicionais: Verifique se um número é par ou ímpar.
num_paridade = int(input("Digite um número para verificar se é par ou ímpar: "))
if num_paridade % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 9. Laços: Use um loop while para imprimir números de 1 a 5.
print("Números de 1 a 5 com while:")
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# 10. Dicionários: Crie um dicionário de produtos e preços, depois imprima apenas os produtos.
produtos = {
    "arroz": 5.50,
    "feijão": 7.20,
    "macarrão": 4.00
}
print("Produtos disponíveis:")
for produto in produtos.keys():
    print(produto)