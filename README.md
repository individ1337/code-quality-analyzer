# 🔍 CodeQuality Analyzer

**Анализируй качество Python кода за секунды!**  
**Analyze Python code quality in seconds!**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/version-0.1.0-orange)
![Quality](https://img.shields.io/badge/Quality-100%2F100-brightgreen)

---

## 📖 О проекте / About

**Русский:**  
CodeQuality Analyzer — это инструмент командной строки для статического анализа Python кода. Он помогает разработчикам оценивать качество кода, находить слабые места и улучшать читаемость проектов.

**English:**  
CodeQuality Analyzer is a command-line tool for static analysis of Python code. It helps developers evaluate code quality, find weak spots, and improve project readability.

---

## ✨ Возможности / Features

| Русский | English |
|---------|---------|
| 📊 Анализ структуры (функции, классы, импорты) | 📊 Structure analysis (functions, classes, imports) |
| 📏 Метрики кода (строки, средняя длина) | 📏 Code metrics (lines, average length) |
| 📝 Проверка докстрингов | 📝 Docstring checking |
| 🎯 Оценка качества от 0 до 100 | 🎯 Quality score from 0 to 100 |
| 🎨 Красивые цветные отчёты | 🎨 Beautiful colored reports |
| 📋 Поддержка JSON и verbose режимов | 📋 JSON and verbose modes support |
| 📄 Генерация HTML-отчётов | 📄 HTML report generation |

---

## 📋 Все команды / All commands

Команда / Command	                  Описание / Description
code-analyzer ./	                  Анализ текущей папки / Analyze current folder
code-analyzer /путь/к/проекту	      Анализ конкретного проекта / Analyze specific project
code-analyzer ./ --verbose	          Подробный вывод со списком функций / Verbose output with function list
code-analyzer ./ --json	              Вывод в формате JSON / JSON output
code-analyzer ./ --html report.html	  Генерация HTML-отчёта / Generate HTML report
code-analyzer --help	              Показать справку / Show help

---

## 🚀 Установка / Installation

```bash
# 1. Клонируй репозиторий
git clone https://github.com/individ1337/code-quality-analyzer.git
cd code-quality-analyzer

# 2. Создай виртуальное окружение
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Установи зависимости
pip install -r requirements.txt

# 4. Установи проект
pip install -e .
