import pandas as pd                     #data structures
from bs4 import BeautifulSoup           #HTML parsing
import requests                         #HTTP library
import numpy as np                      #arrays

#import tornado.web
#import tornado.ioloop

def scraper():
    
    #Ashley State Plant Board Weather Web data
    url1 = "http://170.94.200.136/weather/Inversion.aspx"
    response1 = requests.get(url1)

    soup1 = BeautifulSoup(response1.content, "html5lib")
    table1 = soup1.find("table", id="MainContent_GridView1")

    data1 = pd.read_html(str(table1),header=0)[0] 
    data1.columns = ['Station', 'Low Temp (F)', 'Time of Low', 'Current Temp (F)', 'Current Time',	'Wind Speed (MPH)',	'Wind Dir',	'High Temp (F)', 'Time Of High']
    
    print(url1)
    print(data1[4:8])
    
    array1 = np.array(data1[4:8])
    
    AshLowT = float(array1[0][1])
    AshCurT = float(array1[0][3])
    AshHiT = float(array1[0][7])
    AshWS = float(array1[0][5])
    
    ChiLowT = float(array1[1][1])
    ChiCurT = float(array1[1][3])
    ChiHiT = float(array1[1][7])
    ChiWS = float(array1[1][5])
    
    CRELowT = float(array1[2][1])
    CRECurT = float(array1[2][3])
    CREHiT = float(array1[2][7])
    CREWS = float(array1[2][5])
    
    CRWLowT = float(array1[3][1])
    CRWCurT = float(array1[3][3])
    CRWHiT = float(array1[3][7])
    CRWWS = float(array1[3][5])    

    dum = array1[:,1:array1.shape[1]]
    wdkeys = ['c1','c2','c3','c4','c5','c6','c7','c8','gv1','gv2','gv3','gv4','gv5','gv6','gv7','gv8','gw1','gw2','gw3','gw4','gw5','gw6','gw7','gw8','s1','s2','s3','s4','s5','s6','s7','s8'] 
    wdvalues = np.ravel(dum).tolist()
    weather_dict = dict(zip(wdkeys, wdvalues))

    time = str(array1[0][4])
    meridian = time.split(' ')[-1] # get just the meridian
    before_noon = meridian == 'AM'
    
    
    temp_inversion = {"c_color":"LightGreen", "gv_color":"LightGreen", "gw_color":"LightGreen", "s_color":"LightGreen"}
    
    
    if before_noon == True:    
    #before noon logic
    #Ashley
        if AshCurT - AshLowT > 3:
#            print("Ashley: no inversion and spray OK")
#            recommendations.append("Ashley: no inversion and spray OK")
            temp_inversion["c_color"] = "LightGreen"
        else:
            if AshCurT - AshLowT < 2:
#                print("Ashley: strong inversion and no spray suggested")
#                recommendations.append("Ashley: strong inversion and no spray suggested")
                temp_inversion["c_color"] = "Crimson"
            else:
                if AshCurT - AshLowT < 2 and AshWS > 4:
#                    print("Ashley: spray OK")
#                    recommendations.append("Ashley: spray OK")
                    temp_inversion["c_color"] = "LightGreen"
                else:
#                    print("Ashley: no spray")
#                    recommendations.append("Ashley: no spray")
                    temp_inversion["c_color"] = "Crimson"
    #Chicot    
        if ChiCurT - ChiLowT > 3:
#            print("Chicot: no inversion and spray OK")
#            recommendations.append("Chicot: no inversion and spray OK")
            temp_inversion["gv_color"] = "LightGreen"
        else:
            if ChiCurT - ChiLowT < 2:
#                print("Chicot: strong inversion and no spray suggested")
#                recommendations.append("Chicot: strong inversion and no spray suggested")
                temp_inversion["gv_color"] = "Crimson"
            else:
                if ChiCurT - AshLowT < 2 and ChiWS > 4:
#                    print("Chicot: spray OK")
#                    recommendations.append("Chicot: spray OK")
                    temp_inversion["gv_color"] = "LightGreen"
                else:
#                    print("Chicot: no spray")
#                    recommendations.append("Chicot: no spray")
                    temp_inversion["gv_color"] = "Crimson"
    #Craighead East           
        if CRECurT - CRELowT > 3:
#            print("Craighead East: no inversion and spray OK")
#            recommendations.append("Craighead East: no inversion and spray OK")
            temp_inversion["gw_color"] = "LightGreen"
            
        else:
            if CRECurT - CRELowT < 2:
#                print("Craighead East: strong inversion and no spray suggested")
#                recommendations.append("Craighead East: strong inversion and no spray suggested")
                temp_inversion["gw_color"] = "Crimson"
            else:
                if CRECurT - CRELowT < 2 and CREWS > 4:
#                    print("Craighead East: spray OK")
#                    recommendations.append("Craighead East: spray OK")
                    temp_inversion["gw_color"] = "LightGreen"
                else:
#                    print("Craighead East: no spray")
#                    recommendations.append("Craighead East: no spray")   
                    temp_inversion["gw_color"] = "Crimson"
                
    #Craighead West         
        if CRWCurT - CRWLowT > 3:
#            print("Craighead West: no inversion and spray OK")
#            recommendations.append("Craighead West: no inversion and spray OK")
            temp_inversion["s_color"] = "LightGreen"
            
        else:
            if CRWCurT - CRWLowT < 2:
#                print("Craighead West: strong inversion and no spray suggested")
#                recommendations.append("Craighead West: strong inversion and no spray suggested")
                temp_inversion["s_color"] = "Crimson"
            else:
                if CRWCurT - CRWLowT < 2 and CRWWS > 4:
#                    print("Craighead West: spray OK")
#                    recommendations.append("Craighead West: spray OK")
                    temp_inversion["s_color"] = "LightGreen"
                else:
#                    print("Craighead West: no spray")    
#                    recommendations.append("Craighead West: no spray")
                    temp_inversion["s_color"] = "Crimson"
      
    #afternoon logic              
    else:
        if abs(AshCurT - AshHiT) <= 5:
#            print("Ashley: no inversion and spray OK")
#            recommendations.append("Ashley: no inversion and spray OK")
            temp_inversion["c_color"] = "LightGreen"
        else:
            if AshCurT - AshHiT >= 7:
#                print("Ashley: strong inversion and no spray suggested")
#                recommendations.append("Ashley: strong inversion and no spray suggested")
                temp_inversion["c_color"] = "Crimson"
            else:
                if AshCurT - AshHiT >= 7 and AshWS > 4:
#                    print("Ashley: spray OK")
#                    recommendations.append("Ashley: spray OK")
                    temp_inversion["c_color"] = "LightGreen"
                else:
#                    print("Ashley: no spray")
                    temp_inversion["c_color"] = "Crimson"

    #Chicot    
        if abs(ChiCurT - ChiHiT) <= 5:
#            print("Chicot: no inversion and spray OK")
#            recommendations.append("Chicot: no inversion and spray OK")
            temp_inversion["gv_color"] = "LightGreen"
        else:
            if ChiCurT - ChiHiT >= 7:
#                print("Chicot: strong inversion and no spray suggested")
#                recommendations.append("Chicot: strong inversion and no spray suggested")
                temp_inversion["gv_color"] = "Crimson"
            else:
                if ChiCurT - ChiHiT >= 7 and ChiWS > 4:
#                    print("Chicot: spray OK")
#                    recommendations.append("Chicot: spray OK")
                    temp_inversion["gv_color"] = "LightGreen"
                else:
#                    print("Chicot: no spray")
#                    recommendations.append("Chicot: no spray")
                    temp_inversion["gv_color"] = "Crimson"

    #Craighead East           
        if abs(CRECurT - CREHiT) <= 5:
#            print("Craighead East: no inversion and spray OK")
#            recommendations.append("Craighead East: no inversion and spray OK")
            temp_inversion["gw_color"] = "LightGreen"
        else:
            if CRECurT - CREHiT >= 7:
#                print("Craighead East: strong inversion and no spray suggested")
#                recommendations.append("Craighead East: strong inversion and no spray suggested")
                temp_inversion["gw_color"] = "Crimson"
            else:
                if CRECurT - CREHiT >= 7 and CREWS > 4:
#                    print("Craighead East: spray OK")
#                    recommendations.append("Craighead East: spray OK")
                    temp_inversion["gw_color"] = "LightGreen"
                else:
#                    print("Craighead East: no spray")
#                    recommendations.append("Craighead East: no spray")
                    temp_inversion["gw_color"] = "Crimson"
       
    #Craighead West         
        if abs(CRWCurT - CRWHiT) <= 5:
#            print("Craighead West: no inversion and spray OK")
#            recommendations.append("Craighead West: no inversion and spray OK")
            temp_inversion["s_color"] = "LightGreen"
        else:
            if CRWCurT - CRWHiT >= 7:
#                print("Craighead West: strong inversion and no spray suggested")
#                recommendations.append("Craighead West: strong inversion and no spray suggested")
                temp_inversion["s_color"] = "Crimson"
            else:
                if CRWCurT - CRWHiT >= 7 and CRWWS > 4:
#                    print("Craighead West: spray OK")
#                    recommendations.append("Craighead West: spray OK")
                    temp_inversion["s_color"] = "LightGreen"
                else:
#                    print("Craighead West: no spray")
#                    recommendations.append("Craighead West: spray OK")
                    temp_inversion["s_color"] = "Crimson"
    

        
    weather_dict.update(temp_inversion)
    
    return weather_dict #data1#, str_var,recommendations

#data = scraper()
#
#
#sched.add_job(scraper, 'interval', seconds=60)
#sched.start()
