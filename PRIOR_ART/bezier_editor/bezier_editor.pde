// see https : // www.processing.org/tutorials/curves/
// see https : // forum.processing.org/two/discussion/26216/can-someone-help-me-to-draw-this#latest
// see https : // forum.processing.org/two/discussion/comment/123853/#Comment_123853
 
final String helpText = 
  "BezierVertex-Editor: You can make a vertex here and use it in another program.\n\nThe 3 buttons on the right allow to change the mode.\nNormal Mode: You can click mouse to add new points,\n"
  +"drag and drop existing points to move them.\nRight mouse click to INSERT additional point between 2 existing points\n\n"
  +"Use Backspace to remove last entry (or all entries), use Delete key to remove highlighted point (click green point first),\n"
  +"\nNormal Mode has just been described. \nIn selection mode you can select a GROUP of points, \nin drag mode you can drag the entire group.\n\nEscape key to unselect all points. "
  +"\n\nSpace to export with println (to the direct window). \nThen you need to copy / paste the code from direct window to your target sketch.\n"
  +"For how to use the data see TARGET SKETCH at the end of the sketch which you need to make to a new sketch.\n\n(click x to hide/show this text)."; 
 
ArrayList<PointMy> listPV = new ArrayList();
 
// drag and drop 
boolean hold=false; 
int holding_i=-1;
 
// help text on off 
boolean textHelpIsOn = true; 
 
// buttons
Button[] buttons;
 
String status="Normal Mode"; 
int mode=0;
 
PVector startPV=new PVector(0, 0); 
 
// -----------------------------------------------------
 
void setup() {
  size(840, 880);
  background(255);
 
  makeArrayList();   // just a test list, you can leave listPV as well empty
 
  makeButtons(); // buttons
}// func 
 
void draw() {
  background(255);
 
  switch(mode) {
  case 0:
    // standard mode 
    // drag and drop management 
    if (hold) {
      PointMy pm = listPV.get(holding_i);
      pm.p.x=mouseX;
      pm.p.y=mouseY;
    }
    break;
 
  case 1:
    // select mode
    if (hold) {
      // rect for show the rect 
      noFill();
      stroke(0); 
      rect(startPV.x, startPV.y, 
        mouseX-startPV.x, mouseY-startPV.y);
 
      // select points 
      for (int i = 0; i < listPV.size(); i++) {
        PointMy pm=listPV.get(i);
        if (pm.p.x>startPV.x&&
          pm.p.y>startPV.y&&
          pm.p.x<mouseX&&
          pm.p.y<mouseY) {
          pm.selected=true;
        }//if
        else {
          pm.selected=false;
        }//else
      }//for
    }//if
    break; 
 
  case 2: 
    // drag mode (for selection) 
    if (hold) {
      for (int i = 0; i < listPV.size(); i++) {
        PointMy pm=listPV.get(i);
        if (pm.selected) {
          pm.p.x+=mouseX-pmouseX;
          pm.p.y+=mouseY-pmouseY;
        }//if
      }//for
    }//if
    break;
 
  default:
    println("unknown mode in draw(): "+mode);
    exit(); 
    return;
  } // switch 
 
  // in ALL modes: 
 
  // show status
  fill(0);
  text(status, 5, height-4);
  stroke(0);
  line(0, height-21, 
    width, height-21);
 
  // show ArrayList
  showArrayList(); 
 
  // text help 
  if (textHelpIsOn) {
    fill(0) ;
    text(helpText, 17, 17);
  }
 
  // show Menu
  for (Button but : buttons) {
    but.update();
    but.display();
  }//for
  //
}// func draw() 
 
// -----------------------------------------------------
 
void showArrayList() {
 
  // show the curve 
  noFill();
  stroke(0);
  beginShape();
  int i=0;
  if (listPV.size()>0) {
    curveVertexPVector(listPV.get(i).p);
    for ( i = 0; i < listPV.size(); i++) {
      curveVertexPVector(listPV.get(i).p);
    }
    i=listPV.size()-1;
    curveVertexPVector(listPV.get(i).p);
  }
  endShape();
 
  //show the points (additionally)
  noStroke();
  float rad=3;
  for ( i = 0; i < listPV.size(); i++) {
    PointMy pm = listPV.get(i);
    PVector pv=pm.p;
    // if we are close to the mouse, color green, else red
    if (dist(mouseX, mouseY, pv.x, pv.y)<11||pm.selected) {
      // near to mouse 
      fill( 0, 255, 0); // green
      rad=7;
    } else {
      // normal 
      fill(255, 0, 0);  // red
      rad=3;
    }
    ellipse(pv.x, pv.y, 
      rad, rad);
  }//for
}//func
 
// ----------------------------------------------------------
// Tools 
 
void makeArrayList() {
 
  // init
 
  int[] coords = {
    // alternating x and y value (which belong together: 0 and 1 is a pair, 2 and 3 is a pair....)
    40, 190, 
    110, 190, 
    140, 230, 
    60, 250, 
    50, 280
  };
 
  // read coords[]
  for (int i = 0; i < coords.length; i += 2) {
    listPV.add (  new PointMy ( new PVector(coords[i], coords[i + 1]+130), false ));
  }
}//func 
 
void curveVertexPVector(PVector pv) {
  // like curveVertex but gets a PVector as input  
  // (just an easy way to use vectors for curveVertex)
  curveVertex(pv.x, pv.y);
}
 
void makeButtons() {
  buttons = new Button[3];
  String[] buttonTexts={ "Normal", "Select", "Drag"   };
  if (buttons.length!=buttonTexts.length) {
    println("Arrays do not have the same length in setup()");
    exit();
    return;
  }
  int unit=29;
  for (int i = 0; i < buttons.length; i++) {
    Button newButton = new Button(
      buttonTexts[i], 
      width-80, i*unit+40, 
      74, unit-6, 
      i);
    buttons[i] = newButton;
  }
}
 
// ----------------------------------------------------------
 
void keyPressed() {
 
  if (key==BACKSPACE) {
    if (listPV.size()>0)
      listPV.remove(listPV.size()-1);
  }
  // ----------------
  else if (key==' ') {
    // SPACE BAR
    String xval="float[] xValues = { ", 
      yval="float[] yValues = { ";
    for (int i = 0; i < listPV.size(); i++) {
      PVector pv=listPV.get(i).p;
      xval += str(pv.x)+",";
      yval += str(pv.y)+",";
    }//for
    println (xval+" };"); 
    println (yval+" };");
    println ("remove last comma");
  }// else if SPACE BAR
  //------------------------
  else if (key=='x') {
    textHelpIsOn = !textHelpIsOn;
  }//else if
  //----------------------------
  else if (key==DELETE) {
    for (int i = 0; i < listPV.size(); i++) {
      PointMy pm=listPV.get(i);
      if (dist(mouseX, mouseY, pm.p.x, pm.p.y)<11) {
        listPV.remove(i);
        return;
      }//if
    }//for
  }//else if
  //----------------------------
  else if (key==ESC) {
    key=0; // kill ESC
    for (int i = 0; i < listPV.size(); i++) {
      PointMy pm=listPV.get(i);
      pm.selected=false;
    }
  }
  //----------------------------
}//func 
 
void mousePressed() {
 
  // this applies in all modes !!! 
  if (mouseButton==LEFT) {
    // right screen border?
    if (mouseX>buttons[0].x) {
      if ( checkMouseOnMenu()) 
        return;
    }
  }
 
  switch(mode) {
 
  case 0:
    //  standard mode
    mousePressedForModeNormal();
    break;
 
  case 1:
    // Select 
    hold=true;
    startPV=new PVector (mouseX, mouseY); 
    break; 
 
  case 2: 
    // Drag selection
    hold=true;
    break;
 
  default:
    println("unknown mode in mousePressed: "+mode);
    exit(); 
    return;
  } // switch
}
 
void mousePressedForModeNormal() {
 
  if (mouseButton==LEFT) {
 
    // apply drag and drop
    for (int i = 0; i < listPV.size(); i++) {
      PVector pv=listPV.get(i).p;
      if (dist(mouseX, mouseY, pv.x, pv.y)<11) {
        hold=true; 
        holding_i=i;
        return;
      }
    }
 
    // no drag and drop, add point   
    listPV.add(new PointMy(new PVector(mouseX, mouseY), false));
  }//if
 
  // ---------------------------------------
 
  else if (mouseButton==RIGHT) {
 
    int result=-1; 
 
    float minDist = 10000; 
 
    println("here 4");
 
    // search pos
    for (int i = 0; i < listPV.size()-1; i++) {
      PVector pv1=listPV.get(i).p;
      PVector pv2=listPV.get(i+1).p;
 
      float dist= dist(mouseX, mouseY, (pv1.x+pv2.x)/2, (pv1.y+pv2.y)/2);
 
      if (dist<minDist&&dist<110) {
        result=i+1;
        minDist=dist;
      }//if
    }//for 
 
    // found something
    if (result>-1) {
      // no drag and drop, add point   
      listPV.add(result, new PointMy(new PVector(mouseX, mouseY), false));
    }
    //
  }//else if
}//func 
 
void mouseReleased() {
  // end drag and drop
  hold=false;
}
 
// -----------------------------
 
boolean checkMouseOnMenu() {
  for (Button but : buttons) {
    but.press();
    if (but.pressed) {
      println(but.index);
      doCommand(but.index);
      return true; // Other buttons won't be pressed, just stop
    }
  }//for
  return false;
}
 
 
void doCommand(int cmd) {
  switch(cmd) {
  case 0:
    status="Normal Mode";
    mode=0;
    break; 
 
  case 1:
    status="Mode to select points (drag and drop mouse over the points)";
    mode=1;
    break; 
 
  case 2:
    status="Drag Mode (drag the group of points previously selected)";
    mode = 2; 
    break; 
 
  default:
    status="Error";
    mode=-1; // unknown
    println ("Error in doCommand: "+cmd); 
    exit();
    return;
  }//switch
}//func 
 
//============================================================================
 
class Button {
 
  String btnText; 
 
  int x, y; // The x- and y-coordinates
  int sizeWidth, sizeHeight; // Dimension (width and height)
 
  //color baseGray; // Default gray value
  //color overGray; // Value when mouse is over the button
  //color pressGray; // Value when mouse is over and pressed
 
  boolean over = false; // True when the mouse is over
  boolean pressed = false; // True when the mouse is over and pressed
 
  int index;
 
  // constructor 
  Button(String text_, 
    int xp_, int yp_, 
    int sizeWidth_, int sizeHeight_, 
    int index_) {
 
    btnText=text_;
 
    x = xp_;
    y = yp_;
 
    sizeWidth = sizeWidth_;
    sizeHeight = sizeHeight_; 
 
    //baseGray = b_;
    //overGray = o_;
    //pressGray = p_;
 
    index=index_;
  } // constructor 
 
  // Updates the over field every frame
  void update() {
    if ((mouseX >= x) && (mouseX <= x + sizeWidth) &&
      (mouseY >= y) && (mouseY <= y + sizeHeight)) {
      over = true;
    } else {
      over = false;
    }
  }
 
  boolean press() {
    if (over) {
      pressed = true;
      return true;
    } else {
      pressed = false; 
      return false;
    }
  }
 
  void release() {
    pressed = false; // Set to false when the mouse is released
  }
 
  void display() {
 
    //if (pressed) {
    //  fill(pressGray);
    //} else if (over) {
    //  fill(overGray);
    //} else {
    //  fill(baseGray);
    //}
 
    // noFill(); 
    fill(111);
    noStroke(); 
    rect(x, y, 
      sizeWidth, sizeHeight);
 
    noFill(); 
    noStroke(); 
    if (mode==index)
      stroke(0, 225, 0);
    // else stroke(0);
    float dist = 2; 
    rect(x+dist, y+dist, 
      sizeWidth-dist-dist, sizeHeight-dist-dist);
 
    fill(255);  // green
    //  textAlign(CENTER); 
    // text(but.index, but.x+but.sizeWidth/2, 40);
    text(btnText, x+6, y+16);
    textAlign(LEFT);
  }
}//class
 
//============================================================================
 
class PointMy {
  PVector p;
  boolean selected=false;
 
  PointMy( PVector p_, boolean selected_) {
    p=p_.copy();
    selected=selected_;
  }//constr
}//class
 
// ##############################################################
//---------------------------------------------------------------
 
// TARGET SKETCH 
//
//ArrayList<PVector> listPV = new ArrayList();
 
//// YOUR DATA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//float[] xValues = { 40.0, 110.0, 140.0, 60.0, 50.0, 231.0 };
//float[] yValues = { 90.0, 90.0, 130.0, 150.0, 180.0, 267.0 };
//// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 
//void setup() {
//  size(840, 880);
//  background(255);
 
//  // read coords[]
//  for (int i = 0; i < xValues.length; i += 1) {
//    listPV.add ( new PVector(xValues[i], yValues[i]));
//  }
//}
 
//// ---------------------------------------------------------------------
 
//void draw() {
//  // show the curve 
//  noFill();
//  stroke(0);
//  beginShape();
//  int i=0;
//  if (listPV.size()>0) {
//    curveVertexPVector(listPV.get(i));
//    for ( i = 0; i < listPV.size(); i++) {
//      curveVertexPVector(listPV.get(i));
//    }
//    i=listPV.size()-1;
//    curveVertexPVector(listPV.get(i));
//  }
//  endShape();
//}
 
//void curveVertexPVector(PVector pv) {
//  // like curveVertex but gets a PVector as input  
//  // (just an easy way to use vectors for curveVertex)
//  curveVertex(pv.x, pv.y);
//}
////
