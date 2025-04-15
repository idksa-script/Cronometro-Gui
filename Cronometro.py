from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

def My_app():
    #Bloque donde agregamos la ventana
    #primer QWidget que se encarga de la ventana
    window = QWidget()
    window.setWindowTitle("Cronometro")
    window.resize(400, 300)
    
    #Crear el primer layout o como yo lo conozco mejor primer div/contenedor
    firstLayout = QVBoxLayout()
    secondLayout = QVBoxLayout()

    #Ahora creare un label 
    label = QLabel("primer layout")
    label.setStyleSheet("color:white")
    firstLayout.addWidget(label)

    label2 = QLabel("Segundo layout")
    label2.setStyleSheet("color red")
    secondLayout.addWidget(label2)
    
    #El fondo donde "reposa" el firstLayout osea el QVBoxLayout
    container1 = QWidget()
    container1.setLayout(firstLayout)
    container1.setStyleSheet("background-color: black;")
    container2 = QWidget()
    container2.setLayout(secondLayout)
    container2.setStyleSheet("background-color: blue")
        
    #asignar el contenedor a la ventana
    window.setLayout(QVBoxLayout())
    window.layout().addWidget(container1)
    window.layout().addWidget(container2)


    return window

app = QApplication([])

ventana = My_app()
ventana.show()

app.exec()
