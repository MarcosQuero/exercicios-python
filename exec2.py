while  True: # O loop infinito foi iniciado
    comando = input("Digite 'sair' para desligar o motor: ")
    
    if comando.lower() == 'sair':
        print("motor desligado.")
        break # A trava de segurança foi acionada!
    else:
        print("O motor continua a rodar...")