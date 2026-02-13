maior_altura = 0
menor_altura = 0
soma_altura_homens = 0
qtd_homens = 0
qtd_mulheres = 0

for i in range(15):
    altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
    genero = input(f"Digite o gênero da pessoa {i+1} (M para Masculino, F para Feminino): ").upper()

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

print("\nResultados:")
print("Maior altura:", maior_altura)
print("Menor altura:", menor_altura)

if qtd_homens > 0:
    media_homens = soma_altura_homens / qtd_homens
    print("Média de altura dos homens:", media_homens)
else:
    print("Nenhum homem registrado.")

print("Número de mulheres:", qtd_mulheres)