#!/usr/bin/env python

import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from lxml import html 

class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit() 


url = 'https://www.hackerrank.com/contests'  
#This does the magic.Loads everything
r = Render(url)  
#result is a QString.
result = r.frame.toHtml()

#QString should be converted to string before processed by lxml
formatted_result = str(result.toAscii())

#Next build lxml tree from formatted_result
tree = html.fromstring(formatted_result)

#Now using correct Xpath we are fetching URL of archives
archive_links = tree.xpath('//*[@id="content"]/div/div/div/div[3]/div/div/div[1]/div/div[1]/ul/li[2]/div[1]/div[2]/span/span/time')
print (archive_links[0].text_content())

#div.campaign:nth-child(1) > a:nth-child(1)