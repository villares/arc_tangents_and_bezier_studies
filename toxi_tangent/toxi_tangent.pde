
    import toxi.geom.*;
    import toxi.processing.*;

    ToxiclibsSupport gfx;

    void setup() {
      size(400, 400);
      noFill();
      gfx=new ToxiclibsSupport(this);
    }

    void draw() {
      // new circle with radius 100
      Circle c=new Circle(width/2, height/2, 100);
      // get direction from centre to point
      Vec2D mousePos=new Vec2D(mouseX, mouseY);
      Vec2D dir=mousePos.sub(c).normalize();
      // tangent direction
      Vec2D tangent=dir.getPerpendicular();
      // point on circle
      Vec2D pos=c.add(dir.scale(c.getRadius()));
      
      background(255);
      gfx.ellipse(c);
      gfx.line(c,pos);
      // scale tangent to be more visible
      tangent.scaleSelf(50);
      gfx.line(pos.sub(tangent),pos.add(tangent));
    }
