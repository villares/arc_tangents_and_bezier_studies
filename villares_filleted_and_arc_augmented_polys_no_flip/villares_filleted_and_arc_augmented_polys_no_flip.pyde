# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

# github.com/villares/villares
from arcs import arc_filleted_poly, arc_augmented_poly

def setup():
    size(400, 400)

def draw():
    background(200)
    p_list = [(30, 160), (250, 50), (350, 150), (mouseX, mouseY)]    
    if mousePressed:
        r_list = [20, 30, 40, -30]
    else:
        r_list = [20, 30, 40, 30]
    noStroke()
    strokeJoin(ROUND)
    fill(255)
    draw_poly(p_list)
    noFill()
    stroke(0)
    arc_augmented_poly(p_list, r_list, auto_flip=keyPressed)

    stroke(180)
    noFill()
    for p, r in zip(p_list, r_list): circle(p[0], p[1], r*2)
    
def draw_poly(pts):
    beginShape()
    for x, y in pts:
        vertex(x, y)
    endShape(CLOSE)
