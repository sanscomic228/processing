x = 0
y = 1
v = 22
z = 155
def setup():
    global x,y
    background(0)
    fullScreen()
    x = width/2
    y = height/2
def draw():
    global x,y,v,z
    strokeWeight(20)
    stroke(random(0,255),random(0,255),random(0,255))
    line(x,y,v,z)
    x = x + random(-100,100)
    y = y + random(-100,100)
    z = z + random(-100,100)
    v = v + random(-100,100)
    
    
