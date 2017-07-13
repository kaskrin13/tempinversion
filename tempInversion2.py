import pandas
import bs4
import requests
import datetime
import pytz

# goes to a website, finds a table on the page and inserts it into a 2d list
# then processes the data added to table (covert text to necessary formats)
# and returns the data for the current day
# input: url = string
# output: todaysData = 2d list
def getData(url):
    # get html from website
    html = requests.get(url)

    # get table from html
    data = [[cell.text.strip() for cell in row('td')] for row in bs4.BeautifulSoup(html.content, "html5lib")('tr')]
    # add column labels
    data[0] = ['Record Date', 'Record Time', 'Record Julian Date', 'Air Temp Max', 'Time Max Air Temp', 'Air Temp Min', 'Time Min Air Temp', 'Air Temp Obs', 'Rel Hum Max', 'Time Max Rel Hum', 'Rel Hum Min', 'Time Min Rel Hum ', 'Rel Hum Obs', 'Precip', 'Wind Speed', 'Wind Dir', 'Solar Rad', 'Soil Temp Avg 2 in', 'Soil Temp Avg 2 in', 'Soil Temp Avg 4 in', 'Soil Temp Obs 4 in']

    # remove last two rows, which are unnecessary
    data.pop(-1)
    data.pop(-1)
    
    # remove unnecessary columns
    for row in data:
        row.pop(2)
        row.pop(7)
        row.pop(7)
        row.pop(7)
        row.pop(7)
        row.pop(7)
        row.pop(7)
        row.pop(8)
        row.pop(8)
        row.pop(8)
        row.pop(8)
        row.pop(8)
        row.pop(8)

    # convert text to float for temperature, humidity, precipitation, and wind speed
    # if data is blank use NaN (not a number)
    for i in range(1, len(data), 1):
        if (data[i][2] == ''):
            data[i][2] = float('NaN')
        else:
            data[i][2] = float(data[i][2])
            
        if (data[i][4] == ''):
            data[i][4] = float('NaN')
        else:
            data[i][4] = float(data[i][4])
            
        if (data[i][6] == ''):
            data[i][6] = float('NaN')
        else:
            data[i][6] = float(data[i][6])

        if (data[i][7] == ''):
            data[i][7] = float('NaN')
        else:
            data[i][7] = float(data[i][7])

    # place data from today's date in a seperate table
    todaysData = []
    today = datetime.datetime.today()
    for row in data[1:]:
        if (today.date() == datetime.datetime.strptime(row[0], '%m/%d/%Y').date()):
            todaysData.append(row)

    return todaysData

# prints the data in a readible format for error checking
# input: data = 2d list
def printData(data):
    s = [[str(e) for e in row] for row in data]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))

# determines if daylight savings time is in effect
def daylightSavings(zonename):
    tz = pytz.timezone(zonename)
    now = pytz.utc.localize(datetime.datetime.utcnow())
    return now.astimezone(tz).dst() != datetime.timedelta(0)

# converts datetime object from UTC to local timezone
# input: utc = datetime
# output: utc+offset = datetime
def utcToLocal(utc):
    timezone = 'America/Chicago'
    tz = pytz.timezone('America/Chicago')
    if (daylightSavings(timezone)):
        return pytz.utc.localize(utc, is_dst=True).astimezone(tz)
    else:
        return pytz.utc.localize(utc, is_dst=False).astimezone(tz)

# checks if more than an hour has passed since the data was last updated 
# returns true if it has, false if not
# input: mostRecentTime = dateTime
# output: moreThanAnHour = boolean
def updatedLastHour(mostRecentTime):
    # Convert now from UTC to central time
    now = utcToLocal(datetime.datetime.now())

    # Make mostRecentTime timezone aware
    tz = pytz.timezone('America/Chicago')
    mostRecentTime = mostRecentTime.replace(tzinfo=tz)
    
    # Use the following code for local hosting/error checking because
    # otherwise 5/6 hours will be subtracted from the current time on the computer 
    # and the fuction will always return false
    #now = datetime.datetime.now()
    delta = now - mostRecentTime

    # Check if more than an hour has passed
    if (delta.seconds / 60) > 60:
        moreThanAnHour = True
    else:
        moreThanAnHour = False
    return moreThanAnHour

# gets lowest temperature of the day by
# searching entries in table (2d list) between the beginning
# of the current day and the last entry (most recent time)
# inputs: data = 2d list
# output: lowTemp = tuple(int, int)
def getLowTemp(data):
    lowTemp = data[0][4]
    index = 0

    #Search new list for lowest temp
    for i in range(0, len(data), 1):
        if data[i][4] < lowTemp:
            lowTemp = data[i][4]
            index = i
    return (lowTemp, index)

# gets highest temperature of the day by
# searching entries in table (2d list) between the beginning
# of the current day and the last entry (most recent time)
# inputs: data = 2d list
# output: highTemp = tuple(int, int)
def getHighTemp(data):
    highTemp = data[0][2]
    index = 0

    #Search new list for lowest temp
    for i in range(0, len(data), 1):
        if data[i][2] < highTemp:
            highTemp = data[i][2]
            index = i
    return (highTemp, index)

# determines whether there is a temperature inversion
# input: data = 2d list
# output: list (inversion, recent temp, recent time, recent wind speed, low temp, low temp time, high temp, high temp time, updated within last hour)
def tempInv(data):
    #Check if data is empty
    #If it is, return empty result
    if (not data):
        return [True, 0, 0, 0, 0, 0, 0, 0, True]
    
    #Get most recent data
    mostRecentTime = datetime.datetime.strptime(data[-1][0] + " " + data[-1][1], '%m/%d/%Y %H:%M:%S')
    #Need to check this, currently using most recent max temp
    mostRecentTemp = data[-1][6]
    mostRecentWindSpeed = data[-1][7]

    #Get high and low temp
    lowTemp = getLowTemp(data)
    highTemp = getHighTemp(data)

    #Determine if there is an inversion
    #Check if before noon
    if mostRecentTime.time() < datetime.time(12):      
        if mostRecentTemp - lowTemp[0] > 3:
            # no inversion and spray OK
            return [False, mostRecentTemp, str(mostRecentTime.time()), mostRecentWindSpeed, lowTemp[0], data[lowTemp[1]][5], highTemp[0], data[highTemp[1]][3], False]
        else:
            if (mostRecentTemp - lowTemp[0]) < 2:
                # strong inversion and no spray suggested
                return [True, mostRecentTemp, str(mostRecentTime.time()), mostRecentWindSpeed, lowTemp[0], data[lowTemp[1]][5], highTemp[0], data[highTemp[1]][3], False]
            else:
                if (mostRecentTemp - lowTemp[0]) < 2 and mostRecentWindSpeed > 4:
                    # no inversion and spray OK
                    return [False, mostRecentTemp, str(mostRecentTime.time()), mostRecentWindSpeed, lowTemp[0], data[lowTemp[1]][5], highTemp[0], data[highTemp[1]][3], False]
                else:
                    # strong inversion and no spray suggested
                    return [True, mostRecentTemp, str(mostRecentTime.time()), mostRecentWindSpeed, lowTemp[0], data[lowTemp[1]][5], highTemp[0], data[highTemp[1]][3], False]
    else:
        if abs(mostRecentTemp - highTemp[0]) <= 5:
            # no inversion and spray OK
            return [False, mostRecentTemp, str(mostRecentTime.time()), mostRecentWindSpeed, lowTemp[0], data[lowTemp[1]][5], highTemp[0], data[highTemp[1]][3], False]
        else:
            if (mostRecentTemp - highTemp[0]) >= 7:
                # strong inversion and no spray suggested
                return [True, mostRecentTemp, str(mostRecentTime.time()), mostRecentWindSpeed, lowTemp[0], data[lowTemp[1]][5], highTemp[0], data[highTemp[1]][3], False]
            else:
                if (mostRecentTemp - highTemp[0]) >= 7 and mostRecentWindSpeed > 4:
                    # no inversion and spray OK
                    return [False, mostRecentTemp, str(mostRecentTime.time()), mostRecentWindSpeed, lowTemp[0], data[lowTemp[1]][5], highTemp[0], data[highTemp[1]][3], False]
                else:
                    # strong inversion and no spray suggested
                    return [True, mostRecentTemp, str(mostRecentTime.time()), mostRecentWindSpeed, lowTemp[0], data[lowTemp[1]][5], highTemp[0], data[highTemp[1]][3], False]

def main():
    urls = [("http://deltaweather.extension.msstate.edu/7-days-hourly-table/DREC-2005", "Verona"), ("http://deltaweather.extension.msstate.edu/7-days-hourly-table/DREC-2013", "Mound Bayou"),
            ("http://deltaweather.extension.msstate.edu/7-days-hourly-table/DREC-2002", "Thighman Lake"), ("http://deltaweather.extension.msstate.edu/7-days-hourly-table/DREC-2012", "Stockett Farm"),
            ("http://deltaweather.extension.msstate.edu/7-days-hourly-table/DREC-2003", "Sidon"), ("http://deltaweather.extension.msstate.edu/7-days-hourly-table/DREC-2007", "Prairie"),
            ("http://deltaweather.extension.msstate.edu/7-days-hourly-table/DREC-2001", "Lyon"), ("http://deltaweather.extension.msstate.edu/7-days-hourly-table/DREC-2011", "Jackson Co."),
            ("http://deltaweather.extension.msstate.edu/7-days-hourly-table/DREC-2006", "Brooksville"), ("http://deltaweather.extension.msstate.edu/7-days-hourly-table/DREC-2010", "Bee Lake")]
    
    results = []
    
    for i in range(0, len(urls), 1):
        data = getData(urls[i][0])
        results.append(tempInv(data))
        results[i].append(urls[i][1])

    return results

if __name__ == "__main__":
    main()
