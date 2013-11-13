#coding=utf8
from selenium import selenium
import time

class Maker(object):
    def __init__(self):
        self.selenium = selenium("localhost", 4444, "*chrome", "http://epub.cnki.net/")
    
    def check_words(self, words=''):
        self.selenium.start()
        sel = self.selenium
        sel.open("/KNS/brief/result.aspx?dbprefix=scdb&action=scdbsearch&db_opt=SCDB")
        time.sleep(5)
        sel.click("id=txt_1_sel")
        sel.select("id=txt_1_sel", u"label=全文")
        sel.type("id=txt_1_value1", unicode(words, 'utf8'))
        sel.click("id=btnSearch")
        time.sleep(10)
        result = sel.get_text("css=div.TitleLeftCell > div.pagerTitleCell")
        self.selenium.stop()
        result = result.split(' ')[1].replace(',', '')
        return int(result)

def test():
    maker = Maker()
    print maker.check_words('云计算')

if __name__ == "__main__":
    test()
