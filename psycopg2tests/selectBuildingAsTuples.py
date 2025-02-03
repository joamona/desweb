from lib.db import Db
db=Db()
query="select id, description, st_astext(geom) from d.buildings where id=%s"
values=[6]
db.query(query, values)
