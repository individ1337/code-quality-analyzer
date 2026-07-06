# CodeQuality Analyzer

Анализируй качество Python кода за секунды.

## Как установить

1. Клонируй репозиторий:
git clone https://github.com/individ1337/code-quality-analyzer.git
cd code-quality-analyzer

2. Создай виртуальное окружение:
python3 -m venv venv
source venv/bin/activate

3. Установи зависимости:
pip install -r requirements.txt
pip install -e .

## Как пользоваться

Просто запусти в терминале:

code-analyzer ./

Анализатор покажет отчёт по всем Python файлам в папке.

## Команды

code-analyzer ./              - обычный отчёт
code-analyzer ./ --verbose    - подробный отчёт
code-analyzer ./ --json       - отчёт в JSON формате
code-analyzer --help          - справка

## Что показывает

- Сколько файлов и строк кода
- Сколько функций и классов
- Есть ли докстринги (описания) у функций и классов
- Оценку качества от 0 до 100
- Рекомендации по улучшению

## Пример отчёта

📁 Файлов: 8
📝 Строк кода: 346
🔧 Функций: 9
📚 Классов: 4
🎯 Оценка качества: 100/100
✅ Отлично! Код в хорошем состоянии.

## Лицензия

MIT

## Ссылка

https://github.com/individ1337/code-quality-analyzer
