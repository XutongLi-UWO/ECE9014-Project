DROP TABLE IF EXISTS Colors CASCADE;
DROP TABLE IF EXISTS PackageTypes CASCADE;
DROP TABLE IF EXISTS StockGroups CASCADE;
DROP TABLE IF EXISTS StockItemHoldings CASCADE;
DROP TABLE IF EXISTS StockItems CASCADE;
DROP TABLE IF EXISTS StockItemStockGroups CASCADE;
DROP TABLE IF EXISTS StockItemTransactions CASCADE;



CREATE TABLE Colors (
    ColorID INT PRIMARY KEY,
    ColorName VARCHAR(255)
);


CREATE TABLE PackageTypes (
    PackageTypeID INT PRIMARY KEY,
    PackageTypeName VARCHAR(255)
);


CREATE TABLE StockGroups (
    StockGroupID INT PRIMARY KEY,
    StockGroupName VARCHAR(255)
);


CREATE TABLE StockItemHoldings (
    StockItemID INT PRIMARY KEY,
    QuantityOnHand INT,
    BinLocation VARCHAR(255),
    LastStocktakeQuantity INT,
    LastCostPrice DECIMAL(10, 2),
    ReorderLevel INT,
    TargetStockLevel INT
);


CREATE TABLE StockItems (
    StockItemID INT PRIMARY KEY,
    StockItemName VARCHAR(255),
    SupplierID INT,
    ColorID INT,
    UnitPackageID INT,
    OuterPackageID INT,
    Brand VARCHAR(255),
    Size VARCHAR(255),
    LeadTimeDays INT,
    QuantityPerOuter INT,
    IsChillerStock BOOLEAN,
    Barcode VARCHAR(255),
    TaxRate DECIMAL(10, 3),
    UnitPrice DECIMAL(10, 2),
    RecommendedRetailPrice DECIMAL(10, 2),
    TypicalWeightPerUnit DECIMAL(10, 3)
);


CREATE TABLE StockItemStockGroups (
    StockItemStockGroupID INT PRIMARY KEY,
    StockItemID INT,
    StockGroupID INT
);


CREATE TABLE StockItemTransactions (
    StockItemTransactionID INT PRIMARY KEY,
    StockItemID INT,
    TransactionTypeID INT,
    CustomerID INT,
    InvoiceID INT,
    SupplierID INT,
    PurchaseOrderID INT,
    TransactionOccurredWhen TIMESTAMP,
    Quantity DECIMAL(10,3)
);
