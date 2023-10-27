DROP TABLE IF EXISTS TransactionTypes CASCADE;
DROP TABLE IF EXISTS DeliveryMethods CASCADE;
DROP TABLE IF EXISTS People CASCADE;
DROP TABLE IF EXISTS Cities CASCADE;
DROP TABLE IF EXISTS StateProvinces CASCADE;
DROP TABLE IF EXISTS Countries CASCADE;
DROP TABLE IF EXISTS PaymentMethods CASCADE;


DROP TABLE IF EXISTS PurchaseOrderLines CASCADE;
DROP TABLE IF EXISTS PurchaseOrders CASCADE;
DROP TABLE IF EXISTS SupplierCategories CASCADE;
DROP TABLE IF EXISTS Suppliers CASCADE;
DROP TABLE IF EXISTS SupplierTransactions CASCADE;


DROP TABLE IF EXISTS BuyingGroups CASCADE;
DROP TABLE IF EXISTS CustomerCategories CASCADE;
DROP TABLE IF EXISTS Customers CASCADE;
DROP TABLE IF EXISTS CustomerTransactions CASCADE;
DROP TABLE IF EXISTS InvoiceLines CASCADE;
DROP TABLE IF EXISTS Invoices CASCADE;
DROP TABLE IF EXISTS OrderLines CASCADE;
DROP TABLE IF EXISTS Orders CASCADE;



DROP TABLE IF EXISTS Colors CASCADE;
DROP TABLE IF EXISTS PackageTypes CASCADE;
DROP TABLE IF EXISTS StockGroups CASCADE;
DROP TABLE IF EXISTS StockItemHoldings CASCADE;
DROP TABLE IF EXISTS StockItems CASCADE;
DROP TABLE IF EXISTS StockItemStockGroups CASCADE;
DROP TABLE IF EXISTS StockItemTransactions CASCADE;



CREATE TABLE TransactionTypes (
    TransactionTypeID INT PRIMARY KEY,
    TransactionTypeName VARCHAR(255)
);

CREATE TABLE DeliveryMethods (
    DeliveryMethodID INT PRIMARY KEY,
    DeliveryMethodName VARCHAR(255)
);

CREATE TABLE People (
    PersonID INT PRIMARY KEY,
    FullName VARCHAR(255),
    PreferredName VARCHAR(255),
    IsEmployee BOOLEAN,
    IsSalesperson BOOLEAN
);



CREATE TABLE Countries (
    CountryID INT PRIMARY KEY,
    CountryName VARCHAR(255),
    FormalName VARCHAR(255),
    LatestRecordedPopulation INT,
    Continent VARCHAR(255),
    Region VARCHAR(255),
    Subregion VARCHAR(255)
);


CREATE TABLE PaymentMethods (
    PaymentMethodID INT PRIMARY KEY,
    PaymentMethodName VARCHAR(255)
);




CREATE TABLE StateProvinces (
    StateProvinceID INT PRIMARY KEY,
    StateProvinceCode VARCHAR(255),
    StateProvinceName VARCHAR(255),
    CountryID INT, 
    SalesTerritory VARCHAR(255),
    LatestRecordedPopulation INT,
    FOREIGN KEY (CountryID) REFERENCES Countries(CountryID) 
);


CREATE TABLE Cities (
    CityID INT PRIMARY KEY,
    CityName VARCHAR(255),
    StateProvinceID INT,
    Latitude VARCHAR(255),
    Longitude VARCHAR(255),
    LatestRecordedPopulation INT,
    FOREIGN KEY (StateProvinceID) REFERENCES StateProvinces(StateProvinceID)
);

-- ======


CREATE TABLE SupplierCategories (
    SupplierCategoryID INT PRIMARY KEY,
    SupplierCategoryName VARCHAR(255)
);

CREATE TABLE BuyingGroups (
    BuyingGroupID INT PRIMARY KEY,
    BuyingGroupName VARCHAR(255) NOT NULL
);


CREATE TABLE CustomerCategories (
    CustomerCategoryID INT PRIMARY KEY,
    CustomerCategoryName VARCHAR(255) NOT NULL
);



CREATE TABLE StockGroups (
    StockGroupID INT PRIMARY KEY,
    StockGroupName VARCHAR(255)
);


CREATE TABLE Colors (
    ColorID INT PRIMARY KEY,
    ColorName VARCHAR(255)
);


CREATE TABLE PackageTypes (
    PackageTypeID INT PRIMARY KEY,
    PackageTypeName VARCHAR(255)
);




CREATE TABLE StockItemHoldings (
    StockItemID INT PRIMARY KEY,
    QuantityOnHand INT,
    BinLocation VARCHAR(255),
    LastStocktakeQuantity INT,
    LastCostPrice DECIMAL(10, 2),
    -- ReorderLevel INT,
    TargetStockLevel INT
);


-- ======



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
    -- DeliveryLocationLat VARCHAR(255),
    -- DeliveryLocationLong VARCHAR(255),
    FOREIGN KEY (SupplierCategoryID) REFERENCES SupplierCategories(SupplierCategoryID),
    FOREIGN KEY (PrimaryContactPersonID) REFERENCES People(PersonID),
    FOREIGN KEY (AlternateContactPersonID) REFERENCES People(PersonID),
    FOREIGN KEY (DeliveryMethodID) REFERENCES DeliveryMethods(DeliveryMethodID),
    FOREIGN KEY (DeliveryCityID) REFERENCES Cities(CityID),
    FOREIGN KEY (PostalCityID) REFERENCES Cities(CityID)
);

CREATE TABLE PurchaseOrders (
    PurchaseOrderID INT PRIMARY KEY,
    SupplierID INT,
    OrderDate DATE,
    DeliveryMethodID INT,
    ContactPersonID INT,
    -- ExpectedDeliveryDate DATE,
    SupplierReference VARCHAR(255),
    IsOrderFinalized BOOLEAN,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
    FOREIGN KEY (DeliveryMethodID) REFERENCES DeliveryMethods(DeliveryMethodID),
    FOREIGN KEY (ContactPersonID) REFERENCES People(PersonID)
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
    -- RecommendedRetailPrice DECIMAL(10, 2),
    TypicalWeightPerUnit DECIMAL(10, 3),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
    FOREIGN KEY (ColorID) REFERENCES Colors(ColorID),
    FOREIGN KEY (UnitPackageID) REFERENCES PackageTypes(PackageTypeID),
    FOREIGN KEY (OuterPackageID) REFERENCES PackageTypes(PackageTypeID)
);



CREATE TABLE PurchaseOrderLines (
    PurchaseOrderLineID INT PRIMARY KEY,
    PurchaseOrderID INT,
    StockItemID INT,
    OrderedOuters INT,
    Description VARCHAR(255),
    ReceivedOuters INT,
    PackageTypeID INT,
    -- ExpectedUnitPricePerOuter DECIMAL(10, 2),
    LastReceiptDate DATE,
    IsOrderLineFinalized BOOLEAN,
    FOREIGN KEY (PurchaseOrderID) REFERENCES PurchaseOrders(PurchaseOrderID),
    FOREIGN KEY (PackageTypeID) REFERENCES PackageTypes(PackageTypeID),
    FOREIGN KEY (StockItemID) REFERENCES StockItems(StockItemID)
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
    -- TaxAmount DECIMAL(10,2),
    -- TransactionAmount DECIMAL(10,2),
    -- OutstandingBalance DECIMAL(10,2),
    FinalizationDate DATE,
    IsFinalized BOOLEAN,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
    FOREIGN KEY (TransactionTypeID) REFERENCES TransactionTypes(TransactionTypeID),
    FOREIGN KEY (PurchaseOrderID) REFERENCES PurchaseOrders(PurchaseOrderID),
    FOREIGN KEY (PaymentMethodID) REFERENCES PaymentMethods(PaymentMethodID)
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
    DeliveryLocationLong VARCHAR(255),
    FOREIGN KEY (DeliveryMethodID) REFERENCES DeliveryMethods(DeliveryMethodID),
    FOREIGN KEY (CustomerCategoryID) REFERENCES CustomerCategories(CustomerCategoryID),
    FOREIGN KEY (BuyingGroupID) REFERENCES BuyingGroups(BuyingGroupID),
    FOREIGN KEY (DeliveryCityID) REFERENCES Cities(CityID),
    FOREIGN KEY (PrimaryContactPersonID) REFERENCES People(PersonID),
    FOREIGN KEY (AlternateContactPersonID) REFERENCES People(PersonID),
    FOREIGN KEY (BillToCustomerID) REFERENCES Customers(CustomerID)
);



CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    SalespersonPersonID INT,
    PickedByPersonID INT,
    ContactPersonID INT,
    BackorderOrderID INT,
    OrderDate DATE,
    -- ExpectedDeliveryDate DATE,
    CustomerPurchaseOrderNumber INT,
    IsUndersupplyBackordered BOOLEAN,
    PickingCompletedWhen TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (SalespersonPersonID) REFERENCES People(PersonID),
    FOREIGN KEY (PickedByPersonID) REFERENCES People(PersonID)
    -- FOREIGN KEY (BackorderOrderID) REFERENCES Orders(OrderID)
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
    ConfirmedReceivedBy TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (DeliveryMethodID) REFERENCES DeliveryMethods(DeliveryMethodID),
    FOREIGN KEY (SalespersonPersonID) REFERENCES People(PersonID),
    FOREIGN KEY (PackedByPersonID) REFERENCES People(PersonID),
    FOREIGN KEY (ContactPersonID) REFERENCES People(PersonID),
    FOREIGN KEY (BillToCustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (AccountsPersonID) REFERENCES People(PersonID)
);


CREATE TABLE CustomerTransactions (
    CustomerTransactionID INT PRIMARY KEY,
    CustomerID INT,
    TransactionTypeID INT,
    InvoiceID INT,
    PaymentMethodID INT,
    TransactionDate DATE,
    AmountExcludingTax DECIMAL(10, 2),
    -- TaxAmount DECIMAL(10, 2),
    -- TransactionAmount DECIMAL(10, 2),
    -- OutstandingBalance DECIMAL(10, 2),
    FinalizationDate DATE,
    IsFinalized BOOLEAN,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (TransactionTypeID) REFERENCES TransactionTypes(TransactionTypeID),
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID),
    FOREIGN KEY (PaymentMethodID) REFERENCES PaymentMethods(PaymentMethodID)
);



CREATE TABLE InvoiceLines (
    InvoiceLineID INT PRIMARY KEY,
    InvoiceID INT,
    StockItemID INT,
    Description VARCHAR(255),
    PackageTypeID INT,
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    -- TaxRate DECIMAL(10, 3),
    -- TaxAmount DECIMAL(10, 2),
    LineProfit DECIMAL(10, 2),
    ExtendedPrice DECIMAL(10, 2),
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID),
    FOREIGN KEY (StockItemID) REFERENCES StockItems(StockItemID),
    FOREIGN KEY (PackageTypeID) REFERENCES PackageTypes(PackageTypeID)
);




CREATE TABLE OrderLines (
    OrderLineID INT PRIMARY KEY,
    OrderID INT,
    StockItemID INT,
    Description TEXT,
    PackageTypeID INT,
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    -- TaxRate DECIMAL(10, 3),
    PickedQuantity INT,
    -- PickingCompletedWhen TIMESTAMP,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (StockItemID) REFERENCES StockItemHoldings(StockItemID),
    FOREIGN KEY (PackageTypeID) REFERENCES PackageTypes(PackageTypeID)
);





CREATE TABLE StockItemStockGroups (
    StockItemStockGroupID INT PRIMARY KEY,
    StockItemID INT,
    StockGroupID INT,
    FOREIGN KEY (StockItemID) REFERENCES StockItemHoldings(StockItemID),
    FOREIGN KEY (StockGroupID) REFERENCES StockGroups(StockGroupID)
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
    Quantity DECIMAL(10,3),
    FOREIGN KEY (StockItemID) REFERENCES StockItemHoldings(StockItemID),
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
    FOREIGN KEY (PurchaseOrderID) REFERENCES PurchaseOrders(PurchaseOrderID),
    FOREIGN KEY (TransactionTypeID) REFERENCES TransactionTypes(TransactionTypeID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
