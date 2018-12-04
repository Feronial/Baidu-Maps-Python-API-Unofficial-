# -*- coding: utf-8 -*-
"""
Created on Tue Dec 04 13:40:58 2018

@author: sonerk
"""

def location_to_location(loc1, loc2):
    EARTH_DIST = 6378.137
    
    loc1_x, loc1_y = loc1.split(',')
    loc2_x, loc2_y = loc2.split(',')
    
    loc1_x = float(loc1_x)
    loc1_y = float(loc1_y)
    loc2_x = float(loc2_x)
    loc2_y = float(loc2_y)
    
    dist_x = (loc2_x * math.pi / 180) - (loc1_x * math.pi / 180)
    dist_y = (loc2_y * math.pi / 180) - (loc1_y * math.pi / 180)
    
    temp = ( math.sin(dist_x / 2)* math.sin(dist_x / 2) ) + ( math.cos(loc1_x * math.pi / 180) * math.cos(loc2_x * math.pi / 180 )) * math.sin(dist_y /2) * math.sin(dist_y / 2)
    
    c = 2 * math.atan2(math.sqrt(temp), math.sqrt(1 - temp))
    meter_Distance = EARTH_DIST * c       
            
    
    return meter_Distance * 1000