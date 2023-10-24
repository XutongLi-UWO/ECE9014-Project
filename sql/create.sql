DROP TABLE IF EXISTS TransactionTypes CASCADE;
DROP TABLE IF EXISTS DeliveryMethods CASCADE;
DROP TABLE IF EXISTS People CASCADE;

DROP TABLE IF EXISTS Cities;


-- Applications Tables

CREATE TABLE TransactionTypes (
    TransactionTypeID INT PRIMARY KEY,
    TransactionTypeName VARCHAR(255) NOT NULL
);

CREATE TABLE DeliveryMethods (
    DeliveryMethodID INT PRIMARY KEY,
    DeliveryMethodName VARCHAR(255) NOT NULL
);

CREATE TABLE People (
    PersonID INT PRIMARY KEY,
    FullName VARCHAR(255) NOT NULL,
    PreferredName VARCHAR(255),
    SearchName VARCHAR(255) NOT NULL,
    IsEmployee BOOLEAN NOT NULL
);


CREATE TABLE Cities (
    CityID INT PRIMARY KEY,
    StateProvinceID INT NOT NULL, -- 这里假设这个字段是整数，您可能需要根据实际情况调整
    CityName VARCHAR(255) NOT NULL,
    Latitude DECIMAL(9,6), -- 通常，纬度使用小数表示，这里我们假设最大精度为6位小数
    Longitude DECIMAL(9,6), -- 同上
    LatestRecordedPopulation INT
    -- 可以添加其他外键约束，如与StateProvince表的关联
);

DROP TABLE IF EXISTS Countries;
CREATE TABLE Countries (
    CountryID INT PRIMARY KEY,
    CountryName VARCHAR(255) NOT NULL,
    FormalName VARCHAR(255) NOT NULL,
    LatestRecordedPopulation INT,
    Continent VARCHAR(255),
    Region VARCHAR(255),
    Subregion VARCHAR(255)
);

DROP TABLE IF EXISTS PaymentMethods;
DROP TABLE IF EXISTS StateProvinces;
CREATE TABLE PaymentMethods (
    PaymentMethodID INT PRIMARY KEY,
    PaymentMethodName VARCHAR(255) NOT NULL
);


CREATE TABLE StateProvinces (
    StateProvinceID INT PRIMARY KEY,
    CountryID INT NOT NULL, 
    StateProvinceName VARCHAR(255) NOT NULL,
    StateProvinceCode VARCHAR(255),
    SalesTerritory VARCHAR(255),
    LatestRecordedPopulation INT,
    -- FOREIGN KEY (CountryID) REFERENCES Countries(CountryID) -- 这是一个外键约束，与Countries表相关联
);


