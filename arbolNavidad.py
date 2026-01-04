#   *    1
#  ***   3
# *****  5 
#******* 7

#cantidad impar de *

pisos_torre = int(input("ingrese los pisos de la torre"))
i =0
impar = 1
while i < pisos_torre:
    print(" "* (pisos_torre-1), "*"*impar)
    pisos_torre-=1
    impar +=2
