#!/usr/bin/python3
import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Запуск команд в контейнерах Distrobox')
    parser.add_argument('--deb', action='store_true', help='Использовать Debian контейнер')
    parser.add_argument('--rpm', action='store_true', help='Использовать RPM контейнер')
    parser.add_argument('command', nargs=argparse.REMAINDER, help='Команда для выполнения в контейнере')

    args = parser.parse_args()

    # Проверяем, что указан ровно один тип контейнера
    if sum([args.deb, args.rpm]) != 1:
        print("Ошибка: укажите ровно один тип контейнера --deb или --rpm")
        sys.exit(1)

    if not args.command:
        print("Ошибка: не указана команда для выполнения")
        sys.exit(1)

    # Определяем имя контейнера
    container_name = "qbox-deb" if args.deb else "qbox-rpm"
    service_command = ' '.join(args.command)

    # Формируем и выполняем команду
    command = f"env distrobox enter {container_name} -- {service_command}"
    print(f"Выполняется: {command}")
    os.system(command)

if __name__ == "__main__":
    main()
