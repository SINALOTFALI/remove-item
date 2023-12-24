import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextEdit, QWidget, QFileDialog

class TextProcessingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Text Processing App')
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Paste or load text here...")

        self.process_button = QPushButton('Process and Save', self)
        self.process_button.clicked.connect(self.process_and_save)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.process_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def process_and_save(self):
        input_text = self.text_edit.toPlainText()

        # Your processing logic
        processed_text = self.process_text(input_text)

        # Ask user for the output file location
        output_file_path, _ = QFileDialog.getSaveFileName(self, 'Save Processed Text', '', 'Text Files (*.txt)')

        if output_file_path:
            with open(output_file_path, 'w') as outfile:
                outfile.write(processed_text)

    def process_text(self, text):
        # Your processing logic
        text = text.replace("0", "")
        text = text.replace("1", "")
        text = text.replace("2", "")
        text = text.replace("3", "")
        text = text.replace("4", "")
        text = text.replace("5", "")
        text = text.replace("6", "")
        text = text.replace("7", "")
        text = text.replace("8", "")
        text = text.replace("9", "")
        text = text.replace(".", "")
        text = text.replace(",", "")
        text = text.replace("-", " ")
        text = text.replace(" e ", "")
        text = text.replace(" ", "")

        unique_lines = set(text.split('\n'))
        unique_data = '\n'.join(unique_lines)

        return unique_data

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = TextProcessingApp()
    mainWin.show()
    sys.exit(app.exec_())
