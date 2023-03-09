# entrada de dados pelo usuário
altura = input('Digite a sua altura: ')
sexo = input('Digite o seu sexo (h para homem e m para mulher): ')

# converte o input string para float
alt = eval(altura)

# estrutura de condição
if sexo == 'h':
    peso = (22.7 * alt) - 58
else:
    peso = (62.1 * alt) - 44.7

print('O peso ideal é: ', peso)
