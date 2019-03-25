
// Pomax at https://stackoverflow.com/a/27048581/19771

class Point{float x,y;public Point(float _x,float _y){x=_x;y=_y;}}

ArrayList<Point> points = new ArrayList<Point>();

void setup() {
  size(400,400);
  noLoop();
}

void draw() {
  background(255);
  if(points.size() < 3) { drawPoints(); return; }
  fill(255,0,0,40);
  stroke(0,0,150);
  drawRoundedPolygon(points, 5);
}

// we can't do anything with less than 3 points...
void drawPoints() {    
  if(points.size()==0) return;
  Point p0 = points.get(0);
  ellipse(p0.x,p0.y,2,2);
  if(points.size()==1) return;
  Point p1 = points.get(1);
  ellipse(p1.x, p1.y,2,2);
}

void drawRoundedPolygon(ArrayList<Point> points, float radius) {
  ArrayList<Point> closed = convertToClosed(points, radius);
  Point p1,p2,p3;
  beginShape();
  for(int i=0, last=closed.size(); i<last; i+=3) { //>
    p1 = closed.get(i);
    p2 = closed.get(i+1);
    p3 = closed.get(i+2);
    // rounded isosceles triangle connector values:
    float[] c = roundIsosceles(p1, p2, p3, 0.75);
    // tell Processing that we have points to add to our shape:
    vertex(p1.x,p1.y);
    bezierVertex(c[0], c[1], c[2], c[3], p3.x, p3.y);
  }
  endShape(CLOSE);
}

ArrayList<Point> convertToClosed(ArrayList<Point> points, float radius) {
  // this value *actually* depends on the angle between the lines.
  // a 180 degree angle means f can be 1, a 10 degree angle needs
  // an f closer to 4!
  final float f = 4;
  ArrayList<Point> closed = new ArrayList<Point>();
  Point p1,p2,p3,p2l,p2l_guide,p2r,p2r_guide,pc;
  float dx1, dy1, dx2, dy2, m;
  for(int i=0, last=points.size(); i<last; i++) { // >
    p1 = points.get(i);
    p2 = points.get((i+1)%last);
    p3 = points.get((i+2)%last);

    dx1 = p2.x - p1.x;
    dy1 = p2.y - p1.y;
    m = sqrt(dx1*dx1+dy1*dy1);
    p2l = new Point(p2.x-radius*dx1/m, p2.y-radius*dy1/m);

    dx2 = p3.x-p2.x;
    dy2 = p3.y-p2.y;
    m = sqrt(dx2*dx2+dy2*dy2);
    p2r = new Point(p2.x+radius*dx2/m, p2.y+radius*dy2/m);

    closed.add(p2l);
    closed.add(p2);
    closed.add(p2r);
  }
  return closed;
}

float[] roundIsosceles(Point p1, Point p2, Point p3, float t) {
  float mt = 1-t,
        c1x = (mt*p1.x + t*p2.x),
        c1y = (mt*p1.y + t*p2.y),
        c2x = (mt*p3.x + t*p2.x),  
        c2y = (mt*p3.y + t*p2.y);
  return new float[]{ c1x, c1y, c2x, c2y };
}

void mousePressed() {
  points.add(new Point(mouseX,mouseY));
  redraw();
}
