import os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


import requests, pprint
import time
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

class UrlExcrption(Exception):
  def __init__(self):
    pass
  def __str__(self):
    return 'url异常'
  pass

class Stats:

  def __init__(self):
    self.ui = QUiLoader().load('ui/http.ui')
    self.ui.sendButton.clicked.connect(self.handleUrl)
    self.ui.clearButton.clicked.connect(self.clearHandle)
    pass

  def check(self, url):
    if len(url) < 5:
      return False
    if url[:5] != 'http:' and url[:6] != 'https:':
      return False
    return True


  def clearHandle(self):
    self.ui.reqTextEdit.clear()
    self.ui.respTextEdit.clear()
    pass


  def handleUrl(self):
    url = self.ui.urlEdit.text().strip()
    try:
      if self.check(url):
        reqInfos = ''
        reqInfos += 'GET '
        reqInfos += url
        reqInfos += '\n'
        reqInfos += str(time.localtime(time.time()))
        reqInfos += '\n'
        reqInfos += 'Content-Length:0\n'
        self.ui.reqTextEdit.setText(reqInfos)
        resp = requests.get(url)
        # pprint.pprint(dict(resp.headers))
        respHeader = dict(resp.headers)
        respInfos = ''
        for item in respHeader:
          # print(item, respHeader[item])
          info = '{}:{}'.format(item, respHeader[item])
          print(info)
          respInfos += info
          respInfos += '\n'
          pass
        self.ui.respTextEdit.setText(respInfos)
        print(respInfos)
        pass
      else:
        raise UrlExcrption()
      pass
    except UrlExcrption as res:
      QMessageBox.about(res)
    pass
  pass

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
