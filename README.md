#  Arc, tangents & Bezier studies

![](https://raw.githubusercontent.com/villares/arc_tangents_and_bezier_studies/master/villares_filleted_and_arc_augmented_polys/sketch_2020_09_26a.gif)

I have added very little new ideas here, most of my findings & previous studies were moved into the `prior_art` folder, I tried to attribute stuff with links.

### Bezier approximation of an arc

The `b_arc` function can be used inside `beginShape()`/`endShape()` as a kind of "arcVertex" (which doesn't exist). It follows mostly the Processing `arc` signature, but does not include PIE and CHORD modes. You can find demos at:

  - [`b_arc`](/villares_bezier_arc_aproximation/villares_bezier_arc_aproximation.pyde) Processing Python (also works on pyp5js)
  - [`b_arc`](/villares_bezier_arc_aproximation_java/villares_bezier_arc_aproximation_java.pde) Processing Java 
  - [`b_arc`](/villares_bezier_arc_aproximation_p5js/villares_bezier_arc_aproximation_p5js.js) p5.js

   > ![b_arc](villares_bezier_arc_aproximation/b_arc.png)
   > ```python
   > x, y, w, h, start_angle, end_angle = 75, 100, 100, 100, 0, PI + QUARTER_PI
   > # Standalone arc replacement
   > b_arc(x, y, w, h, start_angle, end_angle)
   >
   > # mode=2 for use inside beginShape/endShape
   > x += 125
   > beginShape()
   > b_arc(x, y, w, h, start_angle, end_angle, mode=2) 
   > endShape(CLOSE)
   > x += 125
   > beginShape()
   > b_arc(x, y, w, h, start_angle, end_angle, mode=2)
   > vertex(x, y)
   > endShape(CLOSE)
   > ```

### More arcs and tangents

More stuff based on `b_arc`, code kept at [`arcs.py`](https://raw.githubusercontent.com/villares/villares/master/arcs.py). Most functions can also be used with `p_arc`(a polygonal aproximantion of an arc). Except were noted, mostly Processing Python mode funtions, as I have not yet ported them to other languages. *Feel free to contribute porting stuff!*

- The `bar` and `var_bar` functions draws "two connected circles" (both work in pyp5js, [demo here](https://abav.lugaralgum.com/arc_tangents_and_bezier_studies/villares_arcs_and_bars_pyp5js/)!)

    > ![](https://raw.githubusercontent.com/villares/arc_tangents_and_bezier_studies/master/villares_arcs_and_bars/villares_arcs_and_bars.gif)
    > ```python
    > …
    > if not keyPressed:  # By default arc_func=b_arc
    >     # bar(ax, ay, bx, by, thickness) shorter=0 
    >     bar(50, 50, 350, 250, 60, shorter=mouseX)
    >     # var_bar(ax, ay, bx, by, a_radius, b_radius)
    >     var_bar(50, 160, 350, 310, 40, 0)
    >     var_bar(50, 250, 50 + mouseX * .7, 250 + mouseX * .25, 20, 40)
    > else:
    >     bar(50, 50, 350, 250, 60, shorter=mouseX, arc_func=p_arc, num_points=3)
    >     var_bar(50, 160, 350, 310, 40, 0, arc_func=p_arc, num_points=6)
    >     var_bar(50, 250, 50 + mouseX / 2, 250 + mouseX * .20, 20, 40,
    >             arc_func=p_arc, num_points=8)
    > ```

- Rounding polygons "outside" with `arc_augmented_poly`, takes a sequence of points and radii and calculates geometry with the `circ_circ_tangent` function.

- Rounding polygons "in", filleted polygons `arc_filleted_poly`, takes a sequence of points and radii and uses the `arc_corner`function to draw.

- The `circle_arc` function tries to create a simpler interface for Processing `arc`, asking for *x*, *y*, *radius*, *start_angle*, and *sweep* (instead of *width*, *height* and *end_angle*). Now it also allows `b_arc` and `p_arc` drawing. The `half_circle` and `quarter_circle` are similar `arc` (or `b_arc`/`p_arc`) wrappers using a mix of Processing constants to define rotation.

    > ![circle_arc](villares_bezier_arc_aproximation/circle_arc.png)
    > ```python
    > x, y, radius, start_angle, sweep = 75, 105, 50, 0, PI + QUARTER_PI
    > circle_arc(x, y, radius, start_angle, sweep)    # default 'arc' wrapper mode
    > circle_arc(x, y, radius, -QUARTER_PI / 2, -HALF_PI, arc_func=p_arc, num_points=4)
    > 
    > x, y1, y2 = 190, 95, 105
    > half_circle(x, y1, radius, UP, CHORD)  # default 'arc' wrapper mode
    > half_circle(x, y2, radius, DOWN, arc_func=b_arc)
    > 
    > x1, x2, y1, y2 = 300, 310, 95, 105
    > quarter_circle(x1, y1, radius, TOP + LEFT, CHORD)  # default 'arc' wrapper mode
    > quarter_circle(x1, y2, radius, BOTTOM + LEFT, PIE)
    > quarter_circle(x2, y1, radius, TOP + RIGHT)
    > quarter_circle(x2, y2, radius, BOTTOM + RIGHT, arc_func=b_arc)
    > ```

```
