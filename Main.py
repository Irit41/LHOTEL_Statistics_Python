from Customers_Rooms import Amount_of_room_reservations_per_month
from Tasks import Number_of_tasks_per_month

import Products
import Financial


def menu():
    while (True):
        print("************Welcome**************")
        print()
        choice = ''
        try:
            choice = input("""
                      A: Finance Department
                      B: Room reservations department
                      C: Products Department
                      D: Room service department
                      Q: Logout

                      Please enter your choice: """)
        except:
            print('Wrong input. Please enter a number ...')
        if choice == "A" or choice == "a":

            Financial.main()
        elif choice == "B" or choice == "b":
            Amount_of_room_reservations_per_month()
        if choice == "C" or choice == "c":
            Products.main()
        elif choice == "D" or choice == "d":
            Number_of_tasks_per_month()
        elif choice == "Q" or choice == "q":
            exit()
        else:
            # print("You must only select either A or B")
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
