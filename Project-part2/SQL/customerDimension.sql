DROP TABLE IF EXISTS CustomerDimension CASCADE;
CREATE TABLE CustomerDimension (
    Customer_Key INT PRIMARY KEY,
    Customer_Name VARCHAR(255),
    Customer_Type INT,
    Customer_Type_Name VARCHAR(255)
);

INSERT INTO CustomerDimension (Customer_Key, Customer_Name, Customer_Type, Customer_Type_Name)
SELECT
    c.customerid,
    c.customername,
    c.customercategoryid,
    cc.customercategoryname
FROM
    customers c
JOIN
    customercategories cc ON c.customercategoryid = cc.customercategoryid;
