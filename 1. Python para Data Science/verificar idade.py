idade = input('Qual a sua idade? ')
idade = int(idade)
def idade_sem_parametro():
    if idade >=18:
        print('Você pode dirigir')
    else:
        print('Você não pode dirigir')
idade_sem_parametro()