# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# Показывает информацию в файле
def show_data(filename):
    print("\n№ | Фамилия | Имя | Отчество | Телефон | Дополнительная информация")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")

# Записывает информацию в файл
def export_data(filename):
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(filename, "a", encoding="utf-8") as data: 
        surname = input("Введите Фамилию: ")
        name = input("Введите Имя: ")
        patronymic = input("Введите Отчество: ")
        phone = input("Введите номер телефона: ")
        info = input("Введите дополнительную информацию: ")
        data.write(f"{num} | {surname} | {name} | {patronymic} | {phone} | {info}\n")
        print(f"Добавлена запись : {surname} | {name} | {patronymic} | {phone} | {info}\n")

# Изменяет информацию из файла
def edit_data(filename):
    print("\n№ | Фамилия | Имя | Отчество | Телефон | Дополнительная информация")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    surname = input("Введите Фамилию: ")
    name = input("Введите Имя: ")
    patronymic = input("Введите Отчество: ")
    phone = input("Введите номер телефона: ")
    info = input("Введите дополнительную информацию: ")
    num = elements[0]
    if len(surname) == 0:
        surname = elements[1]
    if len(name) == 0:
        name = elements[1]
    if len(patronymic) == 0:
        patronymic = elements[1]        
    if len(phone) == 0:
        phone = elements[2]
    if len(info) == 0:
        info = elements[1]
    edited_line = f"{num} | {surname} | {name} | {patronymic} | {phone} | {info}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

# Удаляет информацию из файла
def delete_data(filename):
    print("\n№ | Фамилия | Имя | Отчество | Телефон | Дополнительная информация")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))

def main():
    my_choice = -1
    file_phone = "phone.txt"

    # Создает файл если его нет в папке
    with open(file_phone, "a", encoding="utf-8") as file:
         file.write("")

    while my_choice != 0:
        print("Выберите одно из действий:")
        print("1 - Вывести инфо на экран")
        print("2 - Произвести запись данных")
        print("3 - Произвести изменение данных")
        print("4 - Произвести удаление данных")
        print("0 - Выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            show_data(file_phone)
        elif action == 2:
            export_data(file_phone)
        elif action == 3:
            edit_data(file_phone)
        elif action == 4:
            delete_data(file_phone)
        else:
            my_choice = 0

    print("До свидания")

if __name__ == "__main__":
    main()