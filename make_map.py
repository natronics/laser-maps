#!/usr/bin/env python
import shapefile
import svgwrite

sf = shapefile.Reader("examples/shapefiles/tl_2009_41_state/tl_2009_41_state")

# calculate width and height
bbox = sf.shapes()[0].bbox
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]


# point list
points = []
for i, p in enumerate(sf.shapes()[0].points):
    if i % 5 == 0:
        points.append((p[0]*100, p[1]*100))

print "Drawing ", len(points), "points"

# make drawing
dwg = svgwrite.Drawing('test.svg', size=(w*100, h*100))
state = dwg.add(dwg.g(id="or", transform="translate("+str(bbox[0]*-100)+","+str(bbox[3]*100)+") scale(1,-1)"))
state.add(dwg.polyline(points, stroke='blue', fill='none'))
dwg.save()
