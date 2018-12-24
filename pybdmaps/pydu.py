# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:48:40 2018

@author: sonerk
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:23:07 2018

@author: sonerk
"""

import requests

#df_China_Geo = pd.read_excel('Geo_Data.xlsx', sheet_name = 'All_China_Location_NotNull')
#df_China_Geo = df_China_Geo[df_China_Geo['Matched'] == 0]



class BdMap:
    
    def __init__(self,authKey,radius):
        
        self.authKey = authKey
        self.radius = radius
              

    def query_Region(self, query, region, domain = 'http://api.map.baidu.com', server = 'place',
                        q_type = 'search', output = 'json'):
    
        url = '/'.join([domain, server, (q_type+'?&query=' + str(query) + '&region=' + str(region) + 
                                                  '&output=' + str(output)  +'&key=' + str(self.authKey))])
        
        baidu_Req = requests.get(url).json()
        
        status = baidu_Req['status']
        
        if str(status) != 'OK':
            
            print(status)
            return -1
        
        else:  
            
            return baidu_Req['results']
                 
    def query_Geo(self, query, region, domain = 'http://api.map.baidu.com', server = 'place',
                        q_type = 'search', output = 'json'):
        
        url = '/'.join([domain, server, (q_type+'?&query=' + str(query) + '&region=' + str(region) + 
                                                  '&output=' + str(output)  +'&key=' + str(self.authKey))])
        
        baidu_Req = requests.get(url).json()
        
        status = baidu_Req['status']
        
        if str(status) != 'OK':
            
            print(status)
            return -1
        
        else:
            
            json_Result = status
            
            try: 
                
                lat, lng = json_Result[0]['location'].values()
            except:
                
                lat = 0
                lng = 0
                
        
        
        
        return lat, lng
    
    def query_Location(self, query, location, domain = 'http://api.map.baidu.com', server = 'place',
                        q_type = 'search', output = 'json'):
        
        url = '/'.join([domain, server, (q_type+'?&query=' + str(query) + '&location=' + str(location) + '&radius='  +
                                                 str(self.radius) + '&output=' + str(output)  +'&key=' + str(self.authKey))])
        
        baidu_Req = requests.get(url).json()
        
        status = baidu_Req['status']
        
        if str(status) != 'OK':
            
            print(status)
            return -1
        
        else:
            
            json_Result = baidu_Req['results']
        
        
        
        return json_Result
    
    def search_Location_Binary(self, query_List, df_China_Geo):
        
        loading = 0
        
        for query_Elem in query_List:
           
            print ('System is Working . . . (0/' + str(len(df_China_Geo)) + ')' )
            for index, geocode in df_China_Geo[['Latitude','Longtitude']].iterrows():
                
                try:
                    q_Result = self.query_Location(query= query_Elem, location=str(geocode['Latitude']) + ','+ str(geocode['Longtitude']))
        
                    for i in range(9000000):
            
                        delay = 0
        
        
                    if q_Result == []:
            
                        df_China_Geo.loc[index,query_Elem] = 0
                    
                    else:
                
                        df_China_Geo.loc[index,query_Elem] = 1
            
                    loading += 1
                    print ('System is Working . . . ' + '(' + str(loading) +'/' + str(len(df_China_Geo)) + ')'+ '  QUERY : ' + query_Elem)
                    
                except:
                    
                    df_China_Geo.loc[index,query_Elem] = 'LINE HATA'
                    continue
                    
                    
            loading = 0
        
        
        df_China_Geo['Range'] =  self.radius
        
        
        return 0
    
    def search_Region_Binary(self, query_List, df_China_Geo):
        
        loading = 0
        
        for query_Elem in query_List:
           
            print ('System is Working . . . (0/' + str(len(df_China_Geo)) + ')' )
            
            for index, region in df_China_Geo['Region'].iterrows():
                
                try:
                    q_Result = self.query_Region(query= query_Elem, region = region)
        
                    for i in range(9000000):
            
                        delay = 0
        
        
                    if q_Result == []:
            
                        df_China_Geo.loc[index,query_Elem] = 0
                    
                    else:
                
                        df_China_Geo.loc[index,query_Elem] = 1
            
                    loading += 1
                    print ('System is Working . . . ' + '(' + str(loading) +'/' + str(len(df_China_Geo)) + ')'+ '  QUERY : ' + query_Elem)
                    
                except:
                    
                    df_China_Geo.loc[index,query_Elem] = 'LINE HATA'
                    continue
                    
                    
            loading = 0
        
        
        df_China_Geo['Range'] =  self.radius
        
        
        return 0
        
    def search_Location_Json(self, query_List, df_China_Geo):
        
        loading = 0
        
        result_List = list()
        
        for query_Elem in query_List:
           
            print ('System is Working . . . (0/' + str(len(df_China_Geo)) + ')' )
            for index, geocode in df_China_Geo[['Latitude','Longtitude']].iterrows():
                
                try:
                    q_Result = self.query_Location(query= query_Elem, location=str(geocode['Latitude']) + ','+ str(geocode['Longtitude']))
        
                    for i in range(9000000):
            
                        delay = 0
        
        
                    result_List.append(q_Result)
            
                    loading += 1
                    print ('System is Working . . . ' + '(' + str(loading) +'/' + str(len(df_China_Geo)) + ')'+ '  QUERY : ' + query_Elem)
                    
                except:
                    
                    df_China_Geo.loc[index,query_Elem] = 'LINE HATA'
                    continue
                    
                    
            loading = 0
        
        
        
        
        
        return result_List
     
    def search_Region_Json(self, query_List, df_China_Geo):
        
        loading = 0
        
        result_List = list()
        
        for query_Elem in query_List:
           
            print ('System is Working . . . (0/' + str(len(df_China_Geo)) + ')' )
            for index, geocode in df_China_Geo[['Latitude','Longtitude']].iterrows():
                
                try:
                    q_Result = self.query_Location(query= query_Elem, location=str(geocode['Latitude']) + ','+ str(geocode['Longtitude']))
        
                    for i in range(9000000):
            
                        delay = 0
        
        
                    result_List.append(q_Result)
            
                    loading += 1
                    print ('System is Working . . . ' + '(' + str(loading) +'/' + str(len(df_China_Geo)) + ')'+ '  QUERY : ' + query_Elem)
                    
                except:
                    
                    df_China_Geo.loc[index,query_Elem] = 'LINE HATA'
                    continue
                    
                    
            loading = 0
        
        
        
        
        
        return result_List
