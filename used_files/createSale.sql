DROP TABLE IF EXISTS BuyingGroups CASCADE;
DROP TABLE IF EXISTS CustomerCategories CASCADE;
DROP TABLE IF EXISTS Customers CASCADE;
DROP TABLE IF EXISTS CustomerTransactions CASCADE;
DROP TABLE IF EXISTS InvoiceLines CASCADE;
DROP TABLE IF EXISTS Invoices CASCADE;
DROP TABLE IF EXISTS OrderLines CASCADE;
DROP TABLE IF EXISTS Orders CASCADE;

CREATE TABLE BuyingGroups (
    BuyingGroupID INT PRIMARY KEY,
    BuyingGroupName VARCHAR(255) NOT NULL
);


CREATE TABLE CustomerCategories (
    CustomerCategoryID INT PRIMARY KEY,
    CustomerCategoryName VARCHAR(255) NOT NULL
);


CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    BillToCustomerID INT,
    CustomerCategoryID INT,
    BuyingGroupID INT,
    PrimaryContactPersonID INT,
    AlternateContactPersonID INT,
    DeliveryMethodID INT,
    DeliveryCityID INT,
    CreditLimit DECIMAL(10,2),
    AccountOpenedDate DATE,
    StandardDiscountPercentage DECIMAL(10,3),
    IsStatementSent BOOLEAN,
    IsOnCreditHold BOOLEAN,
    PaymentDays INT,
    PhoneNumber VARCHAR(255),
    WebsiteURL VARCHAR(255),
    DeliveryAddressLine VARCHAR(255),
    DeliveryLocationLat VARCHAR(255),
    DeliveryLocationLong VARCHAR(255)
);


CREATE TABLE CustomerTransactions (
    CustomerTransactionID INT PRIMARY KEY,
    CustomerID INT,
    TransactionTypeID INT,
    InvoiceID INT,
    PaymentMethodID INT,
    TransactionDate DATE,
    AmountExcludingTax DECIMAL(10, 2),
    TaxAmount DECIMAL(10, 2),
    TransactionAmount DECIMAL(10, 2),
    OutstandingBalance DECIMAL(10, 2),
    FinalizationDate DATE,
    IsFinalized BOOLEAN
);


CREATE TABLE InvoiceLines (
    InvoiceLineID INT PRIMARY KEY,
    InvoiceID INT,
    StockItemID INT,
    Description VARCHAR(255),
    PackageTypeID INT,
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    TaxRate DECIMAL(10, 3),
    TaxAmount DECIMAL(10, 2),
    LineProfit DECIMAL(10, 2),
    ExtendedPrice DECIMAL(10, 2)
);


CREATE TABLE Invoices (
    InvoiceID INT PRIMARY KEY,
    CustomerID INT,
    BillToCustomerID INT,
    OrderID INT,
    DeliveryMethodID INT,
    ContactPersonID INT,
    AccountsPersonID INT,
    SalespersonPersonID INT,
    PackedByPersonID INT,
    InvoiceDate DATE,
    CustomerPurchaseOrderNumber INT,
    DeliveryInstructions TEXT,
    TotalDryItems INT,
    TotalChillerItems INT,
    ConfirmedDeliveryTime TIMESTAMP,
    ConfirmedReceivedBy TEXT
);


CREATE TABLE OrderLines (
    OrderLineID INT PRIMARY KEY,
    OrderID INT,
    StockItemID INT,
    Description TEXT,
    PackageTypeID INT,
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    TaxRate DECIMAL(10, 3),
    PickedQuantity INT,
    PickingCompletedWhen TIMESTAMP
);


CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    SalespersonPersonID INT,
    PickedByPersonID INT,
    ContactPersonID INT,
    BackorderOrderID INT,
    OrderDate DATE,
    ExpectedDeliveryDate DATE,
    CustomerPurchaseOrderNumber INT,
    IsUndersupplyBackordered BOOLEAN,
    PickingCompletedWhen TIMESTAMP
);
