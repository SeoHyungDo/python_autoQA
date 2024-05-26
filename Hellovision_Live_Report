from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest, logging # 로그 레벨 설정

session_logger = logging.getLogger('snowflake.snowpark.session')
session_logger.setLevel(logging.DEBUG) # 로그 레벨 설정

url = "https://rms.lghellovision.com"

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
    print("'안전하지 않은 사이트 이동' 클릭")
    sleep(1)
    
except : 
    print("안전하지 않은 사이트 팝업이 출력되지 않았습니다.")

print("1. 로그인 페이지 검증 진행")

def test_1_top_login_text() :
    Top_login = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div/p')
    Top_login_text = Top_login.text
    assert Top_login_text == '로그인'
    assert(True)
    if Top_login_text == '로그인' : print("상단 로그인 버튼은 " + Top_login_text + " 으로 정상 출력 되었습니다.")
    else : print("Test Fail! 상단 로그인 버튼은 '" + Top_login_text + "' 으로 출력 되었습니다. 수정이 필요합니다")

def test_2_logo_text() :
    left_logo = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[1]/h1/span')
    left_text = left_logo.text
    assert left_text == 'K-Remote Management Solution'
    assert(True)
    if left_text == 'K-Remote Management Solution' : print ("좌측 Logo 하단 Text에 'K-Remote Management Solution이 정상 출력 되었습니다")
    else : print ("Test Fail! 좌측 Logo 하단 Text에 'K-Remote Management Solution이 아닌 '" + left_text + "' 로 출력되어 있습니다.")

def test_3_login_button() :
    login_button = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div/form/fieldset/button')
    login_button_text = login_button.text
    assert login_button_text == '로그인'
    assert(True)
    if login_button_text == '로그인' : print("버튼명은 '로그인'으로 정상 출력 되었습니다")
    else : print ('버튼명이 로그인이 아니라 ' + login_button_text + ' 으로 출력되어 있습니다.')

def test_4_remember_button() :
    remember_button = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/div[2]/div/form/fieldset/div[3]/label')
    remember_button_text = remember_button.text
    assert remember_button_text == '회원정보 기억하기'
    assert(True)
    if remember_button_text == '회원정보 기억하기' : print("버튼명은 '회원정보 기억하기'로 정상 출력 되었습니다")
    else : print ('버튼명이 회원정보 기억하기가 아니라 ' + remember_button_text + ' 으로 출력되어 있습니다.')

browser.find_element(By.XPATH,'//*[@id="userId"]').click()
sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="userId"]').send_keys('비밀')
sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="userPw"]').click()
sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="userPw"]').send_keys('비밀') 
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

global_button = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/header/div[2]/div/p/i')
global_button.click()

def test_5_globalbutton_admin() :
    account_master = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div[1]/div/div[1]/p[1]')
    account_master_text = account_master.text
    assert account_master_text == '마스터'
    assert(True)
    if account_master_text == '마스터' : print("'마스터' 권한이 정상적으로 확인됩니다!")
    else : print("Test Fail! '마스터' 권한이 아닙니다. 해당 계정은 '마스터' 권한이어야 합니다.")

def test_6_account_mail() :
    account_mail = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div[1]/div/div[1]/p[2]')
    account_mail_text = account_mail.text
    assert account_mail_text == 'hyungdo.seo@kaonmedia.com'
    assert(True)
    if account_mail_text == 'hyungdo.seo@kaonmedia.com' : print("'hyungdo.seo@kaonmedia.com' 메일 아이디가 정상적으로 확인됩니다!")
    else : print("Test Fail! 'hyungdo.seo@kaonmedia.com' 메일 아이디가 아닙니다. 메일 아이디를 다시 확인해주세요.")

def test_7_account_mail() :
    Menu_dashboard = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/nav/ul[1]/li/div/span[2]')
    dashboard_name = Menu_dashboard.text
    assert dashboard_name == '대시보드'
    assert(True)
    if dashboard_name == '대시보드' : print ("메뉴명 '대시보드' 정상 출력 되었습니다.")
    else : print("Test Fail! 메뉴명이 '대시보드'가 아닌 " + dashboard_name + " 이 출력되고 있습니다.")

def test_8_Menu_device() :
    Menu_device = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/nav/ul[2]/li/div/span[2]')
    device_name = Menu_device.text
    assert device_name == '장치'
    assert(True)
    if device_name == '장치' : print ("메뉴명 '장치' 정상 출력 되었습니다.")
    else : print("Test Fail! 메뉴명이 '장치'가 아닌 " + device_name + " 이 출력되고 있습니다.")

def test_9_Menu_policy() :
    Menu_Policy = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/nav/ul[3]/li/div/span[2]')
    Policy_name = Menu_Policy.text
    assert Menu_Policy == '정책'
    assert(True)
    if Policy_name == '정책' : print ("메뉴명 '정책' 정상 출력 되었습니다.")
    else : print("Test Fail! 메뉴명이 '정책'이 아닌 " + Policy_name + " 이 출력되고 있습니다.")

def test_10_Menu_Statistics() :
    Menu_Statistics = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/nav/ul[4]/li/div/span[2]')
    Statistics_name = Menu_Statistics.text
    assert Menu_Statistics == '통계'
    assert(True)
    if Statistics_name == '통계' : print ("메뉴명 '통계' 정상 출력 되었습니다.")
    else : print("Test Fail! 메뉴명이 '통계'가 아닌 " + Statistics_name + " 이 출력되고 있습니다.")

def test_11_Menu_CI() :
    Menu_CI = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/nav/ul[5]/li/div/span[2]')
    CI_name = Menu_CI.text
    assert CI_name == '전산정보'
    assert(True)
    if CI_name == '전산정보' : print ("메뉴명 '전산정보' 정상 출력 되었습니다.")
    else : print("Test Fail! 메뉴명이 '전산정보'가 아닌 " + CI_name + " 이 출력되고 있습니다.")

def test_12_File_log() :
    Menu_FileLog = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/nav/ul[6]/li/div/span[2]')
    FileLog_name = Menu_FileLog.text
    assert FileLog_name == '파일 및 로그'
    assert(True)
    if FileLog_name == '파일 및 로그' : print ("메뉴명 '파일 및 로그' 정상 출력 되었습니다.")
    else : print("Test Fail! 메뉴명이 '파일 및 로그'가 아닌 " + FileLog_name + " 이 출력되고 있습니다.")

def test_13_setting() :
    Menu_Setting = browser.find_element(By.XPATH,'//*[@id="rmsApp"]/div/div/nav/ul[7]/li/div/span[2]')
    Setting_name = Menu_Setting.text
    assert Setting_name == '설정'
    assert(True)
    if Setting_name == '설정' : print ("메뉴명 '설정' 정상 출력 되었습니다.")
    else : print("Test Fail! 메뉴명이 '설정'이 아닌 " + Setting_name + " 이 출력되고 있습니다.")

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
