from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

url = "https://URL은 비밀/"

browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()
sleep(1)

try : 
    warning = browser.find_element(By.XPATH,'//*[@id="details-button"]') 
    warning.click() # 안전하지 않은 사이트 뜨는 경우 '고급' 클릭
    print("안전하지 않은 사이트 '고급' 클릭")
    warning_warp = browser.find_element(By.XPATH,'//*[@id="proceed-link"]') 
    warning_warp.click() # '안전하지 않은 사이트' 고급을 누른 경우 '안전하지 않은 사이트 이동' 클릭
    print("안전하지 않은 사이트 이동' 클릭")
    sleep(1)
    
except : 
    print("안전하지 않은 사이트 팝업이 출력되지 않았습니다.")

print("1. 로그인 페이지 검증 진행")

Top_login = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div/p')
Top_login_text = Top_login.text
if Top_login_text == '로그인' : print("상단 로그인 버튼은 " + Top_login_text + " 으로 정상 출력 되었습니다.")
else : print("Test Fail! 상단 로그인 버튼은 '" + Top_login_text + "' 으로 출력 되었습니다. 수정이 필요합니다")

left_logo = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[1]/h1/span')
left_text = left_logo.text
if left_text == 'K-Remote Management Solution' : print ("좌측 Logo 하단 Text에 'K-Remote Management Solution이 정상 출력 되었습니다")
else : print ("좌측 Logo 하단 Text에 'K-Remote Management Solution이 아닌 '" + left_text + "' 로 출력되어 있습니다.")

"""
Login_id_text_box = browser.find_element(By.XPATH,'//*[@id="userId"]')
Login_text = Login_id_text_box.text
if Login_text == '아이디를 입력하세요.' : print ("'ID TextBox에 아이디를 입력하세요' 문구가 정상 출력되었습니다.")
else : print ("ID Textbox에 '아이디를 입력하세요'가 아닌 '" + Login_text + "' 로 출력되어 있습니다.")

Login_pw_text_box = browser.find_element(By.XPATH,'//*[@id="userPw"]')
Login_pw_text = Login_pw_text_box.text
if Login_pw_text == '비밀번호를 입력하세요.' : print ("'PW TextBox에 비밀번호를 입력하세요' 문구가 정상 출력되었습니다.")
else : print ("PW Textbox에 '비밀번호를 입력하세요'가 아닌 '" + Login_text + "' 로 출력되어 있습니다.")
"""

login_button = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div/form/fieldset/button')
login_button_text = login_button.text
if login_button_text == '로그인' : print("버튼명은 '로그인'으로 정상 출력 되었습니다")
else : print ('버튼명이 로그인이 아니라 ' + login_button_text + ' 으로 출력되어 있습니다.')

browser.find_element(By.XPATH,'//*[@id="userId"]').click()
sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="userId"]').send_keys('ID는 비밀')
sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="userPw"]').click()
sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="userPw"]').send_keys('Password는 비밀') 
sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div/form/fieldset/button/span').click()
sleep(10)


try :
   popup1 = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/span') # 장치 품질 로그 / 앱 오류 / 앱 재기동 로그 오류 중 팝업이 한 개인 경우 종료
   popup1.click()
   print("장치 품질 로그 / 앱 오류 / 앱 재기동 로그 오류 중 팝업이 한개의 오류 팝업이 발생하였으며, 해당 팝업을 종료하였습니다.")
   error_name1 = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div/div/div/div[2]/div/p')
   error_detail1 = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div/div/div/div[2]/div/div')
   error_time1 = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div[1]/div/div/div[1]/h5')
   error_name = error_name1.text
   error_detail = error_detail1.text
   error_time = error_time1.text
   print("첫번째 에러 팝업 출력시간은 " + error_time + " 출력된 에러는 " + error_name + " 입니다. 출력된 에러 종류는 " + error_detail + " 입니다." )
   
   popup2 = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/span') # 장치 품질 로그 / 앱 오류 / 앱 재기동 로그 오류 중 팝업이 두 개인 경우 종료
   popup2.click()
   print("장치 품질 로그 / 앱 오류 / 앱 재기동 로그 오류 중 팝업이 두개의 오류 팝업이 발생하였으며, 해당 팝업을 종료하였습니다.")
   error_name2 = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div[2]/div/div/div[2]/div/p')
   error_detail2 = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div[2]/div/div/div[2]/div/div')
   error_time2 = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div[2]/div/div/div[1]/h5')
   error_name = error_name2.text
   error_detail = error_detail2.text
   error_time = error_time2.text
   print("두번째 에러 팝업 출력시간은 " + error_time +" 출력된 에러는 " + error_name + " 입니다. 출력된 에러 종류는 " + error_detail + " 입니다." )
   
   popup3 = browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[3]/div/div/div[1]/span') # 장치 품질 로그 / 앱 오류 / 앱 재기동 로그 오류 중 팝업이 세 개인 경우 종료
   popup3.click()
   print("장치 품질 로그 / 앱 오류 / 앱 재기동 로그 오류 중 팝업이 세개의 오류 팝업이 발생하였으며, 해당 팝업을 종료하였습니다.")
   error_name3 = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div[3]/div/div/div[2]/div/p')
   error_detail3 = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div[3]/div/div/div[2]/div/div')
   error_time3 = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div[3]/div/div/div[1]/h5')
   error_name = error_name3.text
   error_detail = error_detail3.text
   error_time = error_time3.text
   print("세번째 에러 팝업 출력시간은 " + error_time + " 출력된 에러는 " + error_name + " 입니다. 출력된 에러 종류는 " + error_detail + " 입니다." )

except :
   print("팝업이 더 이상 없습니다.")

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


sleep(5)
