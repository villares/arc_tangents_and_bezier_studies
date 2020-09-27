#  Arc, tangents & Bezier studies

![](https://raw.githubusercontent.com/villares/arc_tangents_and_bezier_studies/master/villares_filleted_and_arc_augmented_polys/sketch_2020_09_26a.gif)

### Bezier approximation of an arc

The `b_arc` function can be used inside `beginShape()`/`endShape()` as a kind of "arcVertex" (which doesn't exist). It follows mostly the Processing `arc` signature, but does not include PIE and CHORD modes. You can find demos at:

  - [`b_arc`](/villares_bezier_arc_aproximation/villares_bezier_arc_aproximation.pyde) Processing Python (also works on pyp5js)
  - [`b_arc`](/villares_bezier_arc_aproximation_java/villares_bezier_arc_aproximation_java.pde) Processing Java 
  - [`b_arc`](/villares_bezier_arc_aproximation_p5js/villares_bezier_arc_aproximation_p5js.js) p5.js

### More arcs and tangents

More stuff based on `b_arc`, can be found at [`arcs.py`](https://raw.githubusercontent.com/villares/villares/master/arcs.py), most functions can also be used with `p_arc`.
At this point it is Processing Python mode only, as I have not yet ported them to other languages.
*Feel free to contribute porting stuff!*

- Simple `bar` and `var_bar` functions (draws two connected circles)
- Rounding polygons "outside" with `arc_augmented_poly`
   - uses a `circle_circle_tangent`function
- Rounding polygons "in", filleted polygons `arc_filleted_poly`
- `p_arc` a polygonal aproximantion of an arc

