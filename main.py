# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
import string
import ssl
import mechanize
from functools import wraps
import os
from bs4 import BeautifulSoup




#items_1 = set()
#items_2 = set()
#items_3 = set()
#items_4 = set()
items_0=[]
items_1=[]
items_2=[]
items_3=[]
items_4=[]
items_5=[]
items_6=[]
items_7=[]
items_8=[]
items_9=[]
items_10=[]
items_11=[]
items_12=[]
items_13=[]
items_14=[]

print type(items_1),"WOWOWOWOWOWOOWOWOW"
#items_1.add()
#items_2.add()
data={}

gdate1={'',}
gtime1={'',}
gjob1={'',}
gshow1={'',}
gvenue1={'',}
gloc1={'',}
gclient1={'',}
gtype1={'',}
gpos1={'',}
gstatus1={'',}
gnotes1={'',}

#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

import unicodedata



def safeStr(obj):
    try: return str(obj)
    except UnicodeEncodeError:
        return obj.encode('ascii', 'ignore').decode('ascii')
    except: return ""



def check( joob, date12, time12, venue12, loc12, show12, type12, status12, pos12, notes12, client12, job12):
    global gdate1
    gdate1.add(date12)

    global gtime1
    gtime1.add(time12)

    global gvenue1
    gvenue1.add(venue12)

    global gloc1
    gloc1.add(loc12)


    print date12,time12,venue12,'LOCAL HERO'
import io
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
    c = App.get_running_app().storage()
    print((c))
    with io.open(c + 'cache.html', 'r',encoding='utf-8') as f:

        aaa=f.read()


    #print type(aaa)
    aaa=aaa.replace(u'\u2019',"'")
    aaa=aaa.replace(u'\xa9','c')
    aaa=aaa.replace('©','cc')
    #print aaa
    #print aaa
    #from pyquery import PyQuery
    #html = aaa
    #pq = PyQuery(html)
    soup = BeautifulSoup(aaa, 'html.parser')
    #print(soup.prettify())
    a= list(soup.children)
    zz= soup.select('tr')
    #print zz
    #print len(zz)
    onejob=[]
    print type(onejob)
    onejob=[]
    print type(onejob)
    for g in range(len(zz)):
        #print g/14,(g%14)-1,zz[g]
        #print type(zz)
        a2=(zz[g])
        #print dir(a2)
        az3=list(a2.children)
        #print az3
        job = []
        for j in range(len(az3)):

            az4= az3[j]
            try:
                #print az4.text
                job.append(az4.text)
                #onejob[g]=appendaz4.text
            except:
                ''
                #print az4,'loll'
            #print dir(az4)
        print len(job)
        onejob.append(job)
    #print onejob
        #print g
    for q in range(1,len(onejob[0])-1):
        #items_1.add( onejob[q][1])
        #items_2.add(onejob[q][2])
        #items_3.add(onejob[q][3])
        #items_4.add(onejob[q][4])
        items_0.append(onejob[q][0])
        items_1.append( onejob[q][1])
        items_2.append(onejob[q][2])
        items_3.append(onejob[q][3])
        items_4.append(onejob[q][4])
        items_5.append(onejob[q][5])
        items_6.append(onejob[q][6])
        items_7.append(onejob[q][7])
        items_8.append(onejob[q][8])
        items_9.append(onejob[q][9])
        items_10.append(onejob[q][10])
        items_11.append(onejob[q][11])
        items_12.append(onejob[q][12])
        items_13.append(onejob[q][13])
        #items_14.append(onejob[q][14])
    '''
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
            print 'wfff'
            "SSDFSFSDFSDFSDF"
    '''
    '''

        # print junk
        print
        date1

        if date1 == 'Date' or date1 == '0':
            # print 'init'
            'junk'
        else:
            print date1, '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
            print
            date1
            try:
                m, d, y = string.split(date1, '/')
                date1 = y + '/' + m + '/' + d
            except:
                print date1
                print die
                #date1, 'SDLFKJ :SDLKFJ:SLDKFJ:SLKFDJ:LSKFD'
    '''

    #joob = date1 + ' ' + time1 + ' ~ ' + venue1 + ' ~ ' + loc1 + ' ~ ' + show1 + ' ~  ' + client1 + ' ~ ' + type1 + ' ~ ' + pos1 + ' ~ ' + status1 + ' ~ ' + job1 + ' ~ ' + notes1
    #print joob

    #check(joob, date1, time1, venue1, loc1, show1, type1, status1, pos1, notes1, client1, job1)


class FirstScreen(Screen):
    def sslwrap(self,func):
        @wraps(func)
        def bar(*args, **kw):
            kw['ssl_version'] = ssl.PROTOCOL_TLSv1
            return func(*args, **kw)

        return bar
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
        print type(aa)
        print (dir(res))
        print res.info
        u=''
        for i in res.readlines():
            #print i
            try:
                if "allrights" in i or 'copyright -' in i or 'ino Women’s Cold Crew P' in i:
                    print i,'copy1'
                    i=''


                i=i.encode('utf-8')
                u=u+(i)
            except:

                print 'fauil',i



        c = App.get_running_app().storage()
        print((c))
        b = open(str(c) + 'cache.html', 'w')
        b.write(u)
        b.close()







    def loadcache(self,a, b,c):
        self.parse()
        print date1
        #a, b
    pass

class SecondScreen(Screen):
    pass
class ThirdScreen(Screen):
    pass

class FourthScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(FirstScreen())
sm.add_widget(SecondScreen())
sm.add_widget(ThirdScreen())
sm.add_widget(FourthScreen())



class MyScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        Clock.schedule_once(self.screen_switch_one, 2)

    def screen_switch_one(self, dt):
        self.current = '_first_screen_'
        #Clock.schedule_once(self.screen_switch_two, 2)

    def screen_switch_two(self, dt):
        self.current = '_second_screen_'
        self.ids.first_screen.ids.first_screen_label.text = "Hi I'm The Fifth Screen"
        #Clock.schedule_once(self.screen_switch_three, 2)

    def screen_switch_three(self, dt):
        self.current = '_third_screen_'
        #Clock.schedule_once(self.screen_switch_four, 2)

    def screen_switch_four(self, dt):
        self.current = '_fourth_screen_'
        #Clock.schedule_once(self.screen_switch_one, 2)





class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, GridLayout):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    cols = 9

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        #self.label1_text = str(index)
        #self.label2_text = data['label2']['text']
        self.ids['id_label1'].text = data['label1']['text']  # As an alternate method of assignment
        self.ids['id_label2'].text = data['label2']['text']  # As an alternate method of assignment
        self.ids['id_label3'].text = data['label3']['text']  # As an alternate method of assignment
        self.ids['id_label4'].text = data['label4']['text']  # As an alternate method of assignment
        self.ids['id_label5'].text = data['label5']['text']  # As an alternate method of assignment
        self.ids['id_label6'].text = data['label6']['text']  # As an alternate method of assignment
        self.ids['id_label7'].text = data['label7']['text']  # As an alternate method of assignment
        self.ids['id_label8'].text = data['label8']['text']  # As an alternate method of assignment
        self.ids['id_label9'].text = data['label9']['text']  # As an alternate method of assignment
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
            print("selection changed to {0}".format(rv.data[index]))

            print len(gdate1),'date1'
            print len(gtime1),'gtime1'
            print len(gjob1),'gjob1'
            print len(gvenue1),'gvenue1'
            print len(rv.data),'data'
        else:
            print("selection removed for {0}".format(rv.data[index]))


class RV(RecycleView):
    def __init__(self, **kwargs):
        self.data = []
        parse()
        print "TESTTESTTESTTEST"

        super(RV, self).__init__(**kwargs)
        global items_2
        global items_1
        #global date1
        #global job1
        #global venue1
        #print time1
        print gvenue1
        paired_iter = zip(items_0,items_1, items_2,items_3,items_4,items_5,items_6,items_7,items_8,items_9,items_10,items_11,items_12,items_13)
        print paired_iter,"HOLYCRAPMAN"
        #
        for i0,i1, i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13 in paired_iter:
            d = {'label1': {'text': i0},'label2': {'text': i1}, 'label3': {'text': i2}, 'label4': {'text': i3},'label5': {'text': i4},'label6': {'text': i5},'label7': {'text': i6},'label8': {'text': i7},'label9': {'text': i8}}
            #d = {'label1': {'text': i0},'label2': {'text': i1}, 'label3': {'text': i2}, 'label4': {'text': i3},'label5': {'text': i4},'label6': {'text': i5}}

            self.data.append(d)
            print 'wtf man'
        # can also be performed in a complicated one liner for those who like it tricky
        # self.data = [{'label2': {'text': i1}, 'label3': {'text': i2}} for i1, i2 in zip(items_1, items_2)]



class TestApp(App):
    def build(self):

        return MyScreenManager()
    def storage(self):
        return self.user_data_dir

if __name__ == '__main__':
    TestApp().run()
