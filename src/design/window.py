# Form implementation generated from reading ui file 'design/ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(321, 259)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        # font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ip = QtWidgets.QLabel(parent=self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(10, 60, 301, 16))
        self.ip.setObjectName("ip")
        self.architecture = QtWidgets.QLabel(parent=self.centralwidget)
        self.architecture.setGeometry(QtCore.QRect(10, 80, 301, 16))
        self.architecture.setObjectName("architecture")
        self.processor = QtWidgets.QLabel(parent=self.centralwidget)
        self.processor.setGeometry(QtCore.QRect(10, 100, 301, 16))
        self.processor.setObjectName("processor")
        self.kernel = QtWidgets.QLabel(parent=self.centralwidget)
        self.kernel.setGeometry(QtCore.QRect(10, 120, 301, 16))
        self.kernel.setObjectName("kernel")
        self.python_version = QtWidgets.QLabel(parent=self.centralwidget)
        self.python_version.setGeometry(QtCore.QRect(10, 140, 291, 31))
        self.python_version.setObjectName("python_version")
        self.python_build = QtWidgets.QLabel(parent=self.centralwidget)
        self.python_build.setGeometry(QtCore.QRect(10, 180, 291, 31))
        self.python_build.setObjectName("python_build")
        self.update_data = QtWidgets.QPushButton(parent=self.centralwidget)
        self.update_data.setGeometry(QtCore.QRect(5, 220, 311, 32))
        self.update_data.setObjectName("update_data")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Your computer"))
        self.label.setText(_translate("MainWindow", "Ваш компʼютер"))
        self.ip.setText(_translate("MainWindow", "Ip:"))
        self.architecture.setText(_translate("MainWindow", "Архітектура: "))
        self.processor.setText(_translate("MainWindow", "Процессор: "))
        self.kernel.setText(_translate("MainWindow", "Ядро: "))
        self.python_version.setText(_translate("MainWindow", "Версія Python, на якій працює ця программа:\n"
""))
        self.python_build.setText(_translate("MainWindow", "Сбірка Python, на якій працює ця программа:\n"
""))
        self.update_data.setText(_translate("MainWindow", "Оновити"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())
