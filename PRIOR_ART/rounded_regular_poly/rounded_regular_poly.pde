//https://forum.processing.org/one/topic/rounded-polygon.html

int numVertices = 5;
PVector[] vertices;
PVector[] cwVertices; //clockwise offset from vertices
PVector[] acwVertices; //anticlockwise offset from vertices
PVector[] cwBeziers; //clockwise Bezier control point from vertices
PVector[] acwBeziers; //anticlockwise Bezier control point from vertices
PVector centre;
int radius = 80;
float cornerOffset = 0.3;
float maxCornerOffset = 0.5;
float minCornerOffset = 0.1;
float cornerOffsetInc = 0.01;
float bezierOffset = 0.05;
float bezierOffsetInc = 0.05;
void setup()
{
  size(200, 200);
  background(255);
  frameRate(6);
  smooth();
  noFill();
 
  centre = new PVector(width/2, height/2);
 
  vertices = new PVector[numVertices];
  cwVertices = new PVector[numVertices];
  acwVertices = new PVector[numVertices];
  cwBeziers = new PVector[numVertices];
  acwBeziers = new PVector[numVertices];
 
  for(int v = 0; v < numVertices; v++)
  {
    float vx = centre.x + radius * cos(v * TWO_PI/numVertices);
    float vy = centre.y + radius * sin(v * TWO_PI/numVertices);
    vertices[v] = new PVector(vx, vy);
  }
}
void draw()
{
  background(255);
  for(int v = 0; v < numVertices; v++)
  {
    //anticlockwise vertices and bezier control points
    int u = (v+numVertices-1) % numVertices;
    float dx = vertices[v].x - vertices[u].x;
    float dy = vertices[v].y - vertices[u].y;
    acwVertices[v] = new PVector(vertices[v].x - dx * cornerOffset, vertices[v].y - dy * cornerOffset);
    acwBeziers[v] = new PVector(vertices[v].x - dx * bezierOffset, vertices[v].y - dy * bezierOffset);
    //clockwise vertices and bezier control points
    int w = (v+1) % numVertices;
    dx = vertices[w].x - vertices[v].x;
    dy = vertices[w].y - vertices[v].y;
    cwVertices[v] = new PVector(vertices[v].x + dx * cornerOffset, vertices[v].y + dy * cornerOffset);
    cwBeziers[v] = new PVector(vertices[v].x + dx * bezierOffset, vertices[v].y + dy * bezierOffset);
  }
 
  for(int v = 0; v < numVertices; v++)
  {
    int u = (v+1) % numVertices;
    int w = (v+numVertices-1) % numVertices;
    line(cwVertices[v].x, cwVertices[v].y, acwVertices[u].x, acwVertices[u].y);
   
    float startx = acwVertices[v].x;
    float starty = acwVertices[v].y;
    float controlx1 = acwBeziers[v].x;
    float controly1 = acwBeziers[v].y;
    float controlx2 = cwBeziers[v].x;
    float controly2 = cwBeziers[v].y;
    float endx = cwVertices[v].x;
    float endy = cwVertices[v].y;
    //to see start and end vertices
    //fill(0, 255, 0); ellipse(startx, starty, 5, 5);
    //fill(255, 0, 0); ellipse(endx, endy, 5, 5);
    //noFill();
    bezier(startx, starty, controlx1, controly1, controlx2, controly2, endx, endy);
  }
  cornerOffset += cornerOffsetInc;
  bezierOffset += bezierOffsetInc;
  if(cornerOffset > maxCornerOffset || cornerOffset < minCornerOffset) cornerOffsetInc *= -1;
  if(bezierOffset > cornerOffset)
  {
    bezierOffset = cornerOffset;
    bezierOffsetInc *= -1;
  }
  if(bezierOffset < 0) bezierOffsetInc *= -1;
}
