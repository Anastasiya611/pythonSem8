import os
from data_create import name_data, surname_data, phone_data, adress_data

file_name = "data.txt"
def print_data():
    if os.path.exists(file_name):
        print("вывод данных из файла:")
        with open(file_name, "r", encoding="utf-8") as file:
            list_data = file.readlines()
            for element in list_data:
                print(element)
    else:
        print("файла не существует")

def input_data():
    print("Введите данные для записи в файл:")
    name = name_data()
    surname = surname_data() 
    phone = phone_data()
    adress = adress_data()
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{name};{surname};{phone};{adress};\n")

def filter_data(filter_string):
    with open(file_name, "r", encoding="utf-8") as file:
        list_data = file.readlines()
        if ";" in filter_string:
            list_filter = filter_string.split(";")
        else:
            list_filter = [filter_string]    
        is_found = False
        for element in list_data:
            temp_record = element.split(";")
            count = 0
            for record in temp_record:
                for element_filter in list_filter:
                    if element_filter.lower() in record.lower() and len(element_filter.lower()) == len(record.lower()):
                        count += 1
            if count == len(list_filter):            
                print(element)
                is_found = True
    if not is_found:
        print("таких записей не найдено")

def delete_data():
    with open(file_name, "r", encoding="utf-8") as file:
        delete_data = file.readlines()
        delete_string = input("введите строку для удаления ")
        with open(file_name, "w", encoding="utf-8") as file:
            for delete in delete_data:
                if delete_string in delete:
                    print("Контакт удален")
                else:
                    print(delete)
                    file.write(delete)

def new_data():
    with open(file_name, "r", encoding="utf-8") as file:
        list_data = file.readlines()        
        string = input("введите строку для изменения ")
        with open(file_name, "w", encoding="utf-8") as file:
            for string in list_data:
                new_string = input("Введите новые данные контакта ")
                print(list_data.replace(string,new_string))
                file.write(list_data)