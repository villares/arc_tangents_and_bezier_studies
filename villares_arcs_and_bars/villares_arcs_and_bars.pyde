"""
Demo for var_bar, bar and var_bar_pts

var_bar can use b_arc (default) or p_arc (poly approximation internally based on arc_pts now)
var_bar_pts uses arc_pts
"""

from arcs import bar, var_bar, p_arc, var_bar_pts

mode = 0 

def setup():
    size(400, 400)

def draw():
    background(200)
    fill(0)
    text("press any key to see p_arc polygonal aprox. and var_bar_pts", 20, 20)
    fill(0, 0, 200, 100)
    strokeWeight(1)
    line(50, 50, 350, 250)
    if mode == 0:
        var_bar(50, 160, 350, 310, 40, 0) # by default arc_func=b_arc
        bar(50, 50, 350, 250, thickness=60, shorter=mouseX)
        var_bar(50, 250, 50 + mouseX * .7, 250 + mouseX * .25, 20, 40)
    elif mode == 1:   
        var_bar(50, 160, 350, 310, 40, 0, arc_func=p_arc, num_points=6)
        bar(50, 50, 350, 250, thickness=60, shorter=mouseX,
            arc_func=p_arc, num_points=3)
        var_bar(50, 250, 50 + mouseX / 2, 250 + mouseX * .20, 20, 40,
                arc_func=p_arc, num_points=8)
    else:
        pts1 = var_bar_pts(50, 160, 350, 310, 40, 0, num_points=6)
        pts2 = var_bar_pts(50, 50, 350, 250, 30, 30, shorter=mouseX, num_points=3)
        pts3 = var_bar_pts(50, 250, 50 + mouseX / 2, 250 + mouseX * .20, 20, 40,
                num_points=8)
        strokeWeight(5)
        for px, py in pts1 + pts2 + pts3:
            point(px, py)
        
def keyPressed():
    global mode
    mode = (mode + 1) % 3
