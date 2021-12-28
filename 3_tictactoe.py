import emoji
print(emoji.emojize("                 :beaming_face_with_smiling_eyes:"))
print("           WelCome to the GAME\n'----***------TIC TAC TOE------***----'")
print("\n")
print('-' + " | " + '-' + " | " + '-' + "     1 | 2 | 3")
print('-' + " | " + '-' + " | " + '-' + "     4 | 5 | 6")
print('-' + " | " + '-' + " | " + '-' + "     7 | 8 | 9")
print("\n")


def display_board():
  print("\n")
  print(board[1] + " | " + board[2] + " | " + board[3] + "     1 | 2 | 3")
  print(board[4] + " | " + board[5] + " | " + board[6] + "     4 | 5 | 6")
  print(board[7] + " | " + board[8] + " | " + board[9] + "     7 | 8 | 9")
  print("\n")

def user_choice():
    while True:
        inp=input("[HUMAN] choose your option either 'X' or 'O':=")
        if inp in['X','x']:
            print("[HUMAN] you choose 'X' so you play first")
            print(emoji.emojize(":raising_hands:"))
            return 'x','o'
        elif inp in['O','o']:
            print("[HUMAN] you choose 'O' now machine play first\n")
            print(emoji.emojize(":laptop:"))
            return 'o','x' 
        else:
            print("[HUMAN] enter correct input between 1 to 9:=")     

def human_input(inp):
    while True:
        position=int(input(f"human {inp} enter the position:="))
        if position>0 and position<10:
            if board[position]==' ':
                return position
            else:
                print("already taken")
                print(emoji.emojize(":face_without_mouth:"))
        else:
            print("enter correct value(Except the allocated value)")  
            print(emoji.emojize(":unamused_face:"))          


def new_game():
    while True:
        inp=input("enter Y or y for continue and N or n for stop==")
        if inp in ['Y','y']:
            again=True
            break
        elif inp in ['n','N']:   
            print("Nice to play with you\n")
            print(emoji.emojize(":winking_face:"))
            again=False
            break
        else:
            print("enter correct;=")
    if again:
        print("---***new game***---")
        print(emoji.emojize(":beaming_face_with_smiling_eyes:"))  
        main_game()
    else:
        return False           


def win_check(human,machine):
    winning_places=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]]
    for win_place in winning_places:
        if board[win_place[0]]==board[win_place[1]]==board[win_place[2]]==human:
            print("human you won\n")
            print(emoji.emojize(":winking_face_with_tongue:"))
            inp=new_game()
            if not inp:
                return False
        elif board[win_place[0]]==board[win_place[1]]==board[win_place[2]]==machine:
            print("machine you won\n")
            print(emoji.emojize(":crying_face:"))
            inp=new_game()
            if not inp:
                return False    
    if ' ' not in board:
        print("gane over")
        inp=new_game()
        if not inp:
            return False     
    return True           


def winning(mark,board):
    winning_places=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]]
    for win_place in winning_places:
        if board[win_place[0]]==board[win_place[1]]==board[win_place[2]]==mark:
            return True
            

def win_move(i,board,machine):
    temp_board=list(board)
    temp_board[i]=machine
    if winning(machine,temp_board):
        return True
    else:
        return False    

def machine_input(machine,human,board):
    for i in range (1,10):
        if board[i]==' ' and win_move(i,board,machine):
            return i
    for i in range (1,10):
        if board[i]==' ' and win_move(i,board,human):
            return i
    for i in[1,2,3,4,5,6,7,8,9]:
        if board[i]==' ':
            return i        



def main_game():
    global board
    
    play=True
    board=['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    human,machine=user_choice()
    while play:
        if human=='x':
            x=human_input(human)
            board[x]=human
            display_board()
            play=win_check(human,machine)
            if play:
                o=machine_input(machine,human,board)
                board[o]=machine
                display_board()
                play=win_check(human,machine)
        else:
            x=machine_input(machine,human,board)
            board[x]=machine
            display_board()
            play=win_check(human,machine)
            if play:
                o=human_input(human)
                board[o]=human
                display_board()     
                play=win_check(human,machine)  


if __name__=="__main__":
    main_game()