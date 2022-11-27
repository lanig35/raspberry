from guizero import App, Text, Waffle
from random import randint

# ---- Variables
GRID_SIZE = 5
score = 0

# ---- Fonctions
def add_dot ():
    x,y = randint (0, GRID_SIZE-1), randint (0, GRID_SIZE-1)
    while plateau[x,y].dotty == True:
        x,y = randint (0, GRID_SIZE-1), randint (0, GRID_SIZE-1)
    plateau[x,y].dotty = True
    plateau.set_pixel (x,y,'red')

    speed = 1000
    if score > 30:
        speed= 200;
    elif score > 20:
        speed = 400
    elif score > 10:
        speed = 500

    all_red = True
    for x in range (GRID_SIZE):
        for y in range (GRID_SIZE):
            if plateau[x,y].dotty == False:
                all_red = False

    if all_red == True:
        score_display.value = 'Perdu ! Score = ' + str(score)
    else:
        plateau.after (speed, add_dot)

def clear_dot (x,y):
    global score
    if plateau[x,y].dotty == True:
        plateau[x,y].dotty = False
        plateau.set_pixel (x,y,'white')
    score += 1
    score_display.value = 'Votre score: ' + str (score)

# --- Application
app = App ('Destroy the dots')

instructions = Text (app, text='Clik the dots to destroy them')
plateau = Waffle (app, width=GRID_SIZE, height=GRID_SIZE, command=clear_dot)
plateau.after (1000, add_dot)
score_display = Text (app, text='Votre score: ' + str(score))

app.display ()
