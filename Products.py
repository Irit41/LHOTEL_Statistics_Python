import pandas as pd
import pymssql



def sort_by_category(e):
    '''
    פונקצית עזר לטובת מיון לפי קטגוריה

    '''
    return e['Category']


def create_list_of_categories(product_sales_table):
    category_list = []
    for temp_dict in product_sales_table:
        category_list.append(temp_dict['Category'])  # הכנסה לרשימה את הקטגוריות

    category_list = sorted(set(category_list))  # הורדת כפילויות של קטגוריות
    return category_list


def display_table_of_best_sellers(dictionary_of_best_sellers, category_list):
    """

    :param dictionary_of_best_sellers:   מילון של המוצרים הנמכרים ביותר מכל קטגוריה

    :param category_list: רשימת קטגוריות
    הפונקציה יוצרת מילון המורכב מקטגוריות מוצרים והכמות שלהם
    ושולחת את המילון שנוצר להדפסה
    """

    products = []
    amounts = []
    for dict_value in dictionary_of_best_sellers.values():
        amounts.append(dict_value[0])
        products.append(dict_value[1])

    data = {'Category': category_list, 'Product': products, 'Amount': amounts}
    print_df(data)


def most_products_sales_in_each_category():
    '''
    הפונצקיה מבצעת השמה של טבלת כל המכירות למשתנה , מבצעת השמה לרשימה רק את הקטגוריות הנמצאות בטבלה תיוצרת מילון שהמפתחות שלו הם הרשימה הנ"ל וערכיהם מאותחלים באפס
    המילון המעודכן לאחר ביצוע הלולאה נשלח להצגה

    '''
    product_sales_table = product_sales()
    category_list = create_list_of_categories(product_sales_table)

    dictionary_of_best_sellers = {key: [0] for key in
                                  category_list}
    for temp_dict in product_sales_table:  # עבור כל שורה בטבלת המכירות משווים כמות ומבצעים השמה של הכמות הגדולה ביותר מבין הערך הנ"ל או הערך שקיים במילון לכל קטגוריה בנפרד והשמה של שם המוצר במילון
        for category in category_list:
            if temp_dict['Category'] == category:
                if temp_dict['Amount'] > dictionary_of_best_sellers[category][0]:
                    dictionary_of_best_sellers[category][0] = temp_dict['Amount']
                    dictionary_of_best_sellers[category].append(temp_dict['Description'])
    display_table_of_best_sellers(dictionary_of_best_sellers, category_list)


def print_df(data):
    '''

    :param data: מידע במבנה של מילון
    הפונקציה יוצרת מסגרת תצוגה מהפרמטר שהתקבל ומדפיסה אותה
    '''
    df = pd.DataFrame(data)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(df)


def get_product_sales():
    '''
    פונקציה להצגת נתוני כל המכירות במבנה טבלאי

    '''
    product_sales_table = product_sales()
    print_df(product_sales_table)


def product_sales():
    """
    הפונצקיה יוצרת חיבור עם מסד הנתונים ויוצרת רשימה של מילונים מערך המוחזר מפרוצדורה להצגת כל המכירות
    :return:result_rows :   רשימה של מילונים
    """
    conn = pymssql.connect(server='sql5108.site4now.net',
                           user='db_a79b5b_proj13_admin', password='XXNEA6q6VbvATG6g', database='db_a79b5b_proj13')
    cursor = conn.cursor(as_dict=True)

    cursor.callproc('SumPerProduct')
    result_rows = [row for row in cursor]
    for row in cursor:
        result_rows.append(row)

    result_rows.sort(key=sort_by_category)

    return result_rows


def Product_Purchase_By_Name(product_name):
    """
      הפונצקיה מציגה את נתוני המכירות של מוצר לבקשתו של המשתמש ע"י מעבר על טבלת כל המכירות , יצירת מילון זמני עם פרטי המוצר הנבחר ושליחתו להצגה
    :param product_name: מחרוזת קלט מהמשתמש

    """
    product_name = product_name.lower()
    all_product_sales = product_sales();
    result_dict = {}
    for index in range(len(all_product_sales)):
        temp_dict = all_product_sales[index]
        if temp_dict["Description"].lower() == product_name:
            result_dict = {x: [y, ""] for (x, y) in temp_dict.items()}
            break

    print_df(result_dict) if result_dict else print('No product matching this name was found in our data bases')
