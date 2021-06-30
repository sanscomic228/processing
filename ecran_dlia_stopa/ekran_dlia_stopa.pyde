x = 0
y = 1
v = 22
z = 155
a = 0
def setup():
    global x,y
    background(0)
    fullScreen()
    x = width/2
    y = height/2
def draw():
    global x,y,v,z,a
    strokeWeight(20)
    stroke(random(0,255),random(0,255),random(0,255))
    line(x,y,v,z)
    x = x + random(-100,100)
    y = y + random(-100,100)
    z = z + random(-100,100)
    v = v + random(-100,100)
    a = a + 1
    if x <= 0:
       x = 0
    if z <= 0:
       z = 0
    if v <= 0:
       v = 0
    if y <= 0:
       y = 0 
       if a >= 300:
        background(0,0,205)
        text('''A problem has been detected and Windows has been shut down to prevent damage
        to your computer.
        
        DRAGONITE_HAS_NO_LIFE
        
        If this is the first time you've seen this Stop error screen,
        restart your computer. If this screen appears again, follow
        these steps:
        
        Actually, don't do anything. BSODs are good for your health.
        (If you work for Apple, that is.)
        
        If problems continue, disable or remove any newly installed hardware
        or software. Disable BIOS memory options such as caching or shadowing.
        Of course, you could simply not run anything else that Dragonite uploads to Wizirbi again.
        
        Technical information:
        
        *** STOP: 0/000000D1 (0x000000002, 0x00000000, 0x00001337)
        
        ***       trololo.sys - Address 1337000 base at 10101010, Datestamp 00000000
        
        Begin dump of physical memory
              
                    
      '''      
        noLoop()
        
    
        
        
    
    
