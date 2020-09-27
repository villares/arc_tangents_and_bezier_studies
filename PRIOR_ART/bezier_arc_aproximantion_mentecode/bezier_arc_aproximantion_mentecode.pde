// MenteCode: making a section of a circle with a bezier curve
// http://forum.processing.org/two/discussion/1797/how-to-use-bezier-curve-to-approximate-one-quarter-of-a-circle#Item_3
float angle = 90; //Change this value for angle of bezier
float radius = 100;
 
CircleByBezier bcurve;
 
void setup() {
  size(1000, 1000);  
  bcurve = new CircleByBezier();  
}
 
void draw() {
  background(150);
 
  translate(width/2, height/2);
  noFill();
 
  angle = map(mouseX, 0,width, 0,360);
  bcurve.update(angle, radius);
  bcurve.display();
 
  // curve fit check reference
  ellipseMode(CENTER);
  stroke(255, 0, 0);
  strokeWeight(3);
  ellipse(0, 0, radius*2, radius*2);
 
}
 
class CircleByBezier{
  float angle, radius, lnth;
  PVector pStart, pCtrl1, pCtrl2, pEnd;
 
  void update (float _angle, float _radius) {
    angle = _angle;
    radius = _radius;
    lnth = 4 * tan(radians(angle/4))/3; 
 
    pStart = new PVector(0, -radius);
    pCtrl1 = new PVector(radius * lnth, -radius);
    pCtrl2 = new PVector(-radius * lnth, -radius);
    pEnd   = new PVector(0, -radius);
 
    pCtrl2.rotate(radians(angle)); 
    pEnd.rotate(radians(angle)); 
  }
 
  void display () {
    stroke(0);
    strokeWeight(10);  
    bezier(pStart.x, pStart.y,
           pCtrl1.x, pCtrl1.y, 
           pCtrl2.x, pCtrl2.y, 
           pEnd.x,   pEnd.y);
 
    stroke(0,255,0);
    strokeWeight(15);
    point(pStart.x, pStart.y);
    text("start pt", pStart.x+8, pStart.y);
    point(pCtrl1.x, pCtrl1.y);
    text("ctrl pt1", pCtrl1.x+8, pCtrl1.y);
    point(pCtrl2.x, pCtrl2.y);
    text("ctrl pt2", pCtrl2.x+8, pCtrl2.y);
    point(pEnd.x, pEnd.y);  
    text("end pt", pEnd.x+8, pEnd.y); 
  }
}
