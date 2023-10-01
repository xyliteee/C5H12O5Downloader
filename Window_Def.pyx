import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from Ui_Mainpage import Ui_Form as MainPage
from Ui_LoadingPage import Ui_Form as LoadingPage
from Ui_ErrorPage import Ui_Form as ErrorPage
from Ui_DownloadingPage import Ui_Form as DonwloadingPage
from multiprocessing import *
from qfluentwidgets import *
import httpx
from win11toast import toast
import time
import datetime
import re
import os
import Source_Get

class Thread_Download(QThread):
    
    down_finished_sig = pyqtSignal()
    down_percent_sig = pyqtSignal(object)
    def __init__(self,parent,Quality,downflag,page):#downflag就是传入的空线程
        super().__init__()
        self.parent = parent
        self.Quality = Quality
        self.downflag = downflag
        self.page = page
    def run(self):
        playinfo = self.parent.T_serch.Source_Get.Get_playinfo(self.page)
        if self.Quality == -1:
            self.parent.T_serch.Source_Get.Audio_Download(self.Quality,self.downflag,playinfo)
        else:
            self.parent.T_serch.Source_Get.Mix(self.Quality,self.downflag,playinfo)
        self.down_finished_sig.emit()


class Thread_Search(QThread):
    serch_fin_sigle = pyqtSignal(list)
    def __init__(self,parent,bvlink,cookies):
        super().__init__()
        self.parent = parent
        self.bvlink = bvlink
        self.cookies = cookies
        self.Source_Get = Source_Get.Class_Source_Get(self.bvlink,self.cookies,self)
    def run(self):
        Info = self.Source_Get.Bascical_Info()
        self.serch_fin_sigle.emit(Info)

class Thread_Save_Cover(QThread):
    save_finish_sig = pyqtSignal()
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        
    def run(self):
        self.parent.T_serch.Source_Get.Cover_Download()
        self.save_finish_sig.emit()

class Thread_Toast(QThread):
    def __init__(self,str):
        super().__init__()
        self.str = str
    def run(self):
        #try:
            toast(title = self.str,body = "还没起好名字")
        #except:
            None


class Thread_Get_QRcode(QThread):
    Get_QRcode_signal = pyqtSignal(object)
    Get_cookies_signal = pyqtSignal(object)
    def __init__(self):
        super().__init__()
    def run(self):

        data = Source_Get.QRCode_Get()
        try:
            self.Get_QRcode_signal.emit(0)
            flag =0
            token = data['qrcode_key']
            with httpx.Client() as client:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
                url = f"https://passport.bilibili.com/x/passport-login/web/qrcode/poll?qrcode_key={token}&source=main-fe-header"
                while True:
                    flag += 1
                    data_login = client.get(url=url, headers=headers)  # 请求二维码状态
                    data_login = json.loads(data_login.text)
                    code = str(data_login['data']['message'])
                    if code == "":#扫码确认了

                        SESSDATA = dict(client.cookies)["SESSDATA"]
                        cookie = f"SESSDATA={SESSDATA};"#获取cookie
                        self.Get_cookies_signal.emit(cookie)
                        break
                    elif flag > 10:
                        self.Get_cookies_signal.emit("timeout")
                        break
                    time.sleep(2)
        except Exception as e:
            e = str(e)

            logtime = str(datetime.datetime.now()).replace(" ","-")[:-7]
            logtime = logtime.replace(":","-")
            with open('error_log.txt', 'a') as f:
                f.write(logtime +"二维码扫码"+ e + '\n')

            errorcode = data
            
            self.Get_QRcode_signal.emit(errorcode)
            self.Get_cookies_signal.emit(errorcode)


                

        
    
class Thread_Login(QThread):
    Log_fin_sigle = pyqtSignal(list)
    def __init__(self,input_cookie):
        super().__init__()
        self.input_cookie = input_cookie
    
    def run(self):
        
        Info = Source_Get.Login_Info(self.input_cookie)
        self.Log_fin_sigle.emit(Info)


class MainWindow(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.ui = MainPage()
        self.ui.setupUi(self)
        self.parent = parent
        self.UI_Init()
        self.Input_fuction()
        self.cookies = "None"
        self.BVlink = ""
        self.logoutbvlinktemp = ""
        self.loginbvlinktemp = ""
        self.empth_thread = None
        self.page = 1
        self.VideoDownload_thread = [1,2,3,4,5,6,7,8,9] 
        self.download_toast_message = [1,2,3,4,5,6,7,8,9]

        
        try:
            with open('cookies.json',encoding='utf-8') as f:
                data = json.load(f)

                if data["Auto_login"] == "True":
                    
                    self.cookies = data["user_cookie"]
                    self.Logstart()

                elif data["Auto_login"] == "False":
                    pass

        except Exception as e:
            None


    def UI_Init(self):
        setThemeColor("#d46183")
        self.VideoDownload = self.ui.VideoDownload
        self.Bvinput = self.ui.Bvlink
        self.SearchButton = self.ui.Search
        
        self.Cover = self.ui.Cover

        self.View =self.ui.View
        self.Coin =self.ui.Coin
        self.Like = self.ui.Like
        self.Favorite = self.ui.Favorite

        self.Descripton = self.ui.Description
        self.Maintitle = self.ui.Maintitle

        self.UPID = self.ui.UPID
        self.ProfilePic = self.ui.ProfilePic#UP的头像

        self.Shutdown = self.ui.Shutdown
        self.Minwindow = self.ui.Min

        self.CoverSave = self.ui.CoverSave
        self.VideoDownload = self.ui.VideoDownload
        self.Downchoice = self.ui.down_choice
        self.Pagechoice = self.ui.page_choice

        self.QRcodeGetButton = self.ui.QRcodeGet
        self.QRcodePic = self.ui.QRcode


        self.cookiesinput = self.ui.cookies
        self.loginbutton =self.ui.Login

        self.logpage = self.ui.Logpage
        self.Personpage = self.ui.PersonPage

        self.personProfilePic = self.ui.Profileface#用户的头像
        self.Name = self.ui.Name
        self.Personpage.hide()
        self.Logoutbutton = self.ui.Logout

        self.downloadpagebutton = self.ui.downloadpagebutton

        self.CoverSave.setDisabled(True)
        self.VideoDownload.setDisabled(True)
        self.loginbutton.setDisabled(True)
        self.SearchButton.setDisabled(True)

        self.video_list = ["选择画质"]
        self.Downchoice.addItems(self.video_list)
        
        self.Page_list = ["选择页数"]
        self.Pagechoice.addItems(self.Page_list)

        self.Downchoice.setCurrentIndex(0)
        self.Pagechoice.setCurrentIndex(0)
        

       
        
        

    

    def Input_fuction(self):
        self.SearchButton.clicked.connect(self.Search_start)
        self.CoverSave.clicked.connect(self.Cover_Save)
        self.Shutdown.clicked.connect(QCoreApplication.instance().quit)
        self.QRcodeGetButton.clicked.connect(self.GetQRcode)

        self.cookiesinput.textChanged.connect(self.cookie_input_active)
        
        self.loginbutton.clicked.connect(self.get_cookies_from_input)
        self.loginbutton.clicked.connect(self.Logstart)

        self.VideoDownload.clicked.connect(self.Video_Download)

        self.Downchoice.currentTextChanged.connect(self.Video_choice)
        self.Pagechoice.currentIndexChanged.connect(self.Page_choice)

        self.Logoutbutton.clicked.connect(self.Logout)
        self.Bvinput.textChanged.connect(self.Get_Bvlink)

        self.downloadpagebutton.clicked.connect(lambda:self.parent.StackedWidget.setCurrentWidget(self.parent.Downloadingwindow))


    def get_cookies_from_input(self):
        self.cookies = self.cookiesinput.text()

    def Downchoice_reset(self):
        self.Downchoice.clear()
        self.Pagechoice.clear()

    def Get_Bvlink(self):
        self.BVlink = self.Bvinput.text()
        Bvcode = re.findall(r'bv.{10}',self.BVlink,re.IGNORECASE)
        if len(Bvcode) == 0:
            self.SearchButton.setDisabled(True)
        else:
            self.SearchButton.setDisabled(False)

    def Logout(self):################################################################################
        cookie_json = \
        {
            "user_cookie":self.cookies,
            "Auto_login":"False"
        }

        with open("cookies.json", "w") as f:
            json.dump(cookie_json, f)

        self.cookies = ""
        self.cookiesinput.setPlaceholderText("或者用cookie登录也可以")
        self.Personpage.hide()
        self.parent.Loadingwindow.ProcessingPage.hide()

        if self.logoutbvlinktemp == "":
            pass
        else:
            self.parent.Loadingwindow.Title.setText("解析中")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Loadingwindow)
            self.T_serch = Thread_Search(self,self.logoutbvlinktemp,self.cookies)
            self.T_serch.serch_fin_sigle.connect(self.Basical_Info_Updata)
            self.T_serch.start()
        self.logoutbvlinktemp = ""

    def Down_load_finished_UI_updata(self):

        self.download_toast_message[self.empth_thread] = Thread_Toast("下载已经完成辣")
        self.download_toast_message[self.empth_thread].start()

    def Page_choice(self):
        self.page = int(self.Pagechoice.currentIndex() + 1)


    def Video_choice(self):
        if self.Downchoice.currentText() == "2160P":
            self.Quality = 120
            self.VideoDownload.setDisabled(False)

        elif self.Downchoice.currentText() == "1080P 60":
            self.Quality = 116
            self.VideoDownload.setDisabled(False)

        elif self.Downchoice.currentText() == "1080P+":
            self.Quality = 112
            self.VideoDownload.setDisabled(False)

        elif self.Downchoice.currentText() == "1080P":
            self.Quality = 80
            self.VideoDownload.setDisabled(False)

        elif self.Downchoice.currentText() == "720P":
            self.Quality = 64
            self.VideoDownload.setDisabled(False)

        elif self.Downchoice.currentText() == "480P":
            self.Quality = 32
            self.VideoDownload.setDisabled(False)
        elif self.Downchoice.currentText() == "360P":
            self.Quality = 16
            self.VideoDownload.setDisabled(False)

        elif self.Downchoice.currentText() == "仅下载音频":
            self.Quality = -1
            self.VideoDownload.setDisabled(False)

        elif self.Downchoice.currentText() == "选择画质":
            self.VideoDownload.setDisabled(True)
        

    def Video_Download(self):
        self.empth_thread_list = self.parent.Downloadingwindow.Find_empty_thread()


        if len(self.empth_thread_list) == 0:
            self.download_toast_waring = Thread_Toast("下载队列已经满了")
            self.download_toast_waring.start()
        else:
            self.empth_thread = self.empth_thread_list[0]
            self.parent.StackedWidget.setCurrentWidget(self.parent.Downloadingwindow)
            self.VideoDownload_thread[self.empth_thread] = Thread_Download(self,self.Quality,self.empth_thread,self.page)
            self.VideoDownload_thread[self.empth_thread].down_finished_sig.connect(self.Down_load_finished_UI_updata)
            self.VideoDownload_thread[self.empth_thread].down_percent_sig.connect(self.parent.Downloadingwindow.Percent_updata)
            self.VideoDownload_thread[self.empth_thread].start()



    def QRRelease(self):
        self.QRcodeGetButton.setDisabled(False)
        self.Limit_timer.stop()

    def QRButtonlimittime(self):
        self.limit_time -= 1
        self.QRcodeGetButton.setText(f"{self.limit_time}s")
        if self.limit_time <= 0:
            self.Limit_ui_timer.stop()
            self.QRcodeGetButton.setText("刷新")

    def Cover_Save(self):
        self.Cover_Save_Start = Thread_Save_Cover(self)
        self.Cover_Save_Start.save_finish_sig.connect(lambda:self.CoverSave.setDisabled(False))
        self.Cover_Save_Start.start()
        self.CoverSave.setDisabled(True)
    
    def QR_Updata(self,error):
        if error == 0:
            pixmap = QPixmap('./Qrcode')
            self.QRcodePic.setPixmap(pixmap)

    def cookie_input_active(self):
        if self.cookiesinput.text() == "":
            self.loginbutton.setDisabled(True)
        else:
            self.loginbutton.setDisabled(False)

    def GetQRcode(self):
        
        self.limit_time = 20
        self.QRcodeGetButton.setDisabled(True)
        
        

        self.Limit_timer = QTimer()
        self.Limit_timer.setInterval(20000)
        self.Limit_timer.timeout.connect(self.QRRelease)
        
        self.Limit_ui_timer = QTimer()
        self.Limit_ui_timer.setInterval(1000)
        self.Limit_ui_timer.timeout.connect(self.QRButtonlimittime)

        self.Get_QRcode_Start = Thread_Get_QRcode()
        self.Get_QRcode_Start.Get_QRcode_signal.connect(self.QR_Updata)
        self.Get_QRcode_Start.Get_cookies_signal.connect(self.QRlogin)

        self.Limit_timer.start()
        self.Get_QRcode_Start.start()
        self.Limit_ui_timer.start()

    def Log_Updata(self,Info):
        
        if Info[0] == 10403:
            self.parent.Errorwindow.Error_Str.setText(f"Error:10403，登陆失败，cookie可能过期或错误或者抽风")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow)
            self.cookiesinput.setPlaceholderText("登陆错误")
        elif Info[0] == 10053:
            self.parent.Errorwindow.Error_Str.setText(f"Error:10053，登陆失败，请检查网络连接")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow)
            self.cookiesinput.setPlaceholderText("登陆错误")
        elif Info[0] == 11001:
            self.parent.Errorwindow.Error_Str.setText(f"Error:11001，登陆失败，请检查网络连接")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow)
            self.cookiesinput.setPlaceholderText("登陆错误")
        elif Info[0] == 10061:
            self.parent.Errorwindow.Error_Str.setText(f"Error:10061，登陆失败，请检查代理设置")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow)
            self.cookiesinput.setPlaceholderText("登陆错误")
        elif Info[0] == -1:
            self.parent.Errorwindow.Error_Str.setText(f"Error:-1，登陆失败，未知错误")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow)
            self.cookiesinput.setPlaceholderText("登陆错误")
        elif Info[0] == 0:#登陆成功
            self.parent.StackedWidget.setCurrentWidget(self)
            self.cookiesinput.setPlaceholderText("登录成功")

            try:
                os.remove("Qrcode")#清理二维码
            except:
                None
            ####################################################################################
            self.QRcodePic.setPixmap(QtGui.QPixmap(":/img/qrcode.png"))#设置为默认二维码
            self.personProfilePic.setPixmap(QPixmap.fromImage(Info[2]))#更新头像
            self.Name.setText(Info[1])#更新名称
            self.Personpage.show()#显示用户界面
            self.cookiesinput.setText("")


            cookie_json =   {
                                "user_cookie":self.cookies,
                                "Auto_login":"True"
                            }
            
            with open("cookies.json", "w") as f:
                json.dump(cookie_json, f)


            if self.loginbvlinktemp == "":
                pass
            else:
                self.parent.Loadingwindow.Title.setText("解析中")
                self.parent.StackedWidget.setCurrentWidget(self.parent.Loadingwindow)
                self.T_serch = Thread_Search(self,self.loginbvlinktemp,self.cookies)
                self.T_serch.serch_fin_sigle.connect(self.Basical_Info_Updata)
                self.T_serch.start()
            self.loginbvlinktemp = ""

            

    def QRlogin(self,qrcookies):#qrcookies就是cookies或者错误码
        if qrcookies == "timeout":
            None
        if qrcookies == 11001:
            self.parent.Errorwindow.Error_Str.setText(f"Error:11001，获取二维码失败，请检查网络连接")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow)
        elif qrcookies == 10061:
            self.parent.Errorwindow.Error_Str.setText(f"Error:10061，获取二维码失败，请检查代理设置")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow)
        elif qrcookies == 10053:
            self.parent.Errorwindow.Error_Str.setText(f"Error:10053，获取二维码失败，请检查网络连接")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow)
        elif qrcookies == -1:
            self.parent.Errorwindow.Error_Str.setText(f"Error:-1，获取二维码失败，未知错误")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow) 

        else:#确信网络通畅后
            self.cookies = qrcookies
            self.Logstart()



    def Logstart(self):
        self.cookiesinput.setPlaceholderText("登陆中")
        try:
            self.QRcodeGetButton.setDisabled(False)
            self.QRcodeGetButton.setText("刷新")
            self.Limit_ui_timer.stop()
            self.Limit_timer.stop()
        except:
            None
        self.logthread = Thread_Login(self.cookies)
        self.logthread.Log_fin_sigle.connect(self.Log_Updata)
        self.logthread.start()

    def Basical_Info_Updata(self,Info):#Info = [Error_code,Cover,Title,Descripton,View,Coin,Like,Favorite,Name,Profile,video_list]
        if Info[0] == 0:
            self.parent.StackedWidget.setCurrentWidget(self)

            self.Cover.setPixmap(QPixmap.fromImage(Info[1]))

            self.Maintitle.setText(Info[2])

            self.Descripton.setText(Info[3])

            self.View.setText(f"播放：{Info[4]}")
            self.Coin.setText(f"投币：{Info[5]}")
            self.Like.setText(f"点赞：{Info[6]}")
            self.Favorite.setText(f"收藏：{Info[7]}")

            self.UPID.setText(Info[8])
            self.ProfilePic.setPixmap(QPixmap.fromImage(Info[9]))
            self.CoverSave.setDisabled(False)
            self.video_list = Info[10]
            self.Page_list = Info[11]
            self.Downchoice_reset()

            self.Downchoice.addItems(self.video_list)
            self.Pagechoice.addItems(self.Page_list)
            
        if Info[0] == 404:
            self.parent.Errorwindow.Error_Str.setText(f"Error:11404 索引失败，可能是该视频已丢失")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow)

        elif Info[0] == 11001:
            self.parent.Errorwindow.Error_Str.setText(f"Error:11001 索引失败，请检查网络连接或网址正确性")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow)

        elif Info[0] == 10061:
            self.parent.Errorwindow.Error_Str.setText(f"Error:10061 索引失败，请检查代理设置")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow)

        elif Info[0] == 10053:
            self.parent.Errorwindow.Error_Str.setText(f"Error:10053 索引失败，请检查网络连接")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow)

        elif Info[0] == -1:
            self.parent.Errorwindow.Error_Str.setText(f"Error:-1 索引失败，未知错误")
            self.parent.StackedWidget.setCurrentWidget(self.parent.Errorwindow)
        
    def Search_start(self):
        self.parent.Loadingwindow.ProcessingPage.hide()
        self.parent.Loadingwindow.Title.setText("解析中")
        self.parent.StackedWidget.setCurrentWidget(self.parent.Loadingwindow)
        self.T_serch = Thread_Search(self,self.BVlink,self.cookies)
        self.T_serch.serch_fin_sigle.connect(self.Basical_Info_Updata)
        self.T_serch.start()
        self.logoutbvlinktemp = self.BVlink
        self.loginbvlinktemp = self.BVlink
        self.Bvinput.setText("")#初始化bvlnk输入框，因为和bvlink联动，等于初始化bvlink

class LoadingWindow(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.ui = LoadingPage()
        self.ui.setupUi(self)
        self.parent = parent
        self.UI_Init()

    def UI_Init(self):
        setThemeColor("#d46183")
        self.Title = self.ui.Title
        self.Processing = self.ui.processing
        self.ProcessingPage= self.ui.processingpage
        self.ProcessingPage.hide()#转起来了



class ErrorWindow(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.ui = ErrorPage()
        self.ui.setupUi(self)
        self.parent = parent
        self.UI_Init()
        self.Input_function()

    def UI_Init(self):
        setThemeColor("#d46183")
        self.Error_Str = self.ui.Error_Str
        self.BackButton = self.ui.BackButton

    def Input_function(self):
        self.BackButton.clicked.connect(lambda:self.parent.StackedWidget.setCurrentWidget(self.parent.Mainwindow))



class DownloadingWindow(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.ui = DonwloadingPage()
        self.ui.setupUi(self)
        self.parent = parent
        self.UI_Init()
        self.Input_function()

    def UI_Init(self):
        setThemeColor("#d46183")
        self.Title = [self.ui.Title1,self.ui.Title2,self.ui.Title3]
        self.Processing = [self.ui.processing1,self.ui.processing2,self.ui.processing3]
        self.ProcessBar = [self.ui.ProgressBar1,self.ui.ProgressBar2,self.ui.ProgressBar3]
        self.backbutton = self.ui.BackButton

    def Input_function(self):
        self.backbutton.clicked.connect(lambda:self.parent.StackedWidget.setCurrentWidget(self.parent.Mainwindow))

    def Percent_updata(self,Info):
                if Info[2] == 0:#错误代码为0
                    if Info[0] == "下载完成":#返回的字符串是下载完成，则更新下载完成的UI
                        self.Title[Info[3]].setText(f"{Info[4]}...下载完成")#Info["下载完成",0,Errorcode,downflag,f"{self.Title[:15]}"]
                        self.Processing[Info[3]].setValue(Info[1])
                        self.ProcessBar[Info[3]].setValue(Info[1])
                    else:#否则更新进度条UI
                        self.Title[Info[3]].setText(f"{Info[0]}{Info[1]}%")#Info[f"{self.Title[:15]}...音频已下载：",downloaded_percent,0,downflag]
                        self.Processing[Info[3]].setValue(Info[1])
                        self.ProcessBar[Info[3]].setValue(Info[1])
                elif Info[2] == 10044:
                    self.Title[Info[3]].setText("Error：10044,此分p无此画质，建议前往网页检查")
                else:
                    self.Title[Info[3]].setText("Error：-1，下载错误")

    def Find_empty_thread(self):
        empty_thread_list = []
        for i in range(3):
            t = len(self.Title[i].text())
            if self.Title[i].text() == "等待下载"\
            or self.Title[i].text()[t-4:] == "下载完成"\
            or self.Title[i].text()[t-4:] == "下载错误":
                
                empty_thread_list.append(i)
        return empty_thread_list
        





