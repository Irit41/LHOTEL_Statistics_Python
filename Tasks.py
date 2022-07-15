from matplotlib import pyplot as plt
from SQL_Connection import Connect_to_SQL_Server


cursor = Connect_to_SQL_Server()


def Number_of_tasks_per_month():
    """
    הפונקציה יוצרת ומציגה גרף המתאר את כמות הבקשות לשירות חדרים לפי חודש ע"י יצירת שתי רשימות מנתוני הערך המוחזר מהפרוצדורה המופעלת ,רשימה אחת מכילה את התאריכים והשניה מכילה את כמויות ההופעות שלהם "

        """
    amount_of_room_service_requests = []
    dates = []

    for i in cursor.execute("exec Number_of_tasks_per_month"):
        dates.append(i[0])
        amount_of_room_service_requests.append(i[1])

    plt.bar(dates, amount_of_room_service_requests)
    plt.ylim(0, max(amount_of_room_service_requests) + 1)
    plt.xlabel("Dates")
    plt.ylabel("Amount")
    plt.title("Amount of room service requests")
    plt.show()


if __name__ == '__main__':
    Number_of_tasks_per_month()
