from IPython.display import clear_output
def basic_info():
    print("Welcome to Tic Tac Toe Board Game.")
    choice = "Wrong"
    choice1 = 'Wrong'
    while choice != 'Y':
        user1 = input("Please Your Name as User 1: ")
        choice = input(f"Your Name is {user1}, Correct? Y or N: ").upper()
    while choice1 != 'Y':
        user2 = input("Please Your Name as User 2: ")
        choice1 = input(f"Your Name is {user2}, Correct? Y or N: ").upper()
    return [user1,user2]

def board_pattern():
    board_1 = ["1","2","3"]
    #board_2 = ["-","-","-","-","-"]
    board_3 = ["4","5","6"]
    #board_4 = ["-","-","-","-","-"]
    board_5 = ["7","8","9"]
    borad = [board_1,board_3,board_5]
    return borad

def playing():
    board = board_pattern()
    count = 0
    clear_output()
    while count < 9:
        varis = input("Select position and mark. (format: posi,mark) ")
        posi,mark = varis.split(',')
        posi = int(posi)
        if posi <= 3: # use to replace the board 1 row
            board[0][posi-1] = mark
        elif posi <= 6:# use to replace the board 2 row
            posi = posi - 3
            board[1][posi-1] = mark
        elif posi <= 9:# use to replace the board 3 row
            posi = posi - 6
            board[2][posi-1] = mark
        for new_board in board:
            print(new_board)
        if board[0][0] == board[0][1] == board[0][2] == mark: # these line that following can be use a better method to do it
            return True, mark
        elif board[1][0] == board[1][1] == board[1][2] == mark:
            return True, mark
        elif board[2][0] == board[2][1] == board[2][2] == mark:
            return True, mark
        elif board[0][0] == board[1][0] == board[2][0] == mark:
            return True, mark
        elif board[0][1] == board[1][1] == board[2][1] == mark:
            return True, mark
        elif board[0][2] == board[1][2] == board[2][2] == mark:
            return True, mark
        elif board[0][0] == board[1][1] == board[2][2] == mark:
            return True, mark
        elif board[0][2] == board[1][1] == board[2][0] == mark:
            return True, mark
        count += 1
    return False, mark

def interact():
    user1,user2 = basic_info() #grab the basic info of users, return uesr1 and user2
    hashmap = {user1:'X',user2:'O'}
    for board in board_pattern():# print origenal board
        print(board)
    continues_game = input('Do you want to continue the game? Y or N ').upper()
    if continues_game == 'Y':
        print(f"First user will always go first, and {user1} uses X and {user2} uses O")
        status,mark = playing()
        if status == True:
            print(f'{list(hashmap.keys())[list(hashmap.values()).index(mark)]} is the winner') # This line to use value to get key
        else:
            print('Game is tied. No winner.')
    elif continues_game == 'N':
            print('Closing Game.')

interact()