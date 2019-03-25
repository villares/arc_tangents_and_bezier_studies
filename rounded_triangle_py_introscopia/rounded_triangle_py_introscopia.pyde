# Baseado em código do John - https://github.com/Introscopia

r, r1, r2 = 30, 70, 50
V = []
md = -1

def setup():
    size(500, 500)
    V.append(PVector(250, 150))

    V.append(PVector(250 + 100 * cos(PI / 6.0),
                     250 + 100 * sin(PI / 6.0)))
    V.append(PVector(250 - 100 * cos(PI / 6.0),
                     250 + 100 * sin(PI / 6.0)))

def draw():
    background(200)
    fill(255, 100)
    poly_rounded(V, r)
    fill(200)
    for i in range(3):
        ellipse(V[i].x, V[i].y, 10, 10)

def poly_rounded(P, r0, r1=None, r2=None):
    r1 = r0 if not r1 else r1
    r2 = r0 if not r2 else r2
    a = [0] * 3
    d, d1, d2 = 2 * r, 2 * r1, 2 * r2

    a[0] = atan2(P[1].y - P[0].y, P[1].x - P[0].x) - HALF_PI
    a[1] = atan2(P[2].y - P[1].y, P[2].x - P[1].x) - HALF_PI
    a[2] = atan2(P[0].y - P[2].y, P[0].x - P[2].x) - HALF_PI

    start = a[2] if a[2] < a[0] else a[2] - TWO_PI
    arc(P[0].x, P[0].y, d, d, start, a[0])
    start = a[0] if a[0] < a[1] else a[0] - TWO_PI
    arc(P[1].x, P[1].y, d1, d1, start, a[1])
    start = a[1] if a[1] < a[2] else a[1] - TWO_PI
    arc(P[2].x, P[2].y, d2, d2, start, a[2])

    p01 = PVector(P[0].x + r0 * cos(a[0]), P[0].y + r0 * sin(a[0]))
    p10 = PVector(P[1].x + r1 * cos(a[0]), P[1].y + r1 * sin(a[0]))
    p12 = PVector(P[1].x + r1 * cos(a[1]), P[1].y + r1 * sin(a[1]))
    p21 = PVector(P[2].x + r2 * cos(a[1]), P[2].y + r2 * sin(a[1]))
    p20 = PVector(P[2].x + r2 * cos(a[2]), P[2].y + r2 * sin(a[2]))
    p02 = PVector(P[0].x + r0 * cos(a[2]), P[0].y + r0 * sin(a[2]))

    with pushStyle():
        noStroke()
        with beginClosedShape():
            vertex(P[0].x, P[0].y)
            vertex(p02.x, p02.y)
            vertex(p20.x, p20.y)
            vertex(P[2].x, P[2].y)
            vertex(p21.x, p21.y)
            vertex(p12.x, p12.y)
            vertex(P[1].x, P[1].y)
            vertex(p10.x, p10.y)
            vertex(p01.x, p01.y)

    line(p01.x, p01.y, p10.x, p10.y)
    line(p12.x, p12.y, p21.x, p21.y)
    line(p20.x, p20.y, p02.x, p02.y)


def mouseWheel(E):
    global r, d
    r += 5 * E.getAmount()

def mousePressed():
    global md
    for i in range(3):
        if dist(mouseX, mouseY, V[i].x, V[i].y) < 10:
            md = i
            break

def mouseDragged():
    if md >= 0:
        V[md].x, V[md].y = mouseX, mouseY

def mouseReleased():
    global md
    md = -1
