print("WELCOME TO TIK TAK TOE")
def display_board(board):
    #Printing Board
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("-|-|-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-|-|-")
    print(board[1]+"|"+board[2]+"|"+board[3])

marker=[" "]*10
display_board(marker)
player1_marker=""
player2_marker=""

def input_choice():
    #Taking Player Input
    global player1_marker
    global player2_marker
    print("\nPlayer One\n")
    player1_marker=input("CHOOSE 'X' OR 'O': ")

    while(player1_marker!='X' and player1_marker!='O'):
        player1_marker=input("CHOOSE 'X' OR 'O': ").upper()

    if(player1_marker=='X'):
        player2_marker='O'
    else:
        player2_marker='X'

    print("Player One is "+player1_marker+"\nPlayer Two is "+player2_marker+"\n")

def play():
    play_choice=input("Would you like to play the Game? Yes or No.\n").upper()
    if play_choice=="NO":
        print("THANK YOU!\n")
    elif play_choice=="YES":
        input_choice()
        mark_position()
        replay()
    else:
        print("WRONG INPUT. GAME AUTO-SHUTDOWN")
        print("\n")

def replay():
    global marker
    replay_game=input("Would you like to Replay the Game? Yes or No.\n").upper()
    if replay_game=="NO":
        print("THANK YOU FOR PLAYING THE GAME.\n")
    elif replay_game=="YES":
        marker=[" "]*10
        play()
    else:
        print("WRONG INPUT. GAME AUTO-SHUTDOWN")
        print("\n")

def mark_position():
    global player1_marker
    global player2_marker
    i=1
    a=0
    b=0
    while(i<=9):
        player1=int(input("Player 1 Enter Your Poisition.\n"))
        marker[player1]=player1_marker
        display_board(marker)
        #Result Here
        if result()==player1_marker:
            print("Player 1 Wins!\n")
            break
        else:
            a+=1
        i+=1
        if i<10:
            player2=int(input("Player 2 Enter Your Poisition.\n"))
            marker[player2]=player2_marker
            display_board(marker)
            #Result Here
            if result()==player2_marker:
                print("Player 2 Wins!\n")
                break
            else:
                b+=1 
            i+=1
        if a==b:
            print("Game Tie\n")

def result():
    if(marker[1]==marker[2] and marker[2]==marker[3]):
        return marker[1]
    if(marker[4]==marker[5] and marker[5]==marker[6]):
        return marker[4]
    if(marker[7]==marker[8] and marker[8]==marker[9]):
        return marker[7]
    if(marker[1]==marker[4] and marker[4]==marker[7]):
        return marker[1]
    if(marker[2]==marker[5] and marker[5]==marker[8]):
        return marker[2]
    if(marker[3]==marker[6] and marker[6]==marker[7]):
        return marker[3]
    if(marker[1]==marker[5] and marker[5]==marker[9]):
        return marker[1]
    if(marker[3]==marker[5] and marker[5]==marker[7]):
        return marker[3]
    

play()