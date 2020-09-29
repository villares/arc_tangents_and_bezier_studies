# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

# github.com/villares/villares
from arcs import arc_filleted_poly, arc_augmented_poly  
from line_geometry import poly  # arc_augmented_polu also needs this

def setup():
    size(400, 200)

    p_list = [(30, 160), (250, 50), (350, 150), (200, 100)]
    r_list = [20, 30, 40, 30]
    
    noStroke()
    strokeJoin(ROUND)
    poly(p_list)
    stroke(180)
    noFill()
    for p, r in zip(p_list, r_list): circle(p[0], p[1], r*2)
    noFill()
    stroke(0)
    # arc_filleted_poly(p_list,r_list)
    # saveFrame('arc_filleted_poly.png')
    arc_augmented_poly(p_list,r_list)
    saveFrame('arc_augmented_poly.png')
