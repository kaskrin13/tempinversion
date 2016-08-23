import pandas as pd                     #data structures
from bs4 import BeautifulSoup           #HTML parsing
import requests                         #HTTP library
import numpy as np                      #arrays


def scraper():
    
    #Arkansas State Plant Board Weather Web data
    url1 = "http://170.94.200.136/weather/Inversion.aspx"
    response1 = requests.get(url1)

    soup1 = BeautifulSoup(response1.content, "html5lib")
    table1 = soup1.find("table", id="MainContent_GridView1")

    data1 = pd.read_html(str(table1),header=0)[0] 
    data1.columns = ['Station', 'Low Temp (F)', 'Time of Low', 'Current Temp (F)', 'Current Time',	'Wind Speed (MPH)',	'Wind Dir',	'High Temp (F)', 'Time Of High']
    
    print(url1)
    print(data1[0:4])
    
    array1 = np.array(data1[0:4])
    
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

    time = str(array1[0][4])
    meridian = time.split(' ')[-1] # get just the meridian
    before_noon = meridian == 'AM'
    recommendations = []
    if before_noon == True:    
    #before noon logic
    #Ashley
        if AshCurT - AshLowT > 3:
            print("Ashley: no inversion and spray OK")
            recommendations.append("Ashley: no inversion and spray OK")
            
        else:
            if AshCurT - AshLowT < 2:
                print("Ashley: strong inversion and no spray suggested")
                recommendations.append("Ashley: strong inversion and no spray suggested")
                
            else:
                if AshCurT - AshLowT < 2 and AshWS > 4:
                    print("Ashley: spray OK")
                    recommendations.append("Ashley: spray OK")
                    
                else:
                    print("Ashley: no spray")
                    recommendations.append("Ashley: no spray")
                    
    #Chicot    
        if ChiCurT - ChiLowT > 3:
            print("Chicot: no inversion and spray OK")
            recommendations.append("Chicot: no inversion and spray OK")
            
        else:
            if ChiCurT - ChiLowT < 2:
                print("Chicot: strong inversion and no spray suggested")
                recommendations.append("Chicot: strong inversion and no spray suggested")
                
            else:
                if ChiCurT - AshLowT < 2 and ChiWS > 4:
                    print("Chicot: spray OK")
                    recommendations.append("Chicot: spray OK")
                    
                else:
                    print("Chicot: no spray")
                    recommendations.append("Chicot: no spray")
                      
    #Craighead East           
        if CRECurT - CRELowT > 3:
            print("Craighead East: no inversion and spray OK")
            recommendations.append("Craighead East: no inversion and spray OK")
            
        else:
            if CRECurT - CRELowT < 2:
                print("Craighead East: strong inversion and no spray suggested")
                recommendations.append("Craighead East: strong inversion and no spray suggested")
                
            else:
                if CRECurT - CRELowT < 2 and CREWS > 4:
                    print("Craighead East: spray OK")
                    recommendations.append("Craighead East: spray OK")
                    
                else:
                    print("Craighead East: no spray")
                    recommendations.append("Craighead East: no spray")                   
                
    #Craighead West         
        if CRWCurT - CRWLowT > 3:
            print("Craighead West: no inversion and spray OK")
            recommendations.append("Craighead West: no inversion and spray OK")
            
        else:
            if CRWCurT - CRWLowT < 2:
                print("Craighead West: strong inversion and no spray suggested")
                recommendations.append("Craighead West: strong inversion and no spray suggested")
                
            else:
                if CRWCurT - CRWLowT < 2 and CRWWS > 4:
                    print("Craighead West: spray OK")
                    recommendations.append("Craighead West: spray OK")
                    
                else:
                    print("Craighead West: no spray")    
                    recommendations.append("Craighead West: no spray")
                    
      
    #afternoon logic              
    else:
        if abs(AshCurT - AshHiT) <= 5:
            print("Ashley: no inversion and spray OK")
            recommendations.append("Ashley: no inversion and spray OK")
            
        else:
            if AshCurT - AshHiT >= 7:
                print("Ashley: strong inversion and no spray suggested")
                recommendations.append("Ashley: strong inversion and no spray suggested")
            else:
                if AshCurT - AshHiT >= 7 and AshWS > 4:
                    print("Ashley: spray OK")
                    recommendations.append("Ashley: spray OK")
                else:
                    print("Ashley: no spray")

    #Chicot    
        if abs(ChiCurT - ChiHiT) <= 5:
            print("Chicot: no inversion and spray OK")
            recommendations.append("Chicot: no inversion and spray OK")
        else:
            if ChiCurT - ChiHiT >= 7:
                print("Chicot: strong inversion and no spray suggested")
                recommendations.append("Chicot: strong inversion and no spray suggested")
            else:
                if ChiCurT - ChiHiT >= 7 and ChiWS > 4:
                    print("Chicot: spray OK")
                    recommendations.append("Chicot: spray OK")
                else:
                    print("Chicot: no spray")
                    recommendations.append("Chicot: no spray")

    #Craighead East           
        if abs(CRECurT - CREHiT) <= 5:
            print("Craighead East: no inversion and spray OK")
            recommendations.append("Craighead East: no inversion and spray OK")
        else:
            if CRECurT - CREHiT >= 7:
                print("Craighead East: strong inversion and no spray suggested")
                recommendations.append("Craighead East: strong inversion and no spray suggested")
            else:
                if CRECurT - CREHiT >= 7 and CREWS > 4:
                    print("Craighead East: spray OK")
                    recommendations.append("Craighead East: spray OK")
                else:
                    print("Craighead East: no spray")
                    recommendations.append("Craighead East: no spray")
       
    #Craighead West         
        if abs(CRWCurT - CRWHiT) <= 5:
            print("Craighead West: no inversion and spray OK")
            recommendations.append("Craighead West: no inversion and spray OK")
        else:
            if CRWCurT - CRWHiT >= 7:
                print("Craighead West: strong inversion and no spray suggested")
                recommendations.append("Craighead West: strong inversion and no spray suggested")
            else:
                if CRWCurT - CRWHiT >= 7 and CRWWS > 4:
                    print("Craighead West: spray OK")
                    recommendations.append("Craighead West: spray OK")
                else:
                    print("Craighead West: no spray")
                    recommendations.append("Craighead West: spray OK")
    
    rec = ""
    for i in range(len(recommendations)):
        rec += "<p>"
        rec += recommendations[i]
        rec += "</p>"
        
    
    str_var = ""
    with open("C:/Users/Huang.LabTech2/Desktop/hello/polls/templates/test.html", "w") as out_file:
        str_var = str(data1[0:4].to_html())
        #str_var += "<body text=\"orange\">"
        str_var += "\n"
        #str_var += "<h1>I SAY THEE NAY...NAY!!!!!!</h1>"
        str_var += "\n"
#        str_var += "<p>"
#        str_var += "\n"
        str_var += rec
#        str_var += "\n"
#        str_var += "</p>"
        str_var += "</body>"
        str_var += "\n"
        out_file.write(str_var) 
        print "SAVED!!!!"
    return data1#, str_var,recommendations
