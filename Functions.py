def getBirthday():
    m,d,y=input("enter your birth month"),input("enter your birth day"),input("enter your birth year")
    birthday=(m,d,y)
    s="-"
    if birthday==("4","20","1988"):
        print("Awesome birthday")
    return s.join(birthday)

print(getBirthday())

n=int(input("enter a number"))
def factorial(n):
    factorial=1
    for i in range(1,n+1,1):
        factorial*=i
    return print(factorial)
string=input("enter a word")
letter=input("enter the letter you want to know its frequency")
def count_string(string,letter):
    index=0
    for index in range(len(string)):
        if string[index:index+1]==letter:
            index+=1
        else:
            index+=0
    return print("the letter occurred",index,"times")
count_string(string,letter)