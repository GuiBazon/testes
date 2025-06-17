import time
import random
import os
import shutil

print('Olá, mundo!')

escolha = input('Escolha um número de 1 a 6: ')
numero = random.randint(1, 6)

if int(escolha) == numero:
    time.sleep(3)
    print('Sorte em pae')
    time.sleep(3)
else:
    time.sleep(3)
    print('Ops! Você errou. Uma pasta será deletada... (simulação)')
    time.sleep(5)

    # Cria uma pasta temporária só para exemplo (seguro)
    pasta_teste = "pasta_teste_lixo"
    os.makedirs(pasta_teste, exist_ok=True)
    print(f'Pasta "{pasta_teste}" criada para demonstração.')

    # Deleta a pasta temporária (seguro)
    shutil.rmtree(pasta_teste)
    print(f'Pasta "{pasta_teste}" foi deletada! (apenas demonstração)')