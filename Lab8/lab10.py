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
    names = []
    phones = []
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if len(row) >= 2:
                    names.append(row[0])
                    phones.append(row[1])
        
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("CALL insert_many_users(%s, %s, %s)", (names, phones, []))
        incorrect_data = cur.fetchone()[0]
        conn.commit()
        print("CSV processing complete.")
        if incorrect_data:
            print(f"Skipped incorrect data: {incorrect_data}")
        else:
            print("All data inserted successfully.")
        cur.close()
        conn.close()
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

def insert_console():
    name = input("Name: ")
    phone = input("Phone: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL add_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    conn.close()
    print("User processed.")

def query_data():
    pattern = input("Enter search pattern: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.callproc('search_contacts', (pattern,))
    rows = cur.fetchall()
    print(f"\nFound {len(rows)} records:")
    for r in rows:
        print(r)
    conn.close()

def pagination_data():
    try:
        limit = int(input("Limit: "))
        offset = int(input("Offset: "))
        conn = get_conn()
        cur = conn.cursor()
        cur.callproc('get_contacts_paginated', (limit, offset))
        rows = cur.fetchall()
        print("\n--- Page Result ---")
        for r in rows:
            print(r)
        conn.close()
    except ValueError:
        print("Please enter valid numbers.")

def delete_data():
    val = input("Enter name OR phone to delete: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL delete_user_by_criterion(%s)", (val,))
    conn.commit()
    print("Delete operation complete.")
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
        print("Data saved to data.csv")
    except Exception as e:
        print(f"Error {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    while True:
        print("\n--- PHONEBOOK (LAB 11) ---")
        print("1. Upload from CSV")
        print("2. Add/Update User")
        print("3. Search")
        print("4. Pagination")
        print("5. Delete User")
        print("6. Save to CSV")
        print("0. Exit")
        
        choice = input("Choose: ")
        
        if choice == '1': 
            upload_csv('data.csv')
        elif choice == '2': 
            insert_console()
        elif choice == '3': 
            query_data()
        elif choice == '4': 
            pagination_data()
        elif choice == '5': 
            delete_data()
        elif choice == '6': 
            save_to_csv()
        elif choice == '0': 
            break
        else:
            print("Invalid choice")