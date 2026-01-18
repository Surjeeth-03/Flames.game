import sqlite3
from datetime import date, datetime
import sys

db = "gst_demo.db"
sup_state = "Karnataka"


def setup():
    c = sqlite3.connect(db)
    cur = c.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS gst_data (
            gid INTEGER PRIMARY KEY AUTOINCREMENT,
            cname TEXT,
            gstno TEXT,
            sales REAL,
            gst REAL,
            fdate TEXT
        )
    """)
    c.commit()
    c.close()


def add_row(cname, gstno, sales, gst, fdate):
    c = sqlite3.connect(db)
    cur = c.cursor()
    cur.execute("INSERT INTO gst_data (cname, gstno, sales, gst, fdate) VALUES (?, ?, ?, ?, ?)",
                (cname, gstno, sales, gst, fdate))
    c.commit()
    c.close()
    print("Data added.")


def view_rows():
    c = sqlite3.connect(db)
    cur = c.cursor()
    cur.execute("SELECT * FROM gst_data")
    r = cur.fetchall()
    c.close()
    return r


def update_row(gid, sales, gst):
    c = sqlite3.connect(db)
    cur = c.cursor()
    cur.execute("UPDATE gst_data SET sales=?, gst=? WHERE gid=?", (sales, gst, gid))
    c.commit()
    c.close()
    print("Data updated.")


def delete_row(gid):
    c = sqlite3.connect(db)
    cur = c.cursor()
    cur.execute("DELETE FROM gst_data WHERE gid=?", (gid,))
    c.commit()
    c.close()
    print("Data deleted.")


def demo():
    print("\nAdding gst data :")
    print("Enter your choice: 1")
    add_row("ABC Corp", "27ABCDE1234F2Z5", 100000.0, 18000.0, date(2024, 12, 31).isoformat())

    print("\nViewing gst data:")
    print("Enter your choice: 2")
    rows = view_rows()
    for r in rows:
        try:
            d = datetime.fromisoformat(r[5]).date()
        except:
            d = r[5]
        print((r[0], r[1], r[2], r[3], r[4], d))

    print("\nUpdating gst data:")
    print("Enter your choice: 3")
    if rows:
        gid = rows[0][0]
        print("Enter GST ID to update:", gid)
        update_row(gid, 120000.0, 21600.0)

    print("\nDeleting gst data:")
    print("Enter your choice: 4")
    rows2 = view_rows()
    if rows2:
        gid = rows2[0][0]
        print("Enter GST ID to delete:", gid)
        delete_row(gid)

    print("\nDemo finished.\n")


def menu():
    setup()
    while True:
        print("1. Add GST Data")
        print("2. View GST Data")
        print("3. Update GST Data")
        print("4. Delete GST Data")
        print("5. Demo Run")
        print("0. Exit")
        ch = input("Enter choice: ")

        if ch == "1":
            cname = input("Company name: ")
            gstno = input("GST number: ")
            sales = float(input("Total sales: "))
            gst = float(input("GST paid: "))
            fdate = input("Filing date (YYYY-MM-DD): ")
            add_row(cname, gstno, sales, gst, fdate)

        elif ch == "2":
            rows = view_rows()
            for r in rows:
                print(r)

        elif ch == "3":
            gid = int(input("GST ID: "))
            sales = float(input("New sales: "))
            gst = float(input("New GST paid: "))
            update_row(gid, sales, gst)

        elif ch == "4":
            gid = int(input("GST ID: "))
            delete_row(gid)

        elif ch == "5":
            demo()

        elif ch == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    setup()
    if len(sys.argv) > 1 and sys.argv[1].lower() == "demo":
        demo()
    else:
        menu()



