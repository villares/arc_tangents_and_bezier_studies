"""
Demo for bar and var_bar
"""

from arcs import bar, var_bar, p_arc

def setup():
    size(500, 500)
    
def draw():
    global a_arc
    background(200)
    fill(0)
    text("press any key to see p_arc polygonal aproximantion used", 20, 20)
    fill(0, 0, 200, 100)    
    line(150, 50, 350, 250)
    if not keyPressed:
        # By default arc_func=b_arc
        var_bar(150, 160, 350, 310, 40, 0)
        bar(150, 50, 350, 250, thickness=60, shorter=mouseX)
        var_bar(150, 250, 150 + mouseX / 2, 250 + mouseX *.40, 20, 60)  
    else:
        var_bar(150, 160, 350, 310, 40, 0, arc_func=p_arc, num_points=6)
        bar(150, 50, 350, 250, thickness=60, shorter=mouseX,
            arc_func=p_arc,num_points=3)
        var_bar(150, 250, 150 + mouseX / 2, 250 + mouseX *.40, 20, 60,
                arc_func=p_arc, num_points=8)

        
