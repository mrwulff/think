# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
# from kivy.utils import utils
from kivy.utils import get_color_from_hex as rgb

from kivy.properties import BooleanProperty, ListProperty, ObjectProperty, NumericProperty, DictProperty

from kivy.uix.recycleboxlayout import RecycleBoxLayout

from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout

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
from time import *
index = 99
browser=''
# items_1 = set()
# items_2 = set()
# items_3 = set()
# items_4 = set()
items_0 = []
items_1 = []
items_2 = []
items_3 = []
items_4 = []
items_5 = []
items_6 = []
items_7 = []
items_8 = []
items_9 = []
items_10 = []
items_11 = []
items_12 = []
items_13 = []
items_14 = []
items_15 = []
items_16 = []

##print
type(items_1), "WOWOWOWOWOWOOWOWOW"
# items_1.add()
# items_2.add()
data = {}

gdate1 = {'', }
gtime1 = {'', }
gjob1 = {'', }
gshow1 = {'', }
gvenue1 = {'', }
gloc1 = {'', }
gclient1 = {'', }
gtype1 = {'', }
gpos1 = {'', }
gstatus1 = {'', }
gnotes1 = {'', }
index5=101
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import unicodedata

onejob = []

from datetime import datetime
import humanize


def safeStr(obj):
    try:
        return str(obj)
    except UnicodeEncodeError:
        return obj.encode('ascii', 'ignore').decode('ascii')
    except:
        return ""


def check(joob, date12, time12, venue12, loc12, show12, type12, status12, pos12, notes12, client12, job12):
    global gdate1
    gdate1.add(date12)

    global gtime1
    gtime1.add(time12)

    global gvenue1
    gvenue1.add(venue12)

    global gloc1
    gloc1.add(loc12)

    ##print
    date12, time12, venue12, 'LOCAL HERO'


import io


def loadcache2(self, a, b, c):
    parse()

def check_time(date, time):
    time = str(time)
    time2 = (time)
    date = str(date)

    ##print(date, time)

    d1, d2, d3 = str.split(date, '/')
    newd = d1 + '/' + d2

    t1, t2 = str.split(time2, ':')
    if int(t1) > 12:
        ###print('over12 ', t1)
        t1 = int(t1) - 12
        time2 = str(t1) + ':' + t2 + ' PM'
    else:
        time2 = time2 + ' AM'
    ##print
    time2

    aa = datetime.strptime(date + ' ' + time, '%m/%d/%Y %H:%M')
    # ##print (aa)

    now = (datetime.now())

    diff = now - aa

    global past
    diffh = humanize.naturaltime(now - aa)
    past = False
    neg = (str(diff)[0])
    if neg == '-':
        past = True

        diff2 = -diff
    else:
        diff2 = diff
    day = ''


    try:
        day, hours = str.split(str(diff2), ' days, ')
        hours = str(hours)
        if int(day) == 1:
            day = day + ' day, '
        else:
            day = day + ' days, '



    except:
        try:
            # ##print(diff2, 'GODAMN')
            hours = str(diff2)
            # ##print('`````````````0 days')
        except:

            day, hours = str.split(str(diff2), ' day, ')
            # ##print('``````````1 day')
    # ##print("NNNNNN")

    hours, minutes, junk = str.split(hours, ':')
    # ##print(hours)
    # ##print("OOOOOOOOO")
    hours = str(hours)
    if hours == '0':



        hours = ''
    else:
        # ##print(hours, '    hours')
        try:
            day, hours = str.split(hours, ', ')
            day = day + ', '
        except:
            ###print('dumb')
            pass
        # ##print hours
        ##hours = str(int(hours))
        if int(hours) == 1:
            hours = hours + ' hour '
        else:
            hours = hours + ' hours '
    # ##print('asdfadsf')
    if str(minutes) == 1:
        minutes = str(int(minutes)) + ' minute'
    else:
        minutes = str(int(minutes)) + ' minutes'
    # ##print('erererer')

    if past == False:
        # ##print('ok')
        try:
            a = day + hours + minutes + ' Ago'
        except:
            a = 'ERROR'
        # ##print('no2')
    else:
        # ##print('no3')
        try:
            a = day + hours + minutes + ' Away'
        except:
            a = 'ERROR2'
        # ##print('no4')
    # ##print a
    return (a, time2)
from datetime import *
import time
import humanize
from time import mktime
import webbrowser
#def web(self):
#    webbrowser.open('http://www.anywebsite.domain')
def updated(self,filename):
    if True:
        if filename=='':
            c = App.get_running_app().storage()
            filename=(c + 'cache.html')

        stat=os.stat(filename)
        f= stat.st_mtime
        fc= time.gmtime(f)
        now= time.gmtime()
        fc = datetime.fromtimestamp(mktime(fc))
        now = datetime.fromtimestamp(mktime(now))
        difh=humanize.naturaldelta(now-fc)
        ##print difh
    #MyScreenManager.ids.first_screen.ids.status.text = str('Updated ' + difh + ' ago.')
    ###print dir(self.ids.status)
        return difh
    #except:
     #   return ''
def parse_name():

    c = App.get_running_app().storage()
    ##print((c))
    go=True
    try:
        with io.open(c + 'cache.html', 'r',encoding='utf-8') as f:

            aaa=f.readlines()
            aaa2=f.read()
            ##print('ASSHOLE')
    except:
        ##print 'WTF YOU ASS'
        go=False
        pass
    f=''
    l=''

    if go==True:
        ###print aaa
        for line in aaa:
            ##print line
            if 'lblEmp' in line:
                ##print line
                line=unicode.split(line,'>')
                line=unicode.split(line[1],'<')
                ###print line[0]
                l,f=unicode.split(line[0],', ')
                ###print f,l
        with io.open(c + 'cache.html', 'r', encoding='utf-8') as f2:
            aaa2 = f2.read()
        ###print aaa2
        soup = BeautifulSoup(aaa2, 'html.parser')
        ###print(soup.prettify())
        ####print(soup.prettify())
        a= list(soup.children)
        zz= soup.select('tr')
        ###print str(len (zz))
    if len(f)>0:
        return f,l,str(len (zz))
    else:
        return 'No cache found',''
def parse():
    ##print 'pparse'
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
    ##print App,'App'
    ###print App.get_running_app()
    ###print dir(App.get_running_app())
    ###print App.storage()
    c = App.get_running_app().storage()
    print((c)),'PATH TO SAVE'
    go = True
    try:
        with io.open(c + 'cache.html', 'r', encoding='utf-8') as f:

            aaa = f.read()
    except:
        go = False
        pass

    if go == True:
        items_14=[]
        global onejob
        # ##print type(aaa)
        aaa = aaa.replace(u'\u2019', "'")
        aaa = aaa.replace(u'\xa9', 'c')
        aaa = aaa.replace('©', 'cc')

        soup = BeautifulSoup(aaa, 'html.parser')
        a = list(soup.children)
        zz = soup.select('tr')
        print len(zz)
        if len(zz)<1:
            go=False
    if go==True:


        onejob = []

        for g in range(1,len(zz)-1):
            ###print zz[g],'parser',g

            a2 = (zz[g])
            # ##print dir(a2)
            az3 = list(a2.children)
            # ##print az3
            job = []
            test=[]
            for j in range(len(az3)):
                #print az3[j]

                az4 = az3[j]
                #print az4,'az5',g
                try:

                    job.append(az4.text)

                    if az4.text=='':
                        job.append(az4)
                        #print
                    else:
                        pass
                        #print 'success', az4.text
                    # ##print az4.text

                    # onejob[g]=appendaz4.text
                except:

                    #job.append('Fail')
                    if len(az4)>10:
                        #print 'long',az4
                        job.append(str(az4))
                    if len(az4)<10:
                        #print 'short',az4
                        #print az4,'ax4'
                        test.append(az4)
                    #job.append(az4)
                    #job.append(az4.text)
                    # ##print az4,'loll'
                # ##print dir(az4)
            ###print
            len(job)
            onejob.append(job)
        # ##print onejob
        # ##print g
        #print test,'test'
        if len(onejob) > 0:
            for q in range(1, len(onejob) ):
                #print onejob[q],'onejobq'
                # items_1.add( onejob[q][1])
                # items_2.add(onejob[q][2])
                # items_3.add(onejob[q][3])
                # items_4.add(onejob[q][4])
                items_0.append(onejob[q][0])
                items_1.append(onejob[q][1])
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
                # items_14.append(onejob[q][14])
        #print items_13,'000'
        for z in range(len(items_10)):
            t = items_0[z]
            d = items_1[z]

            try:
                aa, tim2 = check_time(t, d)

                items_14.append(aa)
                items_15.append(tim2)
            except:
                items_14.append('FailTimei')
                items_15.append('FailTime15')



    ###print onejob,'parseone'

    # joob = date1 + ' ' + time1 + ' ~ ' + venue1 + ' ~ ' + loc1 + ' ~ ' + show1 + ' ~  ' + client1 + ' ~ ' + type1 + ' ~ ' + pos1 + ' ~ ' + status1 + ' ~ ' + job1 + ' ~ ' + notes1
    # ##print joob

    # check(joob, date1, time1, venue1, loc1, show1, type1, status1, pos1, notes1, client1, job1)
    try:
        return items_14,items_15
    except:
        return([0],[0])
'''
class MyPopup():
    def web(self):
        ##print 'omg'
    def open(self):
        ##print 'toots'
'''
class FirstScreen(Screen):
    def sslwrap(self, func):
        @wraps(func)
        def bar(*args, **kw):
            kw['ssl_version'] = ssl.PROTOCOL_TLSv1
            return func(*args, **kw)

        return bar

    def login(self, b, c, d):
        ##print
        'calculate'
        # import  urllib3
        ssl.wrap_socket = self.sslwrap(ssl.wrap_socket)

        # requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = ('DES-CBC3-SHA')

        # ##print (urllib3.util.ssl_.DEFAULT_CIPHERS),'urldc'

        global now
        # ssl._DEFAULT_CIPHERS = ('DES-CBC3-SHA')
        ssl.verify = False
        # ##print ssl._DEFAULT_CIPHERS,'dc'
        global browser
        ##print(ssl.OPENSSL_VERSION_INFO), 'test'
        # ssl._create_default_https_context
        ##print
        ##print
        ##print
        ##print(ssl.SSLSocket.cipher)
        # ##print dir(ssl_.wrap_socket)
        # ##print poo

        # PE_LOGIN = 'http://www.thinkrhino.com/employee/lasvegas/'
        PE_LOGIN = 'https://www.thinkrhino.com/employee/lasvegas/index.aspx'
        PE_COUNTRIES = 'https://www.thinkrhino.com/employee/lasvegas/Schedule.aspx'
        # PE_LOGIN='http://google.com'
        # PE_COUNTRIES='https://yahoo.com'
        import operator
        ##print
        c.text

        USERNAME = c.text
        PASSWORD = d.text
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # aaa=open(dir_path+'/test2.html','wb')
        global browser
        browser = mechanize.Browser()
        # ##print dir(browser)
        pass
        browser.set_handle_robots(False)
        browser.set_handle_equiv(False)
        browser.addheaders = [('User-agent',
                               'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        browser.open(PE_LOGIN)

        browser.select_form(name="ctl00")
        browser['emailaddress'] = USERNAME
        browser['mypassword'] = PASSWORD
        # ##print (browser)
        # ##print browser.title

        res = browser.submit()
        # ##print dir(res)
        # ##print res.header_items
        # ##print res.get_data()

        res = browser.open(PE_COUNTRIES)
        aa = res.get_data()  # HTML source of the page

        ##print(browser, 'REAL BROWSER')

        # now= (datetime.now())
        ##print
        type(aa)
        ##print(dir(res))
        ##print
        res.info
        u = ''
        for i in res.readlines():
            # ##print i
            try:
                if "allrights" in i or 'copyright -' in i or 'ino Women’s Cold Crew P' in i:
                    ##print
                    i, 'copy1'
                    i = ''

                i = i.encode('utf-8')
                u = u + (i)
            except:

                ##print
                'fauil', i

        c = App.get_running_app().storage()
        ##print((c))
        b = open(str(c) + 'cache.html', 'w')
        b.write(u)
        b.close()





    def savee(self, a, b, c):
        #parse()
        ###print date1
        # a, b

        if True:
            c = App.get_running_app().storage()
            b = open(c + 'settings.html', 'w')
            print App.get_running_app().root.ids
            print dir(App.get_running_app().root.ids)

            #print self.ids.first_screen.ids.email.text

            b.write(App.get_running_app().root.ids.first_screen.ids.email.text+'##email##\n')
            b.write(App.get_running_app().root.ids.first_screen.ids.password.text+'##password##')


            #self.ids.first_screen.ids.email.text = str(line)
        #except:
            #print
            #'coundt find settings'

    pass
    def loadcache(self,a,b,c):
        parse()

class SecondScreen(Screen):
    # def __init__(self):
    #    ##print 'jesus'
    def wow(self):
        # ##print a
        # ##print'omg'
        ##print
        self
        # ##print dir(self)
        ##print
        self.manager
        ##print(dir(self.manager))
        ##print
        dir(self.manager.screen_names)
        # self.lbl1.text = 'wo2w'
        self.random_number = items_1[3]
        pass

    ##print
    dir(App.get_running_app()), 'trtr'

    app = App.get_running_app()
    ##print
    app, '808'
    ##print(dir(app)), '9009'
    # item_1=['w']*4
    # random_number = item_1[3]


    pass
    def confirm(self):
        confable=False
        print 'ONEJOB',onejob[index5+1],index5
        try:
            ht= onejob[index5 + 1][14]
            h2 = str.split(str(ht), '"')
            confable = True
        except:
            print 'nonconfirmable'
            pass

        if confable==True:
            print type(browser)
            if type(browser)==unicode:
                print(browser, 'browser fail')
            else:
                browser.select_form(name="ctl00")
                print(browser, 'browser 1')
                control_t = browser.form.find_control("__EVENTTARGET")
                control_a = browser.form.find_control("__EVENTARGUMENT")
                print(browser, 'browser 2')
                control_t.readonly = False
                control_a.readonly = False

                control_t.value = str(ht)
                control_a.value = 'Confirm'
                print(browser, 'browser 3')

                response = browser.submit()
                print(browser, 'browser 4')
                aa = response.get_data()
                print(browser, 'browser 5')

                #aaa = open('aaa.html', 'wb')
                #aaa.write((aa))
                #aaa.close()
                #browser.open('test2.html')



class ThirdScreen(Screen):
    #parse()
    ##print 'wow'
    def loadcache(self, a, b, c):
        #camera.take_picture()
        #webbrowser.open('comgooglemapsurl://www.google.com/maps/search/?api=1&query=mgm+grand')
        #webbrowser.open( 'comgooglemapsurl://www.google.com/maps/search/?api=1&query=centurylink+field')
        parse()



class FourthScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(FirstScreen())
sm.add_widget(SecondScreen())
sm.add_widget(ThirdScreen())
sm.add_widget(FourthScreen())

color_ = [.2, .2, .2, 1]
# ##print type(color_1)
# ##print color_1,'wowow'
color_1 = [.1, .1, .1, 1]
clist = [color_, color_1]

#class MyPopup(BoxLayout):
#    def web(self):
#        ##print 'ommmmgg'
#    def open(self):
#        ##print 'what'


class MyScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        Clock.schedule_once(self.screen_switch_one, 0)

    def screen_switch_one(self, dt):
        self.current = '_first_screen_'
        ##print 'loading first screen'
        a = updated(self, '')
        try:
            f, l, j = parse_name()
            ##print a,f,l,j,'parsename'
        except:
            #f, l, j = parse_name()
            f = ''
        #if len(f) > 0:
            #self.ids.first_screen.ids.status.text = str(f + ' ' + l + ':' + j + ' jobs\nUpdated ' + a + ' ago.\n')
        # Clock.schedule_once(self.screen_switch_two, 2)
        root = App.get_running_app().root
        ##print
        root.ids.viewkeys
        ##print
        dir(root.ids.viewkeys)
        print 'why'

        c = App.get_running_app().storage()

        if True:
            email=''
            password=''
            b=open(c + 'settings.html', 'r')

            for line in b.readlines():
                print line
                if '##email##' in line:
                    email,garbage=str.split(line,'##email')
                if '##password##' in line:
                    password, garbage = str.split(line, '##password')

            self.ids.first_screen.ids.email.text = str(email)
            self.ids.first_screen.ids.password.text = str(password)

        #except:
        #    print 'coundt find settings'
        #    b=open(c+'settings.html','w')
        #    b.write('test\ntest')
        #    b.close()
        #    print 'made settings'
        print self.ids.first_screen.ids.email.text
        print self.ids.first_screen.ids.password.text



    def screen_switch_two(self, dt, index):
        global index5
        self.current = '_second_screen_'
        # ##print dt
        # ##print index
        ##print 'piss'
        items_14,items_15=parse()
        ##print items_14

        self.ids.second_screen.ids.second_screen_label.text = str(items_0[index])
        self.ids.second_screen.ids.second_screen_label1.text = items_14[index]
        self.ids.second_screen.ids.second_screen_label2.text = items_1[index]
        self.ids.second_screen.ids.second_screen_label3.text = items_2[index]
        self.ids.second_screen.ids.second_screen_label4.text = items_3[index]
        self.ids.second_screen.ids.second_screen_label5.text = items_4[index]
        self.ids.second_screen.ids.second_screen_label6.text = items_5[index]

        self.ids.second_screen.ids.second_screen_label7.text = items_6[index]
        self.ids.second_screen.ids.second_screen_label8.text = items_7[index]
        self.ids.second_screen.ids.second_screen_label9.text = items_8[index]
        self.ids.second_screen.ids.second_screen_label10.text = items_9[index]
        self.ids.second_screen.ids.second_screen_label11.text = items_10[index]
        self.ids.second_screen.ids.second_screen_label12.text = items_11[index]
        self.ids.second_screen.ids.second_screen_label13.text = items_12[index]
        self.ids.second_screen.ids.second_screen_label14.text = items_13[index]
        ##print
        self.ids.second_screen.ids.second_screen_label10.background_color, 'gtt'

        # self.ids.second_screen.ids.second_screen_label.font_size=10
        ##print
        i = 0
        j = 1
        scl = []

        scl.append(self.ids.second_screen.ids.second_screen_label.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label1.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label2.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label3.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label4.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label5.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label6.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label7.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label8.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label9.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label10.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label11.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label12.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label13.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label14.background_color)
        blankc = [0] * len(scl)
        ##print
        blankc, 'bc', len(scl)
        for q in range(len(scl)):
            if q % 2 == 0:
                # ##print scl[q],'red'
                # scl[q]=color_

                blankc[q] = color_
            else:
                blankc[q] = color_1
            ##print
            scl[q], 'blue'
        ##print
        blankc, 'blankc'
        self.ids.second_screen.ids.second_screen_label4.background_color = blankc[0]
        self.ids.second_screen.ids.second_screen_label1.background_color = blankc[1]
        self.ids.second_screen.ids.second_screen_label.background_color = blankc[2]
        self.ids.second_screen.ids.second_screen_label2.background_color = blankc[3]
        self.ids.second_screen.ids.second_screen_label3.background_color = blankc[4]

        self.ids.second_screen.ids.second_screen_label5.background_color = blankc[5]
        self.ids.second_screen.ids.second_screen_label6.background_color = blankc[6]
        self.ids.second_screen.ids.second_screen_label7.background_color = blankc[7]
        self.ids.second_screen.ids.second_screen_label8.background_color = blankc[8]
        self.ids.second_screen.ids.second_screen_label9.background_color = blankc[9]
        self.ids.second_screen.ids.second_screen_label10.background_color = blankc[10]
        self.ids.second_screen.ids.second_screen_label11.background_color = blankc[11]
        self.ids.second_screen.ids.second_screen_label12.background_color = blankc[12]
        self.ids.second_screen.ids.second_screen_label13.background_color = blankc[13]
        self.ids.second_screen.ids.second_screen_label14.background_color = blankc[14]

        try:
            ##print
            items_13[index], '13'
        except:
            ##print
            'fail13'
        try:
            ##print
            items_12[index], '14'
        except:
            ##print
            'fail14'
        # Clock.schedule_once(self.screen_switch_three, 2)
        index5=index

    def screen_switch_three(self, dt):
        self.current = '_third_screen_'
        # Clock.schedule_once(self.screen_switch_four, 2)

    def screen_switch_four(self, dt):
        self.current = '_fourth_screen_'
        # Clock.schedule_once(self.screen_switch_one, 2)
        '''
    def web(a55):
        ##print 'wowerzs',a55
        ###print 'wow',a,b,index5
        #webbrowser.open('http://www.anywebsite.domain')
        a= onejob[index5+1]
        # ##print a
        ##print a[5]
        b=a[5].replace(' ','+')
        #webbrowser.open('comgooglemapsurl://www.google.com/maps/search/?api=1&query=mgm+grand')

        u='https://www.google.com/maps/search/?api=1&query='+str(b)+''
        ##print u
        # u = 'https://www.go1ogle.com/maps/' + 'mgmgrand' + '"'
        # ##print u
        webbrowser.open(u)
    def email(self):
        a=onejob[index5+1]
        ##print a
        u='https://gmail.com/?subject = [prompt] & body = [prompt]'
        u = 'https://www.google.com/maps/search/?api=1&query=' + str(8) + ''
        u = 'https://www.gmail.com/?api=1&subject=' + str(8) + ''
        to='lvscheduling@gmail.com'
        to='kevincwulff@gmail.com'
        sub='Parking Reimbursment'
        date=a[0]
        job=a[2]
        show=a[3]
        place=a[4]

        u='mailto://'+to+'?subject='+sub+'?body='+date+'\n'+job+'\n'+show+'\n'+place+'\nThanks'
        bo =  date + '\n' + job + '\n' + show + '\n' + place + '\nThanks'
        ##print u
        #Eryka.Adams@Clickdimensions.com?bcc=julie.patrick@clickdimensions.com&subject=RSVP'

        #webbrowser.open(u)
        email.send(recipient=to,
                   subject=sub,
                   text=bo
                   )
    
    def addcal(self):
        a = onejob[index5 + 1]
        date = a[0]
        time = a[1]
        job = a[2]
        show = a[3]
        place = a[4]
        u='https://calendar.google.com/calendar/r/eventedit?text=Your+Event+ Name & dates = '+date+time+' & details ='+date+time+job+show+place+'& location ='+place+ '& sf = true & output = xml & pli = 1'
        ##print u
        u = u.replace(' ', '+')
        ##print u
        webbrowser.open(u)
        '''


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, GridLayout):
    ''' Add selection support to the Label '''
    # global index
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    cols = 9

    def refresh_view_attrs(self, rv, index, data):
        # global index
        ''' Catch and handle the view changes '''
        self.index = index

        # self.label1_text = str(index)
        # self.label2_text = data['label2']['text']
        if index%2==0:
            blank=color_
        else:
            blank=color_1

        self.ids['id_label1'].text = data['label1']['text']  # As an alternate method of assignment
        self.ids['id_label2'].text = data['label2']['text']  # As an alternate method of assignment
        self.ids['id_label3'].text = data['label3']['text']  # As an alternate method of assignment
        self.ids['id_label4'].text = data['label4']['text']  # As an alternate method of assignment
        self.ids['id_label5'].text = data['label5']['text']  # As an alternate method of assignment
        self.ids['id_label6'].text = data['label6']['text']  # As an alternate method of assignment
        # self.ids['id_label10'].text = data['label10']['text']  # As an alternate method of assignment
        self.ids['id_label8'].text = data['label8']['text']  # As an alternate method of assignment
        self.ids['id_label9'].text = data['label9']['text']  # As an alternate method of assignment
        self.ids['id_label11'].text = data['label11']['text']  # As an alternate method of assignment
        blank2=(1,1,1,1)
        b=str((self.ids['id_label1'].text))
        try:
            day = datetime.strptime(b, "%m/%d/%Y")
            ##print type(day),'day'

            today=strftime("%Y-%m-%d",gmtime())
            today=datetime.strptime(today,"%Y-%m-%d")
            ##print type(today),'today'
            ##print day,today
        except:
            day='Failday'
            today='Failtoday'

        try:
            ab10 = str((self.ids['id_label11'].text))
            ab10 = ab10.lower()
        except:
            ab10=''
        ab= str((self.ids['id_label4'].text))
        ###print ab
        ab= ab.lower()

        ##print ab10


        if day>today:
            pass
            ###print 'greater'
            #blank2=[.5,.5,.5,1]
        if today>day:
            ##print 'less'
            blank2=[.5,.5,.6,1]
        if today==day:
            ##print'TODAY'
            blank2 = [.59, .59, .99, 1]
        if 'cancelled' in ab or 'canceled' in ab or 'cancelled' in ab10 or 'canceled' in ab10:

            blank2 = (1, 0, 0, 1)
        if 'called' in ab10 or 'tentative' in ab10:
            blank2 = (0, 1, 0, 1)


        self.ids['id_label1'].color=blank2
        self.ids['id_label2'].color = blank2
        self.ids['id_label3'].color = blank2
        self.ids['id_label4'].color = blank2
        self.ids['id_label5'].color = blank2
        self.ids['id_label6'].color = blank2
        self.ids['id_label8'].color = blank2
        self.ids['id_label9'].color = blank2
        self.ids['id_label11'].color = blank2


        self.ids['id_label1'].background_color=blank
        self.ids['id_label2'].background_color = blank
        self.ids['id_label3'].background_color = blank
        self.ids['id_label4'].background_color=blank
        self.ids['id_label5'].background_color = blank
        self.ids['id_label6'].background_color = blank
        #self.ids['id_label7'].background_color=blank
        self.ids['id_label8'].background_color = blank
        self.ids['id_label9'].background_color = blank
        #self.ids['id_label10'].background_color=blank
        self.ids['id_label11'].background_color = blank


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
            ###print("selection changed to {0}".format(rv.data[index]))
            ##MyScreenManager.screen_switch_two(ScreenManager)
            # ##print dir(MyScreenManager),'msm'
            # ##print dir(MyScreenManager.screen_switch_four)
            # ##print dir(MyScreenManager.current)

            # rint MyScreenManager.current_screen
            # MyScreenManager.current='_second_screen_'
            ##print
            dir(App.get_running_app())
            App.get_running_app().root.screen_switch_two(self, index)

            ##print
            len(gdate1), 'date1'
            ##print
            len(gtime1), 'gtime1'
            ##print
            len(gjob1), 'gjob1'
            ##print
            len(gvenue1), 'gvenue1'
            ##print
            len(rv.data), 'data'
        else:
            pass
            ##print("selection removed for {0}".format(rv.data[index]))


class RV(RecycleView):
    def __init__(self, **kwargs):
        self.data = []
        ##print items_0,len(items_0),'items_0'
        parse()
        ##print items_0,len(items_0),'items_0'
        ##print
        "TESTTESTTESTTEST"

        super(RV, self).__init__(**kwargs)
        global items_2
        global items_1

        gvenue1
        paired_iter = zip(items_0, items_1, items_2, items_3, items_4, items_5, items_6, items_7, items_8, items_9,
                          items_10, items_11, items_12, items_13)
        print items_3
        #print paired_iter, "HOLYCRAPMAN"
        for i in range(len(paired_iter)):
            print paired_iter[i],'man!',i
        #
        for i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13 in paired_iter:
            d = {'label1': {'text': i0}, 'label2': {'text': i1}, 'label3': {'text': i2}, 'label4': {'text': i3},
                 'label5': {'text': i4}, 'label6': {'text': i5}, 'label7': {'text': i6}, 'label8': {'text': i7},
                 'label9': {'text': i8}, 'label10': {'text': i9}, 'label11': {'text': i10}}
            # d = {'label1': {'text': i0},'label2': {'text': i1}, 'label3': {'text': i2}, 'label4': {'text': i3},'label5': {'text': i4},'label6': {'text': i5}}
            print len(d), 'sngle data'

            self.data.append(d)
            ##print
            'wtf man'
        ##print self.data
        ##print 'datadata'
        # can also be performed in a complicated one liner for those who like it tricky
        # self.data = [{'label2': {'text': i1}, 'label3': {'text': i2}} for i1, i2 in zip(items_1, items_2)]


items2_1 = {'apple', 'banana', 'pear', 'pineapple'}
items2_2 = {'dog', 'cat', 'rat', 'bat'}

from plyer import camera
from plyer import email

class TestApp(App):
    def build(self):
        return MyScreenManager()

    def storage(self):
        return self.user_data_dir
    #def web(self,a,b):
        ###print 'wow',a,b,index5
        #webbrowser.open('http://www.anywebsite.domain')
        #a= onejob[index5+1]
        ###print a
        ###print a[5]
        #ab=a[5].replace(' '+'+')
        #u='https://www.googl1e.com/maps/dir/?api=1&"'+str(a[5])+'"'
        #u = 'https://www.go1ogle.com/maps/' + 'mgmgrand' + '"'
        ###print u
        #webbrowser.open(u)
        #webbrowser.open('http://www.anywebsite.domain')
        #camera.take_picture()
        #email.send()



if __name__ == '__main__':
    TestApp().run()