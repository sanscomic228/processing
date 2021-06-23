x = 0
y = 1
a = 2
z = 0
c = 0
def setup():
    global z
    z = height
    global c
    c = width
    background(0)
    fullScreen()
def draw():
    global x,y,a,z,c
    background(0)
    circle(y,height/2,55)
    y = y + 11
    circle(width/2,x,55)
    x = x + 10
    circle(a,a,55)
    a = a + 12
    circle(c,z,55)
    z = z - 13
    c = c - 14
    
    
    
    
    
