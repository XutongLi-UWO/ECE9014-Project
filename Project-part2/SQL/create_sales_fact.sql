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