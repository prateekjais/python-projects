import psycopg2

try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='pgadmin'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()
cur.execute("select * from ipl_match_schedule limit 10")
rows = cur.fetchall()
print("\n show me the list \n")
for row in rows :
    print(" ", row[1])