from selenium import webdriver # WebDriver를 사용하기 위함
from selenium.webdriver.common.by import By # xpath, css, id 값 등 element를 사용하기 위함
from selenium.webdriver.common.keys import Keys # Enter 키 등 기본 키 입력을 넣을수 있게 해줌
from time import sleep
import time
# import pytest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
service = Service(executable_path=ChromeDriverManager().install()) # 자동 업데이트 서비스 객체 생성.
browser = webdriver.Chrome()

url = 'https://www.tistory.com'
#현재 시간 구하기
now = time.strftime('%Y_%m_%d_%H_%M') # m의 경우 월, M의 경우 분이 들어가니 주의

result_pass_list = [] # pass한 TC ID를 보유한 리스트
result_fail_list = [] # fail한 TC ID를 보유한 리스트
fail_reason_list = [] # fail한 이유를 보유한 리스트
tc_count = 2 # 전체 TC 카운트

print("테스트 자동화 시작 시간 : " + now)

tistory_ID = input("테스트 할 ID를 입력하세요 : ") # 테스트 할 ID를 입력 받는다
tistory_PW = input("테스트 할 PW를 입력하세요 : ") # 테스트 할 PW를 입력 받는다
print("\ntest할 ID를 "+ tistory_ID +" 로 실행합니다.")

#테스트 전 과정에 거쳐 에러 발생시 에러 기록하는 try, except 문
try : 
    f = open(f'{now}_test_result.txt','w')
    f.write(f'테스트 수행 일자 - {now}\n')

    #TC_001 홈페이지 진입 확인(Tistory 로고 노출 여부)
    tc_progress = "TC_001"
     
    browser.get(url)
    browser.maximize_window()
    browser.find_element(By.XPATH,'//*[@id="kakaoHead"]/div/div[3]/div/a').click()
    browser.find_element(By.XPATH,'/html/body/div[5]/div/div/a[2]/span[2]').click()
    browser.find_element(By.XPATH,'//*[@id="loginId--1"]').click()
    browser.find_element(By.ID,'loginId--1').send_keys(tistory_ID)
    print("로그인 화면_ID 입력 완료!")

    browser.find_element(By.XPATH,'//*[@id="password--2"]').click()
    browser.find_element(By.ID,'password--2').send_keys(tistory_PW)
    browser.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
    print("로그인 화면_Password 입력 완료!")

    start_time = time.time()
    print("password 입력 후 10초 내에 페이지 로딩이 되었는지 검증 시작")
    browser.implicitly_wait(10) # 10초 대기
    end_time = time.time()

    try :
        if browser.find_element(By.XPATH,'//*[@id="kakaoServiceLogo"]/span[2]').is_displayed() :
            print("Tistory 로고 노출 완료!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = 'Tistory 로고 미노출, 페이지 로딩 실패'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)

    #TC_002 피드 메뉴 존재 확인

    tc_progress = "TC_002"
    start_time = time.time()
    feed = browser.find_element(By.XPATH,'//*[@id="kakaoGnb"]/ul/li[1]/a')
    feedName = feed.text
    print('피드 위치 메뉴명 => ' + feedName)

    try : 
        if feedName == ('피드') :
            print("GNB 메뉴 '피드' 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = 'GNB 메뉴 "피드" 가 아닌 항목 노출'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)


    browser.find_element(By.XPATH,'//*[@id="kakaoGnb"]/ul/li[1]/a').click() # 좌측 상단 '피드' 버튼 클릭
    print("피드 메뉴 진입 성공!")
    end_time = time.time()
    progress_time = end_time - start_time
    print("피드 메뉴 진입하는데 소요된 시간은 " + progress_time + " 초 입니다.")

except Exception as e: 
    print()


#PASS TC 결과
f.write('\n[RESULT - PASS]\n')
for pass_cnt in range(len(result_pass_list)) :
    f.write(f'{result_pass_list[pass_cnt]} : PASS \n')

#FAIL TC 결과
f.write('\n[RESULT - Fail]\n')
for fail_cnt in range(len(result_fail_list)) :
    f.write(f'{result_fail_list[fail_cnt]} : Fail \n')
    f.write(f'{fail_reason_list}')

f.write('\n')
f.write(f'PASS TC COUNT : {len(result_pass_list)}\n') # PASS TC 갯수
f.write(f'Fail TC COUNT : {len(result_fail_list)}\n') # Fail TC 갯수
f.write(f'Complete TC COUNT : {len(result_pass_list) + len(result_fail_list)}\n') # 수행 완료 TC 갯수
f.write(f'Progress TC COUNT (1이 나올 경우 100%) : {(len(result_pass_list) + len(result_fail_list))/tc_count}\n') # TC 진척률
f.write(f'Pass Rate : {(len(result_pass_list)/tc_count)*100}%\n') # PASS 비율
f.write(f'Pass Rate : {(len(result_fail_list)/tc_count)*100}%\n') # Fail 비율

# print("FailList ==> " + result_fail_list)
# print("FailReason ==> " + fail_reason_list)
