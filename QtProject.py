import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QMainWindow
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
from calculator import Ui_MainWindow
import math


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plainTextEdit.setPlainText('Вас приветствует калькулятор 1.0\n\n' +
                                        'Введите 1 число, затем выберите операцию\n' +
                                        'По необходимости калькулятор сообщит вам обо всем.\n'
                                        + 'Учтите, что числа не могут превышать 10000')
        self.string = ''
        self.firstnumber = 1
        self.status = ''
        self.one.clicked.connect(self.first_number)
        self.two.clicked.connect(self.first_number)
        self.three.clicked.connect(self.first_number)
        self.four.clicked.connect(self.first_number)
        self.five.clicked.connect(self.first_number)
        self.six.clicked.connect(self.first_number)
        self.seven.clicked.connect(self.first_number)
        self.eight.clicked.connect(self.first_number)
        self.nine.clicked.connect(self.first_number)
        self.zero.clicked.connect(self.first_number)

        self.pushButton.clicked.connect(self.Reset)
        self.Plus.clicked.connect(self.addition)
        self.Equals.clicked.connect(self.equal)
        self.Umnozh.clicked.connect(self.multiplication)
        self.Minus.clicked.connect(self.difference)
        self.Delenie.clicked.connect(self.division)
        self.SQRT.clicked.connect(self.square_root)
        self.POW.clicked.connect(self.pow)
        self.factorial.clicked.connect(self.FCT)

    def first_number(self):
        if self.firstnumber == 1:
            if len(self.string) <= 4:
                self.string += self.sender().text()
            self.plainTextEdit.setPlainText(self.string)
            self.number1 = float(self.string)
            self.lcdNumber.display(self.number1)
        else:
            self.second_number()

    def equal(self):
        print('I am HERE')
        if self.status == 'addition':
            sum = self.number1 + self.number2
            print(sum)
            self.plainTextEdit.setPlainText('Сумма равна ' + str(sum))
            self.lcdNumber.display(float
                                   (sum))
        elif self.status == 'multiplication':
            m = self.number1 * self.number2
            print(m)
            self.plainTextEdit.setPlainText('Произведение равно ' + str(m))
            self.lcdNumber.display(float
                                   (m))
        elif self.status == 'difference':
            m = self.number1 - self.number2
            print(m)
            self.plainTextEdit.setPlainText('Разность равна ' + str(m))
            self.lcdNumber.display(float
                                   (m))
        elif self.status == 'division':
            m = self.number1 / self.number2
            print(m)
            self.plainTextEdit.setPlainText('Частное равно ' + str(m))
            self.lcdNumber.display(float
                                   (m))
        elif self.status == 'sqrt':
            m = math.sqrt(self.number1)
            print(m)
            self.plainTextEdit.setPlainText('Квадратный корень равен ' + str(m))
            self.lcdNumber.display(float(m))
        elif self.status == 'pow':
            m = self.number1 ** self.number2
            print(m)
            self.plainTextEdit.setPlainText('Степень числа ' + str(m))
            self.lcdNumber.display(float(m))
        elif self.status=='fact':
            m = math.factorial(self.number1)
            self.plainTextEdit.setPlainText('Факториал числа равен ' + str(m))
            self.lcdNumber.display(float(m))
        self.firstnumber = 1

    def Reset(self):
        self.string = ''
        self.plainTextEdit.setPlainText('')
        self.lcdNumber.display(float
                               (0))
        self.firstnumber = 1
        self.status = ''

    def addition(self):
        self.plainTextEdit.setPlainText('Введите 2 число')
        self.status = 'addition'
        self.firstnumber = 0
        self.string = ''

    def multiplication(self):
        self.plainTextEdit.setPlainText('Введите 2 число')
        self.status = 'multiplication'
        self.firstnumber = 0
        self.string = ''

    def division(self):
        self.plainTextEdit.setPlainText('Введите 2 число')
        self.status = 'division'
        self.firstnumber = 0
        self.string = ''

    def difference(self):
        self.plainTextEdit.setPlainText('Введите 2 число')
        self.status = 'difference'
        self.firstnumber = 0
        self.string = ''

    def square_root(self):
        self.status = 'sqrt'
        self.equal()

    def FCT(self):
        self.status = 'fact'
        self.equal()

    def pow(self):
        self.status = 'pow'
        self.plainTextEdit.setPlainText('Введите степень, в которую нужно возвести число')
        self.firstnumber = 0
        self.string = ''

    def second_number(self):
        if len(self.string) <= 4:
            self.string += self.sender().text()
        self.plainTextEdit.setPlainText(self.string)
        self.number2 = float(self.string)
        self.lcdNumber.display(self.number2)
        print(type(self.number2), self.number2)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
