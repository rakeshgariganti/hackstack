from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *
import sys
class browser():
    #Browser slots
    @staticmethod
    def browserurlchanged(self,url):
        self.browseraddress.setText(url.toString())
    @staticmethod
    def browserseturl(self,url):
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.browseraddress.setText(url)
        self.view.load(QUrl(url))
    @staticmethod
    def browseraddresschanged(self):
        url = self.browseraddress.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.view.load(QUrl(url))
    @staticmethod
    def browsertogglereload(self):
        pass
