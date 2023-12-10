DROP TABLE IF EXISTS TimeDimension CASCADE;
DROP TABLE IF EXISTS CustomerDimension CASCADE;
DROP TABLE IF EXISTS ProductDimension CASCADE;

CREATE TABLE TimeDimension (
    Time_Key INT PRIMARY KEY,
    Date DATE,
    Month INT,
    Quarter INT,
    Year INT
);

CREATE TABLE CustomerDimension (
    Customer_Key INT PRIMARY KEY,
    Customer_Name VARCHAR(255),
    Customer_Type INT,
    Customer_Type_Name VARCHAR(255)
);

CREATE TABLE ProductDimension (
    Product_Key INT PRIMARY KEY,
    Product_Type INT,
    Product_Name VARCHAR(255),
    Product_Type_Name VARCHAR(255)
);