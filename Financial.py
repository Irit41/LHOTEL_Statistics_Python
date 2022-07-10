from SQL_Connection import Connect_to_SQL_Server

cursor = Connect_to_SQL_Server()


def Rooms_Income():
    sum_total = 0
    for row in cursor.execute("Calu_Rooms_Income"):
        sum_total += row[0]
    return sum_total


def Purchase_Of_Goods_Expenses():
    sum_total = 0
    for row in cursor.execute("Expenses"):
        sum_total += row[0]
    return sum_total


def Products_Income():
    sum_total = 0
    for row in cursor.execute("Calu_Products_Income"):
        if row[2] != 0:
            percent = (row[1] * row[2]) / 100
            new_price = row[1] - percent
        else:
            new_price = row[1]
        sum_total += new_price * row[0]
    return sum_total




