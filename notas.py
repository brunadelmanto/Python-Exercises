# entrada de dados
nota1 = input('Digite a nota 1 do aluno:')
nota2 = input("Digite a nota 2 do aluno:")

# converção de string para float
n1 = eval(nota1)
n2 = eval(nota2)

# calculo
mediaFinal = 0.4 * n1 + 0.6 * n2

# condição
if mediaFinal >= 5:
    print('Aluno aprovado com média final de', mediaFinal)
else:
    print('Aluno reprovado com média final de', mediaFinal)


