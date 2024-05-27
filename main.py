num1 = int(input("digite o primeiro número:"))
num2 = int(input("digite o segundo número:"))
metodo = input("digite o método da conta (+,-,/,*)")

if metodo == '+':
  resultado = num1 + num2
  print(resultado)

elif metodo == '-':
  resultado = num1 - num2
  print(resultado)

elif metodo == '/':
  resultado = num1 / num2
  print(resultado)

elif metodo == '*':
  resultado = num1 * num2
  print(resultado)