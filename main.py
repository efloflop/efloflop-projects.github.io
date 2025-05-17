from random import*
from time import*
def clear():
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	print()	
def saving(strs, file,):
	with open (file, "w" ) as f:
		print(input(), file=f)
	for i in range(strs-1):
		with open (file, "a" ) as f:
			print(input(), file=f)

def F():
	F=2
	while True:
		F=F+F
		print(F)

def calculator():
		print('num 1')
		a=float(input())
		print('+, -, /, *, **')
		Input=input()
		print('num 2')
		b=float(input())
		if Input == '+':
			print(a+b)
		if Input == '-':
			print(a-b)
		if Input == '/':
			print(a/b)
		if Input == '*':
			print(a*b)
		if Input == '**':
			print(a**b)
def aboba():
	print('###############')
	print('#-########-###')
	print('#--######--###')
	print('#--$----$--###')
	print('###------#####')
	print('#####(+)######')
	print('###############')
	print('###############')

def kazino():
	r0=0
	r1=0
	r2=0
	vibor=0
	Cres=0
	def lost():
		print('---------------------')
		print('╔╦╗     ╔╗ ╔═╗╔══╗╔══╗')
		print('║║║     ║║ ║║║║══╣╚╗╔╝')
		print('║║║     ║╚╗║║║╠══║ ║║ ')
		print('╚═╝     ╚═╝╚═╝╚══╝ ╚╝ ')
		print('---------------------')
	def win():
		print('---------------------')
		print('╔╦╗     ╔╦═╦╗╔══╗╔═╦╗')
		print('║║║     ║║║║║╚║║╝║║║║')
		print('║║║     ║║║║║╔║║╗║║║║')
		print('╚═╝     ╚═╩═╝╚══╝╚╩═╝')
		print('---------------------')
	def animka0():
		print(" ___________  ^")
		print("| _ | _ | _ |_|")
		print("|###########|")
		print("|###########|")
	def animka3():
		print("____________  ^")
		print("|",r0,"|",r1,"|",r2,"|_|")
		print("|###########|")
		print("|###########|")
	def animka2():
		print("____________  ^")
		print("|",randint(0,2),"|",randint(0,2),"|",randint(0,2),"|_|")
		print("|###########|")
		print("|###########|")
	def animka1():
		print(" ___________   ")
		print("| _ | _ | _ |_/")
		print("|###########|")
		print("|###########|")
	print("0,1, or 2")
	vibor=int(input())
	r0=randint(0,2)
	r2=randint(0,2)
	r1=randint(0,2)
	animka0()
	sleep(0.5)
	animka1()
	sleep(0.5)
	for i in range(6):
		animka2()
		sleep(0.5)
	clear()
	animka3()
	sleep(0.5)
	if r0 == r1 or r1 == r2 or r2 == r0:
		if r0 == r1:
			Cres = r0
		elif r1==r2:
			Cres = r1
		elif r2==r0:
			Cres = r0
		if Cres == vibor:
			sleep(1)
			win()
		else:
			sleep(1)
			lost()
	else:
		sleep(1)
		lost()



program=1
while program==1:
	print("Q.QUIT")
	print("1.aboba")
	print("2.calculator")
	print("3.kazino")
	print("4.saving")
	Input=input()
	if Input=='Q':
		program=0
	if Input=='1':
		aboba()
	if Input=='2':
		calculator()
	if Input=='3':
		kazino()
	if Input=='4':
		saving(int(input()), input())
	if Input=='F':
		F()

