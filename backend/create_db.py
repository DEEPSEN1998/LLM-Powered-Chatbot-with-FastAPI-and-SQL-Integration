import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS customers (
  customer_id INTEGER PRIMARY KEY,
  name TEXT,
  gender TEXT,
  location TEXT
)
""")

seed = [
 (1, "Asha", "Female", "Mumbai"),
 (2, "Rohan", "Male", "Delhi"),
 (3, "Priya", "Female", "Mumbai"),
 (4, "Vikram", "Male", "Bangalore"),
 (5, "Sara", "Female", "Pune"),

 (6, "Rahul", "Male", "Kolkata"),
 (7, "Sneha", "Female", "Chennai"),
 (8, "Arjun", "Male", "Hyderabad"),
 (9, "Meera", "Female", "Jaipur"),
 (10, "Kiran", "Male", "Surat"),

 (11, "Ananya", "Female", "Delhi"),
 (12, "Sameer", "Male", "Mumbai"),
 (13, "Tara", "Female", "Indore"),
 (14, "Kabir", "Male", "Patna"),
 (15, "Neha", "Female", "Nagpur"),

 (16, "Dev", "Male", "Lucknow"),
 (17, "Isha", "Female", "Chandigarh"),
 (18, "Ritika", "Female", "Ahmedabad"),
 (19, "Aditya", "Male", "Noida"),
 (20, "Varun", "Male", "Kochi"),
]

c.executemany("INSERT OR IGNORE INTO customers VALUES (?,?,?,?)", seed)
conn.commit()
conn.close()

print("DB and seed done")
