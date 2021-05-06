import os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox


class Stats():
  def __init__(self):
    self.window = QMainWindow()
    self.window.resize(500, 400)
    self.window.move(300, 300)
    self.window.setWindowTitle('薪资统计')

    self.textEdit = QPlainTextEdit(self.window)
    self.textEdit.setPlaceholderText('请输入薪资表')
    self.textEdit.move(10, 25)
    self.textEdit.resize(300, 350)

    self.button = QPushButton('统计', self.window)
    self.button.move(380, 80)
    self.button.clicked.connect(self.handleCalc)
    pass

  def handleCalc(self):
    info = self.textEdit.toPlainText()

    salary_above_20k = ''
    salary_below_20k = ''

    for line in info.splitlines():
      if not line.strip():
        continue
        pass
      parts = line.split(' ')
      print(type(parts))

      parts = [p for p in parts if p]
      name, salary,age = parts
      if int(salary) >= 20000:
        salary_above_20k += name + '\n'
        pass
      else:
        salary_below_20k += name + '\n'
        pass
      pass
    QMessageBox.about(self.window,
                      '统计结果',
                      f'''薪资20000 以上的有：\n{salary_above_20k}
                        \n薪资20000 以下的有：\n{salary_below_20k}'''
                      )
    pass
  pass

app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()


# def handleCalc():
#   info = textEdit.toPlainText()
#   salary_above_20k = ''
#   salary_below_20k = ''
#   for line in info.splitlines():
#     if not line.strip():
#       continue
#     parts = line.split(' ')
#     print(type(parts))
#     parts = [p for p in parts if p]
#     name, salary, age = parts
#     if int(salary) >= 20000:
#       salary_above_20k += name + '\n'
#       pass
#     else:
#       salary_below_20k += name + '\n'
#       pass
#     pass
#   QMessageBox.about(window, '统计结果', f'''薪资20000以上的有:\n{salary_above_20k}\n薪资20000以下的有:\n{salary_below_20k}''')
#   pass
#
#
#
# app = QApplication([]) # 提供图形界面底层管理的功能，在创建其他控件之前要创建Application
#
# window = QMainWindow() # 创建主窗口
# window.resize(500, 400) # 控制窗口大小
# window.move(300, 310) # 控制窗口的位置
# window.setWindowTitle('薪资统计') # 设置窗口标题
#
# textEdit = QPlainTextEdit(window) # 创建文本框，window是textEdit的父窗口
# textEdit.setPlaceholderText("请输入薪资表") # 设置默认显示
# textEdit.move(10,25) # 针对父窗口的位置
# textEdit.resize(300,350) # 设置窗口大小
#
# button = QPushButton('统计', window)
# button.move(380,80)
# button.clicked.connect(handleCalc)
#
# window.show() # 通过show方法展现窗口
#
# app.exec_()