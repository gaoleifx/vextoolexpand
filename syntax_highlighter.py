from PySide2.QtCore import Qt, QRegExp
from PySide2.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont

class VEXHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 定义高亮规则
        self.highlighting_rules = []
        
        # 关键字格式
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6"))  # 蓝色
        keyword_format.setFontWeight(QFont.Bold)
        keywords = [
            "if", "else", "for", "while", "return", "break", "continue",
            "vector", "float", "int", "string", "void", "matrix"
        ]
        for word in keywords:
            pattern = f"\\b{word}\\b"
            self.highlighting_rules.append((pattern, keyword_format))
            
        # 函数格式
        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#DCDCAA"))  # 黄色
        self.highlighting_rules.append((
            r"\b[A-Za-z0-9_]+(?=\()", 
            function_format
        ))
        
        # 注释格式
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955"))  # 绿色
        self.highlighting_rules.append((
            r"//[^\n]*",
            comment_format
        ))
        
        # 字符串格式
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#CE9178"))  # 橙色
        self.highlighting_rules.append((
            r'"[^"\\]*(\\.[^"\\]*)*"',
            string_format
        ))
        
        # 数字格式
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#B5CEA8"))  # 浅绿色
        self.highlighting_rules.append((
            r"\b\d+\b",
            number_format
        ))

    def highlightBlock(self, text):
        """对文本块应用高亮规则"""
        for pattern, format in self.highlighting_rules:
            expression = QRegExp(pattern)  # 直接使用 QRegExp，不需要 QtCore 前缀
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length) 