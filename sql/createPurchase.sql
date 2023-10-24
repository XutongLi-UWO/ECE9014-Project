DROP TABLE IF EXISTS PurchaseOrderLines CASCADE;
DROP TABLE IF EXISTS PurchaseOrders CASCADE;
DROP TABLE IF EXISTS SupplierCategories CASCADE;
DROP TABLE IF EXISTS Suppliers CASCADE;
DROP TABLE IF EXISTS SupplierTransactions CASCADE;


CREATE TABLE PurchaseOrderLines (
    PurchaseOrderLineID INT PRIMARY KEY,
    PurchaseOrderID INT,
    StockItemID INT,
    OrderedOuters INT,
    Description VARCHAR(255),
    ReceivedOuters INT,
    PackageTypeID INT,
    ExpectedUnitPricePerOuter DECIMAL(10, 2),
    LastReceiptDate DATE,
    IsOrderLineFinalized BOOLEAN
    -- FOREIGN KEY (PurchaseOrderID) REFERENCES PurchaseOrders(PurchaseOrderID),
    -- FOREIGN KEY (PackageTypeID) REFERENCES PurchaseOrders(PurchaseOrderID),
    -- FOREIGN KEY (PurchaseOrderID) REFERENCES PurchaseOrders(PurchaseOrderID)
);


CREATE TABLE PurchaseOrders (
    PurchaseOrderID INT PRIMARY KEY,
    SupplierID INT,
    OrderDate DATE,
    DeliveryMethodID INT,
    ContactPersonID INT,
    ExpectedDeliveryDate DATE,
    SupplierReference VARCHAR(255),
    IsOrderFinalized BOOLEAN
);


CREATE TABLE SupplierCategories (
    SupplierCategoryID INT PRIMARY KEY,
    SupplierCategoryName VARCHAR(255)
);


CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY,
    SupplierName VARCHAR(255),
    SupplierCategoryID INT,
    PrimaryContactPersonID INT,
    AlternateContactPersonID INT,
    DeliveryMethodID INT,
    DeliveryCityID INT,
    PostalCityID INT,
    SupplierReference VARCHAR(255),
    PaymentDays INT,
    PhoneNumber VARCHAR(50),
    WebsiteURL VARCHAR(255),
    DeliveryAddressLine VARCHAR(255),
    DeliveryLocationLat VARCHAR(255),
    DeliveryLocationLong VARCHAR(255)
);


CREATE TABLE SupplierTransactions (
    SupplierTransactionID INT PRIMARY KEY,
    SupplierID INT,
    TransactionTypeID INT,
    PurchaseOrderID INT,
    PaymentMethodID INT,
    SupplierInvoiceNumber VARCHAR(255),
    TransactionDate DATE,
    AmountExcludingTax DECIMAL(10,2),
    TaxAmount DECIMAL(10,2),
    TransactionAmount DECIMAL(10,2),
    OutstandingBalance DECIMAL(10,2),
    FinalizationDate DATE,
    IsFinalized BOOLEAN
);
