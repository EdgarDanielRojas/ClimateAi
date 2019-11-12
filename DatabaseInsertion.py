import mysql.connector
import csv #

mydb = mysql.connector.connect(
  host="database-1.cdbq6xqd24lq.us-east-1.rds.amazonaws.com",
  user="admin",
  database="climateai"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tanoms")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
mycursor.execute("CREATE TABLE tanoms(id INT AUTO_INCREMENT PRIMARY KEY, lat float(5,2), lon float(5,2),tanom float(10,9),month tinyint)")

sql = "INSERT INTO tanoms (lat, lon, tanom, month) VALUES (%s, %s,%s,%s)"
with open('datapoints.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0;
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if row[5] != '':
                decomposedDate = row[1].split('/');
                month = decomposedDate[0];
                tupleToInsert = (float(row[2]),float(row[3]),float(row[5]),int(month))
                mycursor.execute(sql, tupleToInsert)
                print(line_count);
                #values.append(tupleToInsert);
                line_count += 1;
    print(f'Processed {line_count} lines.')
mydb.commit()
