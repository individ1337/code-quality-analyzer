# CodeQuality Analyzer

**Анализируй качество Python кода за секунды!**  
**Analyze Python code quality in seconds!**

## Установка / Installation

1. Клонируй репозиторий:
git clone https://github.com/individ1337/code-quality-analyzer.git
cd code-quality-analyzer

2. Создай виртуальное окружение:
python3 -m venv venv
source venv/bin/activate

3. Установи зависимости:
pip install -r requirements.txt
pip install -e .

## Как использовать / How to use

# Анализировать текущую папку / Analyze current folder

code-analyzer ./

# Анализировать другой проект / Analyze another project

code-analyzer /путь/к/проекту

Примеры / Examples:

code-analyzer ~/Desktop/my-project          # Linux/Mac
code-analyzer C:\Users\Имя\Documents\my-project  # Windows

## Дополнительные режимы / Additional modes

code-analyzer ./ --verbose   # Подробный отчёт / Verbose output
code-analyzer ./ --json      # Вывод в JSON / JSON output
code-analyzer --help         # Справка / Help

## Что показывает

- Сколько файлов и строк кода
- Сколько функций и классов
- Есть ли докстринги (описания) у функций и классов
- Оценку качества от 0 до 100
- Рекомендации по улучшению

## Пример отчёта / Example output

======================================================================
📊  ОТЧЕТ О КАЧЕСТВЕ КОДА / CODE QUALITY REPORT
======================================================================

📁  Файлов / Files: 8
📝  Строк кода / Lines of code: 346

🔧  Функции / Functions: 9 (все с докстрингами / all with docstrings)
📚  Классы / Classes: 4 (все с докстрингами / all with docstrings)
📦  Импортов / Imports: 13

----------------------------------------------------------------------
🎯  Оценка качества / Quality Score: 100/100
   ✅ Отлично! Код в хорошем состоянии. / Excellent! Code is in good shape.
======================================================================

## Лицензия / License

MIT
