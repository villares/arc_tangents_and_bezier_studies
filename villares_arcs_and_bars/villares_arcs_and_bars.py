"""
Demo for
- var_bar: Tangent/tangent shape on 2 circles of arbitrary radius;
  It uses the b_arc funtion, Bezier approximation of arcs
  but it can also use p_arc, a poly approximation.  
- bar: simplified version, both ends with same radius;
- var_bar_pts: but provides vertex coords for a var_bar-like shape
  using arc_pts like the p_arc function does.
"""

from arcs import bar, var_bar, p_arc, var_bar_pts

mode = 0 

def setup():
    size(400, 400)

def draw():
    background(200)
    fill(0)
    text('click to toggle p_arc polygonal approx. and var_bar_pts', 20, 20)
    text(('var_bar with b_arc', 'var_bar with p_arc', 'var_bar_pts')[mode], 20, 380)
    fill(0, 0, 200, 100)
    stroke_weight(1)
    line(50, 50, 350, 250)
    if mode == 0:
        var_bar(50, 165, 350, 315, 40, 0) # by default arc_func=b_arc
        bar(50, 55, 350, 255, thickness=60, shorter=mouse_x)
        var_bar(50, 255, 50 + mouse_x * 0.6, 255 + mouse_x * 0.25, 20, 40)
    elif mode == 1:   
        var_bar(50, 165, 350, 315, 40, 0, arc_func=p_arc, num_points=6)
        bar(50, 55, 350, 255, thickness=60, shorter=mouse_x,
            arc_func=p_arc, num_points=3)
        var_bar(50, 255, 50 + mouse_x * 0.6, 255 + mouse_x * 0.25, 20, 40,
                arc_func=p_arc, num_points=8)
    else:
        pts1 = var_bar_pts(50, 165, 350, 315, 40, 0, num_points=6)
        pts2 = var_bar_pts(50, 55, 350, 255, 30, 30, shorter=mouse_x, num_points=3)
        pts3 = var_bar_pts(50, 255, 50 + mouse_x * 0.6, 255 + mouse_x * 0.25, 20, 40,
                num_points=8)
        stroke_weight(5)
        points(pts1 + pts2 + pts3)
        
def mouse_pressed():
    global mode
    mode = (mode + 1) % 3
