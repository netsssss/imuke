# coding = utf-8
'''
我真帅
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time as tm
import sys
import re
import os
import msvcrt

#初始化全局变量
browser = webdriver
browserUrl = r''
loginUrl = r'https://passport.zhihuishu.com/login?service=http://online.zhihuishu.com/onlineSchool/'
believe = True
changeBrowser = False
chrome_options = Options()
locator = ()

#初始化js语句
js = "document.getElementsByClassName('controlsBar')[0].style.display='block';" #显示进度条
jsnoOverlay = "document.getElementById('popbox_overlay').style.display='none';" #关闭开始的弹题
jsnoPop = "document.getElementsByClassName('wrap_popchapter')[0].remove();" #关闭遮罩层
jsSpeed = "document.getElementsByClassName('speedList')[0].style.display='block';" #打开倍速列表
jsnoSpeed = "document.getElementsByClassName('speedList')[0].style.display='none';" #关闭倍速列表

#程序开始
#logo
def showlogo():
    print('##### 欢迎使用 imuke 1.0 #####')
    print('##### 作者:netsssss #####')
    print('##### 托管于Github #####')
    print()
    print('##### 注: 使用"ctrl+c"可终止程序 #####')
    print()
    print()
    print()
    print()
    print('■■■◣    ◢■■■◣    ■    ◢■■■◣')
    print('      ■    ■      ■    ■    ■      ■')
    print('◢■■◤    ■      ■    ■    ◥■■■■')
    print('■          ■      ■    ■           ■')
    print('◥■■■    ◥■■■◤    ■          ■')
    print()
    print()
    print()
    print()
#自定义设置
def costom():
    global browser
    global browserUrl
    global loginUrl
    global believe
    global changeBrowser
    global chrome_options
    
    print()
    print('##### 请注意:#自定义设置将不会被保存,需要每次使用时重新配置#')
    print()
    print('##### 自定义浏览器: ')
    print('##### 1.Chrome')
    print('##### 2.Chrome内核其他浏览器')
    custombrowserchoice = str(input('##### 请输入您希望使用的浏览器对应的数字/不输入将使用默认Chrome: '))
    if custombrowserchoice == '2':
        print()
        print('##### 请输入指向浏览器的完整路径(,注意:一直写到.exe文件,例如:"D:\\browser\\360chrome.exe")/不输入将使用默认Chrome:')
        custombrowserUrl = str(input())
        if custombrowserUrl != '':
            browserUrl = custombrowserUrl
            chrome_options.binary_location = browserUrl
            changeBrowser = True
            print('##### 自定义浏览器成功')
    print()
    custombelieve = str(input('##### 自定义登录: 若不想使用自动登录,即打开网页后手动登陆,请输入"1"/不输入将使用自动登陆: '))
    if custombelieve == '1':
        believe = False
        print('##### 自定义登陆设置成功')
    print()
    customloginUrl = str(input('##### 自定义URL: 请输入智慧树登录页面的完整URL/不输入将使用默认URL: '))
    if customloginUrl != '':
        loginUrl = customloginUrl
        print('##### 自定义设置URL成功')
    print()
    print('##### 自定义设置结束,请注意:#自定义设置将不会被保存#')
    print()
    tm.sleep(1)

def stopwait():
    while True:
        chr = msvcrt.getche()
        if ord(chr) == 49:
            return True
    False

#打开浏览器
def getopen():
    global browser
    global browserUrl
    global loginUrl
    global believe
    global changeBrowser
    global chrome_options
    global locator

    if believe == True:
        classNumber = -100
        username = str(input('##### 请输入账号: '))
        password = str(input('##### 请输入密码: '))
        try:
            classNumber = int(input('##### 请输入要观看列表中第几门课程: '))-1
        except:
            pass
        if username == '' or password == '' or classNumber == -100:
            print()
            print('##### 注意: 检测到有必填项为空,取消使用自动登录改为手动登录')
            print()
            believe = False
            tm.sleep(2)

    print('##### 正在开启浏览器,大概20秒,请耐心等待')
    print()
    try:
        if changeBrowser == True:
            browser = webdriver.Chrome(chrome_options=chrome_options)
        else:
            browser = webdriver.Chrome("chromedriver.exe")
    except Exception as e:
        print(e.args)
        print('##### 加载驱动失败,具体请查看说明文档')
        print('##### 程序结束,谢谢您的使用^_^')
        input('##### 回车键退出')
        sys.exit()
        pass
    try:
        browser.get(loginUrl)
        if believe == True:
            print("##### 打开登录页面并自动登陆")
            browser.find_element_by_name('username').send_keys(username)
            browser.find_element_by_name('password').send_keys(password)
            browser.find_element_by_class_name('wall-sub-btn').click()
    except:
        print('##### 打开页面失败,具体请查看说明文档')
        print('##### 程序结束,谢谢您的使用^_^')
        input('##### 回车键退出')
        sys.exit()
        pass

    if believe == False:
        print('##### 打开页面成功, 请操作并停留至看课页面,输入"1"结束等待')
        # tm.sleep(60)
        if(stopwait()):
            print()
        print('##### 完成等待,即将获取新窗口句柄')

    if believe == True:
        #如果有大于两科课程则翻页课程
        tm.sleep(2)
        if classNumber > 2:
            browser.find_element_by_id('course_recruit_studying_next').click()
            tm.sleep(1)
            classNumber = classNumber - 2
        browser.find_elements_by_class_name('speedPromote_btn')[classNumber].click()
        #切换标签页
        print('##### 切换标签页,等待2秒')
        tm.sleep(2)
#获得窗口句柄
def getwindow():
    global browser
    global browserUrl
    global loginUrl
    global believe
    global changeBrowser
    global chrome_options
    
    #获取当前窗口的句柄
    currentWin = browser.current_window_handle
    #跳转到另一个新页面
    tm.sleep(3)
    #获取所有窗口的句柄
    handles = browser.window_handles
    for i in handles:
        if currentWin == i:
            continue
    else:
        #将driver与新的页面绑定起来
        browser.switch_to_window(i)
#检测弹题
def testProblem():
    global browser
    global browserUrl
    global loginUrl
    global believe
    global changeBrowser
    global chrome_options
    global locator

    try:
        locator=(By.XPATH,"")
        WebDriverWait(browser,5,1).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR,'.popbtn_cancel')))
        print('##### 发现弹题')
        try:
            print('##### 尝试关闭弹题')
            tm.sleep(1)
            browser.execute_script(jsnoPop) #执行JS关闭弹题
            tm.sleep(1)
            browser.execute_script(jsnoOverlay) #执行JS关闭遮罩层
            try:
                browser.find_elements_by_class_name('popbtn_cancel').click()
                browser.find_elements_by_class_name('popboxes_close').click()
            except:
                pass
            print('##### 关闭弹题成功')
            try:
                browser.execute_script(js) #执行JS显示进度条
                browser.find_elements_by_class_name('bigPlayButton')[0].click()
            except:
                pass
        except Exception as e:
            print(e.args)
            print('##### 关闭弹题失败,请在5秒内手动点击关闭')
            tm.sleep(5)
            pass
    except:
        pass
#检测初始化窗口
def testinitwindow():
    try:
        tm.sleep(1)
        browser.find_elements_by_class_name('popbtn_yes')[0].click()
        print('##### 关闭弹窗1成功')
    except:
        print('##### 未发现弹窗1')
        pass

    try:
        tm.sleep(1)
        browser.find_elements_by_class_name('j-popup-close')[0].click()
        print('##### 关闭弹窗2成功')
    except:
        print('##### 未发现弹窗2')
        pass
#获得时间
def gettime(timename,elementname):
    global browser
    global browserUrl
    global loginUrl
    global believe
    global changeBrowser
    global chrome_options

    temptime = (browser.find_element_by_class_name(elementname).text).split(':')
    timename = (int(temptime[0]) * 3600) + (int(temptime[1]) * 60) + int(temptime[2])
    return timename
#获得下一集
def getnext(per):
    if per > 0.8:
        print("##### 当前播放视频进度已超过80%")
        try:
            browser.find_element_by_class_name('tm_next_lesson').click()
            print("##### 播放下一集")
        except:
            print('##### 获取下一集失败或课程已经全部看完')
            print('##### 程序结束,谢谢您的使用^_^')
            input('##### 回车键退出')
            sys.exit()
            pass
        return True
    return False

def watchtv():
    global browser
    global browserUrl
    global loginUrl
    global believe
    global changeBrowser
    global chrome_options
    global g
    global t

    for g in range(0,10000):
        #清屏
        os.system('clear')
        showlogo()

        #看课开始
        print('##### 看课开始')
        tm.sleep(1)
        print('##### 等待3秒获得初始进度')
        tm.sleep(3)

        #初始化时间变量
        init_duration = 0
        init_currentTime = 0
        duration = 0
        currentTime = 0

        #获得初始时间
        browser.execute_script(js) #执行JS显示进度条
        init_duration = gettime(init_duration,'duration')
        browser.execute_script(js) #执行JS显示进度条
        init_currentTime = gettime(init_currentTime,'currentTime')

        per = round((init_currentTime/init_duration),2)
        print('##### 初始进度:' + str(per*100) + '%')
        #判断进度
        if(getnext(per)):
            continue

        print('##### 开启1.5倍速播放')
        browser.execute_script(jsSpeed) #执行JS开启1.5倍速列表
        browser.find_element_by_class_name('speedTab15').click()
        browser.execute_script(jsnoSpeed) #执行JS关闭1.5倍速列表

        print('##### 看课中,等待弹题')
        for t in range(init_currentTime,init_duration):

            #获得当前时间
            browser.execute_script(js) #执行JS显示进度条
            duration = gettime(duration,'duration')
            browser.execute_script(js) #执行JS显示进度条
            currentTime = gettime(currentTime,'currentTime')

            per = round((currentTime/duration),2)
            #判断进度
            if(getnext(per)):
                break

            testProblem()
#我真帅
def handsome():
    tm.sleep(1)
    try:
        browser.find_element_by_id('searchValue').send_keys('我真帅')
    except:
        print('##### 当前停留页面不正确,请重启程序')
        print('##### 程序结束,谢谢您的使用^_^')
        input('##### 回车键退出')
        sys.exit()
        pass


#logo
showlogo()
mr = str(input('##### 是否使用默认设置? 输入"1"进入自定义设置/不输入将使用默认设置: '))
if mr == '1':
    #自定义设置
    costom()
#启动浏览器
getopen()
#获得窗口句柄
getwindow()
#检测弹题
print('##### 等待初始化,最长等待5秒')
testProblem()
#关闭初始化窗口
testinitwindow()

#我真帅
handsome()

'''
以上为打开课程观看页面
以下代码开始获取视频列表与当前播放视频及时间
'''

#看课
watchtv()