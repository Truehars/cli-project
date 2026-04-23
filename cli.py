import requests

BASE_URL = "http://127.0.0.1:8000"


def handle_response(res):
    try:
        print(res.json())
    except:
        print("Error:", res.status_code)
        print(res.text)


def create():
    id = int(input("ID: "))
    name = input("Name: ")
    age = int(input("Age: "))

    res = requests.post(f"{BASE_URL}/students", json={
        "id": id,
        "name": name,
        "age": age
    })
    handle_response(res)


def read():
    res = requests.get(f"{BASE_URL}/students")
    handle_response(res)


def update():
    id = int(input("ID to update: "))
    name = input("New Name: ")
    age = int(input("New Age: "))

    res = requests.put(f"{BASE_URL}/students/{id}", json={
        "id": id,
        "name": name,
        "age": age
    })
    handle_response(res)


def delete():
    id = int(input("ID to delete: "))
    res = requests.delete(f"{BASE_URL}/students/{id}")
    handle_response(res)


if __name__ == "__main__":
    print("1. Create\n2. Read\n3. Update\n4. Delete")
    choice = input("Select: ")

    if choice == "1":
        create()
    elif choice == "2":
        read()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()