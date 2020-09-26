"""
Demo for bar and var_bar
Pressa any key to see p_arc polygonal aproximantion used
"""

from arcs import bar, var_bar, p_arc

def setup():
    size(500, 500)
    
def draw():
    global a_arc
    background(200)

    fill(0, 0, 200, 100)    
    line(150, 250, 350, 450)
    if not keyPressed:
        var_bar(150, 50, 350, 200, 20, 60)  # arc_func=b_arc
        var_bar(150, 180, 350, 330, 40, 0)
        bar(150, 250, 350, 450, thickness=60, shorter=100)
    else:
        var_bar(150, 50, 350, 200, 20, 60, p_arc, num_points=4)
        var_bar(150, 180, 350, 330, 40, 0, p_arc, num_points=6)
        bar(150, 250, 350, 450, thickness=60, shorter=100,
            arc_func=p_arc,num_points=3)

        
