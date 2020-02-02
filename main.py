import mechanize
#import ssl
import os
import requests

'''
import urllib
#ssl._create_default_https_context = ssl._create_unverified_context
page=0
full_html=''
full_list=[]
tot=str(len(full_list))
debug=True
from datetime import datetime
past=False
box=''
confirm_list=[]
browser=''
now=''
'''
print dir(requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS)
print requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS
#requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS=('ALL:@SECLEVEL=0')
#requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS=('DES-CBC3-SHA')
print requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS
#from urllib.requests import urlopen
import ssl
print(ssl.OPENSSL_VERSION_INFO)
#print 'kevin'
#url = 'https://www.thinkrhino.com/employee/lasvegas/index.aspx'
#print dir(ssl)
#ctx=ssl.SSLContext(ssl.PROTOCOL_TLS)
#print dir(ctx)
#ssl._create_default_https_context = ssl._create_unverified_context
ssl.verify=False
#print "OMG",ssl._DEFAULT_CIPHERS
#ssl._DEFAULT_CIPHERS = ('DES-CBC3-SHA')
#ssl._DEFAULT_CIPHERS = ('ALL:@SECLEVEL=0')
#ctx.get_ciphers()
#print "WTF",ssl._DEFAULTCIPHERS
#ctx = ssl.SSLContext()
#ctx.set_ciphers('ALL:@SECLEVEL=0')
#ctx.set_ciphers('ALL:@SECLEVEL=0')
url = 'https://www.thinkrhino.com/employee/lasvegas/index.aspx'
#r=requests.get(url)
#print r.headers
#print (len(r.text))
#print r.text
#b=open('temp23.txt','w')
#b.close()
#value=unicode(r.text,'utf-8')
#v=r.text
#v=v.encode('utf-8')
#print v
#b=open('temp23.txt','wb')
#b.write(v)
'''
payload={'emailaddress': 'kevincwulff@gmail.com','mypassword':'blink182'}
r=requests.post("https://www.thinkrhino.com/employee/lasvegas/index.aspx",data=payload)
v= r.text.encode('utf-8')
print v

b=open('temp23.txt','wb')
b.write(v)
'''



from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen



class CustomScreen(Screen):
    hue = NumericProperty(0)


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''

class SelectableLabel(RecycleDataViewBehavior, GridLayout,Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(True)
    selectable = BooleanProperty(True)
    cols = 6

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        #print index
        self.label1_text = data['label1']['text']
        self.label2_text = data['label2']['text']
        self.label3_text = data['label3']['text']
        self.label4_text = data['label4']['text']
        self.label5_text = data['label5']['text']
        self.label6_text = data['label6']['text']
        #self.label2_text = data['label2']['text']
        #self.ids['id_label3'].text = data['label3']['text']  # As an alternate method of assignment
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            popup = Popup(title='Test popup',
                          content=Label(text='Hello world'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()
            #pass
            #print("selection changed to {0}".format(rv.data[index]))
        else:
            pass
            #print("selection removed for {0}".format(rv.data[index]))





class FirstScreen():
    pass
class wow():
    pass



from functools import wraps
class RV(Screen):

    def parse():
        '''
        date1=''
        time1=''
        job1=''
        show1=''
        venue1=''
        loc1=''
        client1=''
        type1=''
        pos1=''
        status1=''
        notes1=''
        '''

        aaa = open('test2.html', 'r')
        ab = aaa.read()
        # print ab
        ab, junk = split(ab, 'Back to previous page')
        part = split(ab, '<tr')
        x = 0
        o = 0
        for i in range(2, len(part) - 1):
            # for i in range(1,5):
            stuff = []
            # print i,' LINE'
            # print part[i]
            # print part[i]
            c = part[i]
            c = split(c, '<')
            # print part[i]
            print
            for d in range(len(c)):
                # print c[d]
                try:
                    a, b = split(c[d], '">')
                    # print b,
                    stuff.append(b)
                except:
                    1
                    # print c[d]
                '''
                try:
                    a,b=split(c[d],'">')
                    #print b
                    if len(b)>0:
                        #print b

                        b=replace(b,'&nbsp;','   ')
                        b=replace(b,';',';\n')

                        stuff.append(b)

                except:
                    'crap'


            print stuff
    '''
            print
            stuff
            if '\r\n\t\t\t' in stuff[0]:
                stuff.remove('\r\n\t\t\t')
                print
                'FUCK YOUFF YOWRE'
            try:

                junk = stuff[13]

                date1 = stuff[0 + o]
                time1 = stuff[1 + o]
                job1 = stuff[2 + o]
                show1 = stuff[3 + o]
                venue1 = stuff[4 + o]
                loc1 = stuff[5 + o]
                client1 = stuff[6 + o]
                type1 = stuff[7 + o]
                pos1 = stuff[8 + o]
                status1 = stuff[10 + o]
                notes1 = stuff[11 + o]


            except:

                date1 = stuff[0]
                time1 = stuff[1]
                job1 = stuff[2]
                show1 = stuff[3]
                venue1 = stuff[4]
                loc1 = stuff[5]
                client1 = stuff[6]
                type1 = stuff[7]
                pos1 = stuff[8]
                status1 = stuff[10]
                notes1 = stuff[11]
                print
                "SSDFSFSDFSDFSDF"

            # print junk
            print
            date1

            if date1 == 'Date' or date1 == '0':
                # print 'init'
                'junk'
            else:
                print
                date1, '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
                print
                date1
                try:
                    m, d, y = split(date1, '/')
                    date1 = y + '/' + m + '/' + d
                except:
                    print
                    date1, 'SDLFKJ :SDLKFJ:SLDKFJ:SLKFDJ:LSKFD'

                joob = date1 + ' ' + time1 + ' ~ ' + venue1 + ' ~ ' + loc1 + ' ~ ' + show1 + ' ~  ' + client1 + ' ~ ' + type1 + ' ~ ' + pos1 + ' ~ ' + status1 + ' ~ ' + job1 + ' ~ ' + notes1

                print
                joob
                check(joob, date1, time1, venue1, loc1, show1, type1, status1, pos1, notes1, client1)

    pass
class RaV(Screen):
    pass
class RVScreen(Screen):
    pass

class SettingScreen(Screen):
    pass
class LoginScreen(Screen):
    def sslwrap(self,func):
        @wraps(func)
        def bar(*args, **kw):
            kw['ssl_version'] = ssl.PROTOCOL_TLSv1
            return func(*args, **kw)

        return bar




    def getdate(self, msg):

        today = date.today()

        # print dir(self.ids.items)
        self.lbl.text = str(today)
    def loadcache(self,b,c,d):
        c = App.get_running_app().storage()
        print(dir(c))
        b = open(str(c) + 'cache.html', 'r')
        for line in b.readlines():
            print line

    def login(self,b,c,d):
        print 'calculate'
        #import  urllib3
        ssl.wrap_socket = self.sslwrap(ssl.wrap_socket)

        #requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = ('DES-CBC3-SHA')

        #print (urllib3.util.ssl_.DEFAULT_CIPHERS),'urldc'

        global now
        #ssl._DEFAULT_CIPHERS = ('DES-CBC3-SHA')
        ssl.verify=False
        #print ssl._DEFAULT_CIPHERS,'dc'
        global browser
        print(ssl.OPENSSL_VERSION_INFO),'test'
        #ssl._create_default_https_context
        print
        print
        print
        print (ssl.SSLSocket.cipher)
        #print dir(ssl_.wrap_socket)
        #print poo

        #PE_LOGIN = 'http://www.thinkrhino.com/employee/lasvegas/'
        PE_LOGIN = 'https://www.thinkrhino.com/employee/lasvegas/index.aspx'
        PE_COUNTRIES = 'https://www.thinkrhino.com/employee/lasvegas/Schedule.aspx'
        #PE_LOGIN='http://google.com'
        #PE_COUNTRIES='https://yahoo.com'
        import operator
        print c.text

        USERNAME = c.text
        PASSWORD = d.text
        dir_path = os.path.dirname(os.path.realpath(__file__))
        #aaa=open(dir_path+'/test2.html','wb')
        browser = mechanize.Browser()
        #print dir(browser)
        pass
        browser.set_handle_robots(False)
        browser.set_handle_equiv(False)
        browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        browser.open(PE_LOGIN)

        browser.select_form(name="ctl00")
        browser['emailaddress'] = USERNAME
        browser['mypassword'] = PASSWORD
        #print (browser)
        #print browser.title

        res = browser.submit()
        #print dir(res)
        #print res.header_items
        #print res.get_data()

        res = browser.open(PE_COUNTRIES)
        aa= res.get_data()   # HTML source of the page

        print (browser,'REAL BROWSER')

        #now= (datetime.now())
        print (aa)

        c = App.get_running_app().storage()
        print(dir(c))
        b = open(str(c) + 'cache.html', 'w')
        b.write(aa)
        b.close()


        return aa



class MyScreenManager(ScreenManager):
    pass

class SwitchingScreenApp(App):
    '''
    def build_config(self, config):
        config.setdefaults('section1', {
            'key1': 'value1',
            'key2': '42'
        })
    '''

    def storage(self):
        return self.user_data_dir

    def build(self):
        # a=self.get_application_config()
        # self.get_application
        # print ((a),'omg')
        # print (type(a))
        # b=open(a,'w')
        # b.write('omg')
        # b.close()

        return MyScreenManager()


if __name__ == "__main__":
    SwitchingScreenApp().run()
