"""
This one training of my coding that cand help me to practice my python.

Lets make a program that can make a deriveds.

Ok so let's started.

Let's make some users stories:

	- As a user i want to evaluate a simple derived
	- As a user i have my element to derived
"""

#Let's start
print("Hello friend! \n Let's make some matematics! \n The constant would be only a numbre if yo have a letter as a constant use '0' \n The varible only could be 'x', 'y' or 'z' ")
"""def return_constant():
	alphabet = ('a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, ')
	constants = alphabet.split()
	for constant in constants:
		print(constant)"""

# We declare a variable that the user introduce.
user_constant = input("Give me a constant to derived: ")
user_constant = int(user_constant)
user_variable = input("Give me a varible to derived: ")

def make_derived(constant, varible):
	if type(constant) == int:
		constant = constant * 0
		print("The derived of your constant is: " + str(constant))
	else:
		#print(type(varible))
		#print(varible)
		print("That is not a number (if your constant is a letter use '0')")

	if varible == 'x' or varible == 'y' or varible == 'z' or varible == 'X' or varible == 'Y' or varible == 'Z':
		varible = 1
		print ("The derived of your varible is: " + str(varible))
	elif varible != 'x' or varible == 'y' or varible == 'z' or varible == 'X' or varible == 'Y' or varible == 'Z':
		print("Error. You use a diferent letter for your varible")
	else:
		print('Something is wrong')

make_derived(user_constant, user_variable)

"""list_of_elements = user_constant.split()

for element in list_of_elements:
	print(type(element))
	if element == int or element == 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, ':
		print(element * 0)
	else:
		print('Que pasa?')"""



''''funcion = input("Ingrese una funcion: ")
print (funcion)
funcion_1 = funcion.split()
funcion_1
for element in funcion_1:
	if (element != 'AND' and element != 'OR' and element != 'XOR' and element != 'NOT'):
		print ("Estupida las funciones permitidas son AND OR XOR NOT")
	else:
		print ("Bien")

aridad = input("Ingrese la aridad: ")
print (aridad)
terminal = input ("Ingrese una terminal: ")
print (terminal)'''


