

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    print('O maior é o', num1)
elif num2 > num3 and num2 > num1:
    print('O maior é o', num2)   
elif num3 > num2 and num3 > num1:
    print('O maior é o', num3)  
else:
    print('Tem valores iguais no conjunto')       