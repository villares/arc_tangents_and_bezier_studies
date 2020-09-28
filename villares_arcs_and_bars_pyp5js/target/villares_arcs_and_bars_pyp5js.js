// Transcrypt'ed from Python, 2020-09-27 21:13:46
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, all, any, assert, bool, bytearray, bytes, callable, chr, deepcopy, delattr, dict, dir, divmod, enumerate, getattr, hasattr, isinstance, issubclass, len, list, object, ord, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, setattr, sorted, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {ADD, ALT, ARROW, AUDIO, AUTO, AXES, BACKSPACE, BASELINE, BEVEL, BEZIER, BLEND, BLUR, BOLD, BOLDITALIC, BOTTOM, BURN, CENTER, CHORD, CLAMP, CLOSE, CONTROL, CORNER, CORNERS, CROSS, CURVE, DARKEST, DEGREES, DEG_TO_RAD, DELETE, DIFFERENCE, DILATE, DODGE, DOWN_ARROW, ENTER, ERODE, ESCAPE, EXCLUSION, FILL, GRAY, GRID, HALF_PI, HAND, HARD_LIGHT, HSB, HSL, IMAGE, IMMEDIATE, INVERT, ITALIC, LANDSCAPE, LEFT, LEFT_ARROW, LIGHTEST, LINEAR, LINES, LINE_LOOP, LINE_STRIP, MIRROR, MITER, MOVE, MULTIPLY, NEAREST, NORMAL, OPAQUE, OPEN, OPTION, OVERLAY, P2D, PI, PIE, POINTS, PORTRAIT, POSTERIZE, PROJECT, QUADRATIC, QUADS, QUAD_STRIP, QUARTER_PI, RADIANS, RADIUS, RAD_TO_DEG, REPEAT, REPLACE, RETURN, RGB, RIGHT, RIGHT_ARROW, ROUND, SCREEN, SHIFT, SOFT_LIGHT, SQUARE, STROKE, SUBTRACT, TAB, TAU, TEXT, TEXTURE, THRESHOLD, TOP, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, TWO_PI, UP_ARROW, VIDEO, WAIT, WEBGL, _CTX_MIDDLE, _DEFAULT_FILL, _DEFAULT_LEADMULT, _DEFAULT_STROKE, _DEFAULT_TEXT_FILL, _P5_INSTANCE, abs, accelerationX, accelerationY, accelerationZ, acos, add_library, alpha, ambientLight, ambientMaterial, angleMode, append, applyMatrix, arc, arrayCopy, asin, atan, atan2, background, beginContour, beginShape, bezier, bezierDetail, bezierPoint, bezierTangent, bezierVertex, blend, blendMode, blue, boolean, box, brightness, byte, camera, ceil, changed, char, circle, color, colorMode, concat, cone, constrain, copy, cos, createA, createAudio, createButton, createCamera, createCanvas, createCapture, createCheckbox, createColorPicker, createDiv, createElement, createFileInput, createGraphics, createImage, createImg, createInput, createNumberDict, createP, createRadio, createSelect, createShader, createSlider, createSpan, createStringDict, createVector, createVideo, createWriter, cursor, curve, curveDetail, curvePoint, curveTangent, curveTightness, curveVertex, cylinder, day, debugMode, degrees, deviceOrientation, directionalLight, disableFriendlyErrors, displayDensity, displayHeight, displayWidth, dist, ellipse, ellipseMode, ellipsoid, endContour, endShape, erase, exp, fill, filter, float, floor, focused, frameCount, frameRate, fullscreen, getURL, getURLParams, getURLPath, global_p5_injection, green, height, hex, hour, httpDo, httpGet, httpPost, hue, image, imageMode, input, int, join, key, keyCode, keyIsDown, keyIsPressed, lerp, lerpColor, lightness, lights, line, loadBytes, loadFont, loadImage, loadJSON, loadModel, loadPixels, loadShader, loadStrings, loadTable, loadXML, log, logOnloaded, loop, mag, map, match, matchAll, max, millis, min, minute, model, month, mouseButton, mouseIsPressed, mouseX, mouseY, nf, nfc, nfp, nfs, noCanvas, noCursor, noDebugMode, noErase, noFill, noLoop, noSmooth, noStroke, noTint, noise, noiseDetail, noiseSeed, norm, normalMaterial, orbitControl, ortho, pAccelerationX, pAccelerationY, pAccelerationZ, pRotationX, pRotationY, pRotationZ, perspective, pixelDensity, pixels, plane, pmouseX, pmouseY, point, pointLight, popMatrix, popStyle, pow, pre_draw, preload, push, pushMatrix, pushStyle, pwinMouseX, pwinMouseY, py_clear, py_get, py_pop, py_sort, py_split, quad, quadraticVertex, radians, random, randomGaussian, randomSeed, rect, rectMode, red, redraw, remove, removeElements, resetMatrix, resetShader, resizeCanvas, reverse, rotate, rotateX, rotateY, rotateZ, rotationX, rotationY, rotationZ, round, saturation, save, saveCanvas, saveFrames, saveJSON, saveStrings, saveTable, scale, second, select, selectAll, set, setAttributes, setCamera, setMoveThreshold, setShakeThreshold, shader, shearX, shearY, shininess, shorten, shuffle, sin, size, smooth, specularMaterial, sphere, splice, splitTokens, sq, sqrt, square, start_p5, str, stroke, strokeCap, strokeJoin, strokeWeight, subset, tan, text, textAlign, textAscent, textDescent, textFont, textLeading, textSize, textStyle, textWidth, texture, textureMode, textureWrap, tint, torus, touches, translate, triangle, trim, turnAxis, unchar, unhex, updatePixels, vertex, width, winMouseX, winMouseY, windowHeight, windowWidth, year} from './pyp5js.js';
var __name__ = 'villares_arcs_and_bars_pyp5js';
export var setup = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
	}
	else {
	}
	size (400, 400);
};
export var draw = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
	}
	else {
	}
	background (200);
	fill (0);
	text ('press any key to see p_arc polygonal aproximantion used', 20, 20);
	fill (0, 0, 200, 100);
	line (50, 50, 350, 250);
	if (!(keyIsPressed)) {
		bar (50, 50, 350, 250, 60, __kwargtrans__ ({shorter: mouseX}));
		var_bar (50, 160, 350, 310, 40, 0);
		var_bar (50, 250, 50 + mouseX * 0.7, 250 + mouseX * 0.25, 20, 40);
	}
	else {
		bar (50, 50, 350, 250, __kwargtrans__ ({thickness: 60, shorter: mouseX, arc_func: p_arc, num_points: 3}));
		var_bar (50, 160, 350, 310, 40, 0, __kwargtrans__ ({arc_func: p_arc, num_points: 6}));
		var_bar (50, 250, 50 + mouseX / 2, 250 + mouseX * 0.2, 20, 40, __kwargtrans__ ({arc_func: p_arc, num_points: 8}));
	}
};
export var PVector = function (v) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'v': var v = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return createVector (v);
};
export var DEBUG = false;
export var ROTATION = dict ([[0, 0], [1, HALF_PI], [2, PI], [3, PI + HALF_PI]]);
export var circle_arc = function (x, y, radius, start_ang, sweep_ang) {
	var kwargs = dict ();
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					case 'radius': var radius = __allkwargs0__ [__attrib0__]; break;
					case 'start_ang': var start_ang = __allkwargs0__ [__attrib0__]; break;
					case 'sweep_ang': var sweep_ang = __allkwargs0__ [__attrib0__]; break;
					default: kwargs [__attrib0__] = __allkwargs0__ [__attrib0__];
				}
			}
			delete kwargs.__kwargtrans__;
		}
		var args = tuple ([].slice.apply (arguments).slice (5, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	var arc_func = kwargs.py_pop ('arc_func', arc);
	arc_func (x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang, ...args, __kwargtrans__ (kwargs));
};
export var quarter_circle = function (x, y, radius, quadrant) {
	var kwargs = dict ();
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					case 'radius': var radius = __allkwargs0__ [__attrib0__]; break;
					case 'quadrant': var quadrant = __allkwargs0__ [__attrib0__]; break;
					default: kwargs [__attrib0__] = __allkwargs0__ [__attrib0__];
				}
			}
			delete kwargs.__kwargtrans__;
		}
		var args = tuple ([].slice.apply (arguments).slice (4, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	circle_arc (x, y, radius, ROTATION [quadrant], HALF_PI, ...args, __kwargtrans__ (kwargs));
};
export var half_circle = function (x, y, radius, quadrant) {
	var kwargs = dict ();
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					case 'radius': var radius = __allkwargs0__ [__attrib0__]; break;
					case 'quadrant': var quadrant = __allkwargs0__ [__attrib0__]; break;
					default: kwargs [__attrib0__] = __allkwargs0__ [__attrib0__];
				}
			}
			delete kwargs.__kwargtrans__;
		}
		var args = tuple ([].slice.apply (arguments).slice (4, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	circle_arc (x, y, radius, ROTATION [quadrant], PI, ...args, __kwargtrans__ (kwargs));
};
export var b_circle_arc = function (x, y, radius, start_ang, sweep_ang, mode) {
	if (typeof mode == 'undefined' || (mode != null && mode.hasOwnProperty ("__kwargtrans__"))) {;
		var mode = 0;
	};
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					case 'radius': var radius = __allkwargs0__ [__attrib0__]; break;
					case 'start_ang': var start_ang = __allkwargs0__ [__attrib0__]; break;
					case 'sweep_ang': var sweep_ang = __allkwargs0__ [__attrib0__]; break;
					case 'mode': var mode = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	b_arc (x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang, __kwargtrans__ ({mode: mode}));
};
export var b_arc = function (cx, cy, w, h, start_angle, end_angle, mode) {
	if (typeof mode == 'undefined' || (mode != null && mode.hasOwnProperty ("__kwargtrans__"))) {;
		var mode = 0;
	};
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'cx': var cx = __allkwargs0__ [__attrib0__]; break;
					case 'cy': var cy = __allkwargs0__ [__attrib0__]; break;
					case 'w': var w = __allkwargs0__ [__attrib0__]; break;
					case 'h': var h = __allkwargs0__ [__attrib0__]; break;
					case 'start_angle': var start_angle = __allkwargs0__ [__attrib0__]; break;
					case 'end_angle': var end_angle = __allkwargs0__ [__attrib0__]; break;
					case 'mode': var mode = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var theta = end_angle - start_angle;
	if (mode != 1 || abs (theta) < HALF_PI) {
		var x0 = cos (theta / 2.0);
		var y0 = sin (theta / 2.0);
		var x3 = x0;
		var y3 = 0 - y0;
		var x1 = (4.0 - x0) / 3.0;
		var y1 = (y0 != 0 ? ((1.0 - x0) * (3.0 - x0)) / (3.0 * y0) : 0);
		var x2 = x1;
		var y2 = 0 - y1;
		var bezAng = start_angle + theta / 2.0;
		var cBezAng = cos (bezAng);
		var sBezAng = sin (bezAng);
		var rx0 = cBezAng * x0 - sBezAng * y0;
		var ry0 = sBezAng * x0 + cBezAng * y0;
		var rx1 = cBezAng * x1 - sBezAng * y1;
		var ry1 = sBezAng * x1 + cBezAng * y1;
		var rx2 = cBezAng * x2 - sBezAng * y2;
		var ry2 = sBezAng * x2 + cBezAng * y2;
		var rx3 = cBezAng * x3 - sBezAng * y3;
		var ry3 = sBezAng * x3 + cBezAng * y3;
		var __left0__ = tuple ([w / 2.0, h / 2.0]);
		var rx = __left0__ [0];
		var ry = __left0__ [1];
		var px0 = cx + rx * rx0;
		var py0 = cy + ry * ry0;
		var px1 = cx + rx * rx1;
		var py1 = cy + ry * ry1;
		var px2 = cx + rx * rx2;
		var py2 = cy + ry * ry2;
		var px3 = cx + rx * rx3;
		var py3 = cy + ry * ry3;
		if (DEBUG) {
			ellipse (px3, py3, 3, 3);
			ellipse (px0, py0, 5, 5);
		}
	}
	if (mode == 0) {
		beginShape ();
	}
	if (mode != 1) {
		vertex (px3, py3);
	}
	if (abs (theta) < HALF_PI) {
		bezierVertex (px2, py2, px1, py1, px0, py0);
	}
	else {
		b_arc (cx, cy, w, h, start_angle, end_angle - theta / 2.0, __kwargtrans__ ({mode: 1}));
		b_arc (cx, cy, w, h, start_angle + theta / 2.0, end_angle, __kwargtrans__ ({mode: 1}));
	}
	if (mode == 0) {
		endShape ();
	}
};
export var p_circle_arc = function (x, y, radius, start_ang, sweep_ang, mode) {
	if (typeof mode == 'undefined' || (mode != null && mode.hasOwnProperty ("__kwargtrans__"))) {;
		var mode = 0;
	};
	var kwargs = dict ();
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					case 'radius': var radius = __allkwargs0__ [__attrib0__]; break;
					case 'start_ang': var start_ang = __allkwargs0__ [__attrib0__]; break;
					case 'sweep_ang': var sweep_ang = __allkwargs0__ [__attrib0__]; break;
					case 'mode': var mode = __allkwargs0__ [__attrib0__]; break;
					default: kwargs [__attrib0__] = __allkwargs0__ [__attrib0__];
				}
			}
			delete kwargs.__kwargtrans__;
		}
	}
	else {
	}
	p_arc (x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang, __kwargtrans__ (__mergekwargtrans__ ({mode: mode}, kwargs)));
};
export var p_arc = function (cx, cy, w, h, start_angle, end_angle, mode, num_points, vertex_func) {
	if (typeof mode == 'undefined' || (mode != null && mode.hasOwnProperty ("__kwargtrans__"))) {;
		var mode = 0;
	};
	if (typeof num_points == 'undefined' || (num_points != null && num_points.hasOwnProperty ("__kwargtrans__"))) {;
		var num_points = 24;
	};
	if (typeof vertex_func == 'undefined' || (vertex_func != null && vertex_func.hasOwnProperty ("__kwargtrans__"))) {;
		var vertex_func = vertex;
	};
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'cx': var cx = __allkwargs0__ [__attrib0__]; break;
					case 'cy': var cy = __allkwargs0__ [__attrib0__]; break;
					case 'w': var w = __allkwargs0__ [__attrib0__]; break;
					case 'h': var h = __allkwargs0__ [__attrib0__]; break;
					case 'start_angle': var start_angle = __allkwargs0__ [__attrib0__]; break;
					case 'end_angle': var end_angle = __allkwargs0__ [__attrib0__]; break;
					case 'mode': var mode = __allkwargs0__ [__attrib0__]; break;
					case 'num_points': var num_points = __allkwargs0__ [__attrib0__]; break;
					case 'vertex_func': var vertex_func = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var sweep_angle = end_angle - start_angle;
	if (mode == 0) {
		beginShape ();
	}
	if (sweep_angle < 0) {
		var __left0__ = tuple ([end_angle, start_angle]);
		var start_angle = __left0__ [0];
		var end_angle = __left0__ [1];
		var sweep_angle = -(sweep_angle);
		var angle = float (sweep_angle) / abs (num_points);
		var a = end_angle;
		while (a >= start_angle) {
			var sx = cx + (cos (a) * w) / 2.0;
			var sy = cy + (sin (a) * h) / 2.0;
			vertex_func (sx, sy);
			a -= angle;
		}
	}
	else if (sweep_angle > 0) {
		var angle = sweep_angle / int (num_points);
		var a = start_angle;
		while (a <= end_angle) {
			var sx = cx + (cos (a) * w) / 2.0;
			var sy = cy + (sin (a) * h) / 2.0;
			vertex_func (sx, sy);
			a += angle;
		}
	}
	else {
		var sx = cx + (cos (start_angle) * w) / 2.0;
		var sy = cy + (sin (start_angle) * h) / 2.0;
		vertex_func (sx, sy);
	}
	if (mode == 0) {
		endShape ();
	}
};
export var bar = function (x1, y1, x2, y2, thickness) {
	var kwargs = dict ();
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x1': var x1 = __allkwargs0__ [__attrib0__]; break;
					case 'y1': var y1 = __allkwargs0__ [__attrib0__]; break;
					case 'x2': var x2 = __allkwargs0__ [__attrib0__]; break;
					case 'y2': var y2 = __allkwargs0__ [__attrib0__]; break;
					case 'thickness': var thickness = __allkwargs0__ [__attrib0__]; break;
					default: kwargs [__attrib0__] = __allkwargs0__ [__attrib0__];
				}
			}
			delete kwargs.__kwargtrans__;
		}
	}
	else {
	}
	var_bar (x1, y1, x2, y2, thickness / 2, __kwargtrans__ (kwargs));
};
export var var_bar = function (p1x, p1y, p2x, p2y, r1, r2) {
	if (typeof r2 == 'undefined' || (r2 != null && r2.hasOwnProperty ("__kwargtrans__"))) {;
		var r2 = null;
	};
	var kwargs = dict ();
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'p1x': var p1x = __allkwargs0__ [__attrib0__]; break;
					case 'p1y': var p1y = __allkwargs0__ [__attrib0__]; break;
					case 'p2x': var p2x = __allkwargs0__ [__attrib0__]; break;
					case 'p2y': var p2y = __allkwargs0__ [__attrib0__]; break;
					case 'r1': var r1 = __allkwargs0__ [__attrib0__]; break;
					case 'r2': var r2 = __allkwargs0__ [__attrib0__]; break;
					default: kwargs [__attrib0__] = __allkwargs0__ [__attrib0__];
				}
			}
			delete kwargs.__kwargtrans__;
		}
	}
	else {
	}
	var r2 = (r2 !== null ? r2 : r1);
	var draw_internal_circles = kwargs.py_pop ('internal', true);
	var arc_func = kwargs.py_pop ('arc_func', b_arc);
	var shorter = kwargs.py_pop ('shorter', 0);
	var d = dist (p1x, p1y, p2x, p2y);
	var ri = r1 - r2;
	if (d > abs (ri)) {
		var clipped_ri_over_d = min (1, max (-(1), ri / d));
		var beta = asin (clipped_ri_over_d) + HALF_PI;
		pushMatrix ();
		translate (p1x, p1y);
		var angle = atan2 (p1x - p2x, p2y - p1y);
		rotate (angle + HALF_PI);
		var x1 = cos (beta) * r1;
		var y1 = sin (beta) * r1;
		var x2 = cos (beta) * r2;
		var y2 = sin (beta) * r2;
		beginShape ();
		var offset = (shorter < d ? shorter / 2.0 : d / 2.0);
		arc_func (offset, 0, r1 * 2, r1 * 2, -(beta) - PI, beta - PI, __kwargtrans__ (__mergekwargtrans__ ({mode: 2}, kwargs)));
		arc_func (d - offset, 0, r2 * 2, r2 * 2, beta - PI, PI - beta, __kwargtrans__ (__mergekwargtrans__ ({mode: 2}, kwargs)));
		endShape (CLOSE);
		popMatrix ();
	}
	else if (draw_internal_circles) {
		arc_func (p1x, p1y, r1 * 2, r1 * 2, 0, TWO_PI, __kwargtrans__ (kwargs));
		arc_func (p2x, p2y, r2 * 2, r2 * 2, 0, TWO_PI, __kwargtrans__ (kwargs));
	}
};

//# sourceMappingURL=villares_arcs_and_bars_pyp5js.map