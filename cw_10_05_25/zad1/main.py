import sqlite3

def printLaptops():
    cursor.execute("SELECT * FROM sales WHERE product = 'Laptop'")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
        
def printFromSpecificPeriod(from_date, to_date):
    cursor.execute("SELECT * FROM sales WHERE date BETWEEN ? AND ?", (from_date, to_date))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
        
def printTransactionsAboveValue(value):
    cursor.execute("SELECT * FROM sales WHERE price > ?", (value,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
        
def calculateAndPrintTotalValueForEachProduct():
    cursor.execute("SELECT product, SUM(price) FROM sales GROUP BY product")
    rows = cursor.fetchall()

    for row in rows:
        print(f"Product: {row[0]}, Total Value: {row[1]}")
        
def findDayWithMostSales():
    cursor.execute("SELECT date, COUNT(*) FROM sales GROUP BY date ORDER BY COUNT(*) DESC LIMIT 1")
    row = cursor.fetchone()
    print(f"Day with most sales: {row[0]}, Number of sales: {row[1]}")
    
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()


print("1. Print all laptops")
printLaptops()
print("2. Print all transactions from a specific period")
printFromSpecificPeriod("2025-05-07", "2025-05-08")
print("3. Print all transactions above a specific value")
printTransactionsAboveValue(200)
print("4. Calculate and print the total value for each product")
calculateAndPrintTotalValueForEachProduct()
print("5. Find the day with the most sales")
findDayWithMostSales()


conn.close()


