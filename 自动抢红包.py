from appium import webdriver
import time

desired_caps = {

    'platformName': 'Android',
    # 使用哪种平台
    'deviceName': '158bcb1',
    # 启用设备名称
    'platformVersion': '8.1',
    # 指定平台的系统版本
    'appPackage': 'com.tencent.mm',
    # 待测试的app的package
    'appActivity': 'com.tencent.mm.ui.LauncherUI'
    # 待测试的Activity的名字
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)
# 打开微信后等待5s时间

'''
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return(x,y)
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.75)
    y2 = int(l[1] * 0.25)
    driver.swipe(x1,y1,x1,y2,t)
'''
num = 0
num0 = 0
while 1:
    driver.find_element_by_id("com.tencent.mm:id/an7").click()
    # 点开最顶端的群聊
    try:
        driver.find_element_by_id("com.tencent.mm:id/a92").click()
        # 如果有多条消息未读按钮，则点击以到达未读消息顶端
    except:
        while num0 < 5:
            if num < 5:
                try:
                    driver.find_element_by_id("com.tencent.mm:id/abz").click()
                    # 如果找到红包，则打开
                except:
                    driver.swipe(300, 1000, 300, 300, 0)
                    num0 += 1
                    # 没有找到红包，则向上大幅度划动一次，num0+1
                try:
                    driver.find_element_by_id("com.tencent.mm:id/bv8").click()
                    # 如果打开了红包，则点击“开”
                except:
                    num += 1
                    # 如果五次打不开红包，则认为此群的没有可以继续打开的红包，退出群聊
                try:
                    driver.find_element_by_id("com.tencent.mm:id/hg").click()
                    # 领取完红包之后，点击左上角的箭头以返回
                except:
                    pass
                try:
                    driver.find_element_by_id("com.tencent.mm:id/bsv").click()
                    # 如果红包未领取完已过期，则点击×返回
                except:
                    pass
                driver.swipe(100, 450, 100, 200, 0)
                # 向下滑动以找到下一个红包的位置
            else:
                break
        try:
            driver.find_element_by_id("android:id/text1").click()
            # 执行完毕，退出群聊
        except:
            driver.find_element_by_id("com.tencent.mm:id/h1").click()
            # 如果点开了公众号列表，则点击左上角退出
    num = 0
    num0 = 0
    time.sleep(1)
    driver.swipe(100, 400, 100, 200, 0)
    # 找到下一个群聊的位置

'''
names_all = driver.find_elements_by_id("com.tencent.mm:id/an7")
#"com.tencent.mm:id/an7"为所有昵称的id，首先收集所有昵称的id到变量names_all
target = "434脱单率100%"
target_trans = target.decode("utf-8")
for n in names_all:
	if n.get_attribute("text") == target_trans:
		n.click()
		break
'''

