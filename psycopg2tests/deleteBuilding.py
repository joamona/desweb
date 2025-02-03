from lib.db import Db
db=Db()
query="delete from d.buildings where id=%s"
values=[29]
db.query(query, values)
