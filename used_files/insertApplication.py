import csv
import psycopg2


conn = psycopg2.connect(
    dbname="postgres",
    user="westernuniversity",
    password="",
    host="localhost",
    port="5432"
)
cur = conn.cursor()



with open('Application/Application.TransactionTypes.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        cur.execute(
            "INSERT INTO TransactionTypes (TransactionTypeID, TransactionTypeName) VALUES (%s, %s)",
            (row[0], row[1])
        )



with open('Application/Application.DeliveryMethods.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        cur.execute(
            "INSERT INTO DeliveryMethods (DeliveryMethodID, DeliveryMethodName) VALUES (%s, %s)",
            (row[0], row[1])
        )



with open('Application/Application.People.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        cur.execute(
            "INSERT INTO People (PersonID, FullName, PreferredName, SearchName, IsEmployee, IsSalesperson) VALUES (%s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5])
        )




with open('Application/Application.Countries.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        cur.execute(
            "INSERT INTO Countries (CountryID, CountryName, FormalName, LatestRecordedPopulation, Continent, Region, Subregion) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        )



with open('Application/Application.PaymentMethods.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        cur.execute(
            "INSERT INTO PaymentMethods (PaymentMethodID, PaymentMethodName) VALUES (%s, %s)",
            (row[0], row[1])
        )




with open('Application/Application.StateProvinces.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        cur.execute(
            "INSERT INTO StateProvinces (StateProvinceID, StateProvinceCode, StateProvinceName, CountryID, SalesTerritory, LatestRecordedPopulation) VALUES (%s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5])
        )


with open('Application/Application.Cities.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  
    next(reader)  
    for row in reader:
        if row[5] == "NULL":
            row[5] = None
        cur.execute(
            "INSERT INTO Cities (CityID, CityName, StateProvinceID, Latitude, Longitude, LatestRecordedPopulation) VALUES (%s, %s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4], row[5])
        )






conn.commit()
cur.close()
conn.close()
