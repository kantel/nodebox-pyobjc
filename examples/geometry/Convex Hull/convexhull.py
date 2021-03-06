"""The convex hull algorith as presented by 
   https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain

   This algorithm is faster than it might appear. It calculates the convex hull for a million
   points in less than 10s on a 2 GHz machine.
   
   Displaying a million points takes about 4-8 minutes
"""

# This is new with Nodebox 1.9.13; size(0,0) sets size to main screen size
try:
    size(0, 0)
except:
    # if we're running an older version, set some reasonable default
    size(800, 800)

import time

# how many points 1,000,000 takes about 5 min.
noOfPoints = 10000

# inset from canvas size
inset = 20


def convex_hull(points):
    """Computes the convex hull of a set of 2D points.

    Input: an iterable sequence of (x, y) pairs representing the points.
    Output: a list of vertices of the convex hull in counter-clockwise order,
      starting from the vertex with the lexicographically smallest coordinates.
    Implements Andrew's monotone chain algorithm. O(n log n) complexity.
    
    https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain
    """

    # Sort the points lexicographically (tuples are compared lexicographically).
    # Remove duplicates to detect the case we have just one unique point.
    points = sorted(set(points))

    # Boring case: no points or a single point, possibly repeated multiple times.
    if len(points) <= 1:
        return points

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull 
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list. 
    return lower[:-1] + upper[:-1]


# Example: convex hull of a 10-by-10 grid.
# assert convex_hull([(i//10, i%10) for i in range(100)]) == [(0, 0), (9, 0), (9, 9), (0, 9)]

def mark( point, style="CROSS" ):
    """Mark a point with a cross or a rect."""
    push()
    
    fill( 0 )
    strokewidth( 1 )
    stroke( 0.5, 0,0, 0.5 )
    if style == "CROSS":
        beginpath()
        moveto( point[0]-2, point[1] )
        lineto( point[0]+2, point[1] )
        moveto( point[0]  , point[1]-2 )
        lineto( point[0]  , point[1]+2 )
        endpath(draw=1)
    else:
        rect(point[0],point[1], 1, 1)
    pop()

def createRandomPoints( count, width, height, inset):
    # create the random points
    points = []
    midx = (width - inset ) / 2.0
    midy = (height - inset) / 2.0
    # fill(0.5)
    strokewidth(1)
    stroke(0)
    for i in xrange( count ):
        px = inset + random() * (width - inset * 2)
        py = inset + random() * (height - inset * 2)
        points.append( (px,py) )
        mark( (px,py), style="CROSS" )
        # line(px-0.5,py,px+0.5,py)
        # rect(px-0.5,py-0.5,1.0,1.0)
    return points


def displayHullPoints( outline ):
    # display result (clumsy it is...)
    push()
    beginpath()
    nofill()
    beginpath()
    moveto( outline[0][0], outline[0][1] )
    strokewidth( 1 )
    stroke( 1,0,0,0.5 )
    oval( outline[0][0]-4, outline[0][1]-4, 8, 8, True)
    for p in outline[1:-1]:
        strokewidth( 1 )
        stroke( 0,0,1,0.5 )
        lineto( p[0], p[1] )
        strokewidth( 1 )
        stroke( 1,0,0,0.5 )
        oval( p[0]-4, p[1]-4, 8, 8, True)
    strokewidth( 1 )
    stroke( 0,0,1,0.5 )
    lineto( outline[-1][0], outline[-1][1] )
    strokewidth( 1 )
    stroke( 1,0,0,0.5 )
    oval( outline[-1][0]-4, outline[-1][1]-4, 8, 8, True)
    endpath(draw=1)
    pop()

t_start = time.time()

# create & display points
points = createRandomPoints( noOfPoints, WIDTH, HEIGHT, inset)
t_points = time.time()

# calculate the hull points
outline = convex_hull(points)

noofhullpoints = len(outline)

t_hull = time.time()

# display the hull
displayHullPoints( outline )

t_display = time.time()

print
print "#Total points:", len(points)
print "#Hull points:", len(outline)

print "Time creating and displaying points: %.3f sek." % (round(t_points - t_start, 3), )
print "Time calculating hull: %.3f sek." % (round(t_hull - t_points, 3), )
print "Time displaying hull: %.3f sek." % (round(t_display - t_hull, 3), )
