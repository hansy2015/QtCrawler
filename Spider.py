import os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

import requests
import re
import time


'''请求网页'''
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'
}

import requests, pprint
import time
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QIcon
from threading import Thread


class Spider:
  def __init__(self):
    qfile_stats = QFile("ui/stats.ui")
    qfile_stats.open(QFile.ReadOnly)
    qfile_stats.close()
    self.ui = QUiLoader().load('ui/spider.ui')
    self.ui.startButton.clicked.connect(self.startGrab)
    pass

  def startGrab(self):
    self.seed = self.ui.webPageLineEdit.text()
    t = Thread(target=self.Go)
    t.start()
    pass

  def Go(self):
    response = requests.get(self.seed, headers=headers)
    html = response.text
    citys = re.findall('<a target="_blank" href="(.*?)" data-v-f53df81a>', html)
    for city in citys:
      if '\"' in city:
        continue
        pass
      if city.split('/')[-1] == 'zhenghun':
        continue
        pass
      self.Spider(city)
    pass

  def Spider(self, mainUrl):
    response = requests.get(mainUrl, headers=headers)
    html = response.text
    path_name = self.ui.pathLineEdit.text()
    dir_name = re.findall('<link rel="alternate".*?href="(.*?)">', html)[-1].split('/')[-1]
    if not os.path.exists(dir_name):
      os.mkdir(dir_name)
      pass

    urls = re.findall('<img src="(.*?)" alt=".*?">', html)
    urls = [url for url in urls if url[:5] == 'https']

    for url in urls:
      '''获取图片的名字'''
      time.sleep(0.5)
      file_name = url.split('/')[-1].split('?')[0]
      self.ui.textEdit.append("asdadasdasdas")
      print(path_name + '\\' + dir_name + '\\' + file_name)
      response = requests.get(url, headers=headers)
      with open(dir_name + '/' + file_name, 'wb') as f:
        f.write(response.content)
        pass
      pass
    pass



app = QApplication([])
app.setWindowIcon(QIcon('logo.jpeg'))
sp = Spider()
sp.ui.show()
app.exec_()
