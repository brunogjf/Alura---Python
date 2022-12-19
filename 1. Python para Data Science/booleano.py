idades = [18, 22, 15, 50]

def verificar (idades):
    for idade in idades:   
        if idade >= 18: 
            print('Pode dirigir')
        else:
            print('Não pode dirigir')
verificar(idades)