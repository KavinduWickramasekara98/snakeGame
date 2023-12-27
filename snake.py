from turtle import Turtle
INIT_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.box_lists=[]
        self.create_snake()
        self.head = self.box_lists[0]
    def create_snake(self):
        for position in INIT_POSITIONS:
            new_box=Turtle("square")
            new_box.color("white")
            new_box.penup()
            new_box.goto(position)
            self.box_lists.append(new_box)
    def move(self):
        for index in range(len(self.box_lists)-1,0,-1):
            new_x=self.box_lists[index-1].xcor()
            new_y=self.box_lists[index-1].ycor()
            self.box_lists[index].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)