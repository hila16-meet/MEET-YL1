import turtle

shape="circle"
size=50

# initialization
turtle.penup()
turtle.goto(-300,0)
turtle.clear()
turtle.pendown()
turtle.shape("classic")
turtle.pensize(5)
turtle.pencolor("red")

def print_square_brush(x,y):
    global size
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(size)
    turtle.left(90)
    turtle.forword(size)
    turtle.left(90)
    turtle.forword(size)
    turtle.left(90)
    turtle.forword(size)
    turtle.end_fill()
    turtle.penup()

def print_circle_brush(x,y):
    global size
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.circle(size)
    turtle.end_fill()
    
    turtle.penup()

def drawShape(x,y):
    if shape == "circle":
        print_circle_brush(x,y)
    elif shape=="square":
        print_square_brush(x,y)
        
#turtle.onscreenclick(print_square_brush, btn=3, add=True)

#def switch_shape():
    #turtle.onscreenclick(print_square_brush, btn=3, add=True)
    #shape = "square" 


#turtle.getscreen().onkeypress(onscreenclick(turtle.goto), "d")

turtle.onscreenclick(drawShape)

#turtle.getscreen().onkeypress(change_color,"")

#print_squre_brush(size) 
#print_circle_brush(size)

#turtle.onscreenclick(print_square_brush, btn=3, add=True)

"""if turtle.onscreenclick(print_square_brush, btn=3, add=True):
    shape = "square" """
turtle.mainloop()
