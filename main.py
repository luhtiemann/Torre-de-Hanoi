def torrehanoi(disco, origem, destino, auxiliar):
  if disco == 1:
    print('Mover disco {} da torre {} para a torre {}'.format(disco, origem, destino))
  else:
    torrehanoi(disco - 1, origem, auxiliar, destino)
    print('Mover disco {} da torre {} para a torre {}'.format(disco, origem, destino))
    torrehanoi(disco - 1, auxiliar, destino, origem)
    
def main():
  disco = int(input("Digite a quantidade de discos: "))
  print('')
  torrehanoi(disco, 'A', 'B', 'C')
  print(f"\nFoi necessario {2**disco-1} movimentos para completar o puzzle! :)")

main()