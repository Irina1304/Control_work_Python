text = "Выберите одно из следующих действий и нажмите соответствующую цифру:\n[1] - записать заметку в формате csv \n[2] - прочитать cписок всех заметок\n[3] - редактировать заметку\n[4] - удалить заметку\n[5] - вывести все заметки за определенную дату\n[6] - вывести заметку по номеру ID\nДля выхода нажмите [0]"

def choice_todo():
    while True:
        print(text)
        flag = int(input())
        if flag == 1:
        elif flag == 2:
        elif flag == 3:
        elif flag == 4:
        elif flag == 5:
        elif flag == 6:
        elif flag == 0:
            break
        else:
            print("Такого пункта меню не существует")
