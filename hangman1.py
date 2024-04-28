import pygame as pg
import math 
import random

pg.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1080
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60
clock = pg.time.Clock()
run = True



# Buttons
radius = 24
space = 20 
letters = [] #[399,122,"A", True]
x_start = round((SCREEN_WIDTH-(radius*2 + space)*13)/2)
y_start = 540

A = 65 #Using ACII value to print letters on the button. A->65, b->66 and so on 

for i in range(26):
    x = x_start + space*2 + ((radius*2 + space)* (i%13))
    y = y_start + ((i//13) * (space + radius*2))
    letters.append([x,y,chr(A+i),True])

# Fonts
font = pg.font.SysFont("comicsans",45)
WORD = pg.font.SysFont("comicsans",40)
TITLE = pg.font.SysFont("comicsans",70)

# Time to load images so we can draw a hangman 
images = []
for i in range(0,7):
    image = pg.image.load("man"+str(i+1)+".png")
    images.append(image)

print(images)

#game variables
hangman = 0
lists = ["apple"], ["bannana"], ["pineapple:"], ["pear"], ["mango"], ["grapes"], ["kiwi"], ["dragonfruit"], ["strawberry"], ["orange"], ["watermelon"]
words = random.choice(lists)
guessed = []# to track the letters that have been guessed

# function to draw buttons, and hangman 
def draw():
    screen.fill((255, 255, 255)) # display with white color 
    title = TITLE.render("HangMan",1,(0,0,0,0))
    screen.blit(title,(SCREEN_WIDTH/1.9 -title.get_width()/2, 10)) # Title in center and then y axis = 24

    # draw word on the screen 
    disp_word = ""
    for letter in words:
        if letter in guessed:
            disp_word += letter + " "

        else:
            disp_word +="_"

    text = WORD.render(disp_word,1,(0,0,0,0))
    screen.blit(text,(500,250))

    # buttons at center
    for btn_pos in letters:
        x,y,ltr,visible = btn_pos # making button visible and invisible after clicking it 

        if visible:
            pg.draw.circle(screen,(0,0,0,0),(x,y),radius,4)
            txt = font.render(ltr,1,(0,0,0,0))
            screen.blit(txt,(x-txt.get_width()/2,y-txt.get_height()/2))
    
    screen.blit(images[hangman],(50, 50))
    pg.display.update()


while run:
    clock.tick(FPS)
    draw()
# Triggering the event
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run = False

        if event.type==pg.MOUSEBUTTONDOWN:

            x_mouse, y_mouse = pg.mouse.get_pos()
            #print(pos)

            for letter in letters:
                x,y,ltr,visible=letter

                if visible:
                    dist = math.sqrt((x - x_mouse) ** 2 + (y - y_mouse) ** 2)

                    if dist<=radius:
                        letter[3]=False # to invisible the clicked button
                        guessed.append(ltr)
                        if ltr not in words:
                            hangman +=1


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# deciding if you won the game or not
    won=True
    for letter in words:
        if letter not in guessed:
            won=False
            break

    if won:
        draw()
        pg.time.delay(1000)
        screen.fill((0,0,0,0))
        text=WORD.render("YOU WON!",1,(129,255,0,255))
        win.blit(text,(SCREEN_WIDTH/2 - text.get_width()/2, SCREEN_HEIGHT/2 - text.get_height()/2))
        pg.display.update()
        pg.time.delay(4000)
        print("WON")
        break

    if hangman==6:
        draw()
        pg.time.delay(1000)
        screen.fill((0, 0, 0, 0))
        text = WORD.render("YOU LOST", 1, (255, 0, 5, 255))
        answer=WORD.render("The answer is "+words,1,(129,255,0,0))
        screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2,
                           SCREEN_HEIGHT / 2 - text.get_height() / 2))
        screen.blit(answer, (( SCREEN_WIDTH / 2 - answer.get_width() / 2),
                             (SCREEN_HEIGHT / 2 - text.get_height() / 2)+70))
        
        pg.display.update()
        pg.time.delay(4000)
        print("LOST")
        break


pg.quit()