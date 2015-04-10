import simplegui
import random

def new_game():
    global cards, state, exposed, onecardx, twocardx, turns, lable
    cards = range(8)
    cards.extend(cards)
    random.shuffle(cards)
    exposed = [False]*16
    state, onecardx, twocardx, turns = 0, 0, 0, 0
    lable = "Turns = 0"

def mouseclick(pos):
    global state, exposed, lable, onecardx, twocardx, turns
    cardx = pos[0]//50
    if exposed[cardx] == False:
        if state == 0:
            onecardx = cardx
            exposed[cardx] = True
            state = 1
        elif state == 1:
            twocardx = cardx
            exposed[cardx] = True
            if cards[onecardx] != cards[twocardx]:
                state = 2
                turns += 1
            else:
                state = 0
                turns += 1
            lable = "Turns = " + str(turns)
        else:
            exposed[cardx] = True
            exposed[onecardx] = False
            exposed[twocardx] = False
            onecardx = cardx
            state = 1
    
def draw(canvas):
    for i in range(16):
        if exposed[i] == False:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 100], [i*50, 100]], 1, "Black", "Green")
        else:
            canvas.draw_text(str(cards[i]), [50*i+10, 60], 48, "White")
    label.set_text(lable)
        
new_game()

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label(lable)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)

frame.start()
