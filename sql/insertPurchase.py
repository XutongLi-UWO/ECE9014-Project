import csv
import psycopg2


conn = psycopg2.connect(
    dbname="postgres",
    user="westernuniversity",
    password="",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

with open('Purchasing/Purchasing.PurchasingOrderLines.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        cur.execute(
            "INSERT INTO PurchasingOrderLines (PurchasingOrderLinesID, PurchaseOrderID, StockItemID, OrderedOuters, Description, ReceivedOuters, PackageTypeID, ExpectedUnitPricePerOuter, LastReceiptDate, IsOrderLineFinalized) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        )

conn.commit()
cur.close()
conn.close()

with open('Purchasing/Purchasing.PurchasingOrder.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        cur.execute(
            "INSERT INTO PurchasingOrder (PurchaseOrderID, SupplierID, OrderDate, DeliveryMethodID, ContactPersonID, ExpectedDeliveryDate, SupplierReference, IsOrderFinalized) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        )

conn.commit()
cur.close()
conn.close()

with open('Purchasing/Purchasing.SupplierCategories.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        cur.execute(
            "INSERT INTO SupplierCategories (SupplierCategoryID, SupplierCategoryName) VALUES (%s, %s)",
            (row[0], row[1])
        )

conn.commit()
cur.close()
conn.close()

with open('Purchasing/Purchasing.Suppliers.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        cur.execute(
            "INSERT INTO Suppliers (SupplierID, SupplierName, SupplierCategoryID, PrimaryContactPersonID, AlternateContactPersonID, DeliveryMethodID, DeliveryCityID, PostalCityID, SupplierReference, PaymentDays, PhoneNumber, WebsiteURL, DeliveryAddressLine, DeliveryLocationLat, DeliveryLocationLong) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])
        )

conn.commit()
cur.close()
conn.close()

with open('Purchasing/Purchasing.SupplierTransactions.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        cur.execute(
            "INSERT INTO SupplierTransactions (SupplierTransactionID, SupplierID, TransactionTypeID, PurchaseOrderID, PaymentMethodID, SupplierInvoiceNumber, TransactionDate, AmountExcludingTax, TaxAmount, TransactionAmount, OutstandingBalance, FinalizationDate, IsFinalized) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
        )
conn.commit()
cur.close()
conn.close()