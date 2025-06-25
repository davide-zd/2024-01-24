from database.DB_connect import DBConnect
from model.prodotto import Prodotto


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getMetodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select gm.Order_method_type as metodo
                    from go_methods gm 
                    order by metodo"""
        cursor.execute(query)

        for row in cursor:
            result.append(row["metodo"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct year(gds.`Date`) as anno
                    from go_daily_sales gds"""
        cursor.execute(query)

        for row in cursor:
            result.append(row["anno"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes(anno, metodo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select gp.Product_number id, gp.Product nome, (gds.Unit_sale_price * gds.Quantity) * COUNT(gp.Product_number) as p_vendita_tot
                    from go_products gp, go_daily_sales gds, go_methods gm 
                    where gp.Product_number = gds.Product_number
                        and year(gds.`Date`) = %s
                        and gm.Order_method_code = gds.Order_method_code
                        and gm.Order_method_type = %s
                    group by id"""
        cursor.execute(query, (anno, metodo))

        for row in cursor:
            result.append(Prodotto(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(anno, metodo, numeroS):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t1.id1 nodo1, t2.id2 nodo2
                    from 
                    (select gp.Product_number id1, gp.Product nome1, sum(gds.Unit_sale_price*gds.Quantity) as p_vendita_tot1
                    from go_products gp, go_daily_sales gds, go_methods gm 
                    where gp.Product_number = gds.Product_number
                        and year(gds.`Date`) = %s
                        and gm.Order_method_code = gds.Order_method_code
                        and gm.Order_method_type = %s
                    group by id1) t1, 
                    (select gp.Product_number id2, gp.Product nome2, sum(gds.Unit_sale_price*gds.Quantity) as p_vendita_tot2
                    from go_products gp, go_daily_sales gds, go_methods gm 
                    where gp.Product_number = gds.Product_number
                        and year(gds.`Date`) = %s
                        and gm.Order_method_code = gds.Order_method_code
                        and gm.Order_method_type = %s
                    group by id2) t2
                    where t1.id1 != t2.id2
                        and (t2.p_vendita_tot2 - t1.p_vendita_tot1)/t1.p_vendita_tot1 > %s"""
        cursor.execute(query, (anno, metodo, anno, metodo, numeroS))

        for row in cursor:
            result.append((row["nodo1"], row["nodo2"]))
        cursor.close()
        conn.close()
        return result

