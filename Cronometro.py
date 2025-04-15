from PySide6.QtWidgets import QApplication, QWidget, QLabel

def My_app():
    window = QWidget()
    window.setWindowTitle("Cronometro")
    window.resize(400, 300)
    label = QLabel("Hola que hace", parent=window)
    return window

app = QApplication([])

ventana = My_app()
ventana.show()

app.exec()
