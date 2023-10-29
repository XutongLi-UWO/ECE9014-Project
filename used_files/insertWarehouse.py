import csv
import psycopg2
import json

json_file_path = "../run.json"

with open(json_file_path, 'r') as json_file:
    postgres_settings = json.load(json_file)

username = postgres_settings["user"]
password = postgres_settings["password"]
dbname = postgres_settings["database"]
host = postgres_settings["host"]
port = postgres_settings["port"]


conn = psycopg2.connect(
    dbname = dbname,
    user = username,
    password = password,
    host = host,
    port = port
)
cur = conn.cursor()

with open('Warehouse/Warehouse.StockItemStockGroups.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 3):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO StockItemStockGroups (StockItemStockGroupID, StockItemID, StockGroupID) VALUES (%s, %s, %s)",
            (row[0], row[1], row[2])
        )

with open('Warehouse/Warehouse.Colors.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 2):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO Colors (ColorID, ColorName) VALUES (%s, %s)",
            (row[0], row[1])
        )



with open('Warehouse/Warehouse.StockItemTransactions.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 9):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO StockItemTransactions (StockItemTransactionID, StockItemID, TransactionTypeID, CustomerID, InvoiceID, SupplierID, PurchaseOrderID, TransactionOccurredWhen, Quantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        )



with open('Warehouse/Warehouse.StockItems.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 16):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO StockItems (StockItemID, StockItemName, SupplierID, ColorID, UnitPackageID, OuterPackageID, Brand, Size, LeadTimeDays, QuantityPerOuter, IsChillerStock, Barcode, TaxRate, UnitPrice, RecommendedRetailPrice, TypicalWeightPerUnit) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
        )



with open('Warehouse/Warehouse.StockItemHoldings.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 7):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO StockItemHoldings (StockItemID, QuantityOnHand, BinLocation, LastStocktakeQuantity, LastCostPrice, ReorderLevel, TargetStockLevel) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        )


with open('Warehouse/Warehouse.StockGroups.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 2):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO StockGroups (StockGroupID, StockGroupName) VALUES (%s, %s)",
            (row[0], row[1])
        )

with open('Warehouse/Warehouse.PackageTypes.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 2):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO PackageTypes (PackageTypeID, PackageTypeName) VALUES (%s, %s)",
            (row[0], row[1])
        )


conn.commit()
cur.close()
conn.close()

