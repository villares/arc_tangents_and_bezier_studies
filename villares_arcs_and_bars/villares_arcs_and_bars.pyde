from arcs import b_arc, p_arc

def setup():
    size(500, 500)
    
def draw():
    global a_arc
    background(200)
    
    if not keyPressed:
        a_arc = b_arc
    else:
        a_arc = p_arc
        
    fill(0, 0, 200, 100)
    var_bar(100, 50, 300, 200, 0, 30)
    var_bar(100, 150, 300, 300, 40, 10)
    line(100, 200, 300, 400)
    bar(100, 200, 300, 400, 20, 200)
    
    
def bar(x1, y1, x2, y2, thickness, shorter=0):
    """
    O código para fazer as barras, dois pares (x, y),
    um parâmetro de encurtamento: shorter
    """
    L = dist(x1, y1, x2, y2)
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = shorter / 2
        beginShape()
        a_arc(0, offset, thickness, thickness, PI, TWO_PI, mode=2)
        a_arc(0, L - offset, thickness, thickness, 0, PI, mode=2)
        endShape(CLOSE)

def var_bar(p1x, p1y, p2x, p2y, r1, r2=None):
    """
    Tangent/tangent shape on 2 circles of arbitrary radius
    """
    if r2 is None:
        r2 = r1
    #line(p1x, p1y, p2x, p2y)
    d = dist(p1x, p1y, p2x, p2y)
    ri = r1 - r2
    if d > abs(ri):
        rid = (r1 - r2) / d
        if rid > 1:
            rid = 1
        if rid < -1:
            rid = -1
        beta = asin(rid) + HALF_PI
        with pushMatrix():
            translate(p1x, p1y)
            angle = atan2(p1x - p2x, p2y - p1y)
            rotate(angle + HALF_PI)
            x1 = cos(beta) * r1
            y1 = sin(beta) * r1
            x2 = cos(beta) * r2
            y2 = sin(beta) * r2
            #print((d, beta, ri, x1, y1, x2, y2))
            beginShape()  
            a_arc(0, 0, r1 * 2, r1 * 2,
                -beta - PI, beta - PI, mode=2)
            a_arc(d, 0, r2 * 2, r2 * 2,
                beta - PI, PI - beta, mode=2)
            endShape(CLOSE)

    else:
        ellipse(p1x, p1y, r1 * 2, r1 * 2)
        ellipse(p2x, p2y, r2 * 2, r2 * 2)
