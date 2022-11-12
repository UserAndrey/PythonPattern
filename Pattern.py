import turtle
t=turtle.Turtle()
t.speed(4500)
t.color('cyan')
t.screen.bgcolor('black')
def circle(p):
  for i in range(75):
    t.circle(40)
    t.left(p)
def square(tf,left,r):
  f=60
  for i in range(r):
    t.fd(f)
    t.left(tf)
    t.fd(f)
    t.left(tf)
    t.fd(f)
    t.left(tf)
    t.fd(f)
    t.left(left)
def spiral(left):
  for i in range(109):
    for color in ['white','cyan']:
      t.color(color)
      t.fd(i)
      t.left(left)
def help(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
circle(10)
help(-300,100)
square(30,130,90)
help(90,270)
square(90,100,80)
help(-90,-170)
square(-30,200,80)
help(-180,-150)
square(45,301,100)
help(-180,450)
square(100,22,80)
help(250,-200)
square(302,13,90)
help(300,450)
spiral(30)
help(-300,-520)
spiral(50)
help(0,-450)
spiral(188)
help(100,500)
square(810,1,60)
help(-290,230)
square(-50,560,80)
turtle.done()
