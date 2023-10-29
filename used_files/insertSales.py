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

# with open('Sales/Sales.Orders.csv', 'r') as file:
#     reader = csv.reader(file, delimiter=';')
#     next(reader)
#     for row in reader:
#         for i in range(0, 11):
#             if row[i] == "NULL":
#                 row[i] = None
#         cur.execute(
#             "INSERT INTO Orders (OrderID, CustomerID, SalespersonPersonID, PickedByPersonID, ContactPersonID, BackorderOrderID, OrderDate, ExpectedDeliveryDate, CustomerPurchaseOrderNumber, IsUndersupplyBackordered, PickingCompletedWhen) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
#             (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
#         )



def reformat_date(date_str):
    date_parts = date_str.split("/")
    return f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"

with open('Sales/Sales.Orders.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader) 
    for row in reader:
        for i in range(0, 11):
            if row[i] == "NULL":
                row[i] = None
            elif i == 6 or i == 7:  
                row[i] = reformat_date(row[i])
        cur.execute(
            "INSERT INTO Orders (OrderID, CustomerID, SalespersonPersonID, PickedByPersonID, ContactPersonID, BackorderOrderID, OrderDate, ExpectedDeliveryDate, CustomerPurchaseOrderNumber, IsUndersupplyBackordered, PickingCompletedWhen) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        )



with open('Sales/Sales.CustomerCategories.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 2):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO CustomerCategories (CustomerCategoryID, CustomerCategoryName) VALUES (%s, %s)",
            (row[0], row[1])
        )

with open('Sales/Sales.OrderLines.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 10):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO OrderLines (OrderLineID, OrderID, StockItemID, Description, PackageTypeID, Quantity, UnitPrice, TaxRate, PickedQuantity, PickingCompletedWhen) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        )

with open('Sales/Sales.BuyingGroups.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 2):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO BuyingGroups (BuyingGroupID, BuyingGroupName) VALUES (%s, %s)",
            (row[0], row[1])
        )

with open('Sales/Sales.Invoices.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 16):
            if row[i] == "NULL":
                row[i] = None
            elif i == 9: 
                row[i] = reformat_date(row[i])
        cur.execute(
            "INSERT INTO Invoices (InvoiceID, CustomerID, BillToCustomerID, OrderID, DeliveryMethodID, ContactPersonID, AccountsPersonID, SalespersonPersonID, PackedByPersonID, InvoiceDate, CustomerPurchaseOrderNumber, DeliveryInstructions, TotalDryItems, TotalChillerItems, ConfirmedDeliveryTime, ConfirmedReceivedBy) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
        )

with open('Sales/Sales.InvoiceLines.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 11):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO InvoiceLines (InvoiceLineID, InvoiceID, StockItemID, Description, PackageTypeID, Quantity, UnitPrice, TaxRate, TaxAmount, LineProfit, ExtendedPrice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        )

with open('Sales/Sales.CustomerTransactions.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 12):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO CustomerTransactions (CustomerTransactionID, CustomerID, TransactionTypeID, InvoiceID, PaymentMethodID, TransactionDate, AmountExcludingTax, TaxAmount, TransactionAmount, OutstandingBalance, FinalizationDate, IsFinalized) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
        )

with open('Sales/Sales.Customers.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0, 20):
            if row[i] == "NULL":
                row[i] = None
            elif i == 10: 
                row[i] = reformat_date(row[i])
        cur.execute(
            "INSERT INTO Customers (CustomerID, CustomerName, BillToCustomerID, CustomerCategoryID, BuyingGroupID, PrimaryContactPersonID, AlternateContactPersonID, DeliveryMethodID, DeliveryCityID, CreditLimit, AccountOpenedDate, StandardDiscountPercentage, IsStatementSent, IsOnCreditHold, PaymentDays, PhoneNumber, WebsiteURL, DeliveryAddressLine, DeliveryLocationLat, DeliveryLocationLong) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19])
        )



conn.commit()
cur.close()
conn.close()

