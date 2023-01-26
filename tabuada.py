tabuada = int(input("Digite um numero para exibir a tabuada: "))

print(f'===== RESULTADO DA TABUADA {tabuada} =====')
for valor in range (1,11,1):
    print(f'{tabuada} x {valor} = {tabuada*valor}')
print('----------------------------')