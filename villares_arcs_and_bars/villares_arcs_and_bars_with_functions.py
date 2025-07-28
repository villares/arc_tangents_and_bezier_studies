"""
Demo for
- var_bar: Tangent/tangent shape on 2 circles of arbitrary radius;
  It uses the b_arc funtion, Bezier aproximation of arcs
  but it can also use p_arc, a poly approximation.  
- bar: simplified version, both ends with same radius;
- var_bar_pts: but provides vertex coords for a var_bar-like shape
  using arc_pts like the p_arc function does.
"""

mode = 0 

def setup():
    size(400, 400)

def draw():
    background(200)
    fill(0)
    text('click to toggle p_arc polygonal aprox. and var_bar_pts', 20, 20)
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
    """
    r2 = r2 if r2 is not None else r1
    draw_internal_circle = kwargs.pop('internal', True)
    arc_func = kwargs.pop('arc_func', b_arc)
    shorter = kwargs.pop('shorter', 0)
    assert not (shorter and r1 != r2),\
        "Can't draw shorter var_bar with different radii. r1={} r2={}".format(r1, r2)
    assert not (kwargs and arc_func == b_arc),\
        "Can't use keyword arguments with b_arc. {}".format(kwargs)
    d = dist(p1x, p1y, p2x, p2y)
    ri = r1 - r2
    if d > abs(ri):
        clipped_ri_over_d = min(1, max(-1, ri / d))
        beta = asin(clipped_ri_over_d) + HALF_PI
        push()
        translate(p1x, p1y)
        angle = atan2(p1x - p2x, p2y - p1y)
        rotate(angle + HALF_PI)
        begin_shape()
        offset = shorter / 2.0 if shorter < d else d / 2.0
        arc_func(offset, 0, r1 * 2, r1 * 2,
                 -beta - PI, beta - PI, mode=2, **kwargs)
        arc_func(d - offset, 0, r2 * 2, r2 * 2,
                 beta - PI, PI - beta, mode=2, **kwargs)
        end_shape(CLOSE)
        pop()
    else:  # draw a circle with the bigger radius if distance is too small
        r = max(r1, r2)
        x, y = (p1x, p1y) if r1 > r2 else (p2x, p2y)
        arc_func(x, y, r * 2, r * 2, 0, TWO_PI, **kwargs)
        if draw_internal_circle:
            r = min(r1, r2)
            x, y = (p1x, p1y) if r1 < r2 else (p2x, p2y)
            arc_func(x, y, r * 2, r * 2, 0, TWO_PI, **kwargs)


def b_arc(cx, cy, w, h, start_angle, end_angle, mode=0):
    """
    Draw a bezier approximation of an arc using the same
    signature as the original Processing arc().
    mode: 0 "normal" arc, using begin_shape() and end_shape()
          1 "middle" used in recursive call of smaller arcs
          2 "naked" like normal, but without begin_shape() and
             end_shape() for use inside a larger PShape/Py5Shape.
    """
    DEBUG = False
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

def p_arc(cx, cy, w, h, start_angle, end_angle, mode=0,
          num_points=24, vertex_func=None):
    """
    A poly approximation of an arc using the same signature as
    the original Processing arc().
    
    mode: 0 "normal" arc-like, using begin_shape() and end_shape()
          1 "middle" not implemented on p_arc, used on recursive b_arc 
          2 "naked" like normal, but without begin_shape() and
             end_shape() for use inside a larger PShape/Py5Shape.
    """
    if mode == 0:
        begin_shape()
    vertex_pts = arc_pts(cx, cy, w, h, start_angle, end_angle, num_points)
    if vertex_func is None or vertex_fun == vertex:
        vertices(vertex_pts)
    else:
        for vx, vy in vertex_pts:
            vertex_func(vx, vy)
    if mode == 0:
        end_shape()

def arc_pts(cx, cy, w, h, start_angle, end_angle, num_points=24):
    """
    Returns points approximating an arc using the same
    signature as the original Processing arc().
    """
    sweep_angle = end_angle - start_angle
    if abs(sweep_angle) < 0.0001:
        vx = cx + cos(start_angle) * w / 2.0
        vy = cy + sin(start_angle) * h / 2.0
        return [(vx, vy)]
    pts_list = []
    step_angle = float(sweep_angle) / num_points    
    va = start_angle
    side = 1 if sweep_angle > 0 else -1
    while va * side < end_angle * side or abs(va - end_angle) < 0.0001:
        vx = cx + cos(va) * w / 2.0
        vy = cy + sin(va) * h / 2.0
        pts_list.append((vx, vy))
        va += step_angle
    return pts_list

def var_bar_pts(p1x, p1y, p2x, p2y, r1, r2=None, **kwargs):
    """
    Tangent/tangent shape on 2 circles of arbitrary radius
    """
    r2 = r2 if r2 is not None else r1
    shorter = kwargs.pop('shorter', 0)
    assert not (shorter and r1 != r2),\
        "Can't draw shorter var_bar with different radii"
    d = dist(p1x, p1y, p2x, p2y)
    ri = r1 - r2
    result = []
    if d > abs(ri):
        clipped_ri_over_d = min(1, max(-1, ri / d))
        beta = asin(clipped_ri_over_d) + HALF_PI
        angle = atan2(p1x - p2x, p2y - p1y) + HALF_PI
        offset = shorter / 2.0 if shorter < d else d / 2.0
        result.extend(arc_pts(offset, 0, r1 * 2, r1 * 2,
                     -beta - PI, beta - PI, **kwargs))
        result.extend(arc_pts(d - offset, 0, r2 * 2, r2 * 2,
                      beta - PI, PI - beta, **kwargs))
        return rotate_offset_points(result, angle, p1x, p1y)
    else:
        r = max(r1, r2)
        x, y = (p1x, p1y) if r1 > r2 else (p2x, p2y)
        return arc_pts(x, y, r * 2, r * 2, 0, TWO_PI, **kwargs)
                          
def rotate_offset_points(pts, angle, offx, offy, y0=0, x0=0):
    return [(((xp - x0) * cos(angle) - (yp - y0) * sin(angle)) + x0 + offx,
             ((yp - y0) * cos(angle) + (xp - x0) * sin(angle)) + y0 + offy)
            for xp, yp in pts]