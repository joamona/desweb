import sys

from lib.db import Db
from lib.settings import SNAP_DISTANCE

db=Db()

geometry="POLYGON((0.00001 0.00001, 100.00001 0.00001, 100.00001 200.1238567, 0.00001 100.00001, 0.00001 0.00001))"
id=30  #the id of the building we want to update

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

#check if the geometry intersects any existing building, except the one we are updating
query=""" 
    select id from d.buildings where ST_intersects(
        geom,
        st_snaptogrid(
            st_geomfromtext(%s, 25830),
            %s
        )
    ) and id != %s
"""

db.query(query, [geometry, SNAP_DISTANCE, id])
if len(db.result) > 0:
    print("There are buildigs that intersect with the new geometry: {0}".format(db.result))
    sys.exit()
else:
    print("The new geometry does not intersect any existing building except the one we are updating")

#now we now that the geometry is valid and does not intersect any existing building
#we can insert the new building
query="update d.buildings set (description, geom) = row(%s,st_snaptogrid(st_geometryfromtext(%s,25830),%s)) where id=%s"
db.query(query, ["Building updated", geometry, SNAP_DISTANCE, id])

#Let's see if the description and coordinates have been modified
query="select id, description, st_astext(geom) from d.buildings where id=%s"
db.query(query, [id])



