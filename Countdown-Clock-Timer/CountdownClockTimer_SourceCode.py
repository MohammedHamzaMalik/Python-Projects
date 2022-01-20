import time
import turtle

window = turtle.Screen()
window.tracer(0)

player = turtle.Turtle()
timer_text = turtle.Turtle()

start = time.time()
while time.time() - start < 5:
    player.forward(1)
    player.left(1)
    timer_text.clear()
    timer_text.write(int(time.time() - start), font=("Courier", 30))

    window.update()