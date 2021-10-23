# Calculadora em Python
print('********** Python Calculator **********')
print()
print('Selecione a opção desejada:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print()
entrada = input('Digite sua opção (1/2/3/4): ')
if entrada not in ('1', '2', '3', '4'):
    print('Esta opção não é válida!')
else:
    print()
    a = int(input('Digite o primeiro número: '))
    print()
    b = int(input('Digite o segundo número: '))
    print()
    if entrada == '1':
        print((str(a) + ' + ' + str(b) + ' ='), (a + b))
    elif entrada == '2':
        print((str(a) + ' - ' + str(b) + ' ='), (a - b))
    elif entrada == '3':
        print((str(a) + ' x ' + str(b) + ' ='), (a * b))
    elif entrada == '4':
        print((str(a) + ' / ' + str(b) + ' ='), (a / b))
