import requests

# Перед запуском этой программы запустить main.py!
if __name__ == '__main__':
    HOST = "localhost"
    PORT = 8080
    token = open("notes/tokens.txt", "r").read().split('\n')[0]

    # Выполняем GET запрос к нашему сервису по URL /sum,
    # передавая 2 параметра: числа a=10 и b=20.
    # Выводим статус-код ответа и ответ сервера на печать
    # response = requests.get(f"http://{HOST}:{PORT}/sum", params={"a": 10, "b": 20})
    # print(f"Status code: {response.status_code}")
    # print(f"Response body: {response.text}")

    a = int(input("0 - delete(id)\n1 - createNote(id)\n2 - noteInfo(id)\n3 - editNote(id, text)"))
    while a > -1 | a < 4:
        if a == 0:
            id1 = int(input('id:'))
            response = requests.post(f"http://{HOST}:{PORT}/{token}/deleteNote", params={"id": int(id1)})
            print(f"Status code: {response.status_code}")
            print(f"Response body: {response.text}")
        elif a == 1:
            id1 = int(input('id:'))
            response = requests.post(f"http://{HOST}:{PORT}/{token}/createNote", params={"id": int(id1)})
            print(f"Status code: {response.status_code}")
            print(f"Response body: {response.text}")
        elif a == 3:
            id1 = int(input('id:\n'))
            s = str(input('text: '))
            response = requests.patch(f"http://{HOST}:{PORT}/{token}/editNote", params={"id": int(id1), "text": s})
            print(f"Status code: {response.status_code}")
            print(f"Response body: {response.text}")
        elif a == 2:
            id1 = int(input('id:'))
            response = requests.get(f"http://{HOST}:{PORT}/{token}/noteInfo", params={"id": int(id1)})
            print(f"Status code: {response.status_code}")
            print(f"Response body: {response.text}")
        else:
            print("end")
        a = int(input("0 - delete(id)\n1 - createNote(id)\n2 - noteInfo(id)\n3 - editNote(id, text)"))
