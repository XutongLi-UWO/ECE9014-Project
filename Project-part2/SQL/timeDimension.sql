DROP TABLE IF EXISTS TimeDimension CASCADE;
CREATE TABLE TimeDimension (
    Time_Key INT PRIMARY KEY,
    Date DATE,
    Month INT,
    Quarter INT,
    Year INT
);

INSERT INTO TimeDimension (time_key, date, month,quarter, year)
SELECT
    DISTINCT TO_CHAR(invoicedate, 'YYYYMMDD')::INTEGER,
	invoicedate,
	EXTRACT(MONTH FROM invoicedate)::INTEGER,
	EXTRACT(QUARTER FROM invoicedate)::INTEGER,
    EXTRACT(YEAR FROM invoicedate)::INTEGER
FROM
    invoices

