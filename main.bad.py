#from __future__ import unicode_literals

from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior


from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
#from kivy.utils import utils
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

grv=''
index=99
gdata=''
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
items_15=[]
items_16=[]

#print type(items_1),"WOWOWOWOWOWOOWOWOW"
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
rv=''
#import sys

import unicodedata

onejob=[]
#data=[]
#from datetime import datetime,
from time import mktime

from datetime import *
import time
import humanize

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


    #print date12,time12,venue12,'LOCAL HERO'
import io

def updated(self,filename):
    try:
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
        print difh
    #MyScreenManager.ids.first_screen.ids.status.text = str('Updated ' + difh + ' ago.')
    #print dir(self.ids.status)
        return difh
    except:
        return ''

def check_time(date,time):
    time=str(time)
    time2 = (time)
    date=str(date)

    #print (date,time)

    d1, d2, d3 = str.split(date, '/')
    newd = d1 + '/' + d2

    t1, t2 = str.split(time2, ':')
    if int(t1) > 12:
        #print('over12 ', t1)
        t1 = int(t1) - 12
        time2 = str(t1) + ':' + t2 + ' PM'
    else:
        time2 = time2 + ' AM'
    #print time2

    aa = datetime.strptime(date + ' ' + time, '%m/%d/%Y %H:%M')
    # #print (aa)

    now = (datetime.now())

    diff = now-aa
    #print diff
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
    hours = ''
    minutes = ''
    ##print("MMMMM ", diff2)


    try:
        day, hours = str.split(str(diff2), ' days, ')
        hours=str(hours)
        if int(day) == 1:
            day = day + ' day, '
        else:
            day = day + ' days, '
        ##print('``````many days')


    except:
        try:
            ##print(diff2, 'GODAMN')
            hours = str(diff2)
            ##print('`````````````0 days')
        except:
            ##print('35234523452345234523452345')
            ##print(diff2, '         WHY THE FUCK')
            day, hours = str.split(str(diff2), ' day, ')
            ##print('``````````1 day')
    ##print("NNNNNN")

    hours, minutes, junk = str.split(hours, ':')
    ##print(hours)
    ##print("OOOOOOOOO")
    hours=str(hours)
    if hours == '0':

        ##print('ppppppppppp')

        hours = ''
    else:
        ##print(hours, '    hours')
        try:
            day, hours = str.split(hours, ', ')
            day = day + ', '
        except:
            pass
            #print('dumb')
        ##print hours
        ##hours = str(int(hours))
        if int(hours) == 1:
            hours = hours + ' hour '
        else:
            hours = hours + ' hours '
    ##print('asdfadsf')
    if str(minutes) == 1:
        minutes = str(int(minutes)) + ' minute'
    else:
        minutes = str(int(minutes)) + ' minutes'
    ##print('erererer')
    
    

    if past == False:
        ##print('ok')
        try:
            a = day + hours + minutes + ' Ago'
        except:
            a = 'ERROR'
        ##print('no2')
    else:
        ##print('no3')
        try:
            a = day + hours + minutes + ' Away'
        except:
            a = 'ERROR2'
        ##print('no4')
    ##print a
    return (a, time2)
def parse_name():

    c = App.get_running_app().storage()
    print((c))
    go=True
    try:
        with io.open(c + 'cache.html', 'r',encoding='utf-8') as f:

            aaa=f.readlines()
            aaa2=f.read()
    except:
        go=False
        pass
    f=''
    l=''

    if go==True:
        #print aaa
        for line in aaa:
            #print line
            if 'lblEmp' in line:
                #print line
                line=unicode.split(line,'>')
                line=unicode.split(line[1],'<')
                #print line[0]
                l,f=unicode.split(line[0],', ')
                #print f,l
        with io.open(c + 'cache.html', 'r', encoding='utf-8') as f2:
            aaa2 = f2.read()
        #print aaa2
        soup = BeautifulSoup(aaa2, 'html.parser')
        #print(soup.prettify())
        ##print(soup.prettify())
        a= list(soup.children)
        zz= soup.select('tr')
        #print str(len (zz))
    if len(f)>0:
        return f,l,str(len (zz))
    else:
        return 'No cache found',''

def parse(file):
    print file,'FFF'
    items_14=[]
    items_15=[]
    #items_10=[]
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
    'cache.html'
    '''
    c = App.get_running_app().storage()
    print((c))
    go=True
    try:
        with io.open(c + file, 'r',encoding='utf-8') as f:

            aaa=f.read()
    except:
        go=False
        print 'unable to read file'

    if go==True:
        #updated(c + 'cache.html')
        global onejob
        ##print type(aaa)
        aaa=aaa.replace(u'\u2019',"'")
        aaa=aaa.replace(u'\xa9','c')
        aaa=aaa.replace(u'\xa0','')
        #aaa=aaa.replace('©','cc')
        ##print aaa
        ##print aaa
        #from pyquery import PyQuery
        #html = aaa
        #pq = PyQuery(html)
        soup = BeautifulSoup(aaa, 'html.parser')
        ##print(soup.prettify())
        a= list(soup.children)
        zz= soup.select('tr')
        ##print zz
        ##print len(zz)
        onejob=[]
        #print type(onejob)
        onejob=[]
        #print type(onejob)
        for g in range(len(zz)):
            # #print g/14,(g%14)-1,zz[g]
            # #print type(zz)
            a2 = (zz[g])
            # #print dir(a2)
            az3 = list(a2.children)
            # #print az3
            job = []
            for j in range(len(az3)):


                az4 = az3[j]
                try:
                    # #print az4.text
                    job.append(az4.text)
                    # onejob[g]=appendaz4.text
                except:
                    ''
                    # #print az4,'loll'
                # #print dir(az4)
            #print
            len(job)
            onejob.append(job)
        print onejob
        # #print g
        items_0=[]
        items_1=[]
        items_2 = []
        items_3 = []
        items_4 = []
        items_5 = []
        items_6 = []
        items_7 = []
        items_8 = []
        items_9 = []
        items_10=[]
        items_11 = []
        items_12 = []
        items_13 = []
        items_14 = []

        if len(onejob)>0:
            for q in range(1,len(onejob[0])-1):
                print q
                #items_1.add( onejob[q][1])
                #items_2.add(onejob[q][2])
                #items_3.add(onejob[q][3])
                #items_4.add(onejob[q][4])
                try:
                    items_0.append(str(onejob[q][0]))
                except:

                    items_0.append('')
                try:
                    items_1.append(str(onejob[q][1]))
                    print (str(onejob[q][1]))
                except:
                    items_1.append('')
                try:
                    items_2.append(str(onejob[q][2]))
                except:
                    #print onejob[q][2]
                    #items_2.append((onejob[q][2]))
                    items_2.append('')
                try:
                    items_3.append((onejob[q][3]))
                except:
                    items_3.append('')
                try:
                    items_4.append((onejob[q][4]))
                except:
                    items_4.append('')
                try:
                    items_5.append((onejob[q][5]))
                except:
                    items_5.append('')
                try:
                    items_6.append((onejob[q][6]))
                except:
                    items_6.append('')
                try:
                    items_7.append((onejob[q][7]))
                except:
                    items_7.append('')
                try:
                    items_8.append((onejob[q][8]))
                except:
                    items_8.append('')

                '''
                items_2.append(str(onejob[q][2]))
                items_3.append(str(onejob[q][3]))
                items_4.append(str(onejob[q][4]))
                items_5.append(str(onejob[q][5]))
                items_6.append(str(onejob[q][6]))
                items_7.append(str(onejob[q][7]))
                items_8.append(str(onejob[q][8]))
                '''
                try:
                    items_9.append(str(onejob[q][9]))


                except:
                    items_9.append('')
                try:
                    items_10.append(str(onejob[q][10]))
                except:
                    items_10.append('')
                try:
                    items_11.append(str(onejob[q][11]))
                except:
                    items_11.append('')
                try:
                    items_12.append(str(onejob[q][12]))
                except:
                    items_12.append('')



                try:
                    items_13.append(str(onejob[q][13]))
                except:
                    items_13.append('')
                #items_14.append(onejob[q][14])
        print items_1
        for z in range(len(items_10)):
            t= items_0[z]
            d=items_1[z]
            #print (t,d,'ratfuck')
            if(len(t))<0:
                aa,tim2=check_time(t,d)
                items_14.append(aa)
                items_15.append(tim2)
            if len(t)==0:
                items_14.append('')
                items_15.append('')
            #print aa
            #print items_14
    print len(items_0)
    print len(items_1)
    print (len(items_2))
    print(len(items_3))
    print(len(items_4))
    print(len(items_5))
    print(len(items_6))
    print(len(items_7))
    print(len(items_8))
    print(len(items_9))
    print(len(items_10))
    print(len(items_11))
    print(len(items_12)),'what'
    print(len(items_13))
    print(len(items_14))



    #joob = date1 + ' ' + time1 + ' ~ ' + venue1 + ' ~ ' + loc1 + ' ~ ' + show1 + ' ~  ' + client1 + ' ~ ' + type1 + ' ~ ' + pos1 + ' ~ ' + status1 + ' ~ ' + job1 + ' ~ ' + notes1
    ##print joob

    #check(joob, date1, time1, venue1, loc1, show1, type1, status1, pos1, notes1, client1, job1)

    return items_14
class FirstScreen(Screen):
    def sslwrap(self,func):
        @wraps(func)
        def bar(*args, **kw):
            kw['ssl_version'] = ssl.PROTOCOL_TLSv1
            return func(*args, **kw)

        return bar
    def login(self,b,c,d):
        #print 'calculate'
        #import  urllib3
        ssl.wrap_socket = self.sslwrap(ssl.wrap_socket)

        #requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = ('DES-CBC3-SHA')

        ##print (urllib3.util.ssl_.DEFAULT_CIPHERS),'urldc'

        global now
        #ssl._DEFAULT_CIPHERS = ('DES-CBC3-SHA')
        ssl.verify=False
        ##print ssl._DEFAULT_CIPHERS,'dc'
        global browser
        #print(ssl.OPENSSL_VERSION_INFO),'test'
        #ssl._create_default_https_context
        #print
        #print
        #print
        #print (ssl.SSLSocket.cipher)
        ##print dir(ssl_.wrap_socket)
        ##print poo

        #PE_LOGIN = 'http://www.thinkrhino.com/employee/lasvegas/'
        PE_LOGIN = 'https://www.thinkrhino.com/employee/lasvegas/index.aspx'
        PE_COUNTRIES = 'https://www.thinkrhino.com/employee/lasvegas/Schedule.aspx'
        #PE_LOGIN='http://google.com'
        #PE_COUNTRIES='https://yahoo.com'
        import operator
        #print c.text

        USERNAME = c.text
        PASSWORD = d.text
        dir_path = os.path.dirname(os.path.realpath(__file__))
        #aaa=open(dir_path+'/test2.html','wb')
        browser = mechanize.Browser()
        ##print dir(browser)
        pass
        browser.set_handle_robots(False)
        browser.set_handle_equiv(False)
        browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        browser.open(PE_LOGIN)

        browser.select_form(name="ctl00")
        browser['emailaddress'] = USERNAME
        browser['mypassword'] = PASSWORD
        ##print (browser)
        ##print browser.title

        res = browser.submit()
        ##print dir(res)
        ##print res.header_items
        ##print res.get_data()

        res = browser.open(PE_COUNTRIES)
        aa= res.get_data()   # HTML source of the page


        #print (browser,'REAL BROWSER')

        #now= (datetime.now())
        #print type(aa)
        #print (dir(res))
        #print res.info
        u=''
        for i in res.readlines():
            ##print i
            try:
                if "allrights" in i or 'copyright -' in i or 'ino Women’s Cold Crew P' in i:
                    #print i,'copy1'
                    i=''


                i=i.encode('utf-8')
                u=u+(i)
            except:
                pass

                #print 'fauil',i



        c = App.get_running_app().storage()
        #print((c))
        b = open(str(c) + 'cache.html', 'w')
        b.write(u)
        b.close()

        App.get_running_app().root.screen_switch_one(self)





    def loadcache(self,a, b,c):
        print 'wowowow'
        parse('cache.html')
        #print date1
        #a, b
    pass

class SecondScreen(Screen):
    #def __init__(self):
    #    #print 'jesus'
    def wow(self):

        self.random_number = items_1[3]
        pass

    #print dir(App.get_running_app()),'trtr'

    app = App.get_running_app()
    #print app,'808'
    #print (dir(app)),'9009'
    #item_1=['w']*4
    #random_number = item_1[3]

    #print 'fuck'
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

color_1 = [.2, .2, .2, 1]
##print type(color_1)
##print color_1,'wowow'
color_ = [.1, .1, .1, 1]
clist=[color_,color_1]

class MyScreenManager(ScreenManager):


    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        Clock.schedule_once(self.screen_switch_one, 2)

    def screen_switch_one(self, dt):
        self.current = '_first_screen_'
        print 'loading first screen'
        a=updated(self,'')
        try:
            f,l,j=parse_name()
            print a
        except:
            f=''
        if len(f)>0:
            self.ids.first_screen.ids.status.text = str(f+' '+l+':'+j+' jobs\nUpdated '+a+' ago.\n')
        #Clock.schedule_once(self.screen_switch_two, 2)
        root = App.get_running_app().root
        print root.ids.viewkeys
        print dir(root.ids.viewkeys)
        print 'why'

    def screen_switch_two(self, dt,index):
        items_14=parse('cache.html')
        self.current = '_second_screen_'
        ##print dt
        ##print index
        #print 'piss'

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
        #print self.ids.second_screen.ids.second_screen_label10.background_color,'gtt'

        #self.ids.second_screen.ids.second_screen_label.font_size=10
        #print
        i=0
        j=1
        scl=[]

        scl.append(self.ids.second_screen.ids.second_screen_label.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label1.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label2.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label3.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label4.background_color)
        scl.append(self.ids.second_screen.ids.second_screen_label5.background_color )
        scl.append(self.ids.second_screen.ids.second_screen_label6.background_color )
        scl.append(self.ids.second_screen.ids.second_screen_label7.background_color )
        scl.append(self.ids.second_screen.ids.second_screen_label8.background_color )
        scl.append(self.ids.second_screen.ids.second_screen_label9.background_color )
        scl.append(self.ids.second_screen.ids.second_screen_label10.background_color )
        scl.append(self.ids.second_screen.ids.second_screen_label11.background_color )
        scl.append(self.ids.second_screen.ids.second_screen_label12.background_color )
        scl.append(self.ids.second_screen.ids.second_screen_label13.background_color )
        scl.append(self.ids.second_screen.ids.second_screen_label14.background_color )
        blankc=[0]*len(scl)
        #print blankc,'bc',len(scl)
        for q in range(len(scl)):
            if q%2==0:
            ##print scl[q],'red'
            #scl[q]=color_

                blankc[q]=color_
            else:
                blankc[q]=color_1
            #print scl[q], 'blue'
        #print blankc,'blankc'
        self.ids.second_screen.ids.second_screen_label4.background_color = blankc[0]
        self.ids.second_screen.ids.second_screen_label1.background_color=blankc[1]
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
            pass
            #print items_13[index],'13'
        except:
            pass
            #print'fail13'
        try:
            pass
            #print items_12[index],'14'
        except:
            pass
            #print 'fail14'
        #Clock.schedule_once(self.screen_switch_three, 2)

    def screen_switch_three(self, dt,index):
        parse()
        self.current = '_third_screen_'
        #Clock.schedule_once(self.screen_switch_four, 2)

    def screen_switch_four(self, dt):
        self.current = '_fourth_screen_'
        print 'now!'
        #Clock.schedule_once(self.screen_switch_one, 2)
    def update(self):
        #print parse(),'yellow'
        parse('old.html')
        #print self,'SELF"'
        #print self.parent.parent.parent
        #RV().__init__()
        #SelectableLabel().refresh_view_attrs(1,1,gdata)
        #print gdata,'totot'
        #print grv
        #print gdata
        i0='wow'
        i1='no'
        #print
        i0='0'
        i1 = '0'
        i2 = '0'

        i3 = '0'
        i4 = '0'
        i5 = '0'
        i6 = '0'
        i7 = '0'
        i8 = '0'
        i9 = '0'
        i10 = '0'
        print rv,'RVRV'
        gdata=   {'label1': {'text': i0},'label2': {'text': i0}, 'label3': {'text': i0}, 'label4': {'text': i0},'label5': {'text': i4},'label6': {'text': i5},'label7': {'text': i6},'label8': {'text': i7},'label9': {'text': i8},'label10': {'text': i9},'label11': {'text': i10}}
        #print self.grv,'grv'
        rv2()

        SelectableLabel().refresh_view_attrs(grv,'',gdata)



#root.SelectableLabel.refresh_view_attrs()





class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    print 'who'
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, GridLayout):
    global gdata
    ''' Add selection support to the Label '''
    #global index
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    cols = 9
    #print 'what'
    #root = App.get_running_app()
    #print root
    #print dir(root)
    def update(self):
        print self.ids
        print (dir(self.ids))
        print 'rar'

    def refresh_view_attrs(self, rv, index, data):
        global grv
        global gdata
        #print data
        #print gdata[index]
        print dir(rv),'wrrr'
        print grv.data
        #rv.data=[]
        #rv2()
        #RV().__init__()


        #data=[]
        #global index
        ''' Catch and handle the view changes '''
        self.index = index
        #print index,'index55',type(data),type(gdata)
        #print 'len',len(data['label1']),len(gdata)
        #data=gdata
        #print data
        #print gdata


        #self.label1_text = str(index)
        #self.label2_text = data['label2']['text']
        #print gdata['label1'],'yoyoyo'
        self.ids['id_label1'].text = data['label1']['text']  # As an alternate method of assignment
        #self.ids['id_label1'].text = 'wow' # As an alternate method of assignment
        self.ids['id_label2'].text = data['label2']['text']  # As an alternate method of assignment
        self.ids['id_label3'].text = data['label3']['text']  # As an alternate method of assignment
        self.ids['id_label4'].text = data['label4']['text']  # As an alternate method of assignment
        self.ids['id_label5'].text = data['label5']['text']  # As an alternate method of assignment
        self.ids['id_label6'].text = data['label6']['text']  # As an alternate method of assignment
        #self.ids['id_label10'].text = data['label10']['text']  # As an alternate method of assignment
        self.ids['id_label8'].text = data['label8']['text']  # As an alternate method of assignment
        self.ids['id_label9'].text = data['label9']['text']  # As an alternate method of assignment
        self.ids['id_label11'].text = data['label11']['text']  # As an alternate method of assignment

        grv=rv
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
            #print("selection changed to {0}".format(rv.data[index]))
            ##MyScreenManager.screen_switch_two(ScreenManager)
            ##print dir(MyScreenManager),'msm'
            ##print dir(MyScreenManager.screen_switch_four)
            ##print dir(MyScreenManager.current)

            #rint MyScreenManager.current_screen
            #MyScreenManager.current='_second_screen_'
            #print dir(App.get_running_app())
            App.get_running_app().root.screen_switch_two(self,index)

            #print len(gdate1),'date1'
            #print len(gtime1),'gtime1'
            #print len(gjob1),'gjob1'
            #print len(gvenue1),'gvenue1'
            #print len(rv.data),'data'
        else:
            pass
            #print("selection removed for {0}".format(rv.data[index]))

def rv2():
    data=[]
    paired_iter = zip(items_0, items_1, items_2, items_3, items_4, items_5, items_6, items_7, items_8, items_9,
                      items_10, items_11, items_12, items_13)
    for i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13 in paired_iter:
        d = {'label1': {'text': i0}, 'label2': {'text': i1}, 'label3': {'text': i2}, 'label4': {'text': i3},
             'label5': {'text': i4}, 'label6': {'text': i5}, 'label7': {'text': i6}, 'label8': {'text': i7},
             'label9': {'text': i8}, 'label10': {'text': i9}, 'label11': {'text': i10}}
        data.append(d)
        global gdata
        gdata = data
class RV(RecycleView):
    def __init__(self, **kwargs):
        self.data = []
        parse('cache.html')
        print "TESTTESTTESTTEST"

        super(RV, self).__init__(**kwargs)
        global items_2
        global items_1
        #global date1
        #global job1
        #global venue1
        ##print time1
        #print gvenue1
        paired_iter = zip(items_0,items_1, items_2,items_3,items_4,items_5,items_6,items_7,items_8,items_9,items_10,items_11,items_12,items_13)
        #print paired_iter,"HOLYCRAPMAN"
        #
        for i0,i1, i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13 in paired_iter:
            d = {'label1': {'text': i0},'label2': {'text': i1}, 'label3': {'text': i2}, 'label4': {'text': i3},'label5': {'text': i4},'label6': {'text': i5},'label7': {'text': i6},'label8': {'text': i7},'label9': {'text': i8},'label10': {'text': i9},'label11': {'text': i10}}
            #d = {'label1': {'text': i0},'label2': {'text': i1}, 'label3': {'text': i2}, 'label4': {'text': i3},'label5': {'text': i4},'label6': {'text': i5}}

            self.data.append(d)
            #print 'wtf man'
            #print data
        # can also be performed in a complicated one liner for those who like it tricky
        # self.data = [{'label2': {'text': i1}, 'label3': {'text': i2}} for i1, i2 in zip(items_1, items_2)]
        #return data
        global gdata
        gdata=self.data
        #print 'self.data',gdata
        #print gdata,'gdata',type(self.data),type(gdata)



items2_1 = {'apple', 'banana', 'pear', 'pineapple'}
items2_2 = {'dog', 'cat', 'rat', 'bat'}


#print SelectableLabel,'dafuq'
#print SelectableLabel.refresh_from_data()
#print RecycleView.refresh_from_data(SelectableRecycleBoxLayout)

class TestApp(App):
    def build(self):

        return MyScreenManager()
    def storage(self):
        return self.user_data_dir

if __name__ == '__main__':
    TestApp().run()
