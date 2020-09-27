// From: http://bazaar.launchpad.net/~philho/+junk/Processing/view/head:/_QuickExperiments/_Static/CircleWithCorner/CircleWithCorner.pde

// [url=http://processing.org/discourse/yabb2/YaBB.pl?num=1272553052/2]How to do this shape ?[/url]
// [url=http://processing.org/discourse/yabb2/YaBB.pl?num=1274367486/0#2]shape arc form[/url]

// Ratio for perfect circle
float pcr = 0.5522847498;

void setup()
{
  size(1100, 550);
  smooth();
}

void draw()
{
  background(222);

  fill(0x8800EE00);
  stroke(#2288FF);
  DrawCircle(50, 50, 20);
  DrawCircle(110, 140, 80);
  DrawCircle(220, 350, 150);

  fill(0x880000EE);
  stroke(#22FF88);
  DrawShape(380, 50, 20);
  DrawShape(440, 140, 80);
  DrawShape(550, 350, 150);

  fill(0x880055AA);
  stroke(#00FF44);
  DrawArc(730, 50, 20);
  DrawArc(790, 140, 80);
  DrawArc(900, 350, 150);
  
  // Checking curvatures
  fill(0x50EE0000);
  noStroke();
  DrawCircle(550, 350, 150);
  DrawCircle(900, 350, 150);
  DrawCircle(900, 350, 75);
}

// First step: draw a circle
void DrawCircle(float x, float y, float r)
{
  float l = (1 - pcr) * r;
  float d = 2 * r;
  // Assume here default CENTER mode
  x -= r; y -= r;

  beginShape();
  vertex(x, y + r); // Left
  bezierVertex(x, y + l,
      x + l, y,
      x + r, y); // Top
  bezierVertex(x + d - l, y,
      x + d, y + l,
      x + d, y + r); // Right
  bezierVertex(x + d, y + d - l,
      x + d - l, y + d,
      x + r, y + d); // Bottom
  bezierVertex(x + l, y + d,
      x, y + d - l,
      x, y + r); // Back to left
  endShape();
}

// Second step: change some sides
void DrawShape(float x, float y, float r)
{
  // Not sure why I have to increase l
  float l = 1.2 * (1 - pcr) * r;
  float d = 2 * r;
  // Assume here default CENTER mode
  // I put x and y to top-left
  x -= r; y -= r;

  beginShape();
  vertex(x + r, y); // Top
  vertex(x + d, y); // Top-Right
  vertex(x + d, y + r); // Right
  bezierVertex(x + d, y + r + l,
      x + r + l, y + d,
      x + r, y + d); // Bottom
  bezierVertex(x + r - l, y + d,
      x, y + r + l,
      x, y + r); // Left
  bezierVertex(x, y + r - l,
      x + r - l, y,
      x + r, y); // Back to Top
  endShape();
}

void DrawArc(float x, float y, float r)
{
  float l = (1 - pcr) * r;
  //float d = 2 * r;
  // Internal radius, here set at half radius
  float ir = r / 2;
  // Assume here default CENTER mode
  // I put x and y to top-left
  x -= r; y -= r;

  beginShape();
  vertex(x, y + r); // Left
  bezierVertex(x, y + l,
      x + l, y,
      x + r, y); // Top
  vertex(x + r, y + ir); // Go down
  bezierVertex(x + r - ir, y + ir,
      x + r - ir, y + r,
      x + r - ir, y + r); // Bottom
  vertex(x, y + r); // Go back to left
  endShape();
}
