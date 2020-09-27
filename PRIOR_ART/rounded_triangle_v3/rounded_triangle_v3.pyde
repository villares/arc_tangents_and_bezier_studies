radius = 50

def setup():
    size(500, 500)

def draw():
    background(200)
    p_list = [PVector(100, 400),
              PVector(300, 100),
              PVector(mouseX, mouseY)]
    r_list = [50, 30, radius]
    for p0, p1, p2, r in zip(p_list,
                             [p_list[-1]] + p_list[:-1],
                             [p_list[-2]] + [p_list[-1]] + p_list[:-2],
                             r_list):
        m1 = (p0 + p1) / 2
        m2 = (p1 + p2) / 2
        strokeWeight(1)
        stroke(0)
        line(p1.x, p1.y, m1.x, m1.y)
        line(p1.x, p1.y, m2.x, m2.y)
        stroke(255)
        strokeWeight(3)
        roundedCorner(p1, m1, m2, r)


def roundedCorner(pc, p1, p2, r):
    """
    Based on Stackoverflow C# rounded corner post 
    https://stackoverflow.com/questions/24771828/algorithm-for-creating-rounded-corners-in-a-polygon
    """
    d1 = pc - p1
    d2 = pc - p2

    # Angle between vector 1 and vector 2 divided by 2
    #angle = (atan2(d1.y, d1.x) - atan2(d2.y, d2.x)) / 2.
    angle = PVector.angleBetween(d1, d2) / 2.

    # The length of segment between angular point and the
    # points of intersection with the circle of a given radius
    tng = abs(tan(angle))
    segment = float(r) / tng if tng != 0 else float(r)

    # Check the segment
    length1 = d1.mag()
    length2 = d2.mag()

    min_len = min(length1, length2)
    r_max = r
    if segment > min_len:
        segment = min_len
        r_max = min_len * tng

    # Points of intersection are calculated by the proportion between
    # the coordinates of the vector, length of vector and the length of the
    # segment.
    p1Cross = GetProportionPoint(pc, segment, length1, d1.x, d1.y)
    p2Cross = GetProportionPoint(pc, segment, length2, d2.x, d2.y)

    # Calculation of the coordinates of the circle
    # center by the addition of angular vectors.
    dx = pc.x * 2 - p1Cross.x - p2Cross.x
    dy = pc.y * 2 - p1Cross.y - p2Cross.y
    L = sqrt(dx * dx + dy * dy)
    d = sqrt(segment * segment + r_max * r_max)
    circlePoint = GetProportionPoint(pc, d, L, dx, dy)

    # StartAngle and EndAngle of arc
    startAngle = atan2(p1Cross.y - circlePoint.y, p1Cross.x - circlePoint.x)
    endAngle = atan2(p2Cross.y - circlePoint.y, p2Cross.x - circlePoint.x)

    # Sweep angle
    sweepAngle = endAngle - startAngle

    # Some additional checks
    if sweepAngle < 0:
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = -sweepAngle

    if sweepAngle > PI:
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = TWO_PI - sweepAngle

    # Draw result using graphics
    noFill()
    line(p1.x, p1.y, p1Cross.x, p1Cross.y)
    line(p2.x, p2.y, p2Cross.x, p2Cross.y)
    arc(circlePoint.x, circlePoint.y,
        2 * r_max, 2 * r_max,
        startAngle, startAngle + sweepAngle)
    fill(0, 0, 100)
    text(str(int(r)) + "  " + str(int(r_max)),
         circlePoint.x, circlePoint.y)

def GetProportionPoint(pt, segment, L, dx, dy):
    # factor = segment / L if L != 0 else 0
    factor = float(segment) / L if L != 0 else segment
    return PVector((pt.x - dx * factor),
                   (pt.y - dy * factor))

def mouseWheel(e):
    global radius
    radius += int(e.getAmount())
