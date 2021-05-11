# =============================================================================
# Search Algorithm 
# =============================================================================
import csv
with open('world-cities_csv.csv','r',newline='') as cities:
    cities_reader = csv.reader(cities, delimiter=',')
    cities_list = []
    for row in cities_reader:
        cities_list.append(row[0])
# =============================================================================
# linear search : loop through elements 
#   check if there is a match
#       if there is a match return true
#       else we move on
# =============================================================================
def isIn(list_items,item):
    i = 0
    count = 0
    while i<len(list_items):
        if item == list_items[i]:
            count += 1
            i += 1
        else:
            i += 1
    return f'{item} has been repeated {count} times'
            
print(isIn(cities_list,'Ankara'))
# =============================================================================
# binary search : List of values in sorted order : L 
# 1. set low  = 0 and high = length of list - 1
# 2. if L[low] == v or L[high] == v, return True
# 3. while low < high -1
#   A. midpoint = low + (high - low)/ 2
#   B. if L[midpoint] == v, return True
#   C. else if L[midpoint] < v , set low = midpoint
#   D. else set high = midpoint
#   return false
# =============================================================================
# I need to order my list !!!
def BinaryIn(L,v):
    if len(L) < 1:
        return False
    low = 0
    high = len(L) - 1
    if L[low] == v :
        return low
    elif L[high] ==v:
        return high
    while low < high -1:
        midpoint = low + (high - low) // 2
        if L[midpoint] == v:
            return midpoint
        elif L[midpoint] < v :
            return low
        else:
            high = midpoint

    return False

favorite_foods = ['barbeque', 'chicken and dumplings', 'gumbo', 'ice cream', 'pecan pie', 'pizza']
print(BinaryIn(favorite_foods, 'gumbo'))
print(BinaryIn(favorite_foods, 'coconut'))
''' sorting algorithms 
    * Selection Sort , example: 
    <input : unsorted list L
    <output: L, with elements sorted smallest to largest 
    1. maxindex = length of L -1 
    2. for i = 0 to maxindex :
        a. find the index with the smallest value between i and maxindex
        b. swap that element with element index i
'''

maxindex = len(cities_list) - 1
minindex = None
for i in range(0,maxindex + 1,1):
    minindex = i
    for j in range(0,maxindex+1,1):
        if cities_list[j] < cities_list[minindex]:
            minindex = j
    temp = cities_list[i]
    cities_list[i] = cities_list[minindex]
    cities_list[minindex] = temp

print(cities_list)
''' *************************Insertion Sort *****************
    compare each element to the next element
    swap it to the start if it is smaller

'''
nums = [11,574,6,47,57,570,258]
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]<nums[j]:
            nums