DROP TABLE IF EXISTS SalesFacts CASCADE;

CREATE TABLE SalesFacts (
    Time_Key INT,
    Customer_Key INT,
    Product_Key INT,
    Sale_Amount DECIMAL(10, 2),
    Purchase_Cost DECIMAL(10, 2),
    Profit DECIMAL(10, 2),
    Order_Quantity INT,
    FOREIGN KEY (Time_Key) REFERENCES TimeDimension (Time_Key),
    FOREIGN KEY (Customer_Key) REFERENCES CustomerDimension (Customer_Key),
    FOREIGN KEY (Product_Key) REFERENCES ProductDimension (Product_Key)
);
INSERT INTO SalesFacts (Time_Key, Customer_Key, Product_Key, Sale_Amount, Purchase_Cost, Order_Quantity, Profit)
SELECT
    (EXTRACT(YEAR FROM o.OrderDateConverted) * 10000) +
    (EXTRACT(MONTH FROM o.OrderDateConverted) * 100) +
    EXTRACT(DAY FROM o.OrderDateConverted) AS Time_Key,
    o.customerid AS Customer_Key,
    ol.stockitemid AS Product_Key,
    COALESCE(SUM(ct.amountexcludingtax), 0) AS Sale_Amount,
    COALESCE(SUM(st.amountexcludingtax), 0) * 0.04 AS Purchase_Cost,
    COALESCE(SUM(ol.quantity), 0) AS Order_Quantity,
    (COALESCE(SUM(ct.amountexcludingtax), 0) - (COALESCE(SUM(st.amountexcludingtax), 0) * 0.04)) AS Profit  FROM
    (SELECT
        orderid,
        customerid,
        CAST(OrderDate AS DATE) AS OrderDateConverted
     FROM orders) o
LEFT JOIN
    orderlines ol ON o.orderid = ol.orderid
LEFT JOIN
    customertransactions ct ON o.customerid = ct.customerid AND o.OrderDateConverted = ct.transactiondate
LEFT JOIN
    suppliertransactions st ON ol.stockitemid = st.purchaseorderid
JOIN
    TimeDimension td ON td.date = o.OrderDateConverted
JOIN
    CustomerDimension cd ON o.customerid = cd.Customer_Key
LEFT JOIN
    ProductDimension pd ON ol.stockitemid = pd.Product_Key
WHERE
    o.OrderDateConverted BETWEEN '2013-01-01'::date AND '2016-12-31'::date
GROUP BY
    (EXTRACT(YEAR FROM o.OrderDateConverted) * 10000) + 
    (EXTRACT(MONTH FROM o.OrderDateConverted) * 100) +
    EXTRACT(DAY FROM o.OrderDateConverted),
    o.customerid,
    ol.stockitemid;
