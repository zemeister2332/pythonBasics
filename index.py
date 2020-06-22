#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 23:39:04 2020

@author: zemeister
"""

# %%
# VARIABLES <==> O'ZGARUVCHILAR
"""
int, float, string, boolean
"""
# ism = qiymat        # ozgaruvchi qiymatini belgilashimiz shart emas

int1 = 10 # int # 4byte
int2 = 11
string1 = "John Wick" # string # 9byte
float1 = 10.11 # float # 4byte

variable_type = type(string1)

print(string1)
# %%
var1 = "Detroit"
var2 = "Tashkent"
jami = var1 + var2
print(jami)


var3 = "213"
var4 = "789"
toplam = var3 + var4
print(toplam)

print(len(toplam))

print(toplam[2])
 
num1 = -36.7 # float
num2 = 45 # int
print(num1, num2)

boolean = 1 # false


# %%
# Built in Function

str1 = "misol"
float1 = 10.3
# int(float1)
# round(float1)
str2 = "2020"


# %%
# User Defined Function

son1 = 20
son2 = 30

javob = ((son1+son2*300/20)*son1)/son2


def meningFunk(a,b):
    """
    Bu mening birinchi Function'im
    
    parametr: 
        
    return:    
    """
    javob = ((a+b*300/20)*a)/b
    return javob

print(meningFunk(80, 90))

#-----------------------------------#

def meningFunk1(ahmad,mahmud):
    """
    Bu mening birinchi Function'im
    
    parametr: 
        
    return:    
    """
    javob = ((ahmad+mahmud*400/20)*ahmad)/mahmud
    print(javob)

meningFunk1(100,200)    

#-----------------------------------#

def ismimniAyt():
    print("Mening Ismim Saud")

ismimniAyt()

# %%
# Default and Flexible Function'lar

def doiraniHisobla(r,pi=3.14): # pi - 3.14
    """
    doira hisoblash
    input(parametr): r, pi
    output = doirani uzunligi
    """
    output = 2*pi*r
    print(output)
    
doiraniHisobla(30)

#--------------FLEXIBLE---------------------#
def hisobla(boy,vazn,*args):
    print(args)
    jami = (boy+vazn)*args[2]
    print(jami)

hisobla(180,110,2,34,5,6,23)

# %%
# Lambda Function
# ctrl+1 jamlab eslatma qilish uchun
def hisobla1(x):
    return x*x
print(hisobla1(5))

hisobla2 = lambda x: x*x
print(hisobla2(6))


# %%
# TAKRORLASH

yosh = 10
ism = "John"
familya = "Wick"

def funk(yosh,ism, *args, sochRangi="Qora"):
    print("Bolaning Ismi:", ism," Yoshi: ",yosh, " Sochining Rangi: ",sochRangi)
    print(type(ism))
    print(float(yosh))
    
    output = args[1]*yosh
    return output

natija = funk(yosh, ism, familya, "Traversy")
print("args[0]*yosh: ",natija)

# %%
# LIST'lar

list1 = [1,2,3,4,5,6]

print(type(list1))
 
list2 = ["foo", "bar", "hello"]

print(list2[1])

list3 = [1,2,3,4,5,6]

print(list3[1:-1])

list3.append(7)
print(list3)
list3.remove(7)
print(list3)
list3.reverse()
print(list3)

list4 = [4,3,5,6,2,7,1]
list4.sort()
print(list4)

# %%

def year2Century(year):
    """
    year to century
    """
    str_year = str(year)
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year) == 3):
        if(str_year[1:3] == "00"):  # 100 ,200 300, 400 ... 900
            return int(str_year[0])
        else:                       # 190, 250, 450
            return int(str_year[0])+1
    else:                           # 1750, 1700, 1805
        if(str_year[2:4]=="00"):    # 1700, 1900, 1100
            return int(str_year[:2])
        else:                       # 1705, 1645, 1258
            return int(str_year[:2])+1


def yearToCentury(year):
	if(int(year/100)*100 == year):
		return int(year/100)
	else:
		return (int(year/100) + 1)

inputs = [1834,864,1944,2000,1700,1580]


for input in inputs:
	print("Year: " + str(input) + " Century: " + str(yearToCentury(input)))

liste = [1,2,3,4,5,6,4,23,67,21,-500,23,451,67]

# %%

mini = 100000
for each in liste:
    if(each < mini):
        mini = each
    else:
        continue
print(mini)


list1 = [55,46,22,3,4,6,3,778,66,-77,24,68]
x=list1[0]
for i in list1:
    x=i if x>i else x
print(x)
