import simplegui

decisecond = 0    # 1 decisecond = 100 milisecond
x = 0
y = 0
D = "0"
timer_on = False
 
def format():
    """helper function format the time"""
    global D
    second = decisecond / 10
    minute = second / 60
    if minute == 60:
        print "Reach upper limit. Reset stopwatch!"
        reset_button()    
    D = str(decisecond % 10) #D is the output for deciseconds limited withing 0-9 
    BC = str(second % 60)    #BD is str output for second limited within 0-59
    A = str(minute % 60)     #A is str output for minute limited within 0-59
    if len(BC) == 1:         #when BD is single digit, add "0" before 
        BC = "0" + BC
    if len(A) == 1:          #when A is single digit, add "0" before
        A = "0" + A   
    watch_reading = A + ":" + BC + "." + D
    return watch_reading
 
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    global timer_on
    timer_on = True
    time.start()

def stop_button():
    global timer_on, x, y
    if timer_on == True:
        if D == "0":
            x += 1
        else:
            y += 1
    timer_on = False
    time.stop()    

def reset_button():
    global decisecond, x, y
    decisecond = 0
    x = 0
    y = 0
    
# define event handler for timer with 0.1 sec interval
def time_handler():
    global decisecond
    decisecond += 1
    format()
        
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(), [85, 104], 30, "white")
    canvas.draw_text(str(x) + "/" + str(y), [130, 50], 25, "red")
    
# create frame
f = simplegui.create_frame("Stopwatch Game", 260, 180)

# register event handlers
f.add_button("Start", start_button, 100)
f.add_button("Stop", stop_button, 100)
f.add_button("Reset", reset_button, 100)
f.set_draw_handler(draw_handler)
time = simplegui.create_timer(100, time_handler)

# start frame
f.start()

