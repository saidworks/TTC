string=input("enter a word").lower()
letter=input("enter the letter you want to know its frequency").lower()
def count_string(string,letter):
    times=0
    for index in range(len(string)):
        if string[index:index+1]==letter:
            times+=1
        else:
            times+=0
    return print("the letter occurred",times,"times")
