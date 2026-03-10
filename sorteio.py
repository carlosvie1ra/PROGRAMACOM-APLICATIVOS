id_do_usuario = int(input("coloque seu id: "))
valor_da_compra = float(input("digite o valor de compra: "))

if id_do_usuario % 2 == 0 and valor_da_compra > 500.00:
    print(f"parabens, usuarios {id_do_usuario} ")
else:
    print(f"obrigado pela compra de usuario {id_do_usuario} continue acompanhando suas promoções")