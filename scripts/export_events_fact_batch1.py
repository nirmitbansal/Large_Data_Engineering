import pymysql
import csv
import os

OUTPUT_FILE = r"D:\Nirmit\Large_Data_Engineering\exports\events_fact_batch1.csv"

conn = pymysql.connect(
    host="localhost",
    user="nirmitbansal",
    password="nirmit2708",
    database="ad_analytics",
    cursorclass=pymysql.cursors.SSCursor  # streaming cursor
)

with conn.cursor() as cursor, open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    cursor.execute("""
        SELECT
            id,
            label,
            feature1, feature2, feature3, feature4, feature5,
            feature6, feature7, feature8, feature9, feature10,
            feature11, feature12, feature13,
            load_date
        FROM events_fact
    """)

    for row in cursor:
        writer.writerow(row)

conn.close()

print("Export completed:", OUTPUT_FILE)
