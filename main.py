import random

def par_impar(x):
  if x % 2 == 0:
    return "PAR"
  else:
    return "IMPAR"

def maior_menor(x, y):
  if x > y:
    return "MENOR"
  elif x < y:
    return "MAIOR"

num_aleatorio = random.randint(1, 100)
num_usuario = 0

print("----- JOGO DE ADVINHAÇÃO -----")
print(f"DICA: É um número {par_impar(num_aleatorio)}")

while num_usuario != num_aleatorio:
  num_usuario = int(input("\nInsira um número inteiro entre 1 e 100: "))
  if num_usuario != num_aleatorio:
    print(f"Número INCORRETO! Tente novamente.\nDICA: Escolha um número {maior_menor(num_usuario, num_aleatorio)}.")

print(f"\nSUCESSO! {num_usuario} é o número CORRETO!")