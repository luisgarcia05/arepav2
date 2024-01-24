print("Vamos a hacer una arepa.")
print("Despues de mezclar la harina y el agua...")
cantidadmasaarepa=(input("¿Cuanta gramos de masa te salen?"))
cantidadmasaarepausar=(input("Cuantos vas a usar"))
if cantidadmasaarepausar>cantidadmasaarepa:
    cantidadmasaarepausar=cantidadmasaarepa

print("Ahora escoge 3 ingredientes para añadirle a las arepas")
ingrediente1=input("¿El primero es?")
cantidadcompletaingrediente1= 650
print("la cantidad total de",ingrediente1, "que tienes es de", cantidadcompletaingrediente1, "gramos" )
cantidadingrediente1usar=int(input("cuanto le vas a añadir"))
if cantidadingrediente1usar>cantidadcompletaingrediente1:
    cantidadingrediente1usar=cantidadcompletaingrediente1
if cantidadingrediente1usar<0:
    cantidadingrediente1usar=0

ingrediente2=input("¿El segundo es?")
cantidadcompletaingrediente2= 350
print("la cantidad total de",ingrediente2, "que tienes es de", cantidadcompletaingrediente2, "gramos" )
cantidadingrediente2usar=int(input("cuanto le vas a añadir"))
if cantidadingrediente2usar>cantidadcompletaingrediente2:
   cantidadingrediente2usar=cantidadcompletaingrediente2
if cantidadingrediente2usar<0:
    cantidadingrediente2usar=0

ingrediente3=input("¿El tercero es?")
cantidadcompletaingrediente3= 500
print("la cantidad total de",ingrediente3, "que tienes es de", cantidadcompletaingrediente3, "gramos" )
cantidadingrediente3usar=int(input("cuanto le vas a añadir"))
if cantidadingrediente3usar>cantidadcompletaingrediente3:
    cantidadingrediente3usar=cantidadcompletaingrediente3
if cantidadingrediente3usar<0:
    cantidadingrediente3usar=0

cantidadfinalmasa= cantidadmasaarepa- cantidadmasaarepausar
cantidadfinalingrediente1= cantidadcompletaingrediente1- cantidadingrediente1usar
cantidadfinalingrediente2= cantidadcompletaingrediente2- cantidadingrediente2usar
cantidadfinalingrediente3= cantidadcompletaingrediente3- cantidadingrediente3usar

print("Disfruta tu arepa")

print("Además, te sobraron:")
print(".", cantidadfinalmasa, " gramos de masa de arepa")
print(".", cantidadfinalingrediente1, " gramos de" , ingrediente1)
print(".", cantidadfinalingrediente2, " gramos de" , ingrediente2)
print(".", cantidadfinalingrediente3, " gramos de" , ingrediente3)