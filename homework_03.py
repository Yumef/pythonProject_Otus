
from csv import DictReader
import json

books = []
# Прочесть список книг
# Составить для каждой книги отельный словарь в списке с ключами title, author, genre, publisher
with open('files/books-133064-871075.csv', newline='') as f:
    reader = DictReader(f)
    for row in reader:
        books.append(row)

        row["publisher"] = row["Publisher"]
        row["title"] = row["Title"]
        row["author"] = row["Author"]
        row["pages"] = int(row["Pages"])
        row["genre"] = row["Genre"]

        del row["Publisher"]
        del row["Title"]
        del row["Author"]
        del row["Pages"]
        del row["Genre"]


# Проочесть список юзеров
with open("files/users.json", "r") as f:
    read_users = f.read()
    users = json.loads(read_users)


# Убрать лишние параметры
# Для каждого юзера создать параметр books с пустым списком для словарей из книг
users_result = []
for user in users:
    data = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
        }

    users_result.append(data)

with open("files/result.json", "w") as f:
    text = json.dumps(users_result, indent=4)
    f.write(text)




# Циклом вписать для каждого юзера книги в books
count_books = int(len(books) / len(users_result))

for user in users_result:
    for i in range(count_books):
        data = user.get('books')
        data.append(books[i])
        books.remove(books[i])

u = -1
for i in range(len(books)):
    data = users_result[u+1].get('books')
    data.append(books[i])
    u += 1

with open("files/result.json", "w") as f:
    text = json.dumps(users_result, indent=4)  # отступы
    f.write(text)


