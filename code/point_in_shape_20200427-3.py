#!/usr/bin/env python
# coding: utf-8

# In[77]:


import fiona
import shapely
import pandas as pd
import numpy as np
from shapely.geometry import shape,mapping, Point, Polygon, MultiPolygon


# In[58]:


# multipol = fiona.open("multipol.shp")
# multi= multipol.next() # only one feature in the shapefile
# print(multi)
# {'geometry': {'type': 'MultiPolygon', 'coordinates': [[[(-0.5275288092189501, 0.5569782330345711), (-0.11779769526248396, 0.29065300896286816), (-0.25608194622279135, 0.01920614596670933), (-0.709346991037132, -0.08834827144686286), (-0.8629961587708066, 0.18309859154929575), (-0.734955185659411, 0.39820742637644047), (-0.5275288092189501, 0.5569782330345711)]], [[(0.19974391805377723, 0.060179257362355965), (0.5480153649167734, 0.1293213828425096), (0.729833546734955, 0.03969270166453265), (0.8143405889884763, -0.13956466069142115), (0.701664532650448, -0.38540332906530095), (0.4763124199743918, -0.5006402048655569), (0.26888604353393086, -0.4238156209987196), (0.18950064020486557, -0.2291933418693981), (0.19974391805377723, 0.060179257362355965)]], [[(-0.3764404609475033, -0.295774647887324), (-0.11523687580025621, -0.3597951344430217), (-0.033290653008962945, -0.5800256081946222), (-0.11523687580025621, -0.7413572343149808), (-0.3072983354673495, -0.8591549295774648), (-0.58898847631242, -0.6927016645326505), (-0.6555697823303457, -0.4750320102432779), (-0.3764404609475033, -0.295774647887324)]]]}, 'type': 'Feature', 'id': '0', 'properties': OrderedDict([(u'id', 1)])}


# In[138]:


# shape = fiona.open("/Users/j5/Downloads/westside-la-county-region-current/l.a. county region (current).shp")
shape = fiona.open("/Users/j5/Downloads/south-bay-la-county-region-current/l.a. county region (current).shp")


# print(shape.schema)
first = shape.next()
#print(first)
# print(first['geometry'])
# point = shapely.geometry.Point(lat,lng)
point = shapely.geometry.Point(34.010750, -118.484759)
print(point)
print(first['geometry'])

print(shape)


# In[67]:


# first['geometry']
# point['geometry']
# point.within(first['geometry'])

shape = shapely.geometry.asShape(first['geometry'])
# point = shapely.geometry.Point(34.010750, -118.484759)
# point = shapely.geometry.Point(-118.484759,34.010750)
# point = shapely.geometry.Point(-118.1270,34.0953)
# point = shapely.geometry.Point(-118.4543,34.0434)

# point = shapely.geometry.Point(-118.435371,34.015121)
point = shapely.geometry.Point(-118.165239,34.155432)

# shape.intersects(point)
print(point.within(shape))


# In[44]:


import fiona
import shapely.geometry 

with fiona.open(r"D:\Users\Jonathan\Desktop\CRA-Project v2\Census Division\lcd_000b16a_e.shp") as fiona_collection:

shapefile_record = next(iter(fiona_collection))

shape = shapely.geometry.asShape(shapefile_record['geometry'])
#print(shape)

point = shapely.geometry.Point(573339.364,6177352.077)

# if shape.intersects(point):
#     print("Found shape for point.")
point.within(shape)


# In[65]:


column_names = ['neighborhood', 'lat', 'long']
lat_long = pd.read_csv("/Users/j5/Downloads/covid Los Angeles 20200318 - city_lat_long.csv"

                 , skiprows = 1
                 , names = column_names
                )
print(lat_long)
lat_long.dtypes


# In[139]:


dfl = lat_long
dfl["region"] = ""
shape = shapely.geometry.asShape(first['geometry'])

# shape.intersects(point)
# print(point.within(shape))
# for i in df.index:
#     df.at[i, 'ifor'] = x if <something> else y
#     dfl['region'] = np.where(point.within(shape)==True, '1', '0')

for i, row in lat_long.iterrows():
    point = shapely.geometry.Point(row['long'],row['lat'])
    dfl.at[i, 'region'] = 'westside' if point.within(shape) else ''
    

#    print(dfl['region'])
#     df['color'] = np.where(df['Set']=='Z', 'green', 'red')

    print(point.within(shape))
    print(row['neighborhood'])

#     print(point)
#     print(row['lat'], row['long'])


# In[140]:


print(dfl)
    dfl['region'] = np.where(point.within(shape)==True, '1', '0')


# In[89]:


print(dfl.at[3, 'neighborhood'])


# In[141]:


print(dfl,100)
dfl.to_csv('/Users/j5/Downloads/dfl_region.csv')


# In[137]:


b = fiona.open("/Users/j5/Downloads/westside-la-county-region-current/l.a. county region (current).shp")
# print(b.next())
# print(b.next())
print(b['properties'])


# In[130]:


# for feat in fiona.open('/Users/j5/Downloads/westside-la-county-region-current/l.a. county region (current).shp')
#      print feat
fiona.open('/Users/j5/Downloads/westside-la-county-region-current/l.a. county region (current).shp')


# In[ ]:


# for feat in fiona.open("my.shp")
#      print feat


# In[127]:


with fiona.open("/Users/j5/Downloads/westside-la-county-region-current/l.a. county region (current).shp") as src:
    filtered = filter(lambda f: f['properties']['foo']=='bar', src)

print(filtered)


# In[151]:


# shape = fiona.open("/Users/j5/Downloads/westside-la-county-region-current/l.a. county region (current).shp")
# shape = fiona.open("/Users/j5/Downloads/south-bay-la-county-region-current/l.a. county region (current).shp")

b = fiona.open("/Users/j5/Downloads/westside-la-county-region-current/l.a. county region (current).shp", 'r')


# print(shape.schema)
f = b.next()
#print(first)
# print(first['geometry'])
# point = shapely.geometry.Point(lat,lng)
# point = shapely.geometry.Point(34.010750, -118.484759)
# print(point)
# print(f['geometry'])


# print(shape)


Polygons = {}
with fiona.open("/Users/j5/Downloads/westside-la-county-region-current/l.a. county region (current).shp", 'r') as input:
    for f in input:
#         this_shape = Polygon(shape(f['geometry']))
        this_shape = shapely.geometry.asShape(f['geometry'])
#         this_id = f['properties']['id']
        this_id = f['properties']
        Polygons[this_id] = this_shape

return Polygons 


# In[158]:


import logging
import sys

from shapely.geometry import mapping, shape

import fiona

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

with fiona.open('/Users/j5/Downloads/westside-la-county-region-current/l.a. county region (current).shp', 'r') as source:
    
    # **source.meta is a shortcut to get the crs, driver, and schema
    # keyword arguments from the source Collection.
    with fiona.open(
            'with-shapely.shp', 'w',
            **source.meta) as sink:
        
        for f in source:
            
            try:
                geom = shape(f['geometry'])
                if not geom.is_valid:
                    clean = geom.buffer(0.0)
                    assert clean.is_valid
                    assert clean.geom_type == 'Polygon'
                    geom = clean
                f['geometry'] = mapping(geom)
                sink.write(f)
            
            except Exception, e:
                # Writing uncleanable features to a different shapefile
                # is another option.
                logging.exception("Error cleaning feature %s:", f['id'])


# In[160]:


import geopandas as gpd


# In[163]:


df1 = gpd.read_file("/Users/j5/Downloads/westside-la-county-region-current/l.a. county region (current).shp")


# In[183]:


print(df1['name'])


# In[176]:


print(df1['geometry'])
df1.dtypes


# In[208]:


# p1 = shapely.geometry.Point(-118.165239,34.155432)
# p1 = shapely.geometry.Point( -118.3965,34.0211)
poly = df1['geometry']
# p1.within(poly)
poly.contains(p1)
dfl = lat_long
dfl["region"] = ""

for i, row in lat_long.iterrows():
    p1 = shapely.geometry.Point(row['long'],row['lat'])
#     dfl.at[i, 'region'] = 'westside' if poly.contains(p1) == True else ''
#     print(np.where(poly.contains(p1) == True , 'green', 'red'))
    dfl.at[i, 'region'] = np.where(poly.contains(p1) == True , df1['name'], '')
#     print(poly.contains(p1))

print(dfl)
dfl.dtypes
print(df1['name'])




# In[ ]:


dfl = lat_long
dfl["region"] = ""
shape = shapely.geometry.asShape(first['geometry'])


for i, row in lat_long.iterrows():
    point = shapely.geometry.Point(row['long'],row['lat'])
    dfl.at[i, 'region'] = 'westside' if point.within(shape) else ''
    

    print(point.within(shape))
    print(row['neighborhood'])

    


# In[196]:


poly = df1['geometry']
# p1.within(poly)
# print(poly.contains(p1) == True)
poly.contains(p1) == True
print(np.where(poly.contains(p1) == True , 'green', 'red'))


# In[227]:


poly = df1['geometry']
poly.contains(p1)
dfl = lat_long
dfl["region"] = ""

for i, row in lat_long.iterrows():
    if row['region']=="":
        p1 = shapely.geometry.Point(row['long'],row['lat'])
        dfl.at[i, 'region'] = np.where(poly.contains(p1) == True , df1['name'], '')
print(dfl)
dfl.dtypes
print(df1['name'])


# In[214]:


dfl['region'] == ""


# In[222]:


dfl['region'].empty


# In[228]:


df2 = gpd.read_file('/Users/j5/Downloads/la-county-regions-current/l.a. county region (current).shp')


# In[230]:


print(df2['geometry'])


# In[252]:


dfl = lat_long
dfl["region"] = ""
for j, row in df2.iterrows():
#     poly = df2.at[j,'geometry']
#     print(df2.at[j,'name'])
    for i, row in lat_long.iterrows():
        if row['region']=="":
            poly = df2.at[j,'geometry']
            p1 = shapely.geometry.Point(row['long'],row['lat'])
            dfl.at[i, 'region'] = np.where(poly.contains(p1) == True , df2.at[j,'name'], '')
#             print(dfl)
#     print(df2.at[j,'name'])

print(dfl)


# In[253]:


dfl.to_csv('/Users/j5/Downloads/dfl_region_b.csv')


# In[243]:


for j, row in df2.iterrows():
    print(df2.at[j,'name'])
    poly = df2.at[j,'geometry']
    print(poly)


# In[ ]:




