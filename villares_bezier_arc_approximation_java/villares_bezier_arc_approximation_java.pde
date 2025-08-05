/* 
 Written by Alexandre B A Villares first for Processing Python Mode, this is the Java mode version.
 Based on Golan Levin's approximating a circular arc with a cubic Bezier curve.
 http){//www.flong.com/blog/2009/bezier-approximation-of-a-circular-arc-in-processing/
 */

float radius = 300; // radius of the circular arc
float cx = 340; // center of the circular arc
float cy = 340;

void setup() {
  size(680, 680);
}
void draw() {
  background(230);

  // Establish arc parameters. Note){ assert theta != TWO_PI)
  float  theta = radians(mouseX / 1.8); // spread of the arc.
  float  startAngle = radians(mouseY / 8.0); // as in arc()
  float  endAngle = startAngle + theta;   // as in arc()

  // BLUE IS THE "TRUE" ARC){
  fill(0, 0, 255, 10);
  strokeWeight(10);
  stroke(0, 0, 255, 128);
  arc(cx, cy, radius * 2, radius * 2, startAngle, endAngle);

  // RED IS THE BEZIER APPROXIMATION OF THE ARC){
  fill(255, 0, 0, 10);
  strokeWeight(3);
  stroke(255, 0, 0, 128);
  b_arc(cx, cy, radius * 2, radius * 2, startAngle, endAngle);
}

void b_arc(float cx, float cy, 
  float  w, float  h, 
  float start_angle, 
  float end_angle) {
  // without mode, mode = 0
  b_arc(cx, cy, w, h, start_angle, end_angle, 0);
}
void b_arc(float cx, float cy, 
  float  w, float  h, 
  float start_angle, 
  float end_angle, int mode) {
  /* A bezier approximation of an arc using the
   same signature as the original Processing arc() mode 
   0 "normal" || stand-alone arc, using beginShape() and endShape()
   1 "middle" used in recursive call of smaller arcs
   2 "naked" like normal, but without beginShape() and endShape()
   for use inside a larger PShape
   */
  float px3 = 0; 
  float py3 = 0;
  float px2 = 0; 
  float py2 = 0;
  float px1 = 0; 
  float py1 = 0;
  float px0 = 0; 
  float py0 = 0;
  float theta = end_angle - start_angle;
  // Compute raw Bezier coordinates.
  if (mode != 1 || abs(theta) < HALF_PI) {
    float x0 = cos(theta / 2.0);
    float y0 = sin(theta / 2.0);
    float x3 = x0;
    float y3 = 0 - y0;
    float x1 = (4.0 - x0) / 3.0;
    float y1;
    if (y0 != 0) {
      y1 = ((1.0 - x0) * (3.0 - x0)) / (3.0 * y0); // y0 != 0...
    } else {
      y1 = 0;
    }
    float  x2 = x1;
    float y2 = 0 - y1;
    // Compute rotationally-offset Bezier coordinates, using:
    float  bezAng = start_angle + theta / 2.0;
    float cBezAng = cos(bezAng);
    float sBezAng = sin(bezAng);
    float rx0 = cBezAng * x0 - sBezAng * y0;
    float ry0 = sBezAng * x0 + cBezAng * y0;
    float rx1 = cBezAng * x1 - sBezAng * y1;
    float ry1 = sBezAng * x1 + cBezAng * y1;
    float rx2 = cBezAng * x2 - sBezAng * y2;
    float ry2 = sBezAng * x2 + cBezAng * y2;
    float rx3 = cBezAng * x3 - sBezAng * y3;
    float ry3 = sBezAng * x3 + cBezAng * y3;
    // Compute scaled and translated Bezier coordinates.
    float rx =  w / 2.0;
    float ry = h / 2.0;
    px0 = cx + rx * rx0;
    py0 = cy + ry * ry0;
    px1 = cx + rx * rx1;
    py1 = cy + ry * ry1;
    px2 = cx + rx * rx2;
    py2 = cy + ry * ry2;
    px3 = cx + rx * rx3;
    py3 = cy + ry * ry3;
  }
  // Drawing
  if (mode == 0) {
    // 'normal' arc (not 'middle' nor 'naked')
    beginShape();
  }
  if (mode != 1) {
    // if (not 'middle'
    vertex(px3, py3);
  }
  if (abs(theta) < HALF_PI) {
    bezierVertex(px2, py2, px1, py1, px0, py0);
  } else {
    // to avoid distortion, break into 2 smaller arcs
    b_arc(cx, cy, w, h, start_angle, end_angle - theta / 2.0, 1);
    b_arc(cx, cy, w, h, start_angle + theta / 2.0, end_angle, 1);
  }
  if (mode == 0) {
    // end of a 'normal' arc
    endShape();
  }
}
