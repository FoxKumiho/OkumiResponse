import os
import json
from OkumiResponse.response_mechanism import ResponseMechanism


def load_knowledge_from_file(file_path):
    """Загружает базу знаний из файла, если файл существует"""
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Ошибка чтения файла базы знаний. База знаний пуста.")
            return {}
        except Exception as e:
            print(f"Ошибка при загрузке файла базы знаний: {e}")
            return {}
    return {}


def save_knowledge_to_file(knowledge_base, file_path):
    """Сохраняет базу знаний в файл"""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(knowledge_base, file, ensure_ascii=False, indent=4)
        print(f"База знаний успешно сохранена в файл {file_path}")
    except Exception as e:
        print(f"Ошибка при сохранении базы знаний: {e}")


def main():
    # Файл для хранения базы знаний
    knowledge_file = "knowledge_base.json"

    # Загружаем или создаем базу знаний
    knowledge_data = load_knowledge_from_file(knowledge_file)

    # Инициализация механизма поиска ответа с загруженной базой знаний
    rm = ResponseMechanism(knowledge_base=knowledge_data)

    print("Добро пожаловать в систему поиска ответов Okumi!")
    print("Задайте вопрос или введите 'выход' для завершения.")
    print("Вы можете спросить что-то вроде:")
    print("  - Как вас зовут?")
    print("  - Что такое Okumi?")
    print("  - Какой сегодня день?")

    while True:
        # Получаем вопрос от пользователя
        question = input("\nВведите ваш вопрос: ").strip()

        # Проверка на завершение работы
        if question.lower() == "выход":
            # Сохраняем базу знаний перед выходом
            save_knowledge_to_file(rm.get_all_knowledge(), knowledge_file)
            print("До свидания!")
            break

        # Поиск ответа на вопрос
        answer = rm.find_answer(question)
        print(f"Ответ: {answer}")

        # Предложение добавить новый вопрос-ответ
        add_new = input("Хотите добавить новый вопрос-ответ? (да/нет): ").strip().lower()
        if add_new == "да":
            new_question = input("Введите новый вопрос: ").strip()
            new_answer = input("Введите ответ на новый вопрос: ").strip()

            # Проверка на пустые вопросы и ответы
            if not new_question or not new_answer:
                print("Ошибка: вопрос или ответ не могут быть пустыми!")
                continue

            rm.add_to_knowledge_base(new_question, new_answer)
            print("Новый вопрос-ответ добавлен!")


if __name__ == "__main__":
    main()
