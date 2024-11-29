# test_response_mechanism.py
import unittest
import os
from unittest import mock
from OkumiResponse.response_mechanism import ResponseMechanism


class TestResponseMechanism(unittest.TestCase):

    def setUp(self):
        """Этот метод выполняется перед каждым тестом"""
        self.rm = ResponseMechanism()
        self.test_file = "test_knowledge_base.json"
        self.rm_with_file = ResponseMechanism(storage_file=self.test_file)

    def tearDown(self):
        """Этот метод выполняется после каждого теста"""
        # Удаление временного файла после тестов
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_to_knowledge_base(self):
        """Тестирование добавления вопросов и ответов в базу знаний"""
        self.rm.add_to_knowledge_base("Как тебя зовут?", "Меня зовут Okumi.")
        self.assertIn("как тебя зовут?", self.rm.knowledge_base)
        self.assertEqual(self.rm.knowledge_base["как тебя зовут?"], "Меня зовут Okumi.")

    def test_find_answer_existing(self):
        """Тестирование поиска ответа на существующий вопрос"""
        self.rm.add_to_knowledge_base("Как тебя зовут?", "Меня зовут Okumi.")
        answer = self.rm.find_answer("Как тебя зовут?")
        self.assertEqual(answer, "Меня зовут Okumi.")

    def test_find_answer_non_existing(self):
        """Тестирование поиска ответа на несуществующий вопрос"""
        answer = self.rm.find_answer("Когда твой день рождения?")
        self.assertEqual(answer, "Извините, я не знаю ответа на этот вопрос.")

    def test_update_knowledge_base(self):
        """Тестирование обновления ответа на существующий вопрос"""
        self.rm.add_to_knowledge_base("Как тебя зовут?", "Меня зовут Okumi.")
        self.rm.update_knowledge_base("Как тебя зовут?", "Я — библиотека Okumi.")
        self.assertEqual(self.rm.knowledge_base["как тебя зовут?"], "Я — библиотека Okumi.")

    def test_get_all_knowledge(self):
        """Тестирование получения всех знаний"""
        self.rm.add_to_knowledge_base("Как тебя зовут?", "Меня зовут Okumi.")
        self.rm.add_to_knowledge_base("Сколько тебе лет?", "Мне несколько минут!")
        knowledge = self.rm.get_all_knowledge()
        self.assertEqual(len(knowledge), 2)
        self.assertEqual(knowledge["как тебя зовут?"], "Меня зовут Okumi.")
        self.assertEqual(knowledge["сколько тебе лет?"], "Мне несколько минут!")

    @mock.patch('builtins.open', mock.mock_open())
    def test_save_and_load_from_file(self):
        """Тестирование сохранения и загрузки базы знаний из файла"""

        # Добавляем вопрос-ответ в базу данных
        self.rm_with_file.add_to_knowledge_base("Как тебя зовут?", "Меня зовут Okumi.")
        self.rm_with_file.save_to_file()  # Сохраняем базу знаний в файл

        # Загружаем объект ResponseMechanism с того же файла
        rm_new = ResponseMechanism(storage_file=self.test_file)

        # Проверяем, что база знаний загружена корректно
        answer = rm_new.find_answer("Как тебя зовут?")

        # Ожидаем, что ответ на этот вопрос будет правильным
        self.assertEqual(answer, "Меня зовут Okumi.")

    def test_empty_input(self):
        """Тестирование обработки пустых значений (пустой вопрос или ответ)"""
        self.rm.add_to_knowledge_base("", "")
        self.assertNotIn("", self.rm.knowledge_base)


if __name__ == '__main__':
    unittest.main()



