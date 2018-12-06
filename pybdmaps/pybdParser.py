# -*- coding: utf-8 -*-
"""
Created on Tue Dec 04 13:40:58 2018

@author: sonerk
"""

import re

PARSER = re.compile(r'[,;| ]')

def input_Sample(mode):

	if mode == 'st' :
		
		print('Enter the input as format of Latitude, Longtitude . . .')
		print('For string format : . . . . . . ')
		print('"Latitude, Longtitude", \n  Example : "45.4545, 123.1233"')
		print('For list format : . . . . . . ')
		print(' [Latitude, Longtitude] \n Example : [45.4545, 123.1233]')
		return 0
	
	
	elif mode == 'brd':
		
		return 0

#'brd' is border mode that means, user must give 4 points to determine rectanguler form
# st is radiun mode that means, use must give 2 points tı determine circular form
def location_Parser(location, mode = 'st'):

    
    if mode == 'st' : 
    
        type_Loc = type(location)
        
        if type_Loc == str:
        
            if len(PARSER.split(location)) != 2:
            
                raise Exception('Please Enter With [, ; | (space)] and There must be as least X, Y cordinates . . .')
                return -1
        
            else:
			
                lat , lng = PARSER.split(location)
                return lat, lng
        
        elif type_Loc == list:
        
            if len(location) != 2:
            
                raise Exception('Please Enter With [, ; | (space)] and There must be as least X, Y cordinates . . .')
                return -1
        
            else:
            
                lat, lng = location            
                return lat, lng
        
    elif mode == 'brd':
        
        if type_Loc == str:
            
            if len(PARSER.split(location)) != 4:
            
                raise Exception('Please Enter With [, ; | (space)] and There must be as least X1, Y1, X2, Y2 cordinates . . .')
                return -1
        
            else:
			
                lat , lng = PARSER.split(location)
                return lat1, lng1, lat2, lng2
        
        elif type_Loc == list:
        
            if len(location) != 4:
            
                raise Exception('Please Enter With [, ; | (space)] and There must be as least X1, Y1, X2, Y2 cordinates . . .')
                return -1
        
            else:
            
                lat1, lng1, lat2, lng2 = location            
                return lat1, lng1, lat2, lng2

	