import json
import csv
import psycopg2

with open("iplmatchlist.json", "r") as read_file:
    data = json.load(read_file)

outputFile = open("test.csv", 'w', newline = '')
output = csv.writer(outputFile, delimiter = '|') #create a csv.write
for row in data:
    output.writerow(row.values()) #values row

try:
    conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
except:
    print("I am unable to connect to the database")
