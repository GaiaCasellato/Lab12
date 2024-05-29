from database.DB_connect import DBConnect
from model.Retailer import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct gr.Country 
                    from go_sales.go_retailers gr """

        cursor.execute(query)

        for row in cursor:
            result.append(row["Country"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllretailersCountry(country):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct *
                    from go_sales.go_retailers gr 
                    where gr.Country = %s """

        cursor.execute(query,(country,))

        for row in cursor:
            result.append(Retailer(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getProductsInCommon(r1,r2,year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT COUNT(DISTINCT s1.Product_number) as N 
                    FROM go_sales.go_daily_sales s1, go_sales.go_daily_sales s2
                    WHERE year(s1.Date) = year (s2.Date)
                    AND s1.Product_Number = s2.Product_Number 
                    AND s1.Retailer_code = %s
                    AND s2.Retailer_code = %s
                    AND YEAR(s1.Date) = %s """

        cursor.execute(query, (r1.Retailer_code, r2.Retailer_code,str(year)))

        for row in cursor:
            result.append(row["N"]) #appendo il peso

        cursor.close()
        conn.close()
        return result
