import sys

from lib.db import Db
from lib.settings import SNAP_DISTANCE

db=Db()

geometry="POLYGON((0.00001 0.00001, 100.00001 0.00001, 100.00001 100.00001, 0.00001 100.00001, 0.00001 0.00001))"

#check if the geometry is valid after having simplified it
query=""" 
    select ST_isvalid(
        st_snaptogrid(
            st_geomfromtext(%s, 25830),
            %s
        )
    ) as is_valid
"""
db.query(query, [geometry, SNAP_DISTANCE])

if db.result[0][0]:
    print("The geometry is valid")
else:
    print("The geometry is not valid")
    sys.exit()

#check if the geometry intersects any existing building
query=""" 
    select id from d.buildings where ST_intersects(
        geom,
        st_snaptogrid(
            st_geomfromtext(%s, 25830),
            %s
        )
    )
"""

db.query(query, [geometry, SNAP_DISTANCE])
if len(db.result) > 0:
    print("There are buildigs that intersect with the new geometry: {0}".format(db.result))
    sys.exit()
else:
    print("The new geometry does not intersect any existing building")

#now we now that the geometry is valid and does not intersect any existing building
#we can insert the new building
query="insert into d.buildings (description, geom) values (%s,st_snaptogrid(st_geometryfromtext(%s,25830),%s)) returning id"
db.query(query, ["new building", geometry, SNAP_DISTANCE])

#Let's see if the original coordinates have been modified
query="select id, st_astext(geom) from d.buildings where id=%s"
values=[db.result[0][0]]
print("Original coordinates: {0}".format(geometry))
print("Note the coordinates have been modified to snap to the grid. They have been rounded")
db.query(query, values)





