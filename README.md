#  Arc, tangents & Bezier studies

![](https://raw.githubusercontent.com/villares/arc_tangents_and_bezier_studies/master/villares_filleted_and_arc_augmented_polys/sketch_2020_09_26a.gif)

I have added very little new ideas here, most of my findings & previous studies were moved into the `prior_art` folder, I tried to attribute stuff with links.

### Bezier approximation of an arc

The `b_arc` function can be used inside `beginShape()`/`endShape()` as a kind of "arcVertex" (which doesn't exist). It follows mostly the Processing `arc` signature, but does not include PIE and CHORD modes. You can find demos at:

  - [`b_arc`](/villares_bezier_arc_aproximation/villares_bezier_arc_aproximation.pyde) Processing Python (also works on pyp5js)
  - [`b_arc`](/villares_bezier_arc_aproximation_java/villares_bezier_arc_aproximation_java.pde) Processing Java 
  - [`b_arc`](/villares_bezier_arc_aproximation_p5js/villares_bezier_arc_aproximation_p5js.js) p5.js

### More arcs and tangents

More stuff based on `b_arc`, code kept at [`arcs.py`](https://raw.githubusercontent.com/villares/villares/master/arcs.py). Most functions can also be used with `p_arc`(a polygonal aproximantion of an arc). Except were noted, mostly Processing Python mode funtions, as I have not yet ported them to other languages. *Feel free to contribute porting stuff!*

- `circle_arc` tries to create a simpler interface for Processing `arc`, asking for *x*, *y*, *radius*, *start_angle*, and *sweep* (instead of *width*, *height* and *end_angle*). Now it also allows `b_arc` and `p_arc` drawing. 

- `half_circle` ande `quarter_circle` are similar `arc` (or `b_arc`/`p_arc`) wrappers.

- Simple `bar` and `var_bar` functions to draws "two connected circles" (works in pyp5js)
  > ![](https://raw.githubusercontent.com/villares/arc_tangents_and_bezier_studies/master/villares_arcs_and_bars/villares_arcs_and_bars.gif)

- Rounding polygons "outside" with `arc_augmented_poly`
   - uses `circ_circ_tangent` function

- Rounding polygons "in", filleted polygons `arc_filleted_poly`
   - uses `arc_corner`function`
