def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    #the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
    while True:
        try:
            move = int(input("Enter your move: "))
            if move>0 and move<10:
                break
        except:
            print("Enter a value between 1-9")
    return move

    

def make_list_of_free_fields(board):
    board = [
        [1,2,3]
    ]
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    # The function draws the computer's move and updates the board.
