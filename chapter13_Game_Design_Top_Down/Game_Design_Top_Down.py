####This an example of procedural programming where functions are created to handle all main tasks
from random import choice
def InitializeGrid(board):
    #Initialize grid by random value
    for i in range(8):
        for j in range(8):
            board[i][j]=choice(['Q','R','S','T','U'])
def Initialize(board):
    #Initialize game
    #Intialize the grid
    InitializeGrid(board)
    #Initialize score
    global score
    score=0
    #Initialize turn number
    global turn
    turn=1

def ContinueGame(currentscore,goalscore=100):
    #Return false if game should end , true if game not over
    if currentscore>=goalscore:
        return False
    else:
        return True
def DrawBoard():
    # Display the board to the screen
    linetodraw = ""
    # Draw some blank lines first
    print("\n\n\n")
    print(" ---------------------------------")
    # Now draw rows from 8 down to 1
    for i in range(7, -1, -1):
    # Draw each row
        linetodraw = str(8-i) + ""
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw += " |"
        print(linetodraw)
        print(" ---------------------------------")
    print('  | a | b | c | d | e | f | g | h |')
    global score
    print('current score:',score)

#verify user entry 
def IsValid(move):
     #verify if the user entered an appropriate key 
    cols = [ 'a' , 'b' ,'c' , 'd' , 'e' , 'f' , 'g' , 'h']
    direction = ['u','d','l','r']
    if len(move)==3 and int(move[1])<8:
        for i in cols:
            for j in direction:
                if move.startswith(i):
                    if move.endswith(j):
                        return True
    else:
        return False

def GetMove():
    #instructions
    print("Enter move by specifuing the space and the direction (u,d,l,r). Spaces should list column then row. \n For example, e3u would swap position e3 with the one above, and f7r would swap f7 to the right.")
    
    #Get the move from the user
    move = input("Enter a move : ")
    while not IsValid(move):
        move = input("Enter a move : ")
    return move
def DoRound():
    #Perform one round of the game
    #Display current board
    DrawBoard()
    #Get a move
    move=GetMove()
    #Update board
    Update(board,move)
    #update turn number
    global turn
    turn+=1
def ConvertLetterToCol(Col):
    if Col == 'a':
        return 0
    elif Col == 'b':
        return 1
    elif Col == 'c':
        return 2
    elif Col == 'd':
        return 3
    elif Col == 'e':
        return 4
    elif Col == 'f':
        return 5
    elif Col == 'g':
        return 6
    elif Col == 'h':
        return 7
    else:
    #not a valid column!
        return -1
def SwapPieces(board, move):
    #Swap pieces on board according to move
    #Get original position
    origrow = int(move[1])-1
    origcol = ConvertLetterToCol(move[0])
    #Get adjacent position
    if move[2] == 'u':
        newrow = origrow + 1
        newcol = origcol
    elif move[2] == 'd':
        newrow = origrow - 1
        newcol = origcol
    elif move[2] == 'l':
        newrow = origrow
        newcol = origcol - 1
    elif move[2] == 'r':
        newrow = origrow
        newcol = origcol + 1
    #Swap objects in two positions
    temp = board[origrow][origcol]
    board[origrow][origcol] = board[newrow][newcol]
    board[newrow][newcol] = temp
def RemovePieces(board):
    #Remove 3-in-a-row and 3-in-a-column pieces
    #Create board to store remove-or-not
    remove = [ [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    #Go through rows
    for i in range(8):
        for j in range(6):
            if (board[i][j] == board[i][j+1]) and (board[i][j] == board[i][j+2]):
            #three in a row are the same!
                remove[i][j] = 1;
                remove[i][j+1] = 1;
                remove[i][j+2] = 1;
    #Go through columns
    for j in range(8):
        for i in range(6):
            if (board[i][j] == board[i+1][j]) and (board[i][j] == board[i+2][j]):
            #three in a row are the same!
                remove[i][j] = 1;
                remove[i+1][j] = 1;
                remove[i+2][j] = 1;
            #Eliminate those marked
    global score
    removed_any = False
    for i in range(8):
        for j in range(8):
            if remove[i][j] == 1:
                board[i][j] = 0
                score += 1
                removed_any = True
    return removed_any
def DropPieces(board):
    #Drop pieces to fill in blanks
    for j in range(8):
    #make list of pieces in the column
        listofpieces = []
        for i in range(8):
            if board[i][j] != 0:
                listofpieces.append(board[i][j])
                #copy that list into colulmn
        for i in range(len(listofpieces)) :
            board[i][j] = listofpieces[i]
    #fill in remainder of column with 0s
        for i in range(len(listofpieces), 8):
            board[i][j] = 0
def FillBlanks(board):
    #Fill blanks with random pieces
    for i in range(8):
        for j in range(8):
            if (board[i][j] == 0):
                board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])
def Update(board, move):
    #Update the board according to move
    SwapPieces(board, move)
    pieces_eliminated = True
    while pieces_eliminated:
        pieces_eliminated = RemovePieces(board)
        DropPieces(board)
        FillBlanks(board)
#state variables for main data to be stored ( data structure)
score = 50
goalscore = 100
board=[[0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0]]

#Initialize Game
Initialize(board)

#Loop while game not over
while ContinueGame(score,goalscore):
    #Do a round of the game
    DoRound()