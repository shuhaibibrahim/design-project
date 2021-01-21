from core.pgconnect import conn
from datetime import datetime

cur = conn.cursor()

def insertPlate(number):
	now = datetime.now()
	time = now.strftime("%H:%M:%S")
	date=now.strftime("%m/%d/%Y")

	cur.execute("""INSERT INTO vehicle
	VALUES (%s, %s, %s);""",(number, date, time))
	conn.commit()
	print("Records created successfully");


