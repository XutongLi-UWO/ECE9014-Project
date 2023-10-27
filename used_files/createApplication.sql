DROP TABLE IF EXISTS TransactionTypes CASCADE;
DROP TABLE IF EXISTS DeliveryMethods CASCADE;
DROP TABLE IF EXISTS People CASCADE;
DROP TABLE IF EXISTS Cities CASCADE;
DROP TABLE IF EXISTS StateProvinces CASCADE;
DROP TABLE IF EXISTS Countries CASCADE;
DROP TABLE IF EXISTS PaymentMethods CASCADE;


-- Applications Tables

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
    SearchName VARCHAR(255),
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
