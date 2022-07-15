

from Products import print_df
from SQL_Connection import Connect_to_SQL_Server
import pandas as pd
import matplotlib.pyplot as mp

cursor = Connect_to_SQL_Server()



def menu():
    print("************Financial************")
    print()

    choice = input("""
                      A: Rooms income
                      B: Products income
                      C: Purchase of goods expenses
                      D: Incomes vs expenses graph
                      Q: Logout

                      Please enter your choice: """)

    if choice == "A" or choice == "a":
        print("Total rooms income : ", Rooms_Income())
    elif choice == "B" or choice == "b":
        print("Total products income : ", Products_Income())
        if choice == "C" or choice == "c":
            print("Total purchase of goods expenses : ", Purchase_Of_Goods_Expenses())

        elif choice == "D" or choice == "d":
            incomes_vs_expenses_graph()
    elif choice == "Q" or choice == "q":
        exit()
    else:
        print("Error, Please try again")
        menu()


def incomes_vs_expenses_graph():
    """
    הפונקציה מציגה גרף המתאר השוואה בין הכנסות להוצאות של הבית מלון ע"י מיזוג רשימות המכילות הוצאות הכנסות ומחלקות למילון ויצירת גרף מנתוניו

    """
    incomes = [Rooms_Income(), Products_Income()]
    expenses = [2688, Purchase_Of_Goods_Expenses()]
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
    """
        הפונקציה מבצעת חישוב של כל ההכנסות מהשכרת חדרים במלון וסוכמת אותם למשתנה
        :return:  משתנה המכיל את הסכום הכולל של כל ההכנסות מהשכרת חדרים
        """
    sum_total = 0
    for row in cursor.execute("Calu_Rooms_Income"):
        sum_total += row[0]
    return sum_total


def Purchase_Of_Goods_Expenses():
    """
      הפונקציה מבצעת חישוב של סכומי הוצאות של רכישת סחורה וסוכמת אותם למשתנה
      :return:  משתנה המכיל את הסכום הכולל של הוצאות על רכישת סחורה
      """
    sum_total = 0
    for row in cursor.execute("Expenses"):
        sum_total += row[0]
    return sum_total


def display_Products_Income():
    products_income = Products_Income()
    print("Total products income : ", products_income)


def Products_Income():
    """
    הפונקציה מבצעת חישוב של מחירי כל המוצרים שנרכשו לאחר הנחה וסוכמת אותם למשתנה
    :return:  משתנה המכיל את הסכום הכולל של כל המוצרים שנרכשו
    """
    sum_total = 0
    for row in cursor.execute("Calu_Products_Income"):
        if row[2] != 0:
            percent = (row[1] * row[2]) / 100
            new_price = row[1] - percent
        else:
            new_price = row[1]
        sum_total += new_price * row[0]
    return sum_total


def main():
    menu()


if __name__ == '__main__':
    main()
