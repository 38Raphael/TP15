from PySide2.QtWidgets import QWidget, QVBoxLayout, QApplication, QHBoxLayout, QPushButton, QTextEdit, QTableWidget, \
    QHeaderView, QLabel, QDialog


class SQLClientWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600, 400)
        self.layout = QVBoxLayout()

        self.buttonpanel = ButtonPanel()
        self.notificationpanel = QTextEdit()
        self.resulttable = QTableWidget(5, 3)
        self.resulttable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.layout.addWidget(self.buttonpanel)
        self.layout.addWidget(self.notificationpanel)
        self.layout.addWidget(self.resulttable)

        self.setLayout(self.layout)
        self.show()


class ButtonPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QHBoxLayout()

        self.w1 = QPushButton("Configure")
        self.w2 = QPushButton("Connect")
        self.w3 = QPushButton("Disconnect")

        self.layout.addWidget(self.w1)
        self.layout.addWidget(self.w2)
        self.layout.addWidget(self.w3)

        self.setLayout(self.layout)


#  Partie 2
class LabeledTextField(QWidget):
    def __init__(self, text):
        QWidget.__init__(self)

        self.layout = QHBoxLayout()

        self.wi1 = QLabel(text)
        self.wi2 = QTextEdit()
        self.wi2.setMaximumHeight(38)

        self.layout.addWidget(self.wi1)
        self.layout.addWidget(self.wi2)

        self.setLayout(self.layout)


class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.layout = QVBoxLayout()
        self.setWindowTitle("Configuration")

        self.o1 = LabeledTextField("IP adress")
        self.o2 = LabeledTextField("User")
        self.o3 = LabeledTextField("Password")

        self.layout.addWidget(self.o1)
        self.layout.addWidget(self.o2)
        self.layout.addWidget(self.o3)

        self.setLayout(self.layout)
        self.win = SQLClientWindow()
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    win = ConfigurationDialog()
    app.exec_()
