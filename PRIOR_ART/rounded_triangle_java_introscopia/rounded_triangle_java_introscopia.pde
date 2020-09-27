// código do( John - https://github.com/Introscopia

float r = 100, d;
PVector[] P;
float[] a;
int md = -1;
void setup(){
  size( 500, 500 );
  d = 2*r;
  P = new PVector[3];
  a = new float[3];
  P[0] = new PVector( 250, 150 );
  P[1] = new PVector( 250 + 100*cos(PI/6.0), 250+ 100*sin(PI/6.0) );
  P[2] = new PVector( 250 - 100*cos(PI/6.0), 250+ 100*sin(PI/6.0) );
}

void draw(){
  background(230);
  for(int i=0; i < 3; i++) ellipse( P[i].x, P[i].y, 10, 10 );
  a[0] = atan2( P[1].y - P[0].y, P[1].x - P[0].x ) - HALF_PI;
  a[1] = atan2( P[2].y - P[1].y, P[2].x - P[1].x ) - HALF_PI;
  a[2] = atan2( P[0].y - P[2].y, P[0].x - P[2].x ) - HALF_PI;
  noFill();
  float start = (a[2] < a[0])? a[2] : a[2] - TWO_PI;
  arc( P[0].x, P[0].y, d, d, start, a[0] );
  line( P[0].x + r * cos(a[0]), P[0].y + r * sin(a[0]), P[1].x + r * cos(a[0]), P[1].y + r * sin(a[0]) );
  start = (a[0] < a[1])? a[0] : a[0] - TWO_PI;
  arc( P[1].x, P[1].y, d, d, start, a[1] );
  line( P[1].x + r * cos(a[1]), P[1].y + r * sin(a[1]), P[2].x + r * cos(a[1]), P[2].y + r * sin(a[1]) );
  start = (a[1] < a[2])? a[1] : a[1] - TWO_PI;
  arc( P[2].x, P[2].y, d, d, start, a[2] );
  line( P[2].x + r * cos(a[2]), P[2].y + r * sin(a[2]), P[0].x + r * cos(a[2]), P[0].y + r * sin(a[2]) );
  
}
void mouseWheel( MouseEvent E ){
  r += 5*E.getAmount();
  d = 2*r;
}
void mousePressed(){
  for(int i=0; i < 3; i++){
    if( dist( mouseX, mouseY, P[i].x, P[i].y ) < 10 ){
      md = i;
      break;
    }
  }
}
void mouseDragged(){
  if( md >= 0 ){
    P[md].x = mouseX;
    P[md].y = mouseY;
  }
}
void mouseReleased(){
  md = -1;
}
