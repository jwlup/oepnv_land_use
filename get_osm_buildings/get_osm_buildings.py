import osmnx as ox

buildings = ox.geometries_from_point((48.14908, 11.58051), dict(building=True))

buildings_loc = buildings.loc[:,buildings.columns.str.contains('addr:|geometry')]

print(buildings_loc)
