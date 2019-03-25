def setup():
    size(500, 500)
    
def draw():
    background(200)

    a = PVector(200, 250)
    b = PVector(mouseX, mouseY)
    ra, rb = 75, 25
    strokeWeight(1)
    ellipse(b.x, b.y, rb*2, rb*2)
    ellipse(a.x, a.y, ra*2, ra*2)
    line(a.x, a.y, b.x, b.y)
    strokeWeight(2)
    circ_circ_tangent(b, a, rb, ra)
    
def circ_circ_tangent(p1, p2, r1, r2):
    d = dist(p1.x, p1.y, p2.x, p2.y)    
    ri = r1 - r2
    if d > abs(ri):
        line_angle = atan2(p1.x - p2.x, p2.y - p1.y)
        theta = asin(ri / d)
        
        x1 = cos(line_angle - theta) * r1
        y1 = sin(line_angle - theta) * r1
        x2 = cos(line_angle - theta) * r2
        y2 = sin(line_angle - theta) * r2
        line(p1.x - x1, p1.y - y1, p2.x - x2, p2.y - y2)

        x1 = -cos(line_angle + theta) * r1
        y1 = -sin(line_angle + theta) * r1
        x2 = -cos(line_angle + theta) * r2
        y2 = -sin(line_angle + theta) * r2
        line(p1.x - x1, p1.y - y1, p2.x - x2, p2.y - y2)        
    else:
        println("not possible")
    
