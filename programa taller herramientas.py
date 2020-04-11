def main():
	menu()
#menú
def menu():
	opcion=int(input("por favor digite la opcion que desea realizar:\n1. decimal a binario y hexa decimal\n2. binario a decimal y hexadecimal\n3.hexadecimal a binario y decimal\n4. terminar programa\n"))
	while opcion<1 or opcion>4:
		opcion=int(input("por favor digite una opcion valida\n"))
	while opcion!=4:	
		if opcion==1:
			numero=pedirnumero()
			print(decimal_a_hexadecimal(numero))
			print(hexadecimal_a_binario(decimal_a_hexadecimal(numero)))
			if continuar():
				menu()
			else:
				opcion=4
		elif opcion==2:
			numero=pedirnumero()
			print(binario_decimal(numero))
			print(decimal_a_hexadecimal(binario_decimal(numero)))
			if continuar():
				menu()
			else:
				opcion=4
		else:
			numero=str(pedirnumero())
			numero=numero.upper()
			print(hexadecimal_a_binario(numero))
			print(binario_decimal(int(hexadecimal_a_binario(numero))))
			if continuar():
				menu()
			else:
				opcion=4
#determina si el ususario desea continuar con el programa o no
def continuar():
	continuar=int(input("desea continuar? 1.Si  2.No\n"))
	while continuar!=1 and continuar!=2:
		continuar=int(input("por favor digite una respuesta valida: "))
	if continuar==1:
		return True
	else:
		return False
#pedir numeros
def pedirnumero():
 numero= int(input("Numero: "))
 return numero
#pasar numeros de binario a decimal
def binario_decimal(numero):
  if numero==0:
   return 0
  if numero%10==0:
   return(binario_decimal(numero//10)*2)
  elif numero%10==1:
  	return(1+(binario_decimal(numero//10)*2))
#pasar numeros decimales a hexademial
def decimal_a_hexadecimal(numero):
  hexa=""
  while numero!=0:
    a=numero//16
    b=numero-(a*16)
    if b==10:
      b="A"
    elif b==11:
      b="B"
    elif b==12:
      b="C"
    elif b==13:
      b="D"
    elif b==14:
      b="E"
    elif b==15:
      b="F"
    hexa= str(b)+hexa
    numero=a
  return hexa
 #pasar de hexadecimal a binario
def hexadecimal_a_binario(numero):
  dic_hex={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101',
        '6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011',
        'C':'1100','D':'1101','E':'1110','F':'1111'}
  binario=[]
  for i in numero:
  	if i in dic_hex:
  		#el append lo que hace es asignarle a la lista el valor correspondiente de i segun el diccionario
  	    binario.append(dic_hex[i])
  #aui el .join lo que hace es unir todos los valores del array "binario" sin dejar espacios
  binario_final=("").join(binario)
  return binario_final
 #por qué aqui usé un diccionario? porque estuve averiguando e intentando de otras maneras de como hacer esta conversion y aunque python tenga una funcion que lo hace solo, no creo que le sirva como metodo de demostracion, así que por eso esta funcion está hecha con un diccionario y la anterior no uwu
main()