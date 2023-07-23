from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Qt
from wmian_ui import Ui_Form
import time
import requests
import os
import re


class MainWindow(QMainWindow,Ui_Form):
    list = []
    urls = []
    sum = 0
    path = ''
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.file.clicked.connect(self.readurl)
        self.dir.clicked.connect(self.selectdir)
        self.down.clicked.connect(self.download)
        self.open.clicked.connect(self.openfile)
    
    def readurl(self):
        filename = QFileDialog.getOpenFileName(self, '选择文件', './', 'Text files(*.txt)')
        print(filename)
        with open(filename[0], 'r') as f:
            self.urls = f.readlines()
        # 删除换行符的元素
        for i in range(len(self.urls)):
            self.urls[i] = self.urls[i].strip('\n')
    
    def selectdir(self):
        dirname = QFileDialog.getExistingDirectory(self, '选择文件夹', './')
        self.path = dirname

    def download(self):
        if(self.urls == [] and self.textEdit.toPlainText() == '请输入包含https:\\\\的网址'):
            self.result.setText('请先选择文件或输入链接')
            QApplication.processEvents()
            return
        elif(self.urls == [] and self.textEdit.toPlainText() != '请输入包含https:\\\\的网址'):
            self.urls = self.textEdit.toPlainText().split('\n')
        headers = {'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/5.2.380'}
        for i in range(len(self.urls)):
            self.result.setText(f'正在查找图片...{i+1}/{len(self.urls)}')
            QApplication.processEvents()
            if(self.urls[i] != ''):
                try:
                    r = requests.get(self.urls[i],headers=headers)
                    r.raise_for_status()
                    r.encoding = r.apparent_encoding
                    html = r.text
                except:
                    self.result.setText('error')
                    QApplication.processEvents()
                else:
                    pic = re.findall(r'data-src="(.*?)" data-type="jpg"',html)
                    for i in pic:
                        self.list.append(i)
                        self.sum += 1
        self.result.setText(f'查找完成，共找到{self.sum}张图片')
        QApplication.processEvents()
        time.sleep(1)
        if self.path == '':
            self.path = os.getcwd()
            self.path = self.path + '\\picture'
            if not os.path.exists(self.path):
                os.mkdir(self.path)
        os.chdir(self.path)
        print(self.path)
        self.result.setText('开始下载图片')
        QApplication.processEvents()
        for i in range(len(self.list)):
            self.result.setText(f'正在下载图片...{i+1}/{len(self.list)}')
            QApplication.processEvents()
            QApplication.processEvents()
            try:
                r = requests.get(self.list[i])
                r.raise_for_status()
                r.encoding = r.apparent_encoding
                filename = str(i) + '.jpg'
                with open(filename,'wb') as f:
                    f.write(r.content)
            except:
                self.result.setText('下载失败')
                QApplication.processEvents()
        self.result.setText('下载完成')

    def openfile(self):
        os.startfile(self.path)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.setWindowFlags(window.windowFlags() & ~Qt.WindowMaximizeButtonHint)
    window.show()
    app.exec_()