from setuptools import setup, find_packages

setup(
    name="OkumiResponse",  # Название вашей библиотеки
    version="0.1",         # Версия
    packages=find_packages(),  # Находит все пакеты
    install_requires=[],  # Зависимости, если есть
    author="Miss.Okumi",    # Автор библиотеки
    author_email="your.email@example.com",  # Укажите ваш email для контактов
    description="Библиотека для поиска ответов на основе базы знаний",  # Описание
    url="https://github.com/FoxKumiho/OkumiResponse.git",  # Ссылка на ваш репозиторий GitHub
    classifiers=[  # Список классификаторов для PyPi
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Указываем минимальную версию Python
    keywords="NLP, искусственный интеллект, база знаний",  # Ключевые слова для поиска
)

