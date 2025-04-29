from socket import SOMAXCONN
import statistics

lista=[1,2,10,4,5,0]
#arquivo tupla nao pode ser modificado, somente consultado.
tupla=(1,2,10,4,5,0)
#modifica arquivo tupla para lista.
a = list(tupla)
#modifica arquivo lista para tupla.
b = tuple(lista)
#print ira dar erro pois o arquivo tupla nao pode ser modificado.
# print(b.append(8))

#print de alteração do arquivo lista mediante a permissão
#da variavel A convertendo o arquivo tupla para lista.
print(a.append(20))
print(a)


x = max (lista)
z = min (lista)
y = len (lista)

#print do arquivo lista com maior valor.
print (x)
#print do arquivo lista com menor valor.
print (z)
#print da quantidade de arquivos na lista.
print (y)
#soma dos valores na lista.


pi = 3.14159265359
# o modulo round vai arredondar o valor da variavel, o valor se mantem se for menor de 5
#e sobe se for 5 ou acima,
#na seção "round(pi,2)" o valor apos a virgula determina as casas decimais.
num = round(pi,4)
print(num)

#utilizando a biblioteca de statistics voce consegue
#tirar a media de valores listados dentre outras funções.
media = statistics.mean(lista)
soma = sum(lista)

print (soma)

print(media)

def soma(n1,n2):
    soma = n1+n2
    return soma

num = int(input("informe um numero: "))
num2 = int(input("informe um numero: "))

print(soma(num,num2))



