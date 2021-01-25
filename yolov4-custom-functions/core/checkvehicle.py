from core.pgconnect import conn
from datetime import datetime

cur = conn.cursor()
def check(number):
  cur.execute("""SELECT fuel, owner, email from vowner where pnumber=%s""",(number,))
  row=cur.fetchone()
  # for row in rows:
  #     print(row)
  print("fuel:",row[0],"\nowner",row[1])
  if row[0]!='electric' and row[1]!='public':
    return row[2]
  return False  

