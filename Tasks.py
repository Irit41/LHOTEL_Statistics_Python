from matplotlib import pyplot as plt
from SQL_Connection import Connect_to_SQL_Server

cursor = Connect_to_SQL_Server()


def Number_of_tasks_per_month():
    """
    הפונקציה יוצרת ומציגה גרף המתאר את כמות הבקשות לשירות חדרים לפי חודש ע"י יצירת שתי רשימות מנתוני הערך המוחזר מהפרוצדורה המופעלת ,רשימה אחת מכילה את התאריכים והשניה מכילה את כמויות ההופעות שלהם "
        """
    dates = []

    for i in cursor.execute("exec Number_of_tasks_per_month"):
        date = f"{i[0].month}/{i[0].year}"
        dates.append(date)
    amount_of_room_service_requests = {x: dates.count(x) for x in dates}

    plt.bar(amount_of_room_service_requests.keys(), amount_of_room_service_requests.values())
    plt.ylim(0, max(amount_of_room_service_requests.values()) + 1)
    plt.yticks(range(0, max(amount_of_room_service_requests.values()) + 1))
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.title("Amount of room service requests")
    plt.show()


if __name__ == '__main__':
    Number_of_tasks_per_month()
