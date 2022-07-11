from Products import print_df
from SQL_Connection import Connect_to_SQL_Server
import pandas as pd
import matplotlib.pyplot as mp

cursor = Connect_to_SQL_Server()


def incomes_vs_expenses_graph():

    incomes = [Rooms_Income(), Products_Income()]
    expenses = [300, Purchase_Of_Goods_Expenses()]
    sections = ["Rooms", "Products"]
    incomes_vs_expenses_dict = {"Incomes": incomes, "Expenses": expenses, "Sections": sections}
    data = pd.DataFrame(incomes_vs_expenses_dict)
    df = pd.DataFrame(data, columns=["Sections", "Incomes", "Expenses"])
    print_df(df)
    df['Incomes'] = pd.to_numeric(df['Incomes'])
    df['Expenses'] = pd.to_numeric(df['Expenses'])
    # print(df.dtypes)
    # plot the dataframe
    df.plot(x="Sections", y=["Incomes", "Expenses"], kind="bar", figsize=(9, 8))
    #
    #  print bar graph
    mp.show()


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
