def setup():
    background(0,0,0)
    fullScreen()
    
def draw():
    strokeWeight(random(5,10))
    stroke(random(0,255),random(0,255),random(0,255))
    line(width/2,height/2,(random(0,width)),(random(0,height)))
    strokeWeight(random(5,10))
    stroke(random(0,255),random(0,255),random(0,255))
    point(random(0,width),random(0,height))
