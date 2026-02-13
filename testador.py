import random
import time

print("Iniciando teste automatizado...\n")

maior_altura = 0
menor_altura = 0
soma_altura_homens = 0
qtd_homens = 0
qtd_mulheres = 0

for i in range(15):
    # Gerando dados aleatórios para teste
    altura = round(random.uniform(1.50, 2.30), 2)
    genero = random.choice(['M', 'F'])

    print(f"--- Pessoa {i+1} ---")
    print(f"Altura gerada: {altura}")
    print(f"Gênero gerado: {genero}")
    time.sleep(0.1) # Pequena pausa para visualização

    # Mesma lógica do programa original
    if i == 0:
        maior_altura = altura
        menor_altura = altura
    else:
        if altura > maior_altura:
            maior_altura = altura
        if altura < menor_altura:
            menor_altura = altura

    if genero == 'M':
        soma_altura_homens = soma_altura_homens + altura
        qtd_homens = qtd_homens + 1
    elif genero == 'F':
        qtd_mulheres = qtd_mulheres + 1

print("\n------------------------------")
print("RESULTADOS DO TESTE")
print("------------------------------")
print("Maior altura:", maior_altura)
print("Menor altura:", menor_altura)

if qtd_homens > 0:
    media_homens = soma_altura_homens / qtd_homens
    print(f"Média de altura dos homens: {media_homens:.2f}")
else:
    print("Nenhum homem registrado.")

print("Número de mulheres:", qtd_mulheres)
