# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



import script
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 300)
        Form.setMinimumSize(QtCore.QSize(300, 300))
        Form.setMaximumSize(QtCore.QSize(300, 300))
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 284))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pseudo_jvc = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pseudo_jvc.setObjectName("pseudo_jvc")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pseudo_jvc)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_jvc = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password_jvc.setObjectName("password_jvc")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password_jvc)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.sujet_jvc = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sujet_jvc.setObjectName("sujet_jvc")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sujet_jvc)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.message_jvc = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.message_jvc.setObjectName("message_jvc")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.message_jvc)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.start_script = QtWidgets.QPushButton(self.formLayoutWidget)
        self.start_script.setObjectName("start_script")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.start_script)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Spam mp jvc"))
        self.label.setText(_translate("Form", "Votre pseudo :"))
        self.pseudo_jvc.setPlaceholderText(_translate("Form", "forumeur"))
        self.label_2.setText(_translate("Form", "Votre mot de passe :"))
        self.password_jvc.setPlaceholderText(_translate("Form", "1234"))
        self.label_3.setText(_translate("Form", "Sujet du message :"))
        self.sujet_jvc.setPlaceholderText(_translate("Form", "Salut les khey"))
        self.label_4.setText(_translate("Form", "Le message :"))
        self.message_jvc.setPlaceholderText(_translate("Form", "Mon message  UwU"))
        self.start_script.setText(_translate("Form", "Lancer le script"))
        
        self.start_script.clicked.connect(self.start_click)
        
    
        
    def start_click(self):
        x = 0
        response = {'1' : self.message_jvc.toPlainText(),
                    '2' : self.password_jvc.text(),
                    '3' : self.pseudo_jvc.text(),
                    '4' : self.sujet_jvc.text()}
        
        for i in response:
            if response[i] == "":
                x =+ 1
            else:
                pass
        if x >= 1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Erreur")
            msg.setInformativeText('Tous les champs doivent être remplis')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            script.script('https://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm', response["3"], response["2"], response["4"], response["1"])
        
                


    
        
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
