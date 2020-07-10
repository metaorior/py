#Para usar o input é igual no javascript. e se quiser colocar uma mensagem antes e so fazer isso com ""
#nome=input("Digite seu nome: ")

#print("Nome digitado: " + nome)

# o problema da calculadora
# no caso em python num1 e num2 ( ou qualquer variavel é por padrao uma string)
# -> temos que converter para int
import os
os.system('clear')
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
resultado = num1 + num2
print("soma dos valores: " ,resultado)