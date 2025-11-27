import psycopg2
import csv

DB_CONFIG = {
    'dbname': 'lab10',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost'
}

def get_conn():
    return psycopg2.connect(**DB_CONFIG)

def upload_csv(filename):
    conn = get_conn()
    cur = conn.cursor()
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader, None) 
            for row in reader:
                if len(row) >= 2:
                    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
        print("CSV loaded")
    except Exception as e:
        print(f"Error {e}")
    conn.close()

def insert_console():
    name = input("Name: ")
    phone = input("Phone: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    conn.close()
    print("Added")

def update_data():
    col = input("Name or phone ").strip()
    old_name = input("Name: ")
    new_val = input("Phone: ")
    
    conn = get_conn()
    cur = conn.cursor()
    if col == 'name':
        cur.execute("UPDATE phonebook SET name=%s WHERE name=%s", (new_val, old_name))
    elif col == 'phone':
        cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_val, old_name))
    conn.commit()
    print("updated")
    conn.close()

def query_data():
    mode = input("Search using name or phone?")
    val = input("Search: ")
    conn = get_conn()
    cur = conn.cursor()
    if mode == '1':
        cur.execute("SELECT * FROM phonebook WHERE name LIKE %s", (f'%{val}%',))
    else:
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f'%{val}%',))
    rows = cur.fetchall()
    for r in rows: print(r)
    conn.close()

def delete_data():
    val = input("Type phone: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name=%s OR phone=%s", (val, val))
    conn.commit()
    print("deleted")
    conn.close()

def save_to_csv():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name, phone FROM phonebook")
    rows = cur.fetchall()
    
    try:
        with open('data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Phone'])
            writer.writerows(rows)
        print("Data stored")
    except Exception as e:
        print(f"Error {e}")
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Load CSV (data.csv)")
        print("2. Add manually")
        print("3. Update file")
        print("4. Query")
        print("5. Delete")
        print("6. Save")
        print("0. Exit")
        choice = input("Choose: ")
        if choice == '1': upload_csv('data.csv')
        elif choice == '2': insert_console()
        elif choice == '3': update_data()
        elif choice == '4': query_data()
        elif choice == '5': delete_data()
        elif choice == '6': save_to_csv()
        elif choice == '0': break