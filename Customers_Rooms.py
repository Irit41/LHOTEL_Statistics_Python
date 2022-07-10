import math




from SQL_Connection import Connect_to_SQL_Server
from matplotlib import pyplot as plt
from collections import Counter, OrderedDict

cursor = Connect_to_SQL_Server()


def Month_with_the_most_reservation():
    dates = []
    for row in cursor.execute("SELECT dbo.Customers_Rooms.Bill_Number, dbo.Customers_Rooms.Entry_Date, "
                              "dbo.Rooms.Room_Type,(select count(Bill_Number) from Customers_Rooms where MONTH("
                              "Entry_Date) = MONTH(dbo.Customers_Rooms.Entry_Date)) as sfira FROM     "
                              "dbo.Customers_Rooms INNER JOIN dbo.Rooms ON dbo.Customers_Rooms.Room_Number = "
                              "dbo.Rooms.Room_Number GROUP BY dbo.Customers_Rooms.Bill_Number, "
                              "dbo.Customers_Rooms.Entry_Date, dbo.Rooms.Room_Type"):
        dates.append(row[1])
    print(dates)
    months = [date.month for date in dates]
    res = list(OrderedDict.fromkeys(months))
    amount = list(Counter(months).values())
    plt.bar(res, amount)
    plt.ylim(0, max(amount) + 1)

    plt.yticks(range(0, math.ceil(max(amount)) + 1))
    plt.xlabel("MONTH")
    plt.ylabel("Amount")
    plt.title("Month with the most reservation")
    plt.show()


if __name__ == '__main__':
    Month_with_the_most_reservation()
