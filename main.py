

import sys
from PyQt5 import QtWidgets
from interface import Ui_Form
    
    
        




app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec_())



