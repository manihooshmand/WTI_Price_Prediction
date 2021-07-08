#in barname , fetch data az yek database delkhah (user edit konad) ba jadvale "Oil" shamele 4 sotoone date , WTI_Price , NYSE_Index va WTI_Index mibashad .
from bs4 import BeautifulSoup
import mysql.connector
import requests
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='#######')
cursor1 = cnx.cursor()

#ghesmate 1 : tarikh va gheymate sahm
url1 = 'https://finance.yahoo.com/quote/WTI/history?period1=1514764800&period2=1604966400&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true'
r1 = requests.get(url1)
soup1 = BeautifulSoup (r1.text , 'html.parser')
val1 = soup1.find_all('td')
list1=[]
mainlist=[]
for value in val1 :
    list1.append(value.text)
for i in range (0,len(list1)) :
    if ('2020' in list1[i]) or ('2019' in list1[i]) or ('2018' in list1[i]) :
        mainlist.append([list1[i],float (list1[i+4])])

#ghesmate 2 : gheymate har boshke naft
url2 = 'https://finance.yahoo.com/quote/CL%3DF/history?period1=1514764800&period2=1604966400&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true'
r2 = requests.get(url2)
soup2 = BeautifulSoup (r2.text , 'html.parser')
val2 = soup2.find_all('td')
list2 = []
list22 = []
for value in val2 :
    list2.append(value.text)
for i in range (0,len(list2)) :
    if ('2020' in list2[i]) or ('2019' in list2[i]) or ('2018' in list2[i]) :
        list22.append(float (list2[i+4]))
for i in range (0,len(mainlist)) :
    mainlist[i].append(list22[i])

#ghesmate 3 : shakhese boorse new york
url3 = 'https://finance.yahoo.com/quote/%5ENYA/history?period1=1514764800&period2=1604966400&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true'
r3 = requests.get(url3)
soup3 = BeautifulSoup (r3.text , 'html.parser')
val3 = soup3.find_all('td')
list3 = []
list33 = []
for value in val3 :
    list3.append(value.text)
for i in range (0,len(list3)) :
    if ('2020' in list3[i]) or ('2019' in list3[i]) or ('2018' in list3[i]) :
        if ',' in list3[i+4] :
            list3[i+4] = list3[i+4].replace(",", "")
            list33.append(float (list3[i+4]))
for i in range (0,len(mainlist)) :
    mainlist[i].append(list33[i])


for element in mainlist :
    cursor1.execute ("INSERT INTO Oil (date, WTI_Index,WTI_Price,NYSE_Index) VALUES (\'%s\', %f , %f , %f)" % (element[0],element[1],element[2],element[3]))


cnx.commit()
cnx.close()

print ('adding new data succeeded !')

