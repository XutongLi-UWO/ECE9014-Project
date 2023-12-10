INSERT INTO TimeDimension (time_key, date, month,quarter, year)
SELECT
    DISTINCT TO_CHAR(invoicedate, 'YYYYMMDD')::INTEGER,
	invoicedate,
	EXTRACT(MONTH FROM invoicedate)::INTEGER,
	EXTRACT(QUARTER FROM invoicedate)::INTEGER,
    EXTRACT(YEAR FROM invoicedate)::INTEGER
FROM
    invoices


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
