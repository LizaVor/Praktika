import My1_Class2 as snake_objs
import time

delay=0.1
color_wnd='pink'
color_head='black'
color_snake='white'
color_food='red'
stop = False

screen=snake_objs.Screen(600,600,color_wnd)
food=snake_objs.Food(color_food,'square')

snakes=[snake_objs.Snake(i*30,i*50,'turtle',color_snake,color_head)
        for i in range(1)]

screen.proc_event(snakes)

while True:
    screen.update()

    for snake in snakes:
        snake.step()
        if snake.check_food(food):
            snake.grow()
            screen.plot_score()
            food.move()
        if snake.error():
            stop = True;
            screen.end()
            break
    if stop:
        break
    time.sleep(delay)
