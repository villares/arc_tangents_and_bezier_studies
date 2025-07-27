# Arc, tangents & Bezier studies

![sketch_2020_09_26a](https://raw.githubusercontent.com/villares/sketch-a-day/main/2020/sketch_2020_09_26a/sketch_2020_09_26a.gif)

> from sketch-a-day project, [sketch_2020_09_26a](https://github.com/villares/sketch-a-day/tree/main/2020/sketch_2020_09_26a)

This repository contains the product of my studies trying to work with arcs, bezier approximations of arcs and tangents. I have added very little new ideas here, you can look at the findings & previous studies I moved into the `PRIOR_ART` folder. I tried to attribute stuff with links. 

The functions can be found at [`arcs.py`](https://raw.githubusercontent.com/villares/villares/refs/heads/main/arcs.py), and some depend on [`line_geometry.py`](https://raw.githubusercontent.com/villares/villares/refs/heads/main/line_geometry.py), they were made initially on Processing Python mode and now work with [py5](http://py5coding.org). Most will work with [pyp5js](berinhard.github.io/pyp5js/) or with the modified [pyp5js/py5mode](https://abav.lugaralgum.com/pyp5js/py5mode) too, and I have ported `b_arc` for Processing Java and p5js. **You are welcome to help porting more stuff!**

Please note that the most recent (and maybe unstable?) version of the Python functions shown here, but with support only for py5, are kept at this other repository: [github.com/villares/villares](https://github.com/villares/villares), on [`arcs_helper.py`](https://github.com/villares/villares/blob/main/arc_helpers.py) and [`geometry_helpers.py`](https://github.com/villares/villares/blob/main/geometry_helpers.py) it depends on.

### Bezier approximation of an arc

Processing *PShape* insfrastructure (and *Py5hape* that depends on it) does not contain a fuction for embeding an arc in a larger polyline shape. The `b_arc` function provided here can be used inside `begin_shape()`/`end_shape()` as a kind of "arc_vertex" (which doesn't exist). It follows mostly the Processing/py5 `arc` signature, but does not include PIE and CHORD modes. You can find demos at:

- [`b_arc`](/villares_bezier_arc_aproximation/villares_bezier_arc_aproximation.py) for **py5**, also works on [**pyp5js/py5mode** on your browser](https://abav.lugaralgum.com/pyp5js/py5mode/fullscreen.html?sketch=JTIyJTIyJTIyJTIwJTBBJTIwV3JpdHRlbiUyMGJ5JTIwQWxleGFuZHJlJTIwQiUyMEElMjBWaWxsYXJlcyUyMGZvciUyMHB5NSUyMCUzQ3B5NWNvZGluZy5vcmclM0UlMjBpbXBvcnRlZCUyMG1vZGUlMEElMjBCYXNlZCUyMG9uJTIwR29sYW4lMjBMZXZpbidzJTIwYXBwcm94aW1hdGluZyUyMGElMjBjaXJjdWxhciUyMGFyYyUyMHdpdGglMjBhJTIwY3ViaWMlMjBCZXppZXIlMjBjdXJ2ZS4lMEElMjBodHRwJTNBJTJGJTJGd3d3LmZsb25nLmNvbSUyRmJsb2clMkYyMDA5JTJGYmV6aWVyLWFwcHJveGltYXRpb24tb2YtYS1jaXJjdWxhci1hcmMtaW4tcHJvY2Vzc2luZyUyRiUwQSUyMiUyMiUyMiUwQSUwQURFQlVHJTIwJTNEJTIwRmFsc2UlMEFyYWRpdXMlMjAlM0QlMjAzMDAlMjAlMjAlMjMlMjByYWRpdXMlMjBvZiUyMHRoZSUyMGNpcmN1bGFyJTIwYXJjJTBBY3glMjAlM0QlMjAzNDAlMjAlMjAlMjMlMjBjZW50ZXIlMjBvZiUyMHRoZSUyMGNpcmN1bGFyJTIwYXJjJTBBY3klMjAlM0QlMjAzNDAlMEElMEFkZWYlMjBzZXR1cCgpJTNBJTBBJTIwJTIwJTIwJTIwc2l6ZSg2ODAlMkMlMjA2ODApJTBBJTBBZGVmJTIwZHJhdygpJTNBJTBBJTIwJTIwJTIwJTIwYmFja2dyb3VuZCgyMzApJTBBJTIwJTIwJTIwJTIwc3Ryb2tlX3dlaWdodCgzKSUwQSUwQSUyMCUyMCUyMCUyMCUyMyUyMEVzdGFibGlzaCUyMGFyYyUyMHBhcmFtZXRlcnMuJTIwTm90ZSUzQSUyMGFzc2VydCUyMHRoZXRhJTIwISUzRCUyMFRXT19QSSklMEElMjAlMjAlMjAlMjB0aGV0YSUyMCUzRCUyMHJhZGlhbnMobW91c2VfeCUyMCUyRiUyMDEuOCklMjAlMjAlMjMlMjBzcHJlYWQlMjBvZiUyMHRoZSUyMGFyYy4lMEElMjAlMjAlMjAlMjBzdGFydF9hbmdsZSUyMCUzRCUyMHJhZGlhbnMobW91c2VfeSUyMCUyRiUyMDguMCklMjAlMjAlMjMlMjBhcyUyMGluJTIwYXJjKCklMEElMjAlMjAlMjAlMjBlbmRfYW5nbGUlMjAlM0QlMjBzdGFydF9hbmdsZSUyMCUyQiUyMHRoZXRhJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIzJTIwYXMlMjBpbiUyMGFyYygpJTBBJTBBJTIwJTIwJTIwJTIwJTIzJTIwQkxVRSUyMElTJTIwVEhFJTIwJTIyVFJVRSUyMiUyMEFSQyUzQSUwQSUyMCUyMCUyMCUyMGZpbGwoMCUyQyUyMDAlMkMlMjAyNTUlMkMlMjAxMCklMEElMjAlMjAlMjAlMjBzdHJva2UoMCUyQyUyMDAlMkMlMjAyNTUlMkMlMjAxMjgpJTBBJTIwJTIwJTIwJTIwYXJjKGN4JTJDJTIwY3klMkMlMjByYWRpdXMlMjAqJTIwMiUyQyUyMHJhZGl1cyUyMColMjAyJTJDJTIwc3RhcnRfYW5nbGUlMkMlMjBlbmRfYW5nbGUpJTBBJTIwJTIwJTIwJTIwJTBBJTIwJTIwJTIwJTIwJTIzJTIwUkVEJTIwSVMlMjBUSEUlMjBCRVpJRVIlMjBBUFBST1hJTUFUSU9OJTIwT0YlMjBUSEUlMjBBUkMlM0ElMEElMjAlMjAlMjAlMjBmaWxsKDI1NSUyQzAlMkMwJTJDJTIwMTApJTBBJTIwJTIwJTIwJTIwc3Ryb2tlKDI1NSUyQyUyMDAlMkMlMjAwJTJDJTIwMTI4KSUwQSUyMCUyMCUyMCUyMGJfYXJjKGN4JTJDJTIwY3klMkMlMjByYWRpdXMlMjAqJTIwMiUyQyUyMHJhZGl1cyUyMColMjAyJTJDJTIwc3RhcnRfYW5nbGUlMkMlMjBlbmRfYW5nbGUpJTBBJTBBJTBBZGVmJTIwYl9hcmMoY3glMkMlMjBjeSUyQyUyMHclMkMlMjBoJTJDJTIwc3RhcnRfYW5nbGUlMkMlMjBlbmRfYW5nbGUlMkMlMjBtb2RlJTNEMCklM0ElMEElMjAlMjAlMjAlMjAlMjIlMjIlMjIlMEElMjAlMjAlMjAlMjBEcmF3JTIwYSUyMGJlemllciUyMGFwcHJveGltYXRpb24lMjBvZiUyMGFuJTIwYXJjJTIwdXNpbmclMjB0aGUlMjBzYW1lJTBBJTIwJTIwJTIwJTIwc2lnbmF0dXJlJTIwYXMlMjB0aGUlMjBvcmlnaW5hbCUyMFByb2Nlc3NpbmclMjBhcmMoKS4lMEElMjAlMjAlMjAlMjBtb2RlJTNBJTIwMCUyMCUyMm5vcm1hbCUyMiUyMGFyYyUyQyUyMHVzaW5nJTIwYmVnaW5fc2hhcGUoKSUyMGFuZCUyMGVuZF9zaGFwZSgpJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwMSUyMCUyMm1pZGRsZSUyMiUyMHVzZWQlMjBpbiUyMHJlY3Vyc2l2ZSUyMGNhbGwlMjBvZiUyMHNtYWxsZXIlMjBhcmNzJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwMiUyMCUyMm5ha2VkJTIyJTIwbGlrZSUyMG5vcm1hbCUyQyUyMGJ1dCUyMHdpdGhvdXQlMjBiZWdpbl9zaGFwZSgpJTIwYW5kJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwZW5kX3NoYXBlKCklMjBmb3IlMjB1c2UlMjBpbnNpZGUlMjBhJTIwbGFyZ2VyJTIwUFNoYXBlJTJGUHk1U2hhcGUuJTBBJTIwJTIwJTIwJTIwJTIyJTIyJTIyJTBBJTIwJTIwJTIwJTIwJTIzJTIwQmFzZWQlMjBvbiUyMGlkZWFzJTIwZnJvbSUyMFJpY2hhcmQlMjBEZVZlbmV6YSUyMHZpYSUyMGNvZGUlMjBieSUyMEdvbGFuJTIwTGV2aW4lM0ElMEElMjAlMjAlMjAlMjAlMjMlMjBodHRwJTNBJTJGJTJGd3d3LmZsb25nLmNvbSUyRmJsb2clMkYyMDA5JTJGYmV6aWVyLWFwcHJveGltYXRpb24tb2YtYS1jaXJjdWxhci1hcmMtaW4tcHJvY2Vzc2luZyUyRiUwQSUyMCUyMCUyMCUyMHRoZXRhJTIwJTNEJTIwZW5kX2FuZ2xlJTIwLSUyMHN0YXJ0X2FuZ2xlJTBBJTIwJTIwJTIwJTIwJTIzJTIwQ29tcHV0ZSUyMHJhdyUyMEJlemllciUyMGNvb3JkaW5hdGVzLiUwQSUyMCUyMCUyMCUyMGlmJTIwbW9kZSUyMCElM0QlMjAxJTIwb3IlMjBhYnModGhldGEpJTIwJTNDJTIwSEFMRl9QSSUzQSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHgwJTIwJTNEJTIwY29zKHRoZXRhJTIwJTJGJTIwMi4wKSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHkwJTIwJTNEJTIwc2luKHRoZXRhJTIwJTJGJTIwMi4wKSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHgzJTIwJTNEJTIweDAlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjB5MyUyMCUzRCUyMDAlMjAtJTIweTAlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjB4MSUyMCUzRCUyMCg0LjAlMjAtJTIweDApJTIwJTJGJTIwMy4wJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIweTElMjAlM0QlMjAoKDEuMCUyMC0lMjB4MCklMjAqJTIwKDMuMCUyMC0lMjB4MCkpJTIwJTJGJTIwKDMuMCUyMColMjB5MCklMjBpZiUyMHkwJTIwISUzRCUyMDAlMjBlbHNlJTIwMCUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHgyJTIwJTNEJTIweDElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjB5MiUyMCUzRCUyMDAlMjAtJTIweTElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjMlMjBDb21wdXRlJTIwcm90YXRpb25hbGx5LW9mZnNldCUyMEJlemllciUyMGNvb3JkaW5hdGVzJTJDJTIwdXNpbmclM0ElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjMlMjB4JyUyMCUzRCUyMGNvcyhhbmdsZSklMjAqJTIweCUyMC0lMjBzaW4oYW5nbGUpJTIwKiUyMHklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjMlMjB5JyUyMCUzRCUyMHNpbihhbmdsZSklMjAqJTIweCUyMCUyQiUyMGNvcyhhbmdsZSklMjAqJTIweSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGJlekFuZyUyMCUzRCUyMHN0YXJ0X2FuZ2xlJTIwJTJCJTIwdGhldGElMjAlMkYlMjAyLjAlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBjQmV6QW5nJTIwJTNEJTIwY29zKGJlekFuZyklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBzQmV6QW5nJTIwJTNEJTIwc2luKGJlekFuZyklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjByeDAlMjAlM0QlMjBjQmV6QW5nJTIwKiUyMHgwJTIwLSUyMHNCZXpBbmclMjAqJTIweTAlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjByeTAlMjAlM0QlMjBzQmV6QW5nJTIwKiUyMHgwJTIwJTJCJTIwY0JlekFuZyUyMColMjB5MCUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHJ4MSUyMCUzRCUyMGNCZXpBbmclMjAqJTIweDElMjAtJTIwc0JlekFuZyUyMColMjB5MSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHJ5MSUyMCUzRCUyMHNCZXpBbmclMjAqJTIweDElMjAlMkIlMjBjQmV6QW5nJTIwKiUyMHkxJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwcngyJTIwJTNEJTIwY0JlekFuZyUyMColMjB4MiUyMC0lMjBzQmV6QW5nJTIwKiUyMHkyJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwcnkyJTIwJTNEJTIwc0JlekFuZyUyMColMjB4MiUyMCUyQiUyMGNCZXpBbmclMjAqJTIweTIlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjByeDMlMjAlM0QlMjBjQmV6QW5nJTIwKiUyMHgzJTIwLSUyMHNCZXpBbmclMjAqJTIweTMlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjByeTMlMjAlM0QlMjBzQmV6QW5nJTIwKiUyMHgzJTIwJTJCJTIwY0JlekFuZyUyMColMjB5MyUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMyUyMENvbXB1dGUlMjBzY2FsZWQlMjBhbmQlMjB0cmFuc2xhdGVkJTIwQmV6aWVyJTIwY29vcmRpbmF0ZXMuJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwcnglMkMlMjByeSUyMCUzRCUyMHclMjAlMkYlMjAyLjAlMkMlMjBoJTIwJTJGJTIwMi4wJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwcHgwJTIwJTNEJTIwY3glMjAlMkIlMjByeCUyMColMjByeDAlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBweTAlMjAlM0QlMjBjeSUyMCUyQiUyMHJ5JTIwKiUyMHJ5MCUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHB4MSUyMCUzRCUyMGN4JTIwJTJCJTIwcnglMjAqJTIwcngxJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwcHkxJTIwJTNEJTIwY3klMjAlMkIlMjByeSUyMColMjByeTElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBweDIlMjAlM0QlMjBjeCUyMCUyQiUyMHJ4JTIwKiUyMHJ4MiUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHB5MiUyMCUzRCUyMGN5JTIwJTJCJTIwcnklMjAqJTIwcnkyJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwcHgzJTIwJTNEJTIwY3glMjAlMkIlMjByeCUyMColMjByeDMlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBweTMlMjAlM0QlMjBjeSUyMCUyQiUyMHJ5JTIwKiUyMHJ5MyUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGlmJTIwREVCVUclM0ElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBlbGxpcHNlKHB4MyUyQyUyMHB5MyUyQyUyMDMlMkMlMjAzKSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGVsbGlwc2UocHgwJTJDJTIwcHkwJTJDJTIwNSUyQyUyMDUpJTBBJTIwJTIwJTIwJTIwJTIzJTIwRHJhd2luZyUwQSUyMCUyMCUyMCUyMGlmJTIwbW9kZSUyMCUzRCUzRCUyMDAlM0ElMjAlMjAlMjMlMjAnbm9ybWFsJyUyMGFyYyUyMChub3QlMjAnbWlkZGxlJyUyMG5vciUyMCduYWtlZCcpJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwYmVnaW5fc2hhcGUoKSUwQSUyMCUyMCUyMCUyMGlmJTIwbW9kZSUyMCElM0QlMjAxJTNBJTIwJTIwJTIzJTIwaWYlMjBub3QlMjAnbWlkZGxlJyUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHZlcnRleChweDMlMkMlMjBweTMpJTBBJTIwJTIwJTIwJTIwaWYlMjBhYnModGhldGEpJTIwJTNDJTIwSEFMRl9QSSUzQSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGJlemllcl92ZXJ0ZXgocHgyJTJDJTIwcHkyJTJDJTIwcHgxJTJDJTIwcHkxJTJDJTIwcHgwJTJDJTIwcHkwKSUwQSUyMCUyMCUyMCUyMGVsc2UlM0ElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjMlMjB0byUyMGF2b2lkJTIwZGlzdG9ydGlvbiUyQyUyMGJyZWFrJTIwaW50byUyMDIlMjBzbWFsbGVyJTIwYXJjcyUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGJfYXJjKGN4JTJDJTIwY3klMkMlMjB3JTJDJTIwaCUyQyUyMHN0YXJ0X2FuZ2xlJTJDJTIwZW5kX2FuZ2xlJTIwLSUyMHRoZXRhJTIwJTJGJTIwMi4wJTJDJTIwbW9kZSUzRDEpJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwYl9hcmMoY3glMkMlMjBjeSUyQyUyMHclMkMlMjBoJTJDJTIwc3RhcnRfYW5nbGUlMjAlMkIlMjB0aGV0YSUyMCUyRiUyMDIuMCUyQyUyMGVuZF9hbmdsZSUyQyUyMG1vZGUlM0QxKSUwQSUyMCUyMCUyMCUyMGlmJTIwbW9kZSUyMCUzRCUzRCUyMDAlM0ElMjAlMjAlMjMlMjBlbmQlMjBvZiUyMGElMjAnbm9ybWFsJyUyMGFyYyUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGVuZF9zaGFwZSgpJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTBBJTBB)

- [`b_arc`](/villares_bezier_arc_aproximation/villares_bezier_arc_aproximation.pyde) the legacy Processing Python mode version, works on unmodified **pyp5js**

- [`b_arc`](/villares_bezier_arc_aproximation_java/villares_bezier_arc_aproximation_java.pde) for **Processing Java** 

- [`b_arc`](/villares_bezier_arc_aproximation_p5js/villares_bezier_arc_aproximation_p5js.js) for **p5.js**
  
  > ![b_arc](https://raw.githubusercontent.com/villares/arc_tangents_and_bezier_studies/main/villares_bezier_arc_aproximation/b_arc.png)
  > 
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

### More arcs, the `p_arc` function, and the first shapes with tangents

Other functions based on `b_arc`, and a polygonal approximation called `p_arc` can be found on [`arcs.py`](https://raw.githubusercontent.com/villares/villares/refs/heads/main/arcs.py)) and  [`arc_helpers.py`](https://raw.githubusercontent.com/villares/villares/refs/heads/main/arc_helpers.py):

- The `var_bar` and `bar` functions draw "two connected circles". They can be used with `p_arc`(a polygonal approximation of an arc) instead of the default `b_arc`. 

- The `var_bar_pts` function, based on `arc_pts`, returns the points that `var_bar` would draw with the same arguments (except the `internal` feature). 

- The `arc_pts` function returns a list of points (as tuples), that `p_arc` would draw, but does not draw them. `p_arc` now uses `arc_pts` internally.
  
  > ![](https://raw.githubusercontent.com/villares/arc_tangents_and_bezier_studies/main/villares_arcs_and_bars/villares_arcs_and_bars2.gif)
  > 
  > ```python
  > …
  > # default var_bar & bar with b_arc
  > var_bar(50, 165, 350, 315, 40, 0) # by default arc_func=b_arc
  > bar(50, 55, 350, 255, thickness=60, shorter=mouseX)
  > var_bar(50, 255, 50 + mouseX * 0.6, 255 + mouseX * 0.25, 20, 40)
  > … 
  > # var_bar & bar with p_arc
  > var_bar(50, 165, 350, 315, 40, 0, arc_func=p_arc, num_points=6)
  > bar(50, 55, 350, 255, thickness=60,
  >     shorter=mouseX, arc_func=p_arc, num_points=3)
  > var_bar(50, 255,
  >         50 + mouseX * 0.6, 255 + mouseX * 0.25, 20, 40,
  >         arc_func=p_arc, num_points=8)
  > … 
  > # var_bar_pts
  > pts1 = var_bar_pts(50, 165, 350, 315, 40, 0, num_points=6)
  > pts2 = var_bar_pts(50, 55, 350, 255, 30, 30,
  >                    shorter=mouseX, num_points=3)
  > pts3 = var_bar_pts(50, 255,
  >                    50 + mouseX * 0.6, 255 + mouseX * 0.25, 20, 40,
  >                    num_points=8)
  > strokeWeight(5)
  > for px, py in pts1 + pts2 + pts3:
  >     point(px, py)
  > …
  > ```
  > 
  > The full legacy code of the Processing Python mode example above is at [villares_arcs_and_bars](villares_arcs_and_bars).

- A similar, simpler, interactive `var_bar_pts` example using [py5](https://py5coding.org) *imported mode* can be found at [var_bar_pts_py5_example](var_bar_pts_py5_example), and [you can run it on the browser here](https://abav.lugaralgum.com/pyp5js/py5mode/?sketch=ZGVmJTIwc2V0dXAoKSUzQSUwQSUyMCUyMCUyMCUyMHNpemUoNjAwJTJDJTIwNjAwKSUwQSUyMCUyMCUyMCUyMCUwQWRlZiUyMGRyYXcoKSUzQSUwQSUyMCUyMCUyMCUyMGJhY2tncm91bmQoMTAwJTJDJTIwMTUwJTJDJTIwMTAwKSUwQSUyMCUyMCUyMCUyMHB0cyUyMCUzRCUyMHZhcl9iYXJfcHRzKG1vdXNlX3glMkMlMjBtb3VzZV95JTJDJTIwMjAwJTJDJTIwMzAwJTJDJTIwNDAlMkMlMjAxMDAlMkMlMjBudW1fcG9pbnRzJTNEMTYpJTBBJTIwJTIwJTIwJTIwc3Ryb2tlX3dlaWdodCgxKSUwQSUyMCUyMCUyMCUyMHdpdGglMjBiZWdpbl9jbG9zZWRfc2hhcGUoKSUzQSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHZlcnRpY2VzKHB0cyklMEElMjAlMjAlMjAlMjBzdHJva2Vfd2VpZ2h0KDUpJTBBJTIwJTIwJTIwJTIwcG9pbnRzKHB0cyklMEElMEFkZWYlMjBhcmNfcHRzKGN4JTJDJTIwY3klMkMlMjB3JTJDJTIwaCUyQyUyMHN0YXJ0X2FuZ2xlJTJDJTIwZW5kX2FuZ2xlJTJDJTIwbnVtX3BvaW50cyUzRDI0KSUzQSUwQSUyMCUyMCUyMCUyMCUyMiUyMiUyMiUwQSUyMCUyMCUyMCUyMFJldHVybnMlMjBwb2ludHMlMjBhcHByb3hpbWF0aW5nJTIwYW4lMjBhcmMlMjB1c2luZyUyMHRoZSUyMHNhbWUlMEElMjAlMjAlMjAlMjBzaWduYXR1cmUlMjBhcyUyMHRoZSUyMG9yaWdpbmFsJTIwUHJvY2Vzc2luZyUyMGFyYygpLiUwQSUyMCUyMCUyMCUyMCUyMiUyMiUyMiUwQSUyMCUyMCUyMCUyMHN3ZWVwX2FuZ2xlJTIwJTNEJTIwZW5kX2FuZ2xlJTIwLSUyMHN0YXJ0X2FuZ2xlJTBBJTIwJTIwJTIwJTIwaWYlMjBhYnMoc3dlZXBfYW5nbGUpJTIwJTNDJTIwMC4wMDAxJTNBJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwdnglMjAlM0QlMjBjeCUyMCUyQiUyMGNvcyhzdGFydF9hbmdsZSklMjAqJTIwdyUyMCUyRiUyMDIuMCUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHZ5JTIwJTNEJTIwY3klMjAlMkIlMjBzaW4oc3RhcnRfYW5nbGUpJTIwKiUyMGglMjAlMkYlMjAyLjAlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjByZXR1cm4lMjAlNUIodnglMkMlMjB2eSklNUQlMEElMjAlMjAlMjAlMjBwdHNfbGlzdCUyMCUzRCUyMCU1QiU1RCUwQSUyMCUyMCUyMCUyMHN0ZXBfYW5nbGUlMjAlM0QlMjBmbG9hdChzd2VlcF9hbmdsZSklMjAlMkYlMjBudW1fcG9pbnRzJTIwJTIwJTIwJTIwJTBBJTIwJTIwJTIwJTIwdmElMjAlM0QlMjBzdGFydF9hbmdsZSUwQSUyMCUyMCUyMCUyMHNpZGUlMjAlM0QlMjAxJTIwaWYlMjBzd2VlcF9hbmdsZSUyMCUzRSUyMDAlMjBlbHNlJTIwLTElMEElMjAlMjAlMjAlMjB3aGlsZSUyMHZhJTIwKiUyMHNpZGUlMjAlM0MlMjBlbmRfYW5nbGUlMjAqJTIwc2lkZSUyMG9yJTIwYWJzKHZhJTIwLSUyMGVuZF9hbmdsZSklMjAlM0MlMjAwLjAwMDElM0ElMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjB2eCUyMCUzRCUyMGN4JTIwJTJCJTIwY29zKHZhKSUyMColMjB3JTIwJTJGJTIwMi4wJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwdnklMjAlM0QlMjBjeSUyMCUyQiUyMHNpbih2YSklMjAqJTIwaCUyMCUyRiUyMDIuMCUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHB0c19saXN0LmFwcGVuZCgodnglMkMlMjB2eSkpJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwdmElMjAlMkIlM0QlMjBzdGVwX2FuZ2xlJTBBJTIwJTIwJTIwJTIwcmV0dXJuJTIwcHRzX2xpc3QlMEElMEFkZWYlMjB2YXJfYmFyX3B0cyhwMXglMkMlMjBwMXklMkMlMjBwMnglMkMlMjBwMnklMkMlMjByMSUyQyUyMHIyJTNETm9uZSUyQyUyMCoqa3dhcmdzKSUzQSUwQSUyMCUyMCUyMCUyMCUyMiUyMiUyMiUwQSUyMCUyMCUyMCUyMFRhbmdlbnQlMkZ0YW5nZW50JTIwc2hhcGUlMjBvbiUyMDIlMjBjaXJjbGVzJTIwb2YlMjBhcmJpdHJhcnklMjByYWRpdXMlMEElMjAlMjAlMjAlMjAlMjIlMjIlMjIlMEElMjAlMjAlMjAlMjByMiUyMCUzRCUyMHIyJTIwaWYlMjByMiUyMGlzJTIwbm90JTIwTm9uZSUyMGVsc2UlMjByMSUwQSUyMCUyMCUyMCUyMHNob3J0ZXIlMjAlM0QlMjBrd2FyZ3MucG9wKCdzaG9ydGVyJyUyQyUyMDApJTBBJTIwJTIwJTIwJTIwYXNzZXJ0JTIwbm90JTIwKHNob3J0ZXIlMjBhbmQlMjByMSUyMCElM0QlMjByMiklMkMlNUMlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjJDYW4ndCUyMGRyYXclMjBzaG9ydGVyJTIwdmFyX2JhciUyMHdpdGglMjBkaWZmZXJlbnQlMjByYWRpaSUyMiUwQSUyMCUyMCUyMCUyMGQlMjAlM0QlMjBkaXN0KHAxeCUyQyUyMHAxeSUyQyUyMHAyeCUyQyUyMHAyeSklMEElMjAlMjAlMjAlMjByaSUyMCUzRCUyMHIxJTIwLSUyMHIyJTBBJTIwJTIwJTIwJTIwcmVzdWx0JTIwJTNEJTIwJTVCJTVEJTBBJTIwJTIwJTIwJTIwaWYlMjBkJTIwJTNFJTIwYWJzKHJpKSUzQSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGNsaXBwZWRfcmlfb3Zlcl9kJTIwJTNEJTIwbWluKDElMkMlMjBtYXgoLTElMkMlMjByaSUyMCUyRiUyMGQpKSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGJldGElMjAlM0QlMjBhc2luKGNsaXBwZWRfcmlfb3Zlcl9kKSUyMCUyQiUyMEhBTEZfUEklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBhbmdsZSUyMCUzRCUyMGF0YW4yKHAxeCUyMC0lMjBwMnglMkMlMjBwMnklMjAtJTIwcDF5KSUyMCUyQiUyMEhBTEZfUEklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBvZmZzZXQlMjAlM0QlMjBzaG9ydGVyJTIwJTJGJTIwMi4wJTIwaWYlMjBzaG9ydGVyJTIwJTNDJTIwZCUyMGVsc2UlMjBkJTIwJTJGJTIwMi4wJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwcmVzdWx0LmV4dGVuZChhcmNfcHRzKG9mZnNldCUyQyUyMDAlMkMlMjByMSUyMColMjAyJTJDJTIwcjElMjAqJTIwMiUyQyUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMC1iZXRhJTIwLSUyMFBJJTJDJTIwYmV0YSUyMC0lMjBQSSUyQyUyMCoqa3dhcmdzKSklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjByZXN1bHQuZXh0ZW5kKGFyY19wdHMoZCUyMC0lMjBvZmZzZXQlMkMlMjAwJTJDJTIwcjIlMjAqJTIwMiUyQyUyMHIyJTIwKiUyMDIlMkMlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBiZXRhJTIwLSUyMFBJJTJDJTIwUEklMjAtJTIwYmV0YSUyQyUyMCoqa3dhcmdzKSklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjByZXR1cm4lMjByb3RhdGVfb2Zmc2V0X3BvaW50cyhyZXN1bHQlMkMlMjBhbmdsZSUyQyUyMHAxeCUyQyUyMHAxeSklMEElMjAlMjAlMjAlMjBlbHNlJTNBJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwciUyMCUzRCUyMG1heChyMSUyQyUyMHIyKSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMHglMkMlMjB5JTIwJTNEJTIwKHAxeCUyQyUyMHAxeSklMjBpZiUyMHIxJTIwJTNFJTIwcjIlMjBlbHNlJTIwKHAyeCUyQyUyMHAyeSklMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjByZXR1cm4lMjBhcmNfcHRzKHglMkMlMjB5JTJDJTIwciUyMColMjAyJTJDJTIwciUyMColMjAyJTJDJTIwMCUyQyUyMFRXT19QSSUyQyUyMCoqa3dhcmdzKSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUwQWRlZiUyMHJvdGF0ZV9vZmZzZXRfcG9pbnRzKHB0cyUyQyUyMGFuZ2xlJTJDJTIwb2ZmeCUyQyUyMG9mZnklMkMlMjB5MCUzRDAlMkMlMjB4MCUzRDApJTNBJTBBJTIwJTIwJTIwJTIwcmV0dXJuJTIwJTVCKCgoeHAlMjAtJTIweDApJTIwKiUyMGNvcyhhbmdsZSklMjAtJTIwKHlwJTIwLSUyMHkwKSUyMColMjBzaW4oYW5nbGUpKSUyMCUyQiUyMHgwJTIwJTJCJTIwb2ZmeCUyQyUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCgoeXAlMjAtJTIweTApJTIwKiUyMGNvcyhhbmdsZSklMjAlMkIlMjAoeHAlMjAtJTIweDApJTIwKiUyMHNpbihhbmdsZSkpJTIwJTJCJTIweTAlMjAlMkIlMjBvZmZ5KSUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGZvciUyMHhwJTJDJTIweXAlMjBpbiUyMHB0cyU1RCUwQSUyMCUyMCUyMCUyMA%3D%3D) using [pyp5js/py5mode](https://abav.lugaralgum.com/pyp5js/py5mode/)!

### Filleted polygons and nice shapes that can wrap circles

Perhaps the bigest motivation for starting the studies in this repository, next, we have some functions that povide continous poly-based shapes with tangent arcs. 

- Rounding polygons "in", filleted polygons `arc_filleted_poly`, takes a sequence of points and radii and uses the `arc_corner`function to draw. Notice it may need to make a radius smaller to fit sometimes. A recently added `radius` keyword can be supplied instead of the radius values list.
  
  > ![](https://raw.githubusercontent.com/villares/arc_tangents_and_bezier_studies/main/villares_filleted_and_arc_augmented_polys/arc_filleted_poly.png)
  > 
  > ```python
  > p_list = [(30, 160), (250, 50), (350, 150), (200, 100)]
  > r_list = [20, 30, 40, 30]
  > …
  > arc_filleted_poly(p_list,r_list)  # arc_func=b_arc by default
  > ```
  > 
  > ![](villares_filleted_and_arc_augmented_polys/arc_filleted_poly.gif)
  > 
  > ```python
  > p_list = [(30, 160), (250, 50), (350, 150), (mouseX, mouseY)]
  > r_list = [20, 30, 40, 30]
  > …
  > arc_filleted_poly(p_list,r_list)  # arc_func=b_arc by default
  > ```

- Rounding polygons "outside" with `arc_augmented_poly`, takes a sequence of points and radii and calculates geometry with the `circ_circ_tangent` function. If two points are too close it will reduce the radii.
  
  > ![](https://raw.githubusercontent.com/villares/arc_tangents_and_bezier_studies/main/villares_filleted_and_arc_augmented_polys/arc_augmented_poly.png)
  > 
  > ```python
  > p_list = [(30, 160), (250, 50), (350, 150), (200, 100)]
  > r_list = [20, 30, 40, 30]
  > …
  > arc_augmented_poly(p_list,r_list)  # arc_func=b_arc by default
  > ```
  > 
  > ![](https://raw.githubusercontent.com/villares/arc_tangents_and_bezier_studies/main/villares_filleted_and_arc_augmented_polys/arc_augmented_poly.gif)
  > 
  > ```python
  > p_list = [(30, 160), (250, 50), (350, 150), (mouseX, mouseY)]
  > r_list = [20, 30, 40, 30]
  > …
  > arc_augmented_poly(p_list,r_list)  # arc_func=b_arc by default
  > ```
  
  - `TO DO:` I should document an "ugly" feature of `arc_augmented_poly` that checks for self intersections calculating a polygonal approximation, without drawing the shapes.
  
  ### A few other silly arc helpers

- The `circle_arc` function tries to create a simpler interface for Processing's `arc`, asking for *x*, *y*, *radius*, *start_angle*, and *sweep* (*radius* instead of *width*, *height* and *sweep* instead of *end_angle*). It also allows drawing with `b_arc` or `p_arc`.

- The `half_circle` and `quarter_circle` are similar, very silly `arc` (or `b_arc`/`p_arc`) wrappers using a mix of Processing constants to define rotation.
  
  > ![circle_arc](https://raw.githubusercontent.com/villares/arc_tangents_and_bezier_studies/main/villares_bezier_arc_aproximation/circle_arc.png)
  > 
  > ```python
  > x, y, radius, start_angle, sweep = 75, 105, 50, 0, PI + QUARTER_PI
  > circle_arc(x, y, radius, start_angle, sweep)    # default 'arc' wrapper mode
  > circle_arc(x, y, radius, -QUARTER_PI / 2, -HALF_PI, arc_func=p_arc, num_points=4)
  > 
  > x, y1, y2 = 190, 95, 105
  > half_circle(x, y1, radius, TOP, CHORD)  # default 'arc' wrapper mode
  > half_circle(x, y2, radius, BOTTOM, arc_func=b_arc)
  > 
  > x1, x2, y1, y2 = 300, 310, 95, 105
  > quarter_circle(x1, y1, radius, TOP + LEFT, CHORD)  # default 'arc' wrapper mode
  > quarter_circle(x1, y2, radius, BOTTOM + LEFT, PIE)
  > quarter_circle(x2, y1, radius, TOP + RIGHT)
  > quarter_circle(x2, y2, radius, BOTTOM + RIGHT, arc_func=b_arc)
  > ```

- `circle_arc_pts` will return a list of points like the ones `p_arc` would draw.

----

This page lives at [this repository](https://github.com/villares/arc_tangents_and_bezier_studies/), please open an [issue](https://github.com/villares/arc_tangents_and_bezier_studies/issues) if you have a question. Consider supporting my work with a small donation! [More links about me here](https://abav.lugaralgum.com/links).
