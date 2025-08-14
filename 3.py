#3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. #

sexo = input('digite o sexo (F ou M):').strip().lower()
if sexo =='f':
    print('FEMININO')
elif sexo =='m':
    print('MASCULINO')
else:
    print('entrada inválida!')