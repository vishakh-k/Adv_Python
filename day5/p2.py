import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Drop old table if it exists
cursor.execute("DROP TABLE IF EXISTS student")

# Create new table with 6 columns
cursor.execute("""
CREATE TABLE student (
    name TEXT NOT NULL,
    usn TEXT PRIMARY KEY,
    sem INTEGER,
    dob TEXT,
    dept TEXT,
    address TEXT
)
""") 

conn.commit()
print("Database and student table created successfully.")

# Insert function and data (as before)...

# Function to insert values
def add_values(name, usn, sem, dob, dept, address):
    try:
        cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?)", (name, usn, sem, dob, dept, address))
        conn.commit()
        print(f"Record for {name} saved successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error inserting {name} ({usn}): {e}")

# Insert data
add_values("JHON", "4SN24MC039", 2, "23-05-2025", "MCA", "BCROAD")
add_values("MOHAN", "4SN24MC013", 2, "22-04-2025", "MCA", "BHATKALA")
add_values("SHRAVAN", "4SN24MC012", 2, "23-05-2020", "MCA", "MUGER")
add_values("RITHESH", "4SN24MC011", 2, "09-03-2025", "MCA", "MANGALORE")

def view_data():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    
    if rows:
        print("Student Records:")
        for row in rows:
            print(f"Name: {row[0]}, USN: {row[1]}, Sem: {row[2]}, DOB: {row[3]}, Dept: {row[4]}, Address: {row[5]}")
    else:
        print("No records found.")
        
# Call the function to view the records
view_data()

# Function to update student data
def update_data(usn, name=None, sem=None, dob=None, dept=None, address=None):
    # Prepare the update query dynamically
    updates = []
    params = []

    if name is not None:
        updates.append("name = ?")
        params.append(name)
    if sem is not None:
        updates.append("sem = ?")
        params.append(sem)
    if dob is not None:
        updates.append("dob = ?")
        params.append(dob)
    if dept is not None:
        updates.append("dept = ?")
        params.append(dept)
    if address is not None:
        updates.append("address = ?")
        params.append(address)

    if not updates:
        print("No data to update.")
        return

    # Final SQL command
    sql = f"UPDATE student SET {', '.join(updates)} WHERE usn = ?"
    params.append(usn)

    cursor.execute(sql, params)
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Record with USN {usn} updated successfully.")
    else:
        print(f"No record found with USN {usn}.")

update_data("4SN24MC012", name="SHRAVAN K", address="UDUPI")


def delete_data(usn):
    cursor.execute("DELETE FROM student WHERE usn=?",(usn,));
    conn.commit()
    print("data deleted");

delete_data("4SN24MC012")

# Close the connection at the end
conn.close()


