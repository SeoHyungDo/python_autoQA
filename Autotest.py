from selenium import webdriver # WebDriver를 사용하기 위함
from selenium.webdriver.common.by import By # xpath, css, id 값 등 element를 사용하기 위함
from selenium.webdriver.common.keys import Keys # Enter 키 등 기본 키 입력을 넣을수 있게 해줌
from time import sleep

import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()

url = 'http://www.tistory.com'

"""
bsurl = requests.get(url)
bsurl.raise_for_status()

soup = BeautifulSoup(bsurl.text,"lxml")
print(soup.title)

"""

browser.get(url)
browser.maximize_window()
browser.find_element(By.XPATH,'//*[@id="kakaoHead"]/div/div[2]/div/a').click()
browser.find_element(By.XPATH,'//*[@id="cMain"]/div/div/div/a[2]').click()
browser.find_element(By.XPATH,'//*[@id="loginId--1"]').click()
browser.find_element(By.ID,'loginId--1').send_keys('test_seo')
browser.find_element(By.XPATH,'//*[@id="password--2"]').click()
print("로그인 화면_ID 입력 완료!")
browser.find_element(By.ID,'password--2').send_keys('Te303170!')
browser.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
print("로그인 화면_Password 입력 완료!")
print("로그인 성공! Tistory 메인 화면 출력")
sleep(3)

browser.find_element(By.XPATH,'//*[@id="kakaoGnb"]/ul/li[1]/a').click() # 좌측 상단 '피드' 버튼 클릭
print("피드 메뉴 진입 성공!")
feed = browser.find_element(By.XPATH,'//*[@id="kakaoGnb"]/ul/li[1]/a')
feedName = feed.text
if feedName == '피드' : print("메뉴명은 파드가 맞습니다!")
if feedName != '피드' : print("메뉴명은 현재 파드가 아니라," + feedName + " 입니다")


sleep(10)


