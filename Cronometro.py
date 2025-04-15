from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

def My_app():
    #Bloque donde agregamos la ventana   
    window = QWidget()
    window.setWindowTitle("Cronometro")
    window.resize(400, 300)
    
    #Crear el primer layout o como yo lo conozco mejor primer div/contenedor
    firstLayout = QVBoxLayout()

    #Ahora creare un label 
    label = QLabel("primer layout")
    firstLayout.addWidget(label)

    #asignar el contenedor a la ventana
    window.setLayout(firstLayout)

    return window

app = QApplication([])

ventana = My_app()
ventana.show()

app.exec()
