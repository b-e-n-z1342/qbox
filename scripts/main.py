# python
import os
print("    Qbox launcher TUI    ")
print("||||||||||||||||||||||||||||||||")
print("|| Что вы хотите сделать?     ||")
print("|| [ 1 ] Обновить             ||")
print("|| [ 2 ] Изменить дистребутив ||")
print("|| [ 3 ] Удалить контейнер    ||")
print("|| [ 4 ] Установить контейнер ||")
print("||||||||||||||||||||||||||||||||")

x = input(">>> ").strip()

# Проверка на пустой ввод ДО сравнений
if not x:
    print("Ввод не может быть пустым!")
else:
    # Сравниваем со строками, а не числами
    if x == "1":
        print("в разработке")
    elif x == "2":
        print("реализация")
    elif x == "3":
        print("скоро")
    elif x == "4":
        print("[ 1 ] Debian     sid")
        print("[ 2 ] Fedora     -- ")
        print("[ 3 ] Cent OS    -- ")
        y = input(">>> ").strip()

        if y == "1":
            os.system("distrobox create --image debian:sid --name qbox-deb")
            os.system("distrobox enter qbox-deb -- sudo dpkg --add-architecture i386")
            os.system("distrobox enter qbox-deb -- sudo apt update")
        elif y == "2":
            os.system("distrobox create --image fedora:49 --name qbox-rpm")
            os.system("distrobox enter qbox-rpm -- sudo dnf update")
        elif y == "3":
            print("в разработке")
        else:
            print("Неверный выбор")
    else:
        print("Неверная команда")
