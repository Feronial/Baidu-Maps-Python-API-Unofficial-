# -*- coding: utf-8 -*-
"""
Created on Tue Dec 04 13:40:58 2018

@author: sonerk
"""

import re

PARSER = re.compile(r'[,;| ]')


#'brd' is border mode that means, user must give 4 points to determine rectanguler form
# st is radiun mode that means, use must give 2 points tı determine circular form
def location_Parser(location, mode = 'st'):
    
    if mode == 'st' : 
    
        type_Loc = type(location)
    
        if type_Loc == str:
        
            if len(PARSER.split(location)) < 2:
            
                raise Exception('Please Enter With [, ; | (space)] and There must be as least X, Y cordinates . . .')
                return -1
        
        
        
        elif type_Loc == list:
        
            if len(location) < 2:
            
                raise Exception('Please Enter With [, ; | (space)] and There must be as least X, Y cordinates . . .')
                return -1
        
            else:
            
                lat, lng = location
            
                return lat, lng
        
    elif mode = 'brd':
        
        
    
    
    
    
    