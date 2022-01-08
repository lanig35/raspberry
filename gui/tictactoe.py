from guizero import App, Box, PushButton, Text

# ------- Variables
turn = 'X'

# ------ Fonctions
def clear_board ():
    new_board = [[None,None,None],[None,None,None],[None,None,None]]

    for x in range(3):
        for y in range (3):
            button = PushButton (board, text='', grid=[x,y], width=3,
                                 command=select_square, args=[x,y])
            new_board [x][y] = button

    return new_board

def select_square (x, y):
    plateau [x][y].text = turn
    plateau [x][y].disable()
    toggle_player ()

def toggle_player ():
    global turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    message.value = 'Au tour de ' + turn

# ----- Programme Principal
app = App ('Tic tac toe')

board = Box (app, layout='grid')
plateau = clear_board ()
message = Text (app, text='Au tour de ' + turn)

app.display ()
