#!/usr/bin/env python3
"""Command Line Interface для CodeQuality Analyzer"""

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from pathlib import Path
from analyzer.core import CodeAnalyzer
from report.generator import generate_html_report

console = Console()

@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--verbose', '-v', is_flag=True, help='Подробный вывод')
@click.option('--json', '-j', is_flag=True, help='Вывод в формате JSON')
@click.option('--html', '-h', help='Сгенерировать HTML-отчёт (укажите путь к файлу)')
def analyze(path: str, verbose: bool, json: bool, html: str):
    """Анализирует качество Python кода."""
    
    console.print(Panel.fit(
        "[bold blue]🔍 CodeQuality Analyzer[/bold blue]",
        subtitle="Python 3.12 • Code Analysis"
    ))
    
    analyzer = CodeAnalyzer(path)
    analyzer.analyze()
    
    # Сохраняем оценку качества
    stats = analyzer._get_summary()
    quality_score = analyzer._calculate_quality_score(stats)
    stats['quality_score'] = quality_score
    
    # Передаём оценку в генератор
    if html:
        generate_html_report(analyzer, html, quality_score)
    
    if json:
        import json as jsonlib
        print(jsonlib.dumps(stats, indent=2, ensure_ascii=False))
    else:
        analyzer.print_report()
        
        if verbose:
            print("\n📋  ДЕТАЛЬНАЯ ИНФОРМАЦИЯ")
            print("-"*70)
            
            if analyzer.functions:
                table = Table(title="Функции", box=box.ROUNDED)
                table.add_column("Имя", style="cyan")
                table.add_column("Строк", justify="right")
                table.add_column("Докстринг", justify="center")
                table.add_column("Файл", style="dim")
                
                for func in analyzer.functions[:10]:
                    doc_status = "✅" if func.has_docstring else "❌"
                    table.add_row(
                        func.name,
                        str(func.num_lines),
                        doc_status,
                        Path(func.file_path).name
                    )
                
                if len(analyzer.functions) > 10:
                    table.add_row("...", f"и еще {len(analyzer.functions)-10}", "", "")
                
                console.print(table)

if __name__ == '__main__':
    analyze()
