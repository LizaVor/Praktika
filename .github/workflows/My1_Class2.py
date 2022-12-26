import turtle as t
import random

class Snake:

    def __init__(self,x,y,shape,color_snake,color_head):
        self.head=self.create_turtle(x,y,'triangle',color_head)
        self.snake=[self.create_turtle(-20*(i+1)+x,y,'circle',color_snake) for i in range(4)]
        self.color_snake=color_snake

    def create_turtle(self,x,y,shape,color):
        tmp=t.Turtle()
        tmp.shape(shape)
        tmp.penup()
        tmp.color(color)
        tmp.setx(x)
        tmp.sety(y)
        return tmp

    def step(self):
        (pos, hd)=(self.head.pos(),self.head.heading())
        for s in self.snake:
            (tmp_pos,tmp_hd)=(s.pos(),s.heading())
            s.setheading(hd)
            s.setpos(pos)
            (hd,pos)=(tmp_hd,tmp_pos)
        if self.head.xcor() >= 300:
            self.head.setx(-300)
        if self.head.ycor() >= 300:
            self.head.sety(-300)
        if self.head.xcor() < -300:
            self.head.setx(300)
        if self.head.ycor() < -300:
            self.head.sety(300)
        self.head.forward(20)
        
    def error(self):
        for i in range(1, len(self.snake)):
            if self.snake[0].distance(self.snake[i])<10:
                return True
        return False
    
    def check_food(self,food):
        if self.head.distance(food.food)<18:
            return True
        else:
            return False

    def grow(self):
        [x,y]=self.snake[-1].pos()
        self.snake.append(self.create_turtle(x,y,'circle',self.color_snake))

    def turn(self,angle):
        self.head.setheading(angle)

############################################################
class Screen:

    def __init__(self,width,height,color):
        self.wn=t.Screen()
        self.wn.title('Test game')
        self.wn.bgcolor(color)
        self.wn.setup(width=width, height=height)
        self.wn.tracer(0)
        self.score=0

    def proc_event(self,obj):
        self.objs=obj
        self.wn.listen()
        self.wn.onkeypress(self.goleft,"Left")
        self.wn.onkeypress(self.goright,"Right")
        self.wn.onkeypress(self.goup,"Up")
        self.wn.onkeypress(self.godown,"Down")

    def goleft(self):
        for head in self.objs:
            head.turn(180)

    def goright(self):
        for head in self.objs:
            head.turn(0)

    def goup(self):
        for head in self.objs:
            head.turn(90)

    def godown(self):
        for head in self.objs:
            head.turn(270)

    def update(self):
        self.wn.update()

    def plot_score(self):
        self.score+=1
        self.wn.title('Score ' + str(self.score))
                      
    def end(self):
        end_text = t.Turtle()
        end_text.hideturtle()
        end_text.color('black')
        end_text.penup()
        end_text.goto(-110,-80)
        end_text.write('Game Over... \nUps..\nResult:' + str(self.score), font=('Times New Roman', 40))
######################################
class Food:
    def __init__(self,color,shape):
        self.food=t.Turtle()
        self.food.shape(shape)
        self.food.penup()
        self.food.color(color)
        self.move

    def move(self):
        self.food.setpos(random.randrange(-280,280,20),random.randrange(-280,280,20))
