# template for "Stopwatch: The Game"

import simplegui
import math

# define global variables
time = 0
hits = 0
attempts = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):    
    seconds = str((t % 600)/10)    
    minutes = str(t/600)
    tenths = str(t % 10)
    if (len(seconds) == 1):
        seconds = "0" + seconds
    return minutes + ":" + seconds + "." + tenths
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global hits, attempts
    if (timer.is_running()):
        attempts += 1
        if (time % 10 == 0):
            hits += 1
        timer.stop()

def reset():
    global time, hits, attempts
    time = 0
    hits = 0
    attempts = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [100, 100], 20, "White")
    canvas.draw_text(str(hits) + "/" + str(attempts), [150, 10], 15, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)
timer = simplegui.create_timer(100, timer)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
