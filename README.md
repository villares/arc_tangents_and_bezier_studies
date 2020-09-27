#  Arc, tangents & Bezier studies

### Bezier approximation of an arc

The `b_arc` function can be used inside `beginShape()`/`endShape()` as a kindo of "arcVertex" (which doesn't exist). It follows mostly the `arc`signature, but does not include PIE and CHORD modes.

  - Processing Python (also works on pyp5js)
  - Processing Java 
  - p5.js

### Tangents

All based on 'b_arc`, but can be used with `p_arc` as well.
Processing Python mode only, not yet ported to other languages.

- Simple `bar` and `var_bar` functions (two circles connected)
- Rounded "out" polygons with `arc_augmented_poly`
   - uses a `circle_circle_tangent`function
- Rounded "in" or filleted polygons `arc_filleted_poly()`
 

### Other
- `p_arc` a polygonal aproximantion of an arc

*Feel free to contribute porting stuff!*

