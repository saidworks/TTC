'''
JSON stands for Javascript Object Notation
JSON advantages :
    -Structures data in a text format
    -Human readable (as opposed to binary)
    -Most common way data files are transmitted over the web
    -Most Python data types can be converted to/from JSON

    we can use it like :
    import json
    #write

    myfile = open(filename,'w')
    #convert to json
    json_string = json.dump(data)
    myfile.write(json_string+'\n')

    myfile.close()
    #read
    myfile = open(filename,'r')
    #convert to json
    json_string = myfile.readline()
    data = json.loads(json_string)

    myfile.close()
'''
import json
from football import FootballPlayer,RunningBack,QuarterBack,player1,player2,players
#write
width = 20.0
length = 15
outfile = open("datafile1.dat",'w')
#convert to json
json_string = json.dumps(width)
outfile.write(json_string+'\n')
json_string = json.dumps(length)
outfile.write(json_string+'\n')
outfile.close()
#read
myfile = open('datafile1.dat','r')
#convert to json
json_string = myfile.readlines()
j = len(json_string)
i=0
while i<j:
    data = json.loads(json_string[i])
    print(data)
    i += 1
myfile.close()

with open('football.json','w') as football:
    for player in players:
        json_string = json.dumps(player.__dict__)+ ','
        football.write(json_string)

'''
    Pickle : python module that lets you read and write data other than strings more easily
        -reads and write data in binary format 
        -Can only be used with another Python program that is also running on pickle
        -Not for sending data to other people 
        -Pickle-produced files can contain malicious data (unless you are sure of the source)
    usage:
        import pickle
        outflie = open('Filename','wb')  #b for binary needs to be added, for example for append "ab" 
        pickle.dump(data,outflie)
        outflie.close()
'''
import pickle
account = 13452348656
owner = 'Johny Deep'
balance = -500
account_info = open('BankAccount.dat','wb')
pickle.dump(account,account_info)
pickle.dump(owner,account_info)
pickle.dump(balance,account_info)
pickle.dump(player1,account_info)
pickle.dump(player2,account_info)
account_info.close()

with open('BankAccount.dat','rb') as f:
    data = pickle.load(f)
    print(data)
    data = pickle.load(f)
    print(data)
    data = pickle.load(f)
    print(data)
    newPlayer1 = pickle.load(f)
    newPlayer2 = pickle.load(f)
newPlayers = [newPlayer1,newPlayer2]
for player in newPlayers:
    player.displayName()
    player.printIsGood()



