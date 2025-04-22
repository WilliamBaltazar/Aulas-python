frutas=['uva','pera','caqui','coco']
print(frutas)
ins = input('Adicione outro item: ')
frutas.append(ins)
print(frutas)
#removendo itens de um arquivo lista
rem = input('Qual arquivo voce quer remover: ')
frutas.remove(rem)
print(frutas)
#print de listas diferentes
nome=['zeze','didi','lili']
sobrenome=['tess','bel','lil']
idade=['19','25','32']
print(nome[0],sobrenome[1])
#criação de dicionario
nomedic={}
nomedic["nome"] ="William"
nomedic["idade"] ="30"
nomedic["Profissão"] ="Desenvolvedor"
print(nomedic)
#input de valores
x=input('informe seu nome: ')
y=input('Informe sua idade: ')
z=input('informe sua profissão: ')
#chave+valor com input
nomedic["nome"] = x
nomedic["idade"] = y
nomedic["Profissão"] = z
print(nomedic)
