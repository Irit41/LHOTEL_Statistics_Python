
from Customers_Rooms import Month_with_the_most_reservation
from Tasks import Number_of_tasks_per_month

import Products
import Financial


def menu():
    while True:
        print("------------------------------------------------------------------------------------")
        print("-----------------------------------Welcome-----------------------------------------")
        choice = input("""
                      A: Finance Department
                      B: Month with the most reservation
                      C: Products Department
                      D: Amount of room service requests
                      Q: Logout

                      Please enter your choice: """)

        if choice.upper() == "A":
            Financial.menu()
        elif choice.upper() == "B":
            Month_with_the_most_reservation()
        elif choice.upper() == "C":
            Products.main()
        elif choice.upper() == "D":
            Number_of_tasks_per_month()
        elif choice.upper() == "Q":
            exit()
        else:
            print("Error,Please try again")
            menu()


def main():
    menu()

    # Amount_of_room_reservations_per_month()
    # Month_with_the_most_reservation()
    # Products.get_product_sales()
    # Products.most_products_sales_in_each_category()
    # product_name = input("Product Purchase By Name: ")
    # Products.Product_Purchase_By_Name(product_name)
    # print(Financial.Rooms_Income())
    # print(Financial.Purchase_Of_Goods_Expenses())
    # print(Financial.Products_Income())
    # Financial.incomes_vs_expenses_graph()
    # Number_of_tasks_per_month()
    # Month_with_the_most_reservation()

    # Products.get_product_sales()
    # Products.most_products_sales_in_each_category()


if __name__ == '__main__':
    main()
