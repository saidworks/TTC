#stack structure => based on list
# 'last in first out'
import csv
class Stack:
    _stack = []
    def push(self,item):
        self._stack.append(item)
    def pop(self):
        self._stack.pop()
    def show(self):
        print(self._stack)
# stack gives us => "last in , first out"
# play essential rule in computer => call stack
Books = Stack()
#get list of books
with open("books.csv","r",newline='') as book_list:
    reader = csv.reader(book_list,delimiter=',')
    for row in reader:
        str = row[0] + " by " +row[1].replace(',',' ')
        Books.push(str)

# Books.show()
# Books.pop()
# Books.pop()
# Books.show()
# Books.push('Idiot, The by Dostoevsky  Fyodor')

# Queues
# it can come handy for handling a program for orders eg
# it comes handy when handling Buffer
class Queue:
    _queue = []
    def push(self,item):
        self._queue.insert(len(self._queue),item)
    def pop(self):
        self._queue.pop(0)
    def isEmpty(self):
        return (len(self._queue)) == 0

# =============================================================================
############################## Dictionary #####################################
# Hash table Maps a large of data values into smaller number of indices (called slots) 
# It uses chaining which consists of maling a list of everything in a particular slot 
# Hash function : function to convert a key phrase into a number to index into an array (list)
# =============================================================================
prepare_data = []
books_dict = dict()
with open("books_new.csv","r",newline='') as file:
    new_reader = csv.reader(file,delimiter=',')
    for row in new_reader:
        prepare_data.append(row)

titles = []
authors = []
genres = []
subgenres = []
heights = []
publishers = []
for i in range(1,len(prepare_data)-1,1):
    titles.append(prepare_data[i][0])
    authors.append(prepare_data[i][1])
    genres.append(prepare_data[i][2])
    subgenres.append(prepare_data[i][3])
    heights.append(prepare_data[i][4])
    publishers.append(prepare_data[i][5])
    books_dict['Title'] = titles
    books_dict['Author'] = authors
    books_dict['Genres'] = genres
    books_dict['Subgenres'] = subgenres
    books_dict['Heights'] = heights
    books_dict['Publishers'] = publishers
    

# print(books_dict)
# #del books_dict['Title'] #used to delete a key with it is values
# print('Title' in books_dict)
# =============================================================================
# SET : Collection of items stored using a hash-table does mathematical
#  operations checks membership quickly
# =============================================================================
ingredients = set(['flour','sugar','eggs','milk'])
ingredient_1 = set(['salt','chicken','eggs','sauce'])

if 'milk' in ingredients:
    print('it exists')
ingredients.add('apple')
print(ingredients)
ingredients.remove('apple')
print(ingredients)
print(ingredients - ingredient_1)
print(ingredients | ingredient_1)
print(ingredients & ingredient_1)
print(ingredients ^ ingredient_1) #exclusive or 
