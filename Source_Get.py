import requests
import re
from PyQt5.QtGui import *
import qrcode
import json
import subprocess
import datetime
import os
import time
from win11toast import toast




class Class_Source_Get():
    def __init__(self,input,cookie,parent):
        super().__init__()
        self.b = requests.session()

        self.parent = parent

        Bvcode = re.findall(r'bv.{10}',input,re.IGNORECASE)[0]
        self.bvlink = f"https://www.bilibili.com/video/{Bvcode}/?"
        self.cookie = cookie


    def Bascical_Info(self):

        video_list = []
        pages_list = []
        #混淆符号，未来B站可能改变
        Confound = "u002F"

        self.headers = {
                    "cookie":f"{self.cookie}",
                    "referer":"https://www.bilibili.com",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
                    }
        try:
            self.response = self.b.get(url=self.bvlink, headers=self.headers)
            View = re.findall('"view":(.*?),', self.response.text)[0]
            Coin = re.findall('"coin":(.*?),', self.response.text)[0]
            Like = re.findall('"like":(.*?),', self.response.text)[0]
            Favorite = re.findall('"favorite":(.*?),', self.response.text)[0]

            pages = re.findall('共计(.*?)条视频', self.response.text)
            

            Cover_Link_t = re.findall('content="//(.*?)@', self.response.text)[0].replace(Confound,"")
            Cover_Link = f"https://{Cover_Link_t}"
            self.Coversource = self.b.get(Cover_Link)
            Cover= QImage.fromData(self.Coversource.content)

            self.Title = re.findall('title="(.*?)"', self.response.text)[0].replace("amp;","")

            try:
                Descripton_t = re.findall('"raw_text":"(.*?)"', self.response.text)[0].replace("\\n","  ")
                Descripton_t = Descripton_t.replace("@","")
                Descripton_t = Descripton_t.replace("\\r","")
                Descripton = Descripton_t.replace(Confound,"")[:50]
                Descripton = f"{Descripton}......"
            except IndexError:
                Descripton = "莫得简介"

            Name = re.findall('"name":"(.*?)"', self.response.text)[0]

            ProfilePic_Link_t = re.findall('"face":"(.*?)"', self.response.text)[0].replace(Confound,"")
            ProfilePic_Link = ProfilePic_Link_t.replace("\\","/")

            ProfilePicsource = self.b.get(ProfilePic_Link)
            ProfilePic = QImage.fromData(ProfilePicsource.content)

            playinfo = re.findall('<script>window.__playinfo__=(.*?)</script>',self.response.text)[0]
            playinfo_dic = json.loads(playinfo)


            if len(pages) == 0:
                pages_list.append("P1")
            else:
                pages = int(pages[0])
                for i in range(pages):
                    pages_list.append(f"P{i+1}")

            video_list.append("选择画质")
            video = playinfo_dic["data"]["dash"]["video"]
            if len([item for item in video if item["id"] == 120]) > 0:
                video_list.append("2160P")
            if len([item for item in video if item["id"] == 116]) > 0:
                video_list.append("1080P 60")
            if len([item for item in video if item["id"] == 112]) > 0:
                video_list.append("1080P+")
            if len([item for item in video if item["id"] == 80]) > 0:
                video_list.append("1080P")
            if len([item for item in video if item["id"] == 64]) > 0:
                video_list.append("720P")
            if len([item for item in video if item["id"] == 32]) > 0:
                video_list.append("480P")
            if len([item for item in video if item["id"] == 16]) > 0:
                video_list.append("360P")  
            video_list.append("仅下载音频")
            
            Error_Code = 0
            

            Info = [Error_Code,Cover,self.Title,Descripton,View,Coin,Like,Favorite,Name,ProfilePic,video_list,pages_list]
            
        except IndexError as IE: #IndexError:
            Error_Code = 404
            Info = [Error_Code]
        except Exception as e:
            e = str(e)

            logtime = str(datetime.datetime.now()).replace(" ","-")[:-7]
            logtime = logtime.replace(":","-")
            with open('error_log.txt', 'a') as f:
                f.write(logtime +"视频页面解析"+ e + '\n')

            if "Errno 11001" in e:
                Error_Code = 11001
                Info = [Error_Code]
            elif "WinError 10061" in e:
                Error_Code = 10061
                Info = [Error_Code]
            elif "10053" in e:
                Error_Code = 10053
                Info = [Error_Code]
            else:
                Error_Code = -1
                Info = [Error_Code]
        return Info

    
    def Get_playinfo(self,page):
        bvlink = f"{self.bvlink}p={page}"
        self.response = self.b.get(url=bvlink, headers=self.headers)
        playinfo = re.findall('<script>window.__playinfo__=(.*?)</script>',self.response.text)[0]
        return playinfo

    
    def Video_Download(self,Quality,downflag,playinfo):
        self.path = ".\\save\\Video\\"
        if os.path.exists(self.path) == False:
            os.makedirs(self.path)
        
        self.playinfo_dic = json.loads(playinfo)

        video = self.playinfo_dic["data"]["dash"]["video"]
        self.timelengh = int(self.playinfo_dic["data"]["timelength"])

        self.timelengh_full = int(self.timelengh/1000)
        video_result_list = [item for item in video if item["id"] == Quality]
        try:
            video_result = video_result_list[0]
            video_link = video_result["baseUrl"]
            downloaded_bytes = 0
            video_res = self.b.get(url = video_link,headers= self.headers,stream=True,timeout=5)
            self.video_temp_name = f"{self.path}temp{downflag}.mp4"
            total_length = int(video_res.headers.get('Content-Length'))
            self.b.close()
            for i in range(1,20):
                if i == 1:
                    Byte_range = "0-104857600"
                else:
                    Byte_range = f"{(i-1)*104857600+1}-{i*104857600}"

                mutheaders = {
                                    "cookie":f"{self.cookie}",
                                    "referer":"https://www.bilibili.com",
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                                    "Range":f"bytes={Byte_range}"
                                    }
                
                video_res = self.b.get(url = video_link,headers= mutheaders,stream=True,timeout=5)
                with open(self.video_temp_name, "ab",) as file:
                    for data in video_res.iter_content(chunk_size=32*1024):
                        downloaded_bytes += len(data)
                        downloaded_percent = int(round((downloaded_bytes / total_length) * 100))
                        download_info = [f"{self.Title[:15]}...视频已下载：",downloaded_percent,0,downflag]
                        self.parent.parent.VideoDownload_thread[downflag].down_percent_sig.emit(download_info)
                        file.write(data)

                if i*104857600 > total_length:
                    break

            Errorcode = 0
            self.parent.parent.VideoDownload_thread[downflag].down_percent_sig.emit(["",0,Errorcode,downflag])

        except Exception as e:
            e = str(e)

            logtime = str(datetime.datetime.now()).replace(" ","-")[:-7]
            logtime = logtime.replace(":","-")
            with open('error_log.txt', 'a') as f:
                f.write(logtime +"视频下载"+ e + '\n')

            if "Errno 11001" in e:
                Errorcode = 11001
            elif "WinError 10061" in e or "Max retries" in e:
                Errorcode = 10061
            elif "10053" in e:
                Errorcode = 10053
            elif len(video_result_list) == 0:
                Errorcode = 10044
            else:
                Errorcode = -1

        self.parent.parent.VideoDownload_thread[downflag].down_percent_sig.emit(["",0,Errorcode,downflag,f"{self.Title[:15]}"])


    def Audio_Download(self,Quality,downflag,playinfo):
        self.audiopath = ".\\save\\Audio\\"
        if os.path.exists(self.audiopath) == False:
            os.makedirs(self.audiopath)
        

        self.playinfo_dic = json.loads(playinfo)

        audio = self.playinfo_dic["data"]["dash"]["audio"]
        audio_result = audio[0]
        audio_link = audio_result["baseUrl"]
        audio_res = self.b.get(url = audio_link,headers= self.headers,stream=True)

        try:
            total_length = int(audio_res.headers.get('Content-Length'))

            downloaded_bytes = 0

            if Quality == -1:
                file_name = str(datetime.datetime.now()).replace(" ","-")[:-7]
                file_name = file_name.replace(":","-")
                self.audio_temp_name = f"{self.audiopath}{file_name}.mp3"
            else:
                self.audio_temp_name = f"{self.audiopath}temp{downflag}.mp3"
            

            with open(self.audio_temp_name, "wb") as file:
                
                for data in audio_res.iter_content(chunk_size=32*1024):
                    downloaded_bytes += len(data)
                    downloaded_percent = round((downloaded_bytes / total_length) * 100)
                    download_info = [f"{self.Title[:15]}...音频已下载：",downloaded_percent,0,downflag]
                    self.parent.parent.VideoDownload_thread[downflag].down_percent_sig.emit(download_info)
                    file.write(data)
            Errorcode = 0
            self.parent.parent.VideoDownload_thread[downflag].down_percent_sig.emit(["下载完成",0,Errorcode,downflag,f"{self.Title[:15]}"])
            

        except Exception as e:
            e = str(e)

            logtime = str(datetime.datetime.now()).replace(" ","-")[:-7]
            logtime = logtime.replace(":","-")
            with open('error_log.txt', 'a') as f:
                f.write(logtime +"音频下载"+ e + '\n')

            if "Errno 11001" in e:
                Errorcode = 11001
            elif "WinError 10061" in e or "Max retries" in e:
                Errorcode = 10061
            elif "10053" in e:
                Errorcode = 10053
            else:
                Errorcode = -1
                
            self.parent.parent.VideoDownload_thread[downflag].down_percent_sig.emit(["","",Errorcode,downflag])

    def Mix(self,Quality,downflag,playinfo):
        percent = 0

        self.Video_Download(Quality,downflag,playinfo)
        self.Audio_Download(Quality,downflag,playinfo)

        fulltime = self.timelengh_full
        ctime = 0
        percent = 0
        file_name = str(datetime.datetime.now()).replace(" ","-")[:-7]
        file_name = file_name.replace(":","-")
        final_name = f"{self.path}{file_name}.mp4"
        COMMAND =f'ffmpeg\\bin\\ffmpeg.exe -i {self.video_temp_name} -i {self.audio_temp_name} -c:v copy -c:a aac -strict experimental {final_name}'
        try:    
            process = subprocess.Popen(COMMAND, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8",text=True,creationflags=subprocess.CREATE_NO_WINDOW)
            for line in process.stdout:
                try:
                    current_time = re.findall('time=(.*?) b',line)[0]
                    h = int(current_time[:2])*60*60
                    m = int(current_time[3:5])*60
                    s = int(current_time[6:8])
                    ctime = h+m+s
                except Exception as e:
                    None
                percent = round(100*ctime/fulltime)
                Mix_Info = [f"{self.Title[:15]}...已合并：",percent,0,downflag]
                self.parent.parent.VideoDownload_thread[downflag].down_percent_sig.emit(Mix_Info)
            Mix_Errorcode = 0
            self.parent.parent.VideoDownload_thread[downflag].down_percent_sig.emit(["下载完成",0,Mix_Errorcode,downflag,f"{self.Title[:15]}"])
        except Exception as e:
            e = str(e)
            logtime = str(datetime.datetime.now()).replace(" ","-")[:-7]
            logtime = logtime.replace(":","-")
            with open('error_log.txt', 'a') as f:
                f.write(logtime +"视频合并"+ e + '\n')

            Mix_Errorcode = 1
            self.parent.parent.VideoDownload_thread[downflag].down_percent_sig.emit(["","",Mix_Errorcode,downflag])
        try:
            os.remove(f"{self.path}temp{downflag}.mp4")
            os.remove(f"{self.audiopath}temp{downflag}.mp3")
        except Exception:
            pass
    
        
        

    def Cover_Download(self):
        file_name = self.Title
        file_name = file_name.replace("?","")
        file_name = file_name.replace("、","")
        file_name = file_name.replace("/","")
        file_name = file_name.replace("_","")
        file_name = file_name.replace("*","")
        file_name = file_name.replace("<","")
        file_name = file_name.replace(">","")
        file_name = file_name.replace("|","")
        path = ".\\save\\Cover\\"
        if os.path.exists(path) == False:
            os.makedirs(path)
        with open(f"{path}{file_name}.png", 'wb') as f:
            for chunk in self.Coversource.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        try:
            toast("封面保存在/save/cover/中",body = "还没起好名字")
        except:
            None


def QRCode_Get():
        headers = {
            "referer":"https://www.bilibili.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
            }
        bvlink = 'https://passport.bilibili.com/x/passport-login/web/qrcode/generate?source=main-fe-header'
        try:
            response = requests.get(url=bvlink, headers=headers)
            data = json.loads(response.content)['data']
            qr = qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
            qr.add_data(data['url'])
            qr.make(fit=True)
            img = qr.make_image(fill_color="black")
            img.save("Qrcode")
        except Exception as e:

            e = str(e)
            logtime = str(datetime.datetime.now()).replace(" ","-")[:-7]
            logtime = logtime.replace(":","-")
            with open('error_log.txt', 'a') as f:
                f.write(logtime +"二维码保存"+ e + '\n')
            
            if "Errno 11001" in e:
                data = 11001
            elif "WinError 10061" in e or "Max retries" in e:
                data = 10061
            elif "10053" in e:
                data = 10053
            else:
                data = -1

        return data






def Login_Info(cookie):
    retry_times = 0
    bvlink = "https://space.bilibili.com"
    headers = {
            "cookie":f"{cookie}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.11"}
    while True:
        try:
            response = requests.get(url=bvlink, headers=headers)
            time.sleep(0.5)
            name = re.findall('<title>(.*?)的', response.text)[0]#str
            face_link = re.findall('href="(.*?)"', response.text)[7]#link
            face_link = f"https:{face_link}"
            Facesource = requests.get(face_link)
            FacePic= QImage.fromData(Facesource.content)
            Error_Code = 0
            Info = [Error_Code,name,FacePic]
            break         

        except IndexError as eee:
            retry_times +=1

            if retry_times > 10:
                Error_Code = 10403
                Info = [Error_Code]
                break
            else:

                continue

        except Exception as e:
            retry_times +=1

            if retry_times > 10:
                e = str(e)

                logtime = str(datetime.datetime.now()).replace(" ","-")[:-7]
                logtime = logtime.replace(":","-")
                with open('error_log.txt', 'a') as f:
                    f.write(logtime + "登录出错" +e + '\n')

                if "Errno 11001" in e :
                    Error_Code = 11001
                    Info = [Error_Code]
                elif "10053" in e:
                    Error_Code = 10053
                    Info = [Error_Code]
                elif "WinError 10061" in e or "Max retries" in e:
                    Error_Code = 10061
                    Info = [Error_Code]
                else:
                    Error_Code = -1
                    Info = [Error_Code]
                break
            else:
                continue
            
    return Info