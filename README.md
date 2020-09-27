#  Arc, tangents & Bezier studies

### Bezier approximation of an arc

The `b_arc` function can be used inside `beginShape()`/`endShape()` as a kindo of "arcVertex" (which doesn't exist). It follows mostly the `arc`signature, but does not include PIE and CHORD modes. You can find demos at:

  - [``]() Processing Python (also works on pyp5js)
  - [``]() Processing Java 
  - [``]() p5.js

### Tangents

More stuff based on `b_arc`, can be foud at [`arcs.py`], most functions can also be used with `p_arc`.
At this point it is Processing Python mode only, as I have not yet ported them to other languages.
*Feel free to contribute porting stuff!*

- Simple `bar` and `var_bar` functions (draws two connected circles)
- Rounding polygons "outside" with `arc_augmented_poly`
   - uses a `circle_circle_tangent`function
- Rounding polygons "in", filleted polygons `arc_filleted_poly`
 

### Other

- `p_arc` a polygonal aproximantion of an arc

