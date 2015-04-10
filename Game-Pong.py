import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

def spawn_ball(direction):
    global ball_vel, ball_pos
    ball_vel = [0, 0]
    ball_pos = [300, 200]
    if direction == "Right":
        ball_vel = [random.randrange(2, 4), -(random.randrange(1, 3))]
    if direction == "Left":
        ball_vel = [-(random.randrange(2, 4)), -(random.randrange(1, 3))]        

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2 
    paddle1_pos, paddle2_pos = 160, 160
    paddle1_vel, paddle2_vel = 0, 0
    score1, score2 = 0, 0 
    spawn_ball("Right")
       
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
# update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
# bounce the ball against the wall and the gutter
    if ball_pos[1] <= 20 or ball_pos[1] >= 380:
        ball_vel[1] = -ball_vel[1]
# initialized the ball or bounce the ball back off the paddle
    if ball_pos[0] <= 28:
        if paddle1_pos <= ball_pos[1] <= (paddle1_pos + 80): 
            ball_vel[0] = -1.1*ball_vel[0]
        else:
            spawn_ball("Right")
            score2 += 1
    if ball_pos[0] >= 572: 
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos + 80): 
            ball_vel[0] = -1.1*ball_vel[0]
        else:
            spawn_ball("Left")
            score1 += 1
# update the paddle position
    if 0 <= paddle1_pos + paddle1_vel <= 320:
        paddle1_pos += paddle1_vel
    if 0 <= paddle2_pos + paddle2_vel <= 320:
        paddle2_pos += paddle2_vel
# draw current paddle position
    canvas.draw_polygon([(0, paddle1_pos),(8, paddle1_pos),
                (8, paddle1_pos + 80),(0, paddle1_pos + 80)],1,"White","White")  
    canvas.draw_polygon([(592, paddle2_pos),(600, paddle2_pos),
                (600, paddle2_pos + 80),(592, paddle2_pos + 80)],1,"White","White")
    canvas.draw_circle((ball_pos[0], ball_pos[1]), 20, 1, "White", "White")  
# draw scores
    score_board = str(score1) + ":" + str(score2)
    canvas.draw_text(score_board, [270, 80], 48, "Red") 
# draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

def button_handler():
    new_game()
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']: paddle2_vel = -10
    elif key == simplegui.KEY_MAP['down']: paddle2_vel = 10
    elif key == simplegui.KEY_MAP['w']: paddle1_vel = -10
    elif key == simplegui.KEY_MAP['s']: paddle1_vel = 10

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']: paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']: paddle2_vel = 0
    elif key == simplegui.KEY_MAP['w']: paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']: paddle1_vel = 0
        
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
button1 = frame.add_button('Reset', button_handler, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

new_game()
frame.start()
