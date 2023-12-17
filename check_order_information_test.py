# Ксения Волкова, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


def create_new_order(body):
    response = sender_stand_request.post_new_order(body)
    return response.json()["track"]


def get_order_by_track_number(track_number):
    response = sender_stand_request.get_order(track_number)
    return response


def check_status_code(status_code):
    if (status_code == 200):
        print("Тест пройден")
    else:
        print("Тест провален")


track_number = create_new_order(data.order)
response = get_order_by_track_number(track_number)
check_status_code(response.status_code)
