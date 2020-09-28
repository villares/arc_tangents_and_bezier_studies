
from pyp5js import *

"""
Demo for bar and var_bar
"""

def setup():
    size(400, 400)

def draw():
    background(200)
    fill(0)
    text("press any key to see p_arc polygonal aproximantion used", 20, 20)
    fill(0, 0, 200, 100)
    line(50, 50, 350, 250)
    if not keyIsPressed:
        # By default arc_func=b_arc
        bar(50, 50, 350, 250, 60, shorter=mouseX)
        var_bar(50, 160, 350, 310, 40, 0)
        var_bar(50, 250, 50 + mouseX * .7, 250 + mouseX * .25, 20, 40)
    else:
        bar(50, 50, 350, 250, thickness=60, shorter=mouseX,
            arc_func=p_arc, num_points=3)
        var_bar(50, 160, 350, 310, 40, 0, arc_func=p_arc, num_points=6)
        var_bar(50, 250, 50 + mouseX / 2, 250 + mouseX * .20, 20, 40,
                arc_func=p_arc, num_points=8)

"""
From github.com/villares/villares/arcs.py

2020-09-22 Merges/renames several versions of the arc related functions
2020-09-24 Updates arc_filleted_poly and arc_augmented_poly
2020-09-25 Added bar() and var_bar()
2020-09-26 Moved code from bar() to var_bar() and added several new kwargs
"""
#from warnings import warn
#from line_geometry import is_poly_self_intersecting, triangle_area

def PVector(v):
   return createVector(v)

DEBUG = False
ROTATION = {0: 0,
            # BOTTOM: 0,
            # DOWN: 0,
            1: HALF_PI,
            # LEFT: HALF_PI,
            2: PI,
            # TOP: PI,
            # UP: PI,
            3: PI + HALF_PI,
            # RIGHT: PI + HALF_PI,
            # BOTTOM + RIGHT: 0,
            # DOWN + RIGHT: 0,
            # DOWN + LEFT: HALF_PI,
            # BOTTOM + LEFT: HALF_PI,
            # TOP + LEFT: PI,
            # UP + LEFT: PI,
            # TOP + RIGHT: PI + HALF_PI,
            # UP + RIGHT: PI + HALF_PI,
            }

def circle_arc(x, y, radius, start_ang, sweep_ang, *args, **kwargs):
    arc_func = kwargs.pop('arc_func', arc)
    arc_func(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang, *args, **kwargs)

def quarter_circle(x, y, radius, quadrant, *args, **kwargs):
    circle_arc(x, y, radius, ROTATION[quadrant], HALF_PI, *args, **kwargs)

def half_circle(x, y, radius, quadrant, *args, **kwargs):
    circle_arc(x, y, radius, ROTATION[quadrant], PI, *args, **kwargs)

def b_circle_arc(x, y, radius, start_ang, sweep_ang, mode=0):
    b_arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang,
          mode=mode)

def b_arc(cx, cy, w, h, start_angle, end_angle, mode=0):
    """
    Draw a bezier approximation of an arc using the same
    signature as the original Processing arc().
    mode: 0 "normal" arc, using beginShape() and endShape()
          1 "middle" used in recursive call of smaller arcs
          2 "naked" like normal, but without beginShape() and
             endShape() for use inside a larger PShape.
    """
    # Based on ideas from Richard DeVeneza via code by Gola Levin:
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
        beginShape()
    if mode != 1:  # if not 'middle'
        vertex(px3, py3)
    if abs(theta) < HALF_PI:
        bezierVertex(px2, py2, px1, py1, px0, py0)
    else:
        # to avoid distortion, break into 2 smaller arcs
        b_arc(cx, cy, w, h, start_angle, end_angle - theta / 2.0, mode=1)
        b_arc(cx, cy, w, h, start_angle + theta / 2.0, end_angle, mode=1)
    if mode == 0:  # end of a 'normal' arc
        endShape()

def p_circle_arc(x, y, radius, start_ang, sweep_ang, mode=0, **kwargs):
    p_arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang,
          mode=mode, **kwargs)

def p_arc(cx, cy, w, h, start_angle, end_angle, mode=0,
          num_points=24, vertex_func=vertex):
    """
    A poly approximation of an arc using the same
    signature as the original Processing arc().
    mode: 0 "normal" arc, using beginShape() and endShape()
          2 "naked" like normal, but without beginShape() and
             endShape() for use inside a larger PShape.
    """
    sweep_angle = end_angle - start_angle
    if mode == 0:
        beginShape()
    if sweep_angle < 0:
        start_angle, end_angle = end_angle, start_angle
        sweep_angle = -sweep_angle
        angle = float(sweep_angle) / abs(num_points)
        a = end_angle
        while a >= start_angle:
            sx = cx + cos(a) * w / 2.0
            sy = cy + sin(a) * h / 2.0
            vertex_func(sx, sy)
            a -= angle
    elif sweep_angle > 0:
        angle = sweep_angle / int(num_points)
        a = start_angle
        while a <= end_angle:
            sx = cx + cos(a) * w / 2.0
            sy = cy + sin(a) * h / 2.0
            vertex_func(sx, sy)
            a += angle
    else:  # sweep_angle == 0
        sx = cx + cos(start_angle) * w / 2.0
        sy = cy + sin(start_angle) * h / 2.0
        vertex_func(sx, sy)
    if mode == 0:
        endShape()




def bar(x1, y1, x2, y2, thickness, **kwargs):
    """
    Draw a thick strip with rounded ends.
    It can be shorter than the supporting (axial) line segment.

    # 2020-9-25 First rewrite attempt based on var_bar + arc_func + **kwargs
    # 2020-9-26 Let's do everything in var_bar()!
    """
    var_bar(x1, y1, x2, y2, thickness / 2, **kwargs)

def var_bar(p1x, p1y, p2x, p2y, r1, r2=None, **kwargs):
    """
    Tangent/tangent shape on 2 circles of arbitrary radius

    # 2020-9-25 Added **kwargs, now one can use arc_func=p_arc & num_points=N   
    # 2020-9-26 Added treatment to shorter=N so as to incorporate bar() use.
                Added a keyword argument, internal=True is the default,
                internal=False disables drawing internal circles.
                Minor cleanups, and removed "with" for pushMatrix().
    """
    r2 = r2 if r2 is not None else r1
    draw_internal_circles = kwargs.pop('internal', True)
    arc_func = kwargs.pop('arc_func', b_arc)
    shorter = kwargs.pop('shorter', 0)
    assert not (shorter and r1 != r2),\
        "Can't draw shorter var_bar with different radii"
    d = dist(p1x, p1y, p2x, p2y)
    ri = r1 - r2
    if d > abs(ri):
        clipped_ri_over_d = min(1, max(-1, ri / d))
        beta = asin(clipped_ri_over_d) + HALF_PI
        pushMatrix()
        translate(p1x, p1y)
        angle = atan2(p1x - p2x, p2y - p1y)
        rotate(angle + HALF_PI)
        x1 = cos(beta) * r1
        y1 = sin(beta) * r1
        x2 = cos(beta) * r2
        y2 = sin(beta) * r2
        beginShape()
        offset = shorter / 2.0 if shorter < d else d / 2.0
        arc_func(offset, 0, r1 * 2, r1 * 2,
                 -beta - PI, beta - PI, mode=2, **kwargs)
        arc_func(d - offset, 0, r2 * 2, r2 * 2,
                 beta - PI, PI - beta, mode=2, **kwargs)
        endShape(CLOSE)
        popMatrix()
    elif draw_internal_circles:
        arc_func(p1x, p1y, r1 * 2, r1 * 2, 0, TWO_PI, **kwargs)
        arc_func(p2x, p2y, r2 * 2, r2 * 2, 0, TWO_PI, **kwargs)



