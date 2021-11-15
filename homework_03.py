
from csv import DictReader
import json

books = []
# Прочесть список книг
# Составить для каждой книги отельный словарь в списке с ключами title, author, genre, publisher
with open('files/books-133064-871075.csv', newline='') as f:
   reader = DictReader(f)
   for row in reader:
       books.append(row)


# Проочесть список юзеров
with open("files/users.json", "r") as f:
   read_users = f.read()
   users = json.loads(read_users)


# Для каждого юзера создать параметр books с пустым списком для словарей из книг
with open("files/users.json", "w") as f:
    for user in users:
        user['books'] = []
    text = json.dumps(user, indent=4)  # отступы
    f.write(text)

# Циклом вписать для каждого юзера книги в books
count_books = int(len(books) / len(users))

for user in users:
    for i in range(count_books):
        data = user.get('books')
        data.append(books[i])
        books.remove(books[i])

u = -1
for i in range(len(books)):
    data = users[u+1].get('books')
    data.append(books[i])
    u += 1

with open("files/result.json", "w") as f:
    text = json.dumps(users, indent=4)  # отступы
    f.write(text)


