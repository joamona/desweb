from lib.db import Db

db=Db()
query="update d.buildings set (description, geom) = row(%s,st_geometryfromtext(%s,25830)) where id=%s"

values=["Edificio actualizado", 
        "POLYGON((727988 4373188, 728054 4373192, 728095.84297791088465601 4373142.83781164418905973, 728051 4373093, 727983 4373093, 727988 4373188))",
        5
        ]

db.query(query, values)
