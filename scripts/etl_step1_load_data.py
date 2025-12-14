import os
import pandas as pd
import pymysql
from dotenv import load_dotenv
from tqdm import tqdm

# ==============================
# 1. LOAD ENV VARIABLES
# ==============================
load_dotenv()

# ==============================
# 2. CONFIGURATION
# ==============================
FILE_PATH = r"D:\Nirmit\Large_Data_Engineering\data\raw\dac\train.txt"
CHUNK_SIZE = 900_000        # safe + fast
PROGRESS_FILE = "etl_progress.txt"

# ==============================
# 3. RESUME LOGIC FUNCTIONS
# ==============================
def get_start_row():
    """
    Reads how many rows were already loaded.
    """
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return int(f.read().strip())
    return 0


def save_progress(row_count):
    """
    Saves current progress to file.
    """
    with open(PROGRESS_FILE, "w") as f:
        f.write(str(row_count))


# ==============================
# 4. MYSQL CONNECTION
# ==============================
connection = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DB"),
    autocommit=False
)

cursor = connection.cursor()

# ==============================
# 5. SQL INSERT STATEMENT
# ==============================
insert_sql = """
INSERT INTO events_staging (
    label,
    f1, f2, f3, f4, f5,
    f6, f7, f8, f9, f10,
    f11, f12, f13
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

# ==============================
# 6. DETERMINE RESUME POINT
# ==============================
start_row = get_start_row()
print(f"Resuming ETL from row: {start_row}")

# ==============================
# 7. CSV READER (CHUNKED)
# ==============================
reader = pd.read_csv(
    FILE_PATH,
    sep="\t",
    header=None,
    usecols=list(range(14)),   # label + 13 features
    chunksize=CHUNK_SIZE,
    skiprows=range(start_row) if start_row > 0 else None
)

# ==============================
# 8. ETL LOOP
# ==============================
total_rows = start_row

for chunk in tqdm(reader, desc="ETL Loading"):

    # Convert to object dtype so None is allowed
    chunk = chunk.astype(object)

    # Replace NaN with None → MySQL NULL
    chunk = chunk.where(pd.notnull(chunk), None)

    # Insert chunk
    cursor.executemany(insert_sql, chunk.values.tolist())
    connection.commit()

    total_rows += len(chunk)

    # Save progress
    save_progress(total_rows)

    print(f"Inserted rows: {total_rows:,}")

# ==============================
# 9. CLEANUP
# ==============================
cursor.close()
connection.close()

print("ETL COMPLETED SUCCESSFULLY")
print(f"Total rows inserted: {total_rows:,}")
