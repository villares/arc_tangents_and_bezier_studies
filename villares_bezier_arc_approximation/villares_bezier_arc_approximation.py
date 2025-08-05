""" 
 Written by Alexandre B A Villares for py5 <py5coding.org> imported mode
 Based on Golan Levin's approximating a circular arc with a cubic Bezier curve.
 http://www.flong.com/blog/2009/bezier-approximation-of-a-circular-arc-in-processing/
"""

DEBUG = False
radius = 300  # radius of the circular arc
cx = 340  # center of the circular arc
cy = 340

def setup():
    size(680, 680)

def draw():
    background(230)
    stroke_weight(3)

    # Establish arc parameters. Note: assert theta != TWO_PI)
    theta = radians(mouse_x / 1.8)  # spread of the arc.
    start_angle = radians(mouse_y / 8.0)  # as in arc()
    end_angle = start_angle + theta       # as in arc()

    # BLUE IS THE "TRUE" ARC:
    fill(0, 0, 255, 10)
    stroke(0, 0, 255, 128)
    arc(cx, cy, radius * 2, radius * 2, start_angle, end_angle)
    
    # RED IS THE BEZIER APPROXIMATION OF THE ARC:
    fill(255,0,0, 10)
    stroke(255, 0, 0, 128)
    b_arc(cx, cy, radius * 2, radius * 2, start_angle, end_angle)


def b_arc(cx, cy, w, h, start_angle, end_angle, mode=0):
    """
    Draw a bezier approximation of an arc using the same
    signature as the original Processing arc().
    mode: 0 "normal" arc, using begin_shape() and end_shape()
          1 "middle" used in recursive call of smaller arcs
          2 "naked" like normal, but without begin_shape() and
             end_shape() for use inside a larger PShape/Py5Shape.
    """
    # Based on ideas from Richard DeVeneza via code by Golan Levin:
    # http://www.flong.com/blog/2009/bezier-approximation-of-a-circular-arc-in-processing/
    theta = end_angle - start_angle
    # Compute raw Bezier coordinates.
    if mode != 1 or abs(theta) < HALF_PI:
        x0 = cos(theta / 2.0)
        y0 = sin(theta / 2.0)
        x3 = x0
        y3 = 0 - y0
        x1 = (4.0 - x0) / 3.0
        y1 = ((1.0 - x0) * (3.0 - x0)) / (3.0 * y0) if y0 != 0 else 0
        x2 = x1
        y2 = 0 - y1
        # Compute rotationally-offset Bezier coordinates, using:
        # x' = cos(angle) * x - sin(angle) * y
        # y' = sin(angle) * x + cos(angle) * y
        bezAng = start_angle + theta / 2.0
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
        if DEBUG:
            ellipse(px3, py3, 3, 3)
            ellipse(px0, py0, 5, 5)
    # Drawing
    if mode == 0:  # 'normal' arc (not 'middle' nor 'naked')
        begin_shape()
    if mode != 1:  # if not 'middle'
        vertex(px3, py3)
    if abs(theta) < HALF_PI:
        bezier_vertex(px2, py2, px1, py1, px0, py0)
    else:
        # to avoid distortion, break into 2 smaller arcs
        b_arc(cx, cy, w, h, start_angle, end_angle - theta / 2.0, mode=1)
        b_arc(cx, cy, w, h, start_angle + theta / 2.0, end_angle, mode=1)
    if mode == 0:  # end of a 'normal' arc
        end_shape()
        
