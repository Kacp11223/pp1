x = int(input("x: "))
y = int(input("y: "))
if x*y > 0 and x > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
if x*y > 0 and x < 0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
if x*y < 0 and x > 0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
if x*y < 0 and x < 0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
if x*y==0 and x+y==0:
    print(f"Point P({x},{y}) is in the center of the coordinate system")
