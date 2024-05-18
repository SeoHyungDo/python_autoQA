from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

url = "테스트할 URL" // 보안상 가림

browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()
sleep(1)
browser.find_element(By.XPATH,'//*[@id="userId"]').click()
sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="userId"]').send_keys('ID 입력') // 보안상 가림
sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="userPw"]').click()
sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="userPw"]').send_keys('PW 입력') // 보안상 가림 
sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div/form/fieldset/button/span').click()
sleep(10)

"""
# isDisplay = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div/div/div/div[1]').is_displayed() # 장치 품질 오류 팝업이 보이면 True, 아니면 False
browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div/div/div/div[1]/span').click() # 장치 품질 오류 팝업 제거
print("장치 품질 오류 팝업 제거 성공!")


isDisplay2 = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div[1]/div/div/div[1]').is_displayed() # 앱 오류 팝업이 보이면 True, 아니면 False
browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div[1]/div/div/div[1]/span').click() # 앱 오류 팝업 제거
print("앱 오류 팝업 제거 성공!")

isDisplay3 = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div[2]/div/div/div[1]/span').is_displayed() # 앱 재기동 로그 오류 팝업이 보이면 True, 아니면 False
browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div[2]/div/div/div[1]/span').click() # 앱 재기동 로그 오류 팝업 제거
print("앱 재기동 로그 팝업 제거 성공!")
sleep(5)

"""
browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/div/div[1]/span').click() # 장치 품질 오류 팝업 제거
print("장치 품질 오류 팝업 제거 성공!")
sleep(5)

browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/nav/ul[2]/li/div/span[2]').click() # 장치 리스트 클릭
print("장치 리스트 진입 성공!")

sleep(5)

browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[1]/div/section[2]/div[1]/span/i').click() # 테이블 컬럼 선택 버튼 클릭
print("테이블 컬럼 버튼 클릭 => OK")
browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[1]/div/section[2]/div[1]/div/ul/li[4]/label/input').click() # 테이블 컬럼 'WAN IP' 토글 버튼 클릭
print("WAN IP 토글 버튼 클릭 => OK")
browser.find_element(By.XPATH,'//*[@id="column_menu_wrap"]/div/div/button[2]').click() # 테이블 컬럼 '저장' 버튼 클릭
print("저장 버튼 클릭 => OK")

action = browser.find_element(By.CSS_SELECTOR,'body')
action.send_keys(Keys.PAGE_DOWN)
sleep(0.5)
# browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div/div[3]/div[2]/span[2]/input').click() # 페이지 점프뛸 때 사용
# browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div/div[3]/div[2]/span[2]/input').send_keys('110') # 페이지 점프뛸 때 사용

for p in range(1, 174, 1) :
  for d in range(1, 16, 1) :
     action = browser.find_element(By.CSS_SELECTOR,'body')
     device_list = '//*[@id="data-table"]/tbody/tr[{}]/td[13]/span[2]'.format(d)
     for_play = browser.find_element(By.XPATH, device_list)
     for_play.click() ## 더보기 버튼 클릭
     print("더보기 클릭, 장치 상세 진입")
     SMSTagInfo = browser.find_element(By.XPATH,'//*[@id="accordion_wrap_main"]/div[1]/h3/span[1]') # 해당 기기의 SMS Tag 가져오기
     SMSTag = SMSTagInfo.text
     print("현재 접속한 SMS Tag는 " + SMSTag)
     sleep(10)
     action.send_keys(Keys.PAGE_DOWN)
     sleep(0.5)
     action.send_keys(Keys.PAGE_DOWN)
     sleep(0.5)
     action.send_keys(Keys.PAGE_DOWN)
     sleep(0.5)
     print("Page down 3회 완료")
     browser.find_element(By.XPATH,'//*[@id="accordion_wrap_network"]/div[1]/div[1]').click()
     print("네트워크 탭 클릭")
     sleep(20)
     browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[3]/div[1]/div[2]/span[14]').click()
     print("네트워크_Refresh 클릭")
     sleep(10)
     action.send_keys(Keys.PAGE_UP)
     sleep(0.5)
     action.send_keys(Keys.PAGE_UP)
     sleep(0.5)
     action.send_keys(Keys.PAGE_UP)
     sleep(0.5)
     print("Page UP 3회 완료")
     browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/nav/ul[2]/li/div/span[2]').click()
     print("장치 버튼 클릭")
     sleep(5)
action.send_keys(Keys.PAGE_DOWN)
sleep(0.5) 
browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[3]/div[2]/span[3]/i').click()

sleep(5)

