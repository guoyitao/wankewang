import os
import time

from selenium import webdriver

username = ""
password = ""
videoUrl = 'http://www.wanke001.com/stu/courseWare/10/4019/2519/2082/1'
driver = webdriver.Edge()

def start():
    # 视频网址

    driver.get(videoUrl)

    if str(driver.current_url).startswith("http://account.wanke001.com/login?redirectUri="):
        login()

    lookVideo()

    time.sleep(300000)

    driver.close()
    driver.quit()

def lookVideo():
    while 1:
        time.sleep(5)
        global videoPlayer

        try:
            videoPlayer = driver.find_element_by_id("video_html5_api")
            # 10倍速
            driver.execute_script("arguments[0].playbackRate = 10;", videoPlayer)
            duration = videoPlayer.get_attribute("duration")
            currentTime = videoPlayer.get_attribute("currentTime")
            if float(currentTime) >= float(duration)/1.1:
                print("下个视频")
                driver.find_element_by_id("next_detail").click()
        except:
            print("答题页")
            driver.find_element_by_id("next_detail").click()

def login():
    print("开始登录")
    el_name = driver.find_element_by_id("name")
    el_pwd = driver.find_element_by_id("pwd")
    el_btn_login = driver.find_element_by_id("btn-login")

    el_name.send_keys(username)
    el_pwd.send_keys(password)
    el_btn_login.click()

start()
