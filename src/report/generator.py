"""
Генерация HTML-отчётов
"""

from pathlib import Path
from datetime import datetime
from analyzer.core import CodeAnalyzer


def generate_html_report(analyzer: CodeAnalyzer, output_path: str, quality_score: int = 0):
    """
    Генерирует красивый HTML-отчёт на основе данных анализатора.
    
    Args:
        analyzer: Экземпляр CodeAnalyzer с выполненным анализом
        output_path: Путь для сохранения HTML-файла
        quality_score: Оценка качества (0-100)
    """
    stats = analyzer._get_summary()
    stats['quality_score'] = quality_score
    
    # HTML-шаблон
    html = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Code Quality Report</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f0f4f8;
            padding: 40px 20px;
            color: #1a202c;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            padding: 40px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }}
        .header {{
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        .header h1 {{
            font-size: 2.2em;
            color: #2d3748;
        }}
        .header .subtitle {{
            color: #718096;
            font-size: 1.1em;
        }}
        .score-section {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 30px;
        }}
        .score-number {{
            font-size: 4em;
            font-weight: bold;
        }}
        .score-label {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        .score-status {{
            margin-top: 10px;
            font-size: 1.1em;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}
        .card {{
            background: #f7fafc;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }}
        .card .number {{
            font-size: 2em;
            font-weight: bold;
            color: #2d3748;
        }}
        .card .label {{
            color: #718096;
            margin-top: 5px;
        }}
        .section {{
            margin: 30px 0;
        }}
        .section h2 {{
            font-size: 1.5em;
            color: #2d3748;
            margin-bottom: 15px;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 10px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }}
        th {{
            background: #f7fafc;
            font-weight: 600;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85em;
        }}
        .badge.success {{ background: #c6f6d5; color: #22543d; }}
        .badge.warning {{ background: #fefcbf; color: #744210; }}
        .badge.danger {{ background: #fed7d7; color: #742a2a; }}
        .badge.info {{ background: #bee3f8; color: #2a4365; }}
        .footer {{
            text-align: center;
            color: #a0aec0;
            font-size: 0.9em;
            margin-top: 30px;
            border-top: 1px solid #e2e8f0;
            padding-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Code Quality Report</h1>
            <div class="subtitle">Сгенерировано: {datetime.now().strftime('%d.%m.%Y %H:%M')}</div>
        </div>

        <div class="score-section">
            <div class="score-number">{quality_score}</div>
            <div class="score-label">Оценка качества</div>
            <div class="score-status">
                <span class="badge {'success' if quality_score >= 80 else 'warning' if quality_score >= 60 else 'danger'}">
                    {'✅ Отлично!' if quality_score >= 80 else '⚠️ Хорошо' if quality_score >= 60 else '❌ Требует доработки'}
                </span>
            </div>
        </div>

        <div class="grid">
            <div class="card">
                <div class="number">{stats['total_files']}</div>
                <div class="label">📁 Файлов</div>
            </div>
            <div class="card">
                <div class="number">{stats['total_lines']}</div>
                <div class="label">📝 Строк кода</div>
            </div>
            <div class="card">
                <div class="number">{stats['functions_total']}</div>
                <div class="label">🔧 Функций</div>
            </div>
            <div class="card">
                <div class="number">{stats['classes_total']}</div>
                <div class="label">📚 Классов</div>
            </div>
        </div>

        <div class="section">
            <h2>🔧 Детали по функциям</h2>
            <table>
                <tr>
                    <th>Показатель</th>
                    <th>Значение</th>
                    <th>Статус</th>
                </tr>
                <tr>
                    <td>Всего функций</td>
                    <td>{stats['functions_total']}</td>
                    <td><span class="badge info">{stats['functions_total']}</span></td>
                </tr>
                <tr>
                    <td>Средняя длина</td>
                    <td>{stats['avg_func_lines']} строк</td>
                    <td><span class="badge {'success' if stats['avg_func_lines'] < 30 else 'warning'}">
                        {'✅' if stats['avg_func_lines'] < 30 else '⚠️'}
                    </span></td>
                </tr>
                <tr>
                    <td>Без докстрингов</td>
                    <td>{stats['functions_without_docs']}</td>
                    <td><span class="badge {'success' if stats['functions_without_docs'] == 0 else 'danger'}">
                        {'✅' if stats['functions_without_docs'] == 0 else '❌'}
                    </span></td>
                </tr>
            </table>
        </div>

        <div class="section">
            <h2>📚 Детали по классам</h2>
            <table>
                <tr>
                    <th>Показатель</th>
                    <th>Значение</th>
                    <th>Статус</th>
                </tr>
                <tr>
                    <td>Всего классов</td>
                    <td>{stats['classes_total']}</td>
                    <td><span class="badge info">{stats['classes_total']}</span></td>
                </tr>
                <tr>
                    <td>Средняя длина</td>
                    <td>{stats['avg_class_lines']} строк</td>
                    <td><span class="badge {'success' if stats['avg_class_lines'] < 200 else 'warning'}">
                        {'✅' if stats['avg_class_lines'] < 200 else '⚠️'}
                    </span></td>
                </tr>
                <tr>
                    <td>Без докстрингов</td>
                    <td>{stats['classes_without_docs']}</td>
                    <td><span class="badge {'success' if stats['classes_without_docs'] == 0 else 'danger'}">
                        {'✅' if stats['classes_without_docs'] == 0 else '❌'}
                    </span></td>
                </tr>
            </table>
        </div>

        <div class="section">
            <h2>📦 Импорты</h2>
            <table>
                <tr>
                    <th>Показатель</th>
                    <th>Значение</th>
                </tr>
                <tr>
                    <td>Всего импортов</td>
                    <td>{stats['imports_total']}</td>
                </tr>
            </table>
        </div>

        <div class="footer">
            Сгенерировано с ❤️ с помощью CodeQuality Analyzer
        </div>
    </div>
</body>
</html>
"""
    
    # Сохраняем HTML-файл
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ HTML-отчёт сохранён: {output_path}")
