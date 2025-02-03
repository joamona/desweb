from lib.db import Db
db=Db()
query="select array_to_json(array_agg(filas)) FROM (select id, description, st_astext(geom) from d.buildings where id=%s) as filas"
values=[6]
db.query(query, values)
