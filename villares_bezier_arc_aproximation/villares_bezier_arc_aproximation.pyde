""" 
 Written by Alexandre B A Villares for Processing Python Mode 
 Based on Golan Levin's approximating a circular arc with a cubic Bezier curve.
 http://www.flong.com/blog/2009/bezier-approximation-of-a-circular-arc-in-processing/
"""

radius = 300  # radius of the circular arc
cx = 340  # center poof the circular arc
cy = 340

def setup():
    size(680, 680)

#--------------------------
def draw():
    background(230)

    # Establish arc parameters.
    # (Note: assert theta != TWO_PI)
    theta = radians(mouseX / 1.8)  # spread of the arc.
    startAngle = radians(mouseY / 8.0)  # as in arc()
    endAngle = startAngle + theta        # as in arc()

    #--------------------------
    # RED IS THE "TRUE" ARC:
    noFill()
    strokeWeight(3)
    stroke(0, 0, 255, 128)
    arc(cx, cy, radius * 2, radius * 2, startAngle, endAngle)
    
    #--------------------------
    # RED IS THE BEZIER APPROXIMATION OF THE ARC:
    noFill()
    strokeWeight(3)
    stroke(255, 0, 0, 128)
    b_arc(cx, cy, radius * 2, radius * 2, startAngle, endAngle)


def b_arc(cx, cy, w, h, startAngle, endAngle):
    """
    A bezier approximation of an arc
    using the same signature as the original Processing arc()
    """
    theta = endAngle - startAngle
    
    if theta < HALF_PI:
        # Compute raw Bezier coordinates.
        x0 = cos(theta / 2.0)
        y0 = sin(theta / 2.0)
        x3 = x0
        y3 = 0 - y0
        x1 = (4.0 - x0) / 3.0
        if y0 != 0:
            y1 = ((1.0 - x0) * (3.0 - x0)) / (3.0 * y0)  # y0 != 0...
        else:
            y1 = 0
        x2 = x1
        y2 = 0 - y1
        # Compute rotationally-offset Bezier coordinates, using:
        # x' = cos(angle) * x - sin(angle) * y
        # y' = sin(angle) * x + cos(angle) * y
        bezAng = startAngle + theta / 2.0
        cBezAng = cos(bezAng)
        sBezAng = sin(bezAng)
        rx0 = cBezAng * x0 - sBezAng * y0
        ry0 = sBezAng * x0 + cBezAng * y0
        rx1 = cBezAng * x1 - sBezAng * y1
        ry1 = sBezAng * x1 + cBezAng * y1
        rx2 = cBezAng * x2 - sBezAng * y2
        ry2 = sBezAng * x2 + cBezAng * y2
        rx3 = cBezAng * x3 - sBezAng * y3
        ry3 = sBezAng * x3 + cBezAng * y3
    
        # Compute scaled and translated Bezier coordinates.
        rx, ry = w / 2.0, h / 2.0
        px0 = cx + rx * rx0
        py0 = cy + ry * ry0
        px1 = cx + rx * rx1
        py1 = cy + ry * ry1
        px2 = cx + rx * rx2
        py2 = cy + ry * ry2
        px3 = cx + rx * rx3
        py3 = cy + ry * ry3
        
        # Draw the arc
        bezier(px0, py0, px1, py1, px2, py2, px3, py3)
        
        # Debug points... comment this out!
        ellipse(px0, py0, 5, 5)
    
    else:
         b_arc(cx, cy, w, h, startAngle, endAngle - theta / 2.0)
         b_arc(cx, cy, w, h, startAngle + theta / 2.0, endAngle)
  
        
