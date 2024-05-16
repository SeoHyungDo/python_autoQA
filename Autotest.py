from selenium import webdriver # WebDriver를 사용하기 위함
from selenium.webdriver.common.by import By # xpath, css, id 값 등 element를 사용하기 위함
from selenium.webdriver.common.keys import Keys # Enter 키 등 기본 키 입력을 넣을수 있게 해줌
from time import sleep

browser = webdriver.Chrome()

url = 'http://www.tistory.com'
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


# browser.find_element(By.XPATH,'//*[@id="kakaoHead"]/div/div[2]/div/a[2]').click() # 우측 상단 글로벌 버튼 클릭
# browser.get(By.CLASS_NAME,"txt_id txt_id_type2")


sleep(10)

