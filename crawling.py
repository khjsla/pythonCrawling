# print("jhello")
from selenium import webdriver

import time
from openpyxl import Workbook

import pandas as pd
from selenium.webdriver.common.keys import Keys

location_object_css="div.o-MQd.z8cbW > div.M30cS > div.JF9hh > a.O4GlU" 
upload_id_object_css="div.e1e1d > span.Jv7Aj.MqpiF > a.sqdOP.yWX7d._8A5w5.ZIAjV " 
date_object_css="div.k_Q0X.NnvRN > a.c-Yi7 > time._1o9PC.Nzb55" 
main_text_object_css="div.C7I1f.X7jCj > div.C4VMK > span" 
tag_css=".C7I1f.X7jCj"
comment_more_btn="button.dCJp8.afkep" 
comment_ids_objects_css="ul.Mr508 > div.ZyFrc > li.gElp9.rUo9f > div.P9YgZ > div.C7I1f > div.C4VMK > h3" 
comment_texts_objects_css="ul.Mr508 > div.ZyFrc > li.gElp9.rUo9f > div.P9YgZ > div.C7I1f > div.C4VMK > span" 
print_flag=False 
next_arrow_btn_css1="._65Bje.coreSpriteRightPaginationArrow" 
next_arrow_btn_css2="._65Bje.coreSpriteRightPaginationArrow"
# another code

wb = Workbook(write_only=True)
ws = wb.create_sheet()

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
driver.implicitly_wait(3)

# 로그인
driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input").send_keys("YOUR_INSTA_ID")
driver.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input").send_keys("YOUR_INSTA_PASSWORD")
driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div").click()
time.sleep(1)

# 팝업 종료
driver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button").click()
driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
time.sleep(1)

# 계정 접근
insta_name = driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input")
insta_name.send_keys('YOUR_INSTA_ID')
time.sleep(2)

insta_name.send_keys(Keys.ENTER)
insta_name.send_keys(Keys.ENTER)
time.sleep(2)

# N 번째 게시물 클릭
driver.find_elements_by_css_selector('._9AhH0')[YOUR_INSTA_CONTENT_NUMBER].click()
time.sleep(1)

# 댓글 플러스 버튼 누르기
while True:
    try:
        button = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > li > div > button > span')
    except:
        pass

    if button is not None:
        try:
            driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > li > div > button > span').click()
        except:
            break

# 대댓글 버튼 누르기
buttons = driver.find_elements_by_css_selector('li > ul > li > div > button')

for button in buttons:
    button.send_keys(Keys.ENTER)

    # 댓글 내용 추출
id_f = []
rp_f = []

ids  = driver.find_elements_by_css_selector('div.C4VMK > h3 > div > span > a')
replies = driver.find_elements_by_css_selector('div.C7I1f > div.C4VMK > span')

for id, reply in zip(ids, replies):
    id_a = id.text.strip()
    id_f.append(id_a)

    rp_a = reply.text.strip()
    rp_f.append(rp_a)


    data = {"아이디": id_f,
            "코멘트": rp_f}

df = pd.DataFrame(data)
df.to_excel('result.xlsx')

driver.quit()