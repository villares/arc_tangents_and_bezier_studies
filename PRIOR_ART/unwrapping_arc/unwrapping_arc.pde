// https://forum.processing.org/two/discussion/1797/how-to-use-bezier-curve-to-approximate-one-quarter-of-a-circle

TheArc arc1, arc2;
float h = 20;
float len = 200;
 
void setup()
{
  size(500, 500);
  smooth();
 
  arc1 = new TheArc(new PVector(width/2, height/2-50), len, 90);
  arc2 = new TheArc(new PVector(width/2, height/2-50+h), len-h*PI/2, 90);
}
 
void draw()
{
  background(222);
  strokeWeight(10);
  strokeCap(SQUARE); 
 
  float amt = constrain(mouseX, 10, width-10);
 
  arc1.theta = map(amt, 10,width-10, 0,360);
  arc1.update();
  arc1.display();
 
  arc2.theta = map(amt, 10,width-10, 0,360);
  if (arc2.theta == 0.0) {
    arc2.len = arc1.len;
  } else {   
    arc2.len = (arc1.r-h)*arc1.len/arc1.r;
  }
  arc2.update();
  arc2.display();
 
  fill(0);
  text("theta: "+map(amt, 10,width-10, 0,360)+" degree", 10,20);
 
}
 
class TheArc {
  PVector p1;
  float len;
  float r;
  float theta;
 
  TheArc (PVector _p1, float _len, float _theta) {
    p1 = new PVector(_p1.x, _p1.y);
    len = _len;
    theta = _theta;
  }
 
  void update(){
    r = len/radians(theta);    
  }
 
  void display(){
    if (theta <= 0.0) { 
      line(p1.x, p1.y, p1.x+len, p1.y);
    } else if ((theta > 0) && (theta <= 360)) {  
      noFill();
      arc(p1.x, p1.y+r, 
          2*r, 2*r, 
          -PI/2, -PI/2+radians(theta));
    }    
  }
}
