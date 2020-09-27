// Pomax https://stackoverflow.com/a/27006163/19771
// Click to add points


class Point { 
  float x, y; 
  public Point(float _x, float _y) { 
    x=_x; 
    y=_y;
  }
}

ArrayList<Point> points = new ArrayList<Point>();

void setup() {
  size(400, 400);
  noLoop();
}

void mouseClicked() {
  points.add(new Point(mouseX, mouseY));
  redraw();
}

ArrayList<Point> convertToClosed(ArrayList<Point> points, float radius) {
  // this value *actually* depends on the angle between the lines.
  // a 180 degree angle means f can be 1, a 10 degree angle needs
  // an f closer to 4!
  final float f = 2.5;
  ArrayList<Point> closed = new ArrayList<Point>();
  Point p1, p2, p3, p2l, p2l_guide, p2r, p2r_guide;
  float dx, dy, m;
  for (int i=0, last=points.size(); i<last; i++) { // >
    p1 = points.get(i);
    p2 = points.get((i+1)%last);
    p3 = points.get((i+2)%last);

    dx = p2.x - p1.x;
    dy = p2.y - p1.y;
    m = sqrt(dx*dx+dy*dy);
    dx /= m;
    dy /= m;
    p2l = new Point(p2.x-radius*dx, p2.y-radius*dy);
    p2l_guide = new Point(p2.x-f*radius*dx, p2.y-f*radius*dy);

    dx = p3.x-p2.x;
    dy = p3.y-p2.y;
    m = sqrt(dx*dx+dy*dy);
    dx/=m;
    dy/=m;
    p2r = new Point(p2.x+radius*dx, p2.y+radius*dy);
    p2r_guide = new Point(p2.x+f*radius*dx, p2.y+f*radius*dy);

    closed.add(p2l_guide);
    closed.add(p2l);
    closed.add(p2r);
    closed.add(p2r_guide);
  }
  return closed;
}

void drawRoundedPolygon(ArrayList<Point> points, float radius) {
  ArrayList<Point> closed = convertToClosed(points, radius);
  Point p0, p1, p2, p3, p4, p5;
  for (int i=0, last=closed.size(); i<last; i+=4) { //>
    // previous p2r and p2r_guide:
    p0 = closed.get((i-2+last)%last);
    p1 = closed.get((i-1+last)%last);

    // current p2l_guide, p2l, p2r and p2r_guide:
    p2 = closed.get(i);
    p3 = closed.get((i+1)%last);
    p4 = closed.get((i+2)%last);
    p5 = closed.get((i+3)%last);   

    // line from previous to current:
    line(p0.x, p0.y, p3.x, p3.y);

    // connector segment from current to next:
    beginShape();
    curveVertex(p2.x, p2.y);
    curveVertex(p3.x, p3.y);
    curveVertex(p4.x, p4.y);
    curveVertex(p5.x, p5.y);
    endShape();
  }
}

void draw() {
  background(255);
  //if (points.size() < 3) return drawPoints();
  noFill();
  stroke(0);
  drawRoundedPolygon(points, 10);
}

// we can't do anything with less than 3 points...
void drawPoints() {    
  if (points.size()==0) return;
  Point p0 = points.get(0);
  ellipse(p0.x, p0.y, 2, 2);
  if (points.size()==1) return;
  Point p1 = points.get(1);
  ellipse(p1.x, p1.y, 2, 2);
}
