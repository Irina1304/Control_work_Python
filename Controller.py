from Adding import append
from Saving import save_file
from Reading import read_note
from Editing import edit_file
from Delete import delete_file
from Sorting import sort_file
from ReadOne import select_reading

text = "Выберите одно из следующих действий и нажмите соответствующую цифру:\n[1] - Записать заметку в формате csv \n[2] - Прочитать cписок всех заметок\n[3] - Редактировать заметку\n[4] - Удалить заметку\n[5] - Вывести все заметки за определенную дату\n[6] - Вывести заметку по номеру ID\nДля выхода нажмите [0]"

def choice_todo():
    while True:
        print(text)
        flag = int(input())
        if flag == 1:
            save_file(append())
        elif flag == 2:
            read_note()
        elif flag == 3:
            edit_file()
        elif flag == 4:
            delete_file()
        elif flag == 5:
            sort_file()
        elif flag == 6:
            select_reading()
        elif flag == 0:
            break
        else:
            print("Такого пункта меню не существует")

