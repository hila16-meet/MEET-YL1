import turtle
shape = "circle"
color = "tomato3"
size = 50

# initialization
turtle.penup()
turtle.goto(-300,0)
turtle.clear()
turtle.pendown()
turtle.shape("blank")
turtle.pensize(5)
turtle.color(color, color)

def print_square_brush(x,y):
    global size
    turtle.penup()
    turtle.goto(x + size, y + size)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(size * 2)
    turtle.left(90)
    turtle.forward(size * 2)
    turtle.left(90)
    turtle.forward(size * 2)
    turtle.left(90)
    turtle.forward(size * 2)
    turtle.end_fill()
    turtle.penup

def print_circle_brush(x,y):
    global size
    turtle.penup()
    turtle.goto(x, y - size)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(size)
    turtle.end_fill()
    turtle.penup()

def draw_shape(x,y):
    global shape
    if shape == "circle":
        print_circle_brush(x,y)
    else:
        print_square_brush(x,y)

def change_shape():
    global shape
    if shape == "circle":
        shape = "square"
    else:
        shape = "circle"

def change_color():
    global color
    if color == "tomato3":
        color = "cyan4"
    else:
        color = "tomato3"
    turtle.color(color, color)

def bigger():
    print("bigger")
    global size
    size += 10

def smaller():
    print("smaller")
    global size
    size -= 10

turtle.listen()
turtle.onkeypress(change_shape, "s")
turtle.onkeypress(change_color, "c")
turtle.onkeypress(bigger, "plus")
turtle.onkeypress(smaller, "minus")
turtle.onscreenclick(draw_shape, btn=1)

turtle.mainloop()