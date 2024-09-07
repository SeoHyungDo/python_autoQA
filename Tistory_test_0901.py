import pyautogui
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
tc_count = 14 # 전체 TC 카운트

print("테스트 자동화 시작 시간 : " + now)

tistory_ID = input("테스트 할 ID를 입력하세요 : ") # 테스트 할 ID를 입력 받는다
tistory_PW = input("테스트 할 PW를 입력하세요 : ") # 테스트 할 PW를 입력 받는다
print("\ntest할 ID를 "+ tistory_ID +" 로 실행합니다.")



#테스트 전 과정에 거쳐 에러 발생시 에러 기록하는 try, except 문
try : 
    f = open(f'{now}_test_result.txt','w')
    f.write(f'테스트 수행 일자 - {now}\n')

    #TC_001 홈페이지 진입 확인(Tistory 로고 노출 여부)
    tc_progress = "ATC_001"
    print("----------------------------- ATC_001 -------------------------------") 
    browser.get(url)
    browser.maximize_window()
    
    browser.implicitly_wait(10) # 10초 대기
    print("10초 내에 페이지 로딩이 되었는지 검증 시작")
    
    try :
        if browser.find_element(By.XPATH,'//*[@id="kakaoServiceLogo"]/span').is_displayed() :
            print("Tistory 로고 노출 완료!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = 'Tistory 로고 미노출, 페이지 로딩 실패'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_001.jpg',region=(0,0,1287,900))

    #TC_002 홈 메뉴 존재 확인
    tc_progress = "ATC_002"
    feed = browser.find_element(By.XPATH,'//*[@id="kakaoGnb"]/ul/li[1]/a')
    feedName = feed.text
    print("----------------------------- ATC_002 -------------------------------")
    print('홈 위치 메뉴명 => ' + feedName)

    try : 
        if feedName == '홈' :
            print("GNB 메뉴 '홈' 노출 성공!")
            result_pass_list.append(tc_progress)

        else :
            fail_reason = 'GNB 메뉴 "홈" 가 아닌 항목 노출'
            print(fail_reason)
            result_fail_list.append(tc_progress)
            fail_reason_list.append(fail_reason)
            sleep(0.5) # 빠른 로딩으로 인한 백색화면 캡쳐 방지
            pyautogui.screenshot(f'./{now}_Fail_shot_TC_002.jpg',region=(0,0,1287,900))

    except Exception as e :
        fail_reason = 'GNB 메뉴 "홈" 미 노출 / 오탈자 외의 이슈 발생으로 인한 테스트 실패'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        sleep(0.5) # 빠른 로딩으로 인한 백색화면 캡쳐 방지
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_002.jpg',region=(0,0,1287,900))


    #TC_003 피드 메뉴 존재 확인
    tc_progress = "ATC_003"
    story = browser.find_element(By.XPATH,'//*[@id="kakaoGnb"]/ul/li[2]/a')
    StoryName = story.text
    print("----------------------------- ATC_003 -------------------------------")
    print('피드 위치 메뉴명 => ' + StoryName)

    try : 
        if StoryName == '피드' :
            print("GNB 메뉴 '피드' 노출 성공!")
            result_pass_list.append(tc_progress)

        else :
            fail_reason = 'GNB 메뉴 "피드" 가 아닌 항목 노출'
            print(fail_reason)
            result_fail_list.append(tc_progress)
            fail_reason_list.append(fail_reason)
            sleep(0.5) # 빠른 로딩으로 인한 백색화면 캡쳐 방지
            pyautogui.screenshot(f'./{now}_Fail_shot_TC_003.jpg',region=(0,0,1287,900))

    except Exception as e :
        fail_reason = 'GNB 메뉴 "피드" 미 노출 / 오탈자 외의 이슈 발생으로 인한 테스트 실패'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        sleep(0.5) # 빠른 로딩으로 인한 백색화면 캡쳐 방지
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_003.jpg',region=(0,0,1287,900))


    
    #TC_004 스킨 메뉴 존재 확인
    tc_progress = "ATC_004"
    skin = browser.find_element(By.XPATH,'//*[@id="kakaoGnb"]/ul/li[3]/a')
    SkinName = skin.text
    print("----------------------------- ATC_004 -------------------------------")
    print('스킨 위치 메뉴명 => ' + SkinName)

    try : 
        if SkinName == '스킨' :
            print("GNB 메뉴 '스킨' 노출 성공!")
            result_pass_list.append(tc_progress)

        else :
            fail_reason = 'GNB 메뉴 "스킨" 이 아닌 항목 노출'
            print(fail_reason)
            result_fail_list.append(tc_progress)
            fail_reason_list.append(fail_reason)
            sleep(0.5) # 빠른 로딩으로 인한 백색화면 캡쳐 방지
            pyautogui.screenshot(f'./{now}_Fail_shot_TC_004.jpg',region=(0,0,1287,900))

    except Exception as e :
        fail_reason = 'GNB 메뉴 "스킨" 미 노출 / 오탈자 외의 이슈 발생으로 인한 테스트 실패'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)

    #TC_005 포럼 메뉴 존재 확인
    tc_progress = "ATC_005"
    forum = browser.find_element(By.XPATH,'//*[@id="kakaoGnb"]/ul/li[4]/a')
    ForumName = forum.text
    print("----------------------------- ATC_005 -------------------------------")
    print('포럼 위치 메뉴명 => ' + ForumName)

    try : 
        if ForumName == '포럼' :
            print("GNB 메뉴 '포럼' 노출 성공!")
            result_pass_list.append(tc_progress)

        else :
            fail_reason = 'GNB 메뉴 "포럼" 이 아닌 항목 노출'
            print(fail_reason)
            result_fail_list.append(tc_progress)
            fail_reason_list.append(fail_reason)
            sleep(0.5) # 빠른 로딩으로 인한 백색화면 캡쳐 방지
            pyautogui.screenshot(f'./{now}_Fail_shot_TC_005.jpg',region=(0,0,1287,900))

    except Exception as e :
        fail_reason = 'GNB 메뉴 "포럼" 미 노출 / 오탈자 외의 이슈 발생으로 인한 테스트 실패'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        sleep(0.5) # 빠른 로딩으로 인한 백색화면 캡쳐 방지
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_005.jpg',region=(0,0,1287,900))

    # end_time = time.time()
    # progress_time = end_time - start_time
    # print("피드 메뉴 진입하는데 소요된 시간은 " + progress_time + " 초 입니다.")

    #TC_006 상단 공지아이콘 노출 확인
    tc_progress = "ATC_006"
    print("----------------------------- ATC_006 -------------------------------")   
    try :
        if browser.find_element(By.XPATH,'//*[@id="kakaoHead"]/div/div[2]/div[1]/div/span[2]').is_displayed() :
            print("상단 공지 아이콘 노출 확인!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '상단 공지 아이콘 미노출\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_006.jpg',region=(0,0,1287,900))

    #TC_007 상단 공지 텍스트 확인
    tc_progress = "ATC_007"
    notice_text = browser.find_element(By.XPATH,'//*[@id="kakaoHead"]/div/div[2]/div[1]/div/a')
    NotiText = notice_text.text
    print("----------------------------- ATC_007 -------------------------------")
    print("상단 공지 문구 노출 확인")

    try : 
        if NotiText == '새로워진 티스토리를 소개합니다 ✨' :
            print("'새로워진 티스토리를 소개합니다 ✨'문구 노출 성공!")
            result_pass_list.append(tc_progress)

        else :
            fail_reason = '새로워진 티스토리를 소개합니다 ✨ 문구 노출 실패!\n 출력된 문구 => ' + NotiText
            print(fail_reason)
            result_fail_list.append(tc_progress)
            fail_reason_list.append(fail_reason)
            sleep(0.5) # 빠른 로딩으로 인한 백색화면 캡쳐 방지
            pyautogui.screenshot(f'./{now}_Fail_shot_TC_007.jpg',region=(0,0,1287,900))

    except Exception as e :
        fail_reason = '문구 외의 에러 발생으로 인한 테스트 실패'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_007.jpg',region=(0,0,1287,900))

    

    # TC_008 [시작하기] 버튼 노출여부 확인 / 텍스트 확인을 위한 상단 패스 값 지정
    tc_progress = "ATC_008"
    startbutton = browser.find_element(By.XPATH,'//*[@id="kakaoHead"]/div/div[2]/div[2]/button')
    startbutton_text = startbutton.text
    print("----------------------------- ATC_008 -------------------------------")
    print("우측 상단 [시작하기] 버튼 노출 확인")

    try :
        if startbutton.is_displayed() :
            print("시작 버튼 정상 노출!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '[시작하기] 버튼 노출 실패'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_008.jpg',region=(0,0,1287,900))


    # TC_009 [시작하기] 버튼 텍스트 확인
    tc_progress = "ATC_009"
    print("----------------------------- ATC_009 -------------------------------")
    print("우측 상단 [시작하기] 버튼 명칭 확인")

    try :
        if startbutton_text == '시작하기' :
            print("[시작하기] 버튼 명칭 일치!")
            result_pass_list.append(tc_progress)

        else :
            fail_reason = '[시작하기] 버튼 명칭이 기획대로 구현되지 않았습니다. \n 출력된 문구 => ' + startbutton_text
            print(fail_reason)
            result_fail_list.append(tc_progress)
            fail_reason_list.append(fail_reason)
            sleep(0.5) # 빠른 로딩으로 인한 백색화면 캡쳐 방지
            pyautogui.screenshot(f'./{now}_Fail_shot_TC_009.jpg',region=(0,0,1287,900))

    except Exception as e :
        fail_reason = '[시작하기] 버튼 노출 실패'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_001.jpg',region=(0,0,1287,900))

    #TC_010 오늘의 티스토리 이미지 노출 확인
    tc_progress = "ATC_010"
    print("----------------------------- ATC_010 -------------------------------")   
    try :
        if browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[1]/div[1]/div/div[2]/div/a/div[1]').is_displayed() :
            print("오늘의 티스토리 이미지 노출 확인!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '오늘의 티스토리 이미지 미노출\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_010.jpg',region=(0,0,1287,900))

# TC_011 오늘의 티스토리 하단 페이징 버튼 노출 확인
    tc_progress = "ATC_011"
    print("----------------------------- ATC_011 -------------------------------")   
    try :
        if browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[1]/div[2]/div').is_displayed() :
            print("오늘의 티스토리 하단 페이징 버튼 노출 확인!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '오늘의 티스토리 하단 페이징 버튼 미노출\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_011.jpg',region=(0,0,1287,900))

    #TC_012 오늘의 티스토리 Top5 포스트 노출 여부 확인
    tc_progress = "ATC_012"
    print("----------------------------- ATC_012 -------------------------------") 
    today_tistory_01 = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[2]/div[1]/div/a[2]/div[1]')
    today_tistory_01_text = today_tistory_01.text
    today_tistory_02 = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[2]/div[2]/div/a[2]/div[1]')
    today_tistory_02_text = today_tistory_02.text
    today_tistory_03 = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[2]/div[3]/div/a[2]/div[1]')
    today_tistory_03_text = today_tistory_03.text
    today_tistory_04 = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[2]/div[4]/div/a[2]/div[1]')
    today_tistory_04_text = today_tistory_04.text
    today_tistory_05 = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[2]/div[5]/div/a[2]/div[1]')
    today_tistory_05_text = today_tistory_05.text
    
    try :
        if today_tistory_01.is_displayed() and today_tistory_02.is_displayed() and today_tistory_03.is_displayed() and today_tistory_04.is_displayed() and today_tistory_05.is_displayed() :
            print("오늘의 티스토리 하단 Top5 포스트 -> 5개 포스트 모두 노출 확인!")
            print(today_tistory_01_text)
            print(today_tistory_02_text)
            print(today_tistory_03_text)
            print(today_tistory_04_text)
            print(today_tistory_05_text)
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '오늘의 티스토리 하단 Top5 포스트 미노출\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_012.jpg',region=(0,0,1287,900))

    #TC_013 스토리 크리에이터 메뉴 노출 여부 확인
    tc_progress = "ATC_013"
    print("----------------------------- ATC_013 -------------------------------")
    story_creater_title = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[2]/div/div[2]/div[1]/h2/span')
    story_creater_title_01 = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[2]/div/div[2]/div[2]/div[1]')
    story_creater_title_01_text = story_creater_title_01.text
    story_creater_title_02 = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[2]/div/div[2]/div[3]/div[1]')
    story_creater_title_02_text = story_creater_title_02.text

    try :
        if story_creater_title.is_displayed() and story_creater_title_01.is_displayed() and story_creater_title_02.is_displayed() :
            print("스토리 크리에이터 메뉴 타이틀 및 2명의 크리에이터 노출 성공!")
            print(story_creater_title_01_text)
            print(story_creater_title_02_text)
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '스토리 크리에이터 메뉴 타이틀 및 2명의 크리에이터 미노출\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_013.jpg',region=(0,0,1287,900))

    #TC_014 스토리 크리에이터 메뉴 포스트 2개 노출 여부 확인
    tc_progress = "ATC_014"
    story_creater01 = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[2]/div/div[2]/div[2]/div[2]/a[1]/div[1]/strong')
    story_creater02 = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[2]/div/div[2]/div[2]/div[2]/a[2]/div[1]/strong')
    story_creater01_text = story_creater01.text
    story_creater02_text = story_creater02.text
    
    print("----------------------------- ATC_014 -------------------------------")   
    try :
        if story_creater01.is_displayed() and story_creater02.is_displayed() :
            print("스토리 크리에이터 2개 포스트 노출 성공!")
            print(story_creater01_text)
            print(story_creater02_text)
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '스토리 크리에이터 2개 포스트 미노출\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_014.jpg',region=(0,0,1287,900))

#    action = browser.find_element(By.CSS_SELECTOR,'body')

#    action.send_keys(Keys.PAGE_DOWN)

    browser.find_element(By.XPATH,'//*[@id="kakaoHead"]/div/div[3]/div/a').click()
    browser.find_element(By.XPATH,'/html/body/div[5]/div/div/a[2]/span[2]').click()
    browser.find_element(By.XPATH,'//*[@id="loginId--1"]').click()
    browser.find_element(By.ID,'loginId--1').send_keys(tistory_ID)
    print("로그인 화면_ID 입력 완료!")
    sleep(1)

    browser.find_element(By.XPATH,'//*[@id="password--2"]').click()
    browser.find_element(By.ID,'password--2').send_keys(tistory_PW)
    browser.find_element(By.XPATH,'//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()
    print("로그인 화면_Password 입력 완료!")
    sleep(1)

    browser.find_element(By.XPATH,'//*[@id="kakaoGnb"]/ul/li[1]/a').click() # 좌측 상단 '피드' 버튼 클릭
    print("피드 메뉴 진입 성공!")

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
    f.write(f'{fail_reason_list}\n')

f.write('\n')
f.write(f'PASS TC COUNT : {len(result_pass_list)}\n') # PASS TC 갯수
f.write(f'Fail TC COUNT : {len(result_fail_list)}\n') # Fail TC 갯수
f.write(f'Complete TC COUNT : {len(result_pass_list) + len(result_fail_list)}\n') # 수행 완료 TC 갯수
f.write(f'Progress TC COUNT (1이 나올 경우 100%) : {(len(result_pass_list) + len(result_fail_list))/tc_count}\n') # TC 진척률
f.write(f'Pass Rate : {(len(result_pass_list)/tc_count)*100}%\n') # PASS 비율
f.write(f'Fail Rate : {(len(result_fail_list)/tc_count)*100}%\n') # Fail 비율

# print("FailList ==> " + result_fail_list)
# print("FailReason ==> " + fail_reason_list)
