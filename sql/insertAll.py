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




def reformat_date(date_str):
    date_parts = date_str.split("/")
    return f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"

with open('Application/Application.TransactionTypes.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        cur.execute(
            "INSERT INTO TransactionTypes (TransactionTypeID, TransactionTypeName) VALUES (%s, %s)",
            (row[0], row[1])
        )



with open('Application/Application.DeliveryMethods.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        cur.execute(
            "INSERT INTO DeliveryMethods (DeliveryMethodID, DeliveryMethodName) VALUES (%s, %s)",
            (row[0], row[1])
        )



with open('Application/Application.People.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        cur.execute(
            "INSERT INTO People (PersonID, FullName, PreferredName, SearchName, IsEmployee, IsSalesperson) VALUES (%s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5])
        )




with open('Application/Application.Countries.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        cur.execute(
            "INSERT INTO Countries (CountryID, CountryName, FormalName, LatestRecordedPopulation, Continent, Region, Subregion) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        )



with open('Application/Application.PaymentMethods.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        cur.execute(
            "INSERT INTO PaymentMethods (PaymentMethodID, PaymentMethodName) VALUES (%s, %s)",
            (row[0], row[1])
        )




with open('Application/Application.StateProvinces.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        cur.execute(
            "INSERT INTO StateProvinces (StateProvinceID, StateProvinceCode, StateProvinceName, CountryID, SalesTerritory, LatestRecordedPopulation) VALUES (%s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5])
        )


with open('Application/Application.Cities.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        if row[5] == "NULL":
            row[5] = None
        cur.execute(
            "INSERT INTO Cities (CityID, CityName, StateProvinceID, Latitude, Longitude, LatestRecordedPopulation) VALUES (%s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5])
        )



with open('Purchasing/Purchasing.SupplierCategories.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        cur.execute(
            "INSERT INTO SupplierCategories (SupplierCategoryID, SupplierCategoryName) VALUES (%s, %s)",
            (row[0], row[1])
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




with open('Purchasing/Purchasing.Suppliers.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0,15):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO Suppliers (SupplierID, SupplierName, SupplierCategoryID, PrimaryContactPersonID, AlternateContactPersonID, DeliveryMethodID, DeliveryCityID, PostalCityID, SupplierReference, PaymentDays, PhoneNumber, WebsiteURL, DeliveryAddressLine, DeliveryLocationLat, DeliveryLocationLong) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])
        )





with open('Purchasing/Purchasing.PurchaseOrders.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        cur.execute(
            "INSERT INTO PurchaseOrders (PurchaseOrderID, SupplierID, OrderDate, DeliveryMethodID, ContactPersonID, ExpectedDeliveryDate, SupplierReference, IsOrderFinalized) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
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




with open('Purchasing/Purchasing.PurchaseOrderLines.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0,10):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO PurchaseOrderLines (PurchaseOrderLineID, PurchaseOrderID, StockItemID, OrderedOuters, Description, ReceivedOuters, PackageTypeID, ExpectedUnitPricePerOuter, LastReceiptDate, IsOrderLineFinalized) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        )




with open('Purchasing/Purchasing.SupplierTransactions.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        for i in range(0,13):
            if row[i] == "NULL":
                row[i] = None
        cur.execute(
            "INSERT INTO SupplierTransactions (SupplierTransactionID, SupplierID, TransactionTypeID, PurchaseOrderID, PaymentMethodID, SupplierInvoiceNumber, TransactionDate, AmountExcludingTax, TaxAmount, TransactionAmount, OutstandingBalance, FinalizationDate, IsFinalized) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
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




conn.commit()
cur.close()
conn.close()

