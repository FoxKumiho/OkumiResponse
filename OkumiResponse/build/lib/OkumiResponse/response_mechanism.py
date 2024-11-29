# response_mechanism.py

import json
import logging


class ResponseMechanism:
    def __init__(self, knowledge_base=None, storage_file=None):
        """
        Инициализация механизма поиска ответа.
        :param knowledge_base: База знаний для поиска ответов.
        :param storage_file: Путь к файлу для хранения базы знаний (если задан).
        """
        self.storage_file = storage_file
        self.knowledge_base = knowledge_base if knowledge_base is not None else {}
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

        if self.storage_file:
            self.load_from_file()

    def add_to_knowledge_base(self, question, answer):
        """
        Добавляет пару вопрос-ответ в базу знаний.
        :param question: Вопрос (ключ).
        :param answer: Ответ (значение).
        """
        question = question.strip().lower()
        if question and answer:
            self.knowledge_base[question] = answer
            self.logger.info(f"Добавлен вопрос: {question}")
            if self.storage_file:
                self.save_to_file()
        else:
            self.logger.error("Ошибка: вопрос или ответ не могут быть пустыми.")

    def find_answer(self, question):
        """
        Ищет ответ на вопрос в базе знаний.
        :param question: Вопрос, на который нужно найти ответ.
        :return: Ответ или сообщение о том, что ответа нет.
        """
        question = question.strip().lower()
        if question in self.knowledge_base:
            return self.knowledge_base[question]
        else:
            return "Извините, я не знаю ответа на этот вопрос."

    def update_knowledge_base(self, question, new_answer):
        """
        Обновляет ответ на вопрос в базе знаний.
        :param question: Вопрос, для которого обновляется ответ.
        :param new_answer: Новый ответ на вопрос.
        """
        question = question.strip().lower()
        if question in self.knowledge_base:
            self.knowledge_base[question] = new_answer
            self.logger.info(f"Ответ на вопрос {question} обновлен.")
            if self.storage_file:
                self.save_to_file()
        else:
            return "Этот вопрос не найден в базе знаний."

    def get_all_knowledge(self):
        """
        Возвращает все хранимые в базе знаний вопросы и ответы.
        :return: Словарь всех вопросов и ответов.
        """
        return self.knowledge_base

    def save_to_file(self):
        """Сохраняет базу знаний в файл."""
        try:
            with open(self.storage_file, 'w', encoding='utf-8') as file:
                json.dump(self.knowledge_base, file, ensure_ascii=False, indent=4)
            self.logger.info(f"База знаний сохранена в файл {self.storage_file}")
        except Exception as e:
            self.logger.error(f"Ошибка при сохранении файла: {e}")

    def load_from_file(self):
        """Загружает базу знаний из файла."""
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as file:
                self.knowledge_base = json.load(file)
            self.logger.info(f"База знаний загружена из файла {self.storage_file}")
        except FileNotFoundError:
            self.logger.warning("Файл базы знаний не найден, создается новый.")
        except json.JSONDecodeError:
            self.logger.error("Ошибка чтения базы данных.")
            self.knowledge_base = {}  # Обеспечиваем, чтобы в случае ошибки база данных оставалась пустой
        except Exception as e:
            self.logger.error(f"Ошибка при загрузке файла: {e}")
            self.knowledge_base = {}

    def remove_from_knowledge_base(self, question):
        """
        Удаляет вопрос и ответ из базы знаний.
        :param question: Вопрос для удаления.
        """
        question = question.strip().lower()
        if question in self.knowledge_base:
            del self.knowledge_base[question]
            self.logger.info(f"Вопрос {question} удален из базы знаний.")
            if self.storage_file:
                self.save_to_file()
        else:
            return "Этот вопрос не найден в базе знаний."

    def fuzzy_search(self, question):
        """
        Ищет вопрос, используя нечеткое совпадение.
        :param question: Вопрос, на который нужно найти ответ.
        :return: Ответ или сообщение о том, что ответа нет.
        """
        # Здесь можно добавить простую реализацию нечеткого поиска (например, расстояние Левенштейна)
        for key in self.knowledge_base.keys():
            if self.similar(question, key):
                return self.knowledge_base[key]
        return "Извините, я не знаю ответа на этот вопрос."

    def similar(self, str1, str2):
        """
        Простой метод для проверки схожести строк.
        :param str1: Первая строка.
        :param str2: Вторая строка.
        :return: True, если строки похожи, иначе False.
        """
        return str1.lower() == str2.lower()


