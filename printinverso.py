n=1
lista=[]
while n!=0:
    n=int(input("Digite os números, digite 0 para encerrar"))
    if n!=0:
        lista.append(n)
h=len(lista)
cont=1
while cont<=h:
    num=lista[-cont]
    print(num, end=', ')
    cont+=1

