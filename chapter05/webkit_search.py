#coding:utf-8

try:
    from PySide.QtGui import QApplication
    from PySide.QtCore import QUrl, QEventLoop, QTimer
    from PySide.QtWebKit import QWebView
except ImportError:
    from PyQt4.QtGui import QApplication
    from PyQt4.QtCore import QUrl, QEventLoop, QTimer
    from PyQt4.QtWebKit import QWebView
import lxml.html as lm

def main():
    '''
    首先设置搜索参数和模拟动作事件，获取在此参数和动作下搜索后得到的网页
    然后在这网页下，获取数据
    '''
    app = QApplication([])
    webview = QWebView()
    loop = QEventLoop()
    webview.loadFinished.connect(loop.quit)
    webview.load(QUrl('http://example.webscraping.com/places/default/search'))
    loop.exec_()

    webview.show()## 显示渲染窗口，,可以直接在这个窗口里面输入参数，执行动作，方便调试
    frame = webview.page().mainFrame()
    ## 设置搜索参数
    # frame.findAllElements('#search_term') ##寻找所有的search_term框，返回的是列表
    # frame.findAllElements('#page_size option:checked')
    # ## 表单使用evaluateJavaScript()方法进行提交，模拟点击事件
    # frame.findAllElements('#search')

    frame.findFirstElement('#search_term').setAttribute('value', '.') ##第一个search_term框
    frame.findFirstElement('#page_size option:checked').setPlainText('1000') ##第一个page_size框
    ## 表单使用evaluateJavaScript()方法进行提交，模拟点击事件
    frame.findFirstElement('#search').evaluateJavaScript('this.click()') ##第一个点击框

    ## 轮询网页，等待特定内容出现
    ## 下面不断循环，直到国家链接出现在results这个div元素中，每次循环都会调用app.processEvents()
    ##用于给QT事件执行任务的时间，比如响应事件和更新GUI
    elements = None
    while not elements:
        app.processEvents()
        elements = frame.findAllElements('#results a') ##查找下载网页内的所有a标签
    countries = [e.toPlainText().strip() for e in elements] ##取出所有a标签内的文本内容
    print countries


if __name__ == '__main__':
    main()
'''
# -*- coding: utf-8 -*-

try:
    from PySide.QtGui import QApplication
    from PySide.QtCore import QUrl, QEventLoop, QTimer
    from PySide.QtWebKit import QWebView
except ImportError:
    from PyQt4.QtGui import QApplication
    from PyQt4.QtCore import QUrl, QEventLoop, QTimer
    from PyQt4.QtWebKit import QWebView


def main():
    app = QApplication([])
    webview = QWebView()
    loop = QEventLoop()
    webview.loadFinished.connect(loop.quit)
    webview.load(QUrl('http://127.0.0.1:8000/places/default/search'))
    loop.exec_()

    webview.show()
    frame = webview.page().mainFrame()
    frame.findFirstElement('#search_term').setAttribute('value', '.')
    frame.findFirstElement('#page_size option:checked').setPlainText('1000')
    frame.findFirstElement('#search').evaluateJavaScript('this.click()')

    elements = None
    while not elements:
        app.processEvents()
        elements = frame.findAllElements('#results a')
    countries = [e.toPlainText().strip() for e in elements]
    print countries


if __name__ == '__main__':
    main()
'''
