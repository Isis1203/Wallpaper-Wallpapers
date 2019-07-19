def setup(): 
    size (400, 715) 

def draw(): 
    background(0, 0, 50)
    y1 = 75
    y2 = 0
    i = 40
    # if i % 2 == 0:    
    while i <= 255: 
            noLoop()
            fill(0, 0, random(50, 255))
            noStroke() 
            triangle(0, y1, 41, y2, 80, y1)
            i = i + 11
            y1 = y1 + 36 
            y2 = y2 + 36            
    y1 = 0
    y2 = 75  
    i = 255
    # if i % 2 > 0:    
    while i >= 0: 
            noLoop()
            fill(0, 0, random(50, 255))
            noStroke() 
            triangle(100, y1, 140, y2, 180, y1)
            i = i - 10
            y1 = y1 + 30 
            y2 = y2 + 30
        
    y1 = 75
    y2 = 0
    i = 40
    # if i % 2 == 0:    
    while i <= 255: 
            noLoop()
            fill(0, 0, random(50, 255))
            noStroke() 
            triangle(200, y1, 240, y2, 280, y1)
            i = i + 11
            y1 = y1 + 36 
            y2 = y2 + 36
    y1 = 0
    y2 = 75  
    i = 255
    # if i % 2 > 0:
    while i >= 0: 
            noLoop()
            fill(0, 0, random(50, 255))
            noStroke() 
            triangle(300, y1, 340, y2, 380, y1)
            i = i - 10
            y1 = y1 + 30 
            y2 = y2 + 30
    fill(0, 0, 50)
    rect(0, 0, 400, 200)  
    
    

    
    
    
    
