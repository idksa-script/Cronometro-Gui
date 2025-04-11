from PySide6.QtWidgets import QApplication, QWidget

def My_app():
    window = QWidget()
    window.setWindowTitle("Cronometro")
    window.resize(400, 300)
    return window

app = QApplication([])

ventana = My_app()
ventana.show()

app.exec()
