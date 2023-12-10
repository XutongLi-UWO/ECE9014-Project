DROP TABLE IF EXISTS ProductDimension CASCADE;

CREATE TABLE ProductDimension (
    Product_Key INT PRIMARY KEY,
    Product_Type INT,
    Product_Name VARCHAR(255),
    Product_Type_Name VARCHAR(255)
);

INSERT INTO ProductDimension (Product_Key, Product_Type, Product_Name, Product_Type_Name)
SELECT
    si.stockitemid,
    sg.stockgroupid,
    si.stockitemname,
    sg.stockgroupname
FROM (
    SELECT
        s.stockitemid,
        s.stockgroupid,
        ROW_NUMBER() OVER (PARTITION BY s.stockitemid ORDER BY RANDOM()) AS rn
    FROM
        stockitemstockgroups s
) AS sub
JOIN stockitems si ON si.stockitemid = sub.stockitemid
JOIN stockgroups sg ON sg.stockgroupid = sub.stockgroupid
WHERE sub.rn = 1;
