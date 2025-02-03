from lib.db import Db

db=Db()
query="insert into d.buildings (description, geom) values (%s,st_geometryfromtext(%s,25830)) returning id"

values1=["edificio 1", "POLYGON((727844 4373183,727896 4373187,727893 4373028,727873 4373018,727858 4372987,727796 4372988,727782 4373008,727844 4373183, 727844 4373183))"]
values2=["edificio 2", "POLYGON((727988 4373188,728054 4373192,728051 4373093,727983 4373093,727988 4373188))"]

db.query(query, values1)
db.query(query, values2)




