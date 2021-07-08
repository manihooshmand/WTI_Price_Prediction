#in barname , data ra az yek database e delkhah (user edit konad) va 2 input migirad sepas ba MACHINE LEARNING hodoodi hads mizanad .
import mysql.connector
from sklearn import tree
x=[]
y=[]
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='########')
cursor = cnx.cursor()
query = 'SELECT * FROM Oil;'
cursor.execute(query)
for (date , WTI_Price , NYSE_Index , WTI_Index ) in cursor :
    x.append ([int(WTI_Price) , int(NYSE_Index)])
    y.append (int(WTI_Index))

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

new_price = float (input('Enter the considered Oil Barrel Price : '))
new_NYSE = float (input ('Enter the considered NYSE Index :'))
new_data = [[new_price , new_NYSE]]
answer = clf.predict(new_data)
print ('The WTI Index Would be approximately about : ' , answer[0])
	

