#distância=100m; tempo=20seg vm? vm=deltaS/deltat
distancia =int(input('Qual a distancia? '))
tempo = int(input('Qual o tempo gasto? '))

def velocidade():
    vm = distancia/tempo
    print(f'A velocidade média é de {vm} m/s')

velocidade()