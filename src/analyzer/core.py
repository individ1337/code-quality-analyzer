"""
CodeQuality Analyzer - Core analysis engine
Python 3.12+ optimized
"""

import ast
import sys
from pathlib import Path
from typing import Dict, List
from dataclasses import dataclass


@dataclass
class FunctionInfo:
    """Информация о функции"""
    name: str
    file_path: str
    line_start: int
    line_end: int
    num_lines: int
    has_docstring: bool = False


@dataclass
class ClassInfo:
    """Информация о классе"""
    name: str
    file_path: str
    line_start: int
    line_end: int
    num_lines: int
    has_docstring: bool = False


@dataclass
class ImportInfo:
    """Информация об импорте"""
    module: str
    file_path: str
    line: int


class CodeAnalyzer:
    """Анализирует Python код, используя AST (Python 3.12)"""
    
    def __init__(self, root_path: str):
        self.root_path = Path(root_path).resolve()
        self.functions: List[FunctionInfo] = []
        self.classes: List[ClassInfo] = []
        self.imports: List[ImportInfo] = []
        self.total_lines = 0
        self.total_files = 0

    def analyze(self) -> Dict:
        """Запускает полный анализ проекта"""
        print(f"🔍 Анализ: {self.root_path}")
        print(f"🐍 Python версия: {sys.version.split()[0]}")
        
        for file_path in self.root_path.rglob("*.py"):
            if 'venv' in str(file_path) or '.git' in str(file_path):
                continue
            self.total_files += 1
            self._analyze_file(file_path)
        
        return self._get_summary()

    def _analyze_file(self, file_path: Path):
        """Анализирует один файл"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.splitlines()
            
            self.total_lines += len(lines)
            tree = ast.parse(content, filename=str(file_path))
            
            self._extract_imports(tree, file_path)
            self._extract_functions_and_classes(tree, file_path)
            
        except SyntaxError as e:
            print(f"⚠️ Синтаксическая ошибка в {file_path}: {e}")
        except Exception as e:
            print(f"⚠️ Ошибка в {file_path}: {e}")

    def _extract_imports(self, tree: ast.AST, file_path: Path):
        """Извлекает импорты"""
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.imports.append(ImportInfo(
                        module=alias.name,
                        file_path=str(file_path),
                        line=node.lineno
                    ))
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    self.imports.append(ImportInfo(
                        module=node.module,
                        file_path=str(file_path),
                        line=node.lineno
                    ))

    def _extract_functions_and_classes(self, tree: ast.AST, file_path: Path):
        """Извлекает функции и классы"""
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                end_line = node.end_lineno if hasattr(node, 'end_lineno') else node.lineno
                self.functions.append(FunctionInfo(
                    name=node.name,
                    file_path=str(file_path),
                    line_start=node.lineno,
                    line_end=end_line,
                    num_lines=end_line - node.lineno + 1,
                    has_docstring=bool(ast.get_docstring(node))
                ))
            elif isinstance(node, ast.ClassDef):
                end_line = node.end_lineno if hasattr(node, 'end_lineno') else node.lineno
                self.classes.append(ClassInfo(
                    name=node.name,
                    file_path=str(file_path),
                    line_start=node.lineno,
                    line_end=end_line,
                    num_lines=end_line - node.lineno + 1,
                    has_docstring=bool(ast.get_docstring(node))
                ))

    def _get_summary(self) -> Dict:
        """Собирает сводную статистику"""
        total_funcs = len(self.functions)
        total_classes = len(self.classes)
        
        return {
            'total_files': self.total_files,
            'total_lines': self.total_lines,
            'functions_total': total_funcs,
            'classes_total': total_classes,
            'imports_total': len(self.imports),
            'functions_without_docs': sum(1 for f in self.functions if not f.has_docstring),
            'classes_without_docs': sum(1 for c in self.classes if not c.has_docstring),
            'avg_func_lines': round(sum(f.num_lines for f in self.functions) / max(total_funcs, 1), 2),
            'avg_class_lines': round(sum(c.num_lines for c in self.classes) / max(total_classes, 1), 2)
        }

    def print_report(self):
        """Выводит отчет в консоль"""
        s = self._get_summary()
        
        print("\n" + "="*70)
        print("📊  ОТЧЕТ О КАЧЕСТВЕ КОДА")
        print("="*70)
        print(f"\n📁  Файлов: {s['total_files']}")
        print(f"📝  Строк кода: {s['total_lines']:,}")
        
        print(f"\n🔧  Функции:")
        print(f"   Всего: {s['functions_total']}")
        print(f"   Средняя длина: {s['avg_func_lines']} строк")
        print(f"   Без докстрингов: {s['functions_without_docs']}")
        
        print(f"\n📚  Классы:")
        print(f"   Всего: {s['classes_total']}")
        print(f"   Средняя длина: {s['avg_class_lines']} строк")
        print(f"   Без докстрингов: {s['classes_without_docs']}")
        
        print(f"\n📦  Импортов: {s['imports_total']}")
        
        print("\n" + "-"*70)
        quality_score = self._calculate_quality_score(s)
        print(f"🎯  Оценка качества: {quality_score}/100")
        
        if quality_score >= 80:
            print("   ✅ Отлично! Код в хорошем состоянии.")
        elif quality_score >= 60:
            print("   ⚠️  Хорошо, но есть что улучшить.")
        else:
            print("   ❌ Код требует серьезной доработки.")
        
        print("\n" + "="*70)

    def _calculate_quality_score(self, stats: Dict) -> int:
        """Вычисляет оценку качества кода (0-100)"""
        # Если нет файлов → сразу 0 баллов
        if stats['total_files'] == 0:
            return 0
        
        score = 100
        
        if stats['functions_total'] > 0:
            doc_percent = (stats['functions_total'] - stats['functions_without_docs']) / stats['functions_total']
            score -= (1 - doc_percent) * 20
        
        if stats['classes_total'] > 0:
            doc_percent = (stats['classes_total'] - stats['classes_without_docs']) / stats['classes_total']
            score -= (1 - doc_percent) * 15
        
        if stats['avg_func_lines'] > 30:
            score -= min((stats['avg_func_lines'] - 30) * 0.5, 15)
        
        if stats['avg_class_lines'] > 200:
            score -= min((stats['avg_class_lines'] - 200) * 0.1, 10)
        
        return max(0, int(score))
