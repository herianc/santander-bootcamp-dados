while True:
  valor = float(input())
  if valor > 0:
    #TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
    print(f'Deposito realizado com sucesso! \nSaldo atual: R$ {valor}')
    break;
  elif valor == 0:
    print('Encerrando o programa...')
    break;
  else:
    print('Valor invalido! Digite um valor maior que zero.')