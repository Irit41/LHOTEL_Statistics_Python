from Customers_Rooms import Month_with_the_most_reservation
from Tasks import Number_of_tasks_per_month

import Products
import Financial


def main():
    # Number_of_tasks_per_month()
    # Month_with_the_most_reservation()
    # Products.get_product_sales()
    # Products.most_products_sales_in_each_category()
    product_name = input("Product Purchase By Name: ")
    Products.Product_Purchase_By_Name(product_name)
  #  Financial.Rooms_Income()
   #  Financial.Purchase_Of_Goods_Expenses()
   #  Financial.Products_Income()

    # Number_of_tasks_per_month()
    # Month_with_the_most_reservation()

    # Products.get_product_sales()
    # Products.most_products_sales_in_each_category()


if __name__ == '__main__':
    main()
