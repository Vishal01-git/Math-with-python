from IPython.display import display, Math
def powerfun(x,y):
    display(Math('%g^%g = %g' %(x,y,x**y)))

def divfun(x,y):
    print(f'{x}/{y} = {x/y}')

x = int(input("Enter first number : "))
y = int(input("Enter Second number : "))

display(Math('Enter "1" to perform %g^%g OR Enter "2" to perform \\frac{%g}{%g}' %(x,y,x,y)))

z = input("Enter your choice : ")

if z=="1":
    powerfun(x,y)
elif z=="2":
    divfun(x,y)
else:
    print("Your input is wrong")        