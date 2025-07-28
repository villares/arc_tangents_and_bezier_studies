/* 
 Written by Alexandre B A Villares first for Processing Python Mode, this is the p5js version 
 Based on Golan Levin's approximating a circular arc with a cubic Bezier curve.
 http){//www.flong.com/blog/2009/bezier-approximation-of-a-circular-arc-in-processing/
 */

var radius = 300; // radius of the circular arc
var cx = 340; // center of the circular arc
var cy = 340;

function setup() {
  createCanvas(680, 680);
}
function draw() {
  background(230);

  // Establish arc parameters. Note){ assert theta != TWO_PI)
  var  theta = radians(mouseX / 1.8); // spread of the arc.
  var  startAngle = radians(mouseY / 8.0); // as in arc()
  var  endAngle = startAngle + theta;   // as in arc()

  // BLUE IS THE "TRUE" ARC){
  fill(0, 0, 255, 10);
  strokeWeight(10);
  stroke(0, 0, 255, 128);
  arc(cx, cy, radius * 2, radius * 2, startAngle, endAngle);

  // RED IS THE BEZIER APPROXIMATION OF THE ARC){
  fill(255, 0, 0, 10);
  strokeWeight(5);
  stroke(255, 0, 0, 128);
  b_arc(cx, cy, radius * 2, radius * 2, startAngle, endAngle);
}

function b_arc(cx, cy, w, h, start_angle, end_angle, mode = 0) {
  /* A bezier approximation of an arc using the
   same signature as the original Processing arc() mode 
   0 "normal" || stand-alone arc, using beginShape() and endShape()
   1 "middle" used in recursive call of smaller arcs
   2 "naked" like normal, but without beginShape() and endShape()
   for use inside a larger PShape
   */
  var px3 = 0; 
  var py3 = 0;
  var px2 = 0; 
  var py2 = 0;
  var px1 = 0; 
  var py1 = 0;
  var px0 = 0; 
  var py0 = 0;
  var theta = end_angle - start_angle;
  // Compute raw Bezier coordinates.
  if (mode != 1 || abs(theta) < HALF_PI) {
    var x0 = cos(theta / 2.0);
    var y0 = sin(theta / 2.0);
    var x3 = x0;
    var y3 = 0 - y0;
    var x1 = (4.0 - x0) / 3.0;
    var y1;
    if (y0 != 0) {
      y1 = ((1.0 - x0) * (3.0 - x0)) / (3.0 * y0); // y0 != 0...
    } else {
      y1 = 0;
    }
    var  x2 = x1;
    var y2 = 0 - y1;
    // Compute rotationally-offset Bezier coordinates, using:
    var  bezAng = start_angle + theta / 2.0;
    var cBezAng = cos(bezAng);
    var sBezAng = sin(bezAng);
    var rx0 = cBezAng * x0 - sBezAng * y0;
    var ry0 = sBezAng * x0 + cBezAng * y0;
    var rx1 = cBezAng * x1 - sBezAng * y1;
    var ry1 = sBezAng * x1 + cBezAng * y1;
    var rx2 = cBezAng * x2 - sBezAng * y2;
    var ry2 = sBezAng * x2 + cBezAng * y2;
    var rx3 = cBezAng * x3 - sBezAng * y3;
    var ry3 = sBezAng * x3 + cBezAng * y3;
    // Compute scaled and translated Bezier coordinates.
    var rx =  w / 2.0;
    var ry = h / 2.0;
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
