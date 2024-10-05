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
tc_count = 60 # 전체 TC 카운트

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

    #TC_015 스토리 크리에이터 메뉴 좋아요 버튼 / Count 노출 여부 확인
    tc_progress = "ATC_015"
    heart_icon = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[2]/div/div[2]/div[2]/div[2]/a[1]/div[1]/div/span[1]/span[1]')
    like_count = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[2]/div/div[2]/div[2]/div[2]/a[1]/div[1]/div/span[1]/span[2]')
    
    print("----------------------------- ATC_015 -------------------------------")   
    try :
        if heart_icon.is_displayed() and like_count.is_displayed() :
            print("스토리 크리에이터 첫번째 포스트 좋아요 아이콘, 좋아요 Count 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '스토리 크리에이터 첫번째 포스트 좋아요 아이콘, 좋아요 Count 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_015.jpg',region=(0,0,1287,900))

  #TC_016 스토리 크리에이터 댓글 버튼 / Count 노출 여부 확인
    tc_progress = "ATC_016"
    comment_icon = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[2]/div/div[2]/div[2]/div[2]/a[1]/div[1]/div/span[2]/span[1]')
    comment_count = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[2]/div/div[2]/div[2]/div[2]/a[2]/div[1]/div/span[2]/span[2]')
    
    print("----------------------------- ATC_016 -------------------------------")   
    try :
        if comment_icon.is_displayed() and comment_count.is_displayed() :
            print("스토리 크리에이터 첫번째 포스트 댓글 아이콘, 댓글 Count 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '스토리 크리에이터 첫번째 포스트 댓글 아이콘, 댓글 Count 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_016.jpg',region=(0,0,1287,900))


    #TC_017 스토리 크리에이터 메뉴 하단 페이징 버튼 노출 여부 확인
    tc_progress = "ATC_017"
    post_image = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[2]/div/div[2]/div[2]/div[2]/a[1]/div[2]/div')
    
    print("----------------------------- ATC_017 -------------------------------")   
    try :
        if post_image.is_displayed() :
            print("스토리 크리에이터 포스트 이미지 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '스토리 크리에이터 포스트 이미지 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_017.jpg',region=(0,0,1287,900))


    #TC_018 스토리 크리에이터 메뉴 하단 페이징 버튼 노출 여부 확인
    tc_progress = "ATC_018"
    Paging_left = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[2]/div/div[2]/div[4]/div/button[1]/span')
    Paging_right = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[2]/div/div[2]/div[4]/div/button[2]/span')
    print("----------------------------- ATC_018 -------------------------------")   
    try :
        if Paging_left.is_displayed() and Paging_right.is_displayed() :
            print("스토리 크리에이터 하단 좌, 우 페이징 버튼 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '스토리 크리에이터 하단 좌, 우 페이징 버튼 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_018.jpg',region=(0,0,1287,900))

    action = browser.find_element(By.CSS_SELECTOR,'body')

    action.send_keys(Keys.PAGE_DOWN)

    #TC_019 여행·맛집 탭 아이콘 노출 여부 확인
    tc_progress = "ATC_019"
    travel_icon = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[1]/div/a[1]/span[1]')
    
    print("----------------------------- ATC_019 -------------------------------")   
    try :
        if travel_icon.is_displayed() :
            print("여행·맛집 탭 아이콘 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 아이콘 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_019.jpg',region=(0,0,1287,900))


    #TC_020 여행·맛집 탭 네임 노출 여부 확인
    #여행, dot, 맛집 각각 \n 되어 문법 정확성까진 확인이 안되는 문제가 있어 개선이 필요
    tc_progress = "ATC_020"
    
    travel_text = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[1]/div/a[1]/span[2]')
    travel_text_assert = travel_text.text
    print(travel_text_assert)

    print("----------------------------- ATC_020 -------------------------------")   
    try :
        if travel_text.is_displayed() :
            print("여행·맛집 탭 텍스트 정상 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 텍스트 정상 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_020.jpg',region=(0,0,1287,900))
    
    travel_top1_picture = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[1]/a/div[2]/div')
    travel_top1_blog_image = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[1]/div/a/div/img')
    travel_top1_blog_name = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[1]/div/a/span')
    travel_top1_text_blog_name = travel_top1_blog_name.text
    travel_top1_text_title = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[1]/a/div[1]/strong')
    travel_top1_text_title_text = travel_top1_text_title.text
    travel_top1_text_desc = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[1]/a/div[1]/div[1]/p')
    travel_top1_text_desc_text = travel_top1_text_desc.text
    travel_top1_like_icon = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[1]/a/div[1]/div[2]/span[1]/span[1]')
    travel_top1_like_count = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[1]/a/div[1]/div[2]/span[1]/span[2]')
    travel_top1_like_count_num = travel_top1_like_count.text
    travel_top1_reply_icon = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[1]/a/div[1]/div[2]/span[2]/span[1]')
    travel_top1_reply_count = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[1]/a/div[1]/div[2]/span[2]/span[2]')
    travel_top1_reply_count_num = travel_top1_reply_count.text
    travel_top1_date = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[1]/a/div[1]/div[2]/span[3]')
    travel_top1_date_num = travel_top1_date.text

    print("-------------------- 여행·맛집 탭 좌측 상단 포스트 정보 -------------")
    print("여행·맛집 탭 좌측 상단 포스트 블로그 명 => " + travel_top1_text_blog_name)
    print("여행·맛집 탭 좌측 상단 포스트 타이틀 => " + travel_top1_text_title_text)
    print("여행·맛집 탭 좌측 상단 포스트 내용 => " + travel_top1_text_desc_text)
    print("여행·맛집 탭 좌측 상단 포스트 좋아요 카운트 => " + travel_top1_like_count_num)
    print("여행·맛집 탭 좌측 상단 포스트 댓글 카운트 => " + travel_top1_reply_count_num)
    print("여행·맛집 탭 좌측 상단 포스트 작성 일자 => " + travel_top1_date_num)

    #TC_021 여행·맛집 탭 좌측 상단 포스트 사진 노출 여부 확인
    tc_progress = "ATC_021"
    print("----------------------------- ATC_021 -------------------------------")   
    try :
        if travel_top1_picture.is_displayed() :
            print("여행·맛집 탭 좌측 상단 포스트 사진 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 좌측 상단 포스트 사진 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_021.jpg',region=(0,0,1287,900))

    #TC_022 여행·맛집 탭 좌측 상단 포스트 블로거 아이콘 노출 여부 확인
    tc_progress = "ATC_022"
    print("----------------------------- ATC_022 -------------------------------")   
    try :
        if travel_top1_blog_image.is_displayed() :
            print("여행·맛집 탭 좌측 상단 포스트 블로거 아이콘 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 좌측 상단 포스트 블로거 아이콘 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_022.jpg',region=(0,0,1287,900))
    
    #TC_023 여행·맛집 탭 좌측 상단 포스트 블로그 이름 노출 여부 확인
    tc_progress = "ATC_023"
    print("----------------------------- ATC_023 -------------------------------")   
    try :
        if travel_top1_blog_image.is_displayed() :
            print("여행·맛집 탭 좌측 상단 포스트 블로그 이름 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 좌측 상단 포스트 블로그 이름 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_023.jpg',region=(0,0,1287,900))
    
    #TC_024 여행·맛집 탭 좌측 상단 포스트 타이틀 노출 여부 확인
    tc_progress = "ATC_024"
    print("----------------------------- ATC_024 -------------------------------")   
    try :
        if travel_top1_text_title.is_displayed() :
            print("여행·맛집 탭 좌측 상단 포스트 타이틀 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 좌측 상단 포스트 타이틀 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_024.jpg',region=(0,0,1287,900))
    
    #TC_025 여행·맛집 탭 좌측 상단 포스트 내용 노출 여부 확인
    tc_progress = "ATC_025"
    print("----------------------------- ATC_025 -------------------------------")   
    try :
        if travel_top1_text_desc.is_displayed() :
            print("여행·맛집 탭 좌측 상단 포스트 내용 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 좌측 상단 포스트 내용 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_025.jpg',region=(0,0,1287,900))

    #TC_026 여행·맛집 탭 좌측 상단 포스트 좋아요 아이콘 노출 여부 확인
    tc_progress = "ATC_026"
    print("----------------------------- ATC_026 -------------------------------")   
    try :
        if travel_top1_like_icon.is_displayed() :
            print("여행·맛집 탭 좌측 상단 포스트 좋아요 아이콘 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 좌측 상단 포스트 좋아요 아이콘 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_026.jpg',region=(0,0,1287,900))

    #TC_027 여행·맛집 탭 좌측 상단 포스트 좋아요 카운트 노출 여부 확인
    tc_progress = "ATC_027"
    print("----------------------------- ATC_027 -------------------------------")   
    try :
        if travel_top1_like_count.is_displayed() :
            print("여행·맛집 탭 좌측 상단 포스트 좋아요 Count 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 좌측 상단 포스트 좋아요 Count 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_027.jpg',region=(0,0,1287,900))
    
    #TC_028 여행·맛집 탭 좌측 상단 포스트 댓글 아이콘 노출 여부 확인
    tc_progress = "ATC_028"
    print("----------------------------- ATC_028 -------------------------------")   
    try :
        if travel_top1_reply_icon.is_displayed() :
            print("여행·맛집 탭 좌측 상단 포스트 댓글 아이콘 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 좌측 상단 포스트 댓글 아이콘 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_028.jpg',region=(0,0,1287,900))
    
    #TC_029 여행·맛집 탭 좌측 상단 포스트 댓글 카운트 노출 여부 확인
    tc_progress = "ATC_029"
    print("----------------------------- ATC_029 -------------------------------")   
    try :
        if travel_top1_reply_count.is_displayed() :
            print("여행·맛집 탭 좌측 상단 포스트 댓글 카운트 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 좌측 상단 포스트 댓글 카운트 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_029.jpg',region=(0,0,1287,900))
    
    #TC_030 여행·맛집 탭 좌측 상단 포스트 Date 노출 여부 확인
    tc_progress = "ATC_030"
    print("----------------------------- ATC_030 -------------------------------")   
    try :
        if travel_top1_date.is_displayed() :
            print("여행·맛집 탭 좌측 상단 포스트 Date 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 좌측 상단 포스트 Date 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_030.jpg',region=(0,0,1287,900))
    
    travel_top2_picture = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[2]/a/div[2]/div')
    travel_top2_blog_image = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[2]/div/a/div/img')
    travel_top2_blog_name = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[2]/div/a/span')
    travel_top2_text_blog_name = travel_top2_blog_name.text
    travel_top2_text_title = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[2]/a/div[1]/strong')
    travel_top2_text_title_text = travel_top2_text_title.text
    travel_top2_text_desc = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[2]/a/div[1]/div[1]/p')
    travel_top2_text_desc_text = travel_top2_text_desc.text
    travel_top2_like_icon = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[2]/a/div[1]/div[2]/span[1]/span[1]')
    travel_top2_like_count = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[2]/a/div[1]/div[2]/span[1]/span[2]')
    travel_top2_like_count_num = travel_top2_like_count.text
    travel_top2_reply_icon = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[2]/a/div[1]/div[2]/span[2]/span[1]')
    travel_top2_reply_count = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[2]/a/div[1]/div[2]/span[2]/span[2]')
    travel_top2_reply_count_num = travel_top2_reply_count.text
    travel_top2_date = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[2]/a/div[1]/div[2]/span[3]')
    travel_top2_date_num = travel_top2_date.text

    print("-------------------- 여행·맛집 탭 우측 상단 포스트 정보 -------------")
    print("여행·맛집 탭 우측 상단 포스트 블로그 명 => " + travel_top2_text_blog_name)
    print("여행·맛집 탭 우측 상단 포스트 타이틀 => " + travel_top2_text_title_text)
    print("여행·맛집 탭 우측 상단 포스트 내용 => " + travel_top2_text_desc_text)
    print("여행·맛집 탭 우측 상단 포스트 좋아요 카운트 => " + travel_top2_like_count_num)
    print("여행·맛집 탭 우측 상단 포스트 댓글 카운트 => " + travel_top2_reply_count_num)
    print("여행·맛집 탭 우측 상단 포스트 작성 일자 => " + travel_top2_date_num)

    #TC_031 여행·맛집 탭 우측 상단 포스트 사진 노출 여부 확인
    tc_progress = "ATC_031"
    print("----------------------------- ATC_031 -------------------------------")   
    try :
        if travel_top2_picture.is_displayed() :
            print("여행·맛집 탭 우측 상단 포스트 사진 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 우측 상단 포스트 사진 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_031.jpg',region=(0,0,1287,900))

    #TC_032 여행·맛집 탭 우측 상단 포스트 블로거 아이콘 노출 여부 확인
    tc_progress = "ATC_032"
    print("----------------------------- ATC_032 -------------------------------")   
    try :
        if travel_top1_blog_image.is_displayed() :
            print("여행·맛집 탭 우측 상단 포스트 블로거 아이콘 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 우측 상단 포스트 블로거 아이콘 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_032.jpg',region=(0,0,1287,900))
    
    #TC_033 여행·맛집 탭 우측 상단 포스트 블로그 이름 노출 여부 확인
    tc_progress = "ATC_033"
    print("----------------------------- ATC_033 -------------------------------")   
    try :
        if travel_top2_blog_image.is_displayed() :
            print("여행·맛집 탭 우측 상단 포스트 블로그 이름 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 우측 상단 포스트 블로그 이름 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_033.jpg',region=(0,0,1287,900))
    
    #TC_034 여행·맛집 탭 우측 상단 포스트 타이틀 노출 여부 확인
    tc_progress = "ATC_034"
    print("----------------------------- ATC_034 -------------------------------")   
    try :
        if travel_top2_text_title.is_displayed() :
            print("여행·맛집 탭 우측 상단 포스트 타이틀 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 우측 상단 포스트 타이틀 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_034.jpg',region=(0,0,1287,900))  

    #TC_035 여행·맛집 탭 우측 상단 포스트 내용 노출 여부 확인
    tc_progress = "ATC_035"
    print("----------------------------- ATC_035 -------------------------------")   
    try :
        if travel_top2_text_desc.is_displayed() :
            print("여행·맛집 탭 우측 상단 포스트 내용 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 좌측 상단 포스트 내용 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_035.jpg',region=(0,0,1287,900))

    #TC_036 여행·맛집 탭 우측 상단 포스트 좋아요 아이콘 노출 여부 확인
    tc_progress = "ATC_036"
    print("----------------------------- ATC_036 -------------------------------")   
    try :
        if travel_top2_like_icon.is_displayed() :
            print("여행·맛집 탭 우측 상단 포스트 좋아요 아이콘 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 우측 상단 포스트 좋아요 아이콘 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_036.jpg',region=(0,0,1287,900))

    #TC_037 여행·맛집 탭 우측 상단 포스트 좋아요 카운트 노출 여부 확인
    tc_progress = "ATC_037"
    print("----------------------------- ATC_037 -------------------------------")   
    try :
        if travel_top2_like_count.is_displayed() :
            print("여행·맛집 탭 우측 상단 포스트 좋아요 Count 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 우측 상단 포스트 좋아요 Count 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_037.jpg',region=(0,0,1287,900))
    
    #TC_038 여행·맛집 탭 우측 상단 포스트 댓글 아이콘 노출 여부 확인
    tc_progress = "ATC_038"
    print("----------------------------- ATC_038 -------------------------------")   
    try :
        if travel_top2_reply_icon.is_displayed() :
            print("여행·맛집 탭 우측 상단 포스트 댓글 아이콘 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 우측 상단 포스트 댓글 아이콘 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_038.jpg',region=(0,0,1287,900))
    
    #TC_039 여행·맛집 탭 우측 상단 포스트 댓글 카운트 노출 여부 확인
    tc_progress = "ATC_039"
    print("----------------------------- ATC_039 -------------------------------")   
    try :
        if travel_top2_reply_count.is_displayed() :
            print("여행·맛집 탭 우측 상단 포스트 댓글 카운트 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 우측 상단 포스트 댓글 카운트 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_039.jpg',region=(0,0,1287,900))
    
    #TC_040 여행·맛집 탭 우측 상단 포스트 Date 노출 여부 확인
    tc_progress = "ATC_040"
    print("----------------------------- ATC_040 -------------------------------")   
    try :
        if travel_top2_date.is_displayed() :
            print("여행·맛집 탭 우측 상단 포스트 Date 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 우측 상단 포스트 Date 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_040.jpg',region=(0,0,1287,900))

    travel_top3_picture = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[3]/a/div[2]/div')
    travel_top3_blog_image = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[3]/div/a/div/img')
    travel_top3_blog_name = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[3]/div/a/span')
    travel_top3_text_blog_name = travel_top3_blog_name.text
    travel_top3_text_title = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[3]/a/div[1]/strong')
    travel_top3_text_title_text = travel_top3_text_title.text
    travel_top3_text_desc = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[3]/a/div[1]/div[1]/p')
    travel_top3_text_desc_text = travel_top3_text_desc.text
    travel_top3_like_icon = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[3]/a/div[1]/div[2]/span[1]/span[1]')
    travel_top3_like_count = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[3]/a/div[1]/div[2]/span[1]/span[2]')
    travel_top3_like_count_num = travel_top3_like_count.text
    travel_top3_reply_icon = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[3]/a/div[1]/div[2]/span[2]/span[1]')
    travel_top3_reply_count = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[3]/a/div[1]/div[2]/span[2]/span[2]')
    travel_top3_reply_count_num = travel_top3_reply_count.text
    travel_top3_date = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[3]/a/div[1]/div[2]/span[3]')
    travel_top3_date_num = travel_top3_date.text

    print("-------------------- 여행·맛집 탭 하단 첫번째 포스트 정보 -------------")
    print("여행·맛집 탭 하단 첫번째 포스트 블로그 명 => " + travel_top3_text_blog_name)
    print("여행·맛집 탭 하단 첫번째 포스트 타이틀 => " + travel_top3_text_title_text)
    print("여행·맛집 탭 하단 첫번째 포스트 내용 => " + travel_top3_text_desc_text)
    print("여행·맛집 탭 하단 첫번째 포스트 좋아요 카운트 => " + travel_top3_like_count_num)
    print("여행·맛집 탭 하단 첫번째 상단 포스트 댓글 카운트 => " + travel_top3_reply_count_num)
    print("여행·맛집 탭 하단 첫번째 상단 포스트 작성 일자 => " + travel_top3_date_num)

    #TC_041 여행·맛집 탭 하단 첫번째 포스트 사진 노출 여부 확인
    tc_progress = "ATC_041"
    print("----------------------------- ATC_041 -------------------------------")   
    try :
        if travel_top3_picture.is_displayed() :
            print("여행·맛집 탭 하단 첫번째 포스트 사진 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 첫번째 포스트 사진 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_041.jpg',region=(0,0,1287,900))

    #TC_042 여행·맛집 탭 하단 첫번째 포스트 블로거 아이콘 노출 여부 확인
    tc_progress = "ATC_042"
    print("----------------------------- ATC_042 -------------------------------")   
    try :
        if travel_top3_blog_image.is_displayed() :
            print("여행·맛집 탭 하단 첫번째 포스트 블로거 아이콘 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 첫번째 포스트 블로거 아이콘 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_042.jpg',region=(0,0,1287,900))
    
    #TC_043 여행·맛집 탭 하단 첫번째 포스트 블로그 이름 노출 여부 확인
    tc_progress = "ATC_043"
    print("----------------------------- ATC_043 -------------------------------")   
    try :
        if travel_top3_blog_image.is_displayed() :
            print("여행·맛집 탭 하단 첫번째 포스트 블로그 이름 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 첫번째 포스트 블로그 이름 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_043.jpg',region=(0,0,1287,900))
    
    #TC_044 여행·맛집 탭 하단 첫번째 포스트 타이틀 노출 여부 확인
    tc_progress = "ATC_044"
    print("----------------------------- ATC_044 -------------------------------")   
    try :
        if travel_top3_text_title.is_displayed() :
            print("여행·맛집 탭 하단 첫번째 포스트 타이틀 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 첫번째 포스트 타이틀 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_044.jpg',region=(0,0,1287,900))
    
    #TC_045 여행·맛집 탭 하단 첫번째 포스트 내용 노출 여부 확인
    tc_progress = "ATC_045"
    print("----------------------------- ATC_045 -------------------------------")   
    try :
        if travel_top3_text_desc.is_displayed() :
            print("여행·맛집 탭 하단 첫번째 포스트 내용 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 첫번째 포스트 내용 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_045.jpg',region=(0,0,1287,900))

    #TC_046 여행·맛집 탭 하단 첫번째 포스트 좋아요 아이콘 노출 여부 확인
    tc_prog5ress = "ATC_046"
    print("----------------------------- ATC_046 -------------------------------")   
    try :
        if travel_top3_like_icon.is_displayed() :
            print("여행·맛집 탭 하단 첫번째 포스트 좋아요 아이콘 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 첫번째 포스트 좋아요 아이콘 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_046.jpg',region=(0,0,1287,900))

    #TC_047 여행·맛집 탭 하단 첫번째 포스트 좋아요 카운트 노출 여부 확인
    tc_progress = "ATC_047"
    print("----------------------------- ATC_047 -------------------------------")   
    try :
        if travel_top3_like_count.is_displayed() :
            print("여행·맛집 탭 하단 첫번째 포스트 좋아요 Count 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 첫번째 포스트 좋아요 Count 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_047.jpg',region=(0,0,1287,900))
    
    #TC_048 여행·맛집 탭 하단 첫번째 포스트 댓글 아이콘 노출 여부 확인
    tc_progress = "ATC_048"
    print("----------------------------- ATC_048 -------------------------------")   
    try :
        if travel_top3_reply_icon.is_displayed() :
            print("여행·맛집 탭 하단 첫번째 포스트 댓글 아이콘 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 첫번째 포스트 댓글 아이콘 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_048.jpg',region=(0,0,1287,900))
    
    #TC_049 여행·맛집 탭 하단 첫번째 포스트 댓글 카운트 노출 여부 확인
    tc_progress = "ATC_049"
    print("----------------------------- ATC_049 -------------------------------")   
    try :
        if travel_top3_reply_count.is_displayed() :
            print("여행·맛집 탭 하단 첫번째 포스트 댓글 카운트 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 첫번째 포스트 댓글 카운트 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_049.jpg',region=(0,0,1287,900))
    
    #TC_050 여행·맛집 탭 하단 첫번째 포스트 Date 노출 여부 확인
    tc_progress = "ATC_050"
    print("----------------------------- ATC_050 -------------------------------")   
    try :
        if travel_top3_date.is_displayed() :
            print("여행·맛집 탭 하단 첫번째 포스트 Date 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 첫번째 포스트 Date 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_050.jpg',region=(0,0,1287,900))

    travel_top4_picture = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[4]/a/div[2]/div')
    travel_top4_blog_image = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[4]/div/a/div/img')
    travel_top4_blog_name = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[4]/div/a/span')
    travel_top4_text_blog_name = travel_top4_blog_name.text
    travel_top4_text_title = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[4]/a/div[1]/strong')
    travel_top4_text_title_text = travel_top4_text_title.text
    travel_top4_text_desc = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[4]/a/div[1]/div[1]/p')
    travel_top4_text_desc_text = travel_top4_text_desc.text
    travel_top4_like_icon = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[4]/a/div[1]/div[2]/span[1]/span[1]')
    travel_top4_like_count = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[4]/a/div[1]/div[2]/span[1]/span[2]')
    travel_top4_like_count_num = travel_top4_like_count.text
    travel_top4_reply_icon = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[4]/a/div[1]/div[2]/span[2]/span[1]')
    travel_top4_reply_count = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[4]/a/div[1]/div[2]/span[2]/span[2]')
    travel_top4_reply_count_num = travel_top4_reply_count.text
    travel_top4_date = browser.find_element(By.XPATH,'//*[@id="mArticle"]/div/div[1]/div[3]/div[2]/div[4]/a/div[1]/div[2]/span[3]')
    travel_top4_date_num = travel_top4_date.text

    print("-------------------- 여행·맛집 탭 하단 두번째 포스트 정보 -------------")
    print("여행·맛집 탭 하단 두번째 포스트 블로그 명 => " + travel_top4_text_blog_name)
    print("여행·맛집 탭 하단 두번째 포스트 타이틀 => " + travel_top4_text_title_text)
    print("여행·맛집 탭 하단 두번째 포스트 내용 => " + travel_top4_text_desc_text)
    print("여행·맛집 탭 하단 두번째 포스트 좋아요 카운트 => " + travel_top4_like_count_num)
    print("여행·맛집 탭 하단 두번째 상단 포스트 댓글 카운트 => " + travel_top4_reply_count_num)
    print("여행·맛집 탭 하단 두번째 상단 포스트 작성 일자 => " + travel_top4_date_num)

    #TC_051 여행·맛집 탭 하단 두번째 포스트 사진 노출 여부 확인
    tc_progress = "ATC_051"
    print("----------------------------- ATC_051 -------------------------------")   
    try :
        if travel_top4_picture.is_displayed() :
            print("여행·맛집 탭 하단 두번째 포스트 사진 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 두번째 포스트 사진 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_051.jpg',region=(0,0,1287,900))

    #TC_052 여행·맛집 탭 하단 첫번째 포스트 블로거 아이콘 노출 여부 확인
    tc_progress = "ATC_052"
    print("----------------------------- ATC_052 -------------------------------")   
    try :
        if travel_top4_blog_image.is_displayed() :
            print("여행·맛집 탭 하단 두번째 포스트 블로거 아이콘 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 두번째 포스트 블로거 아이콘 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_052.jpg',region=(0,0,1287,900))
    
    #TC_053 여행·맛집 탭 하단 두번째 포스트 블로그 이름 노출 여부 확인
    tc_progress = "ATC_053"
    print("----------------------------- ATC_053 -------------------------------")   
    try :
        if travel_top4_blog_image.is_displayed() :
            print("여행·맛집 탭 하단 두번째 포스트 블로그 이름 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 두번째 포스트 블로그 이름 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_053.jpg',region=(0,0,1287,900))
    
    #TC_054 여행·맛집 탭 하단 두번째 포스트 타이틀 노출 여부 확인
    tc_progress = "ATC_054"
    print("----------------------------- ATC_054 -------------------------------")   
    try :
        if travel_top4_text_title.is_displayed() :
            print("여행·맛집 탭 하단 두번째 포스트 타이틀 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 두번째 포스트 타이틀 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_054.jpg',region=(0,0,1287,900))
    
    #TC_055 여행·맛집 탭 하단 두번째 포스트 내용 노출 여부 확인
    tc_progress = "ATC_055"
    print("----------------------------- ATC_055 -------------------------------")   
    try :
        if travel_top4_text_desc.is_displayed() :
            print("여행·맛집 탭 하단 두번째 포스트 내용 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 두번째 포스트 내용 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_055.jpg',region=(0,0,1287,900))

    #TC_056 여행·맛집 탭 하단 두번째 포스트 좋아요 아이콘 노출 여부 확인
    tc_progress = "ATC_056"
    print("----------------------------- ATC_056 -------------------------------")   
    try :
        if travel_top4_like_icon.is_displayed() :
            print("여행·맛집 탭 하단 두번째 포스트 좋아요 아이콘 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 두번째 포스트 좋아요 아이콘 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_056.jpg',region=(0,0,1287,900))

    #TC_057 여행·맛집 탭 하단 두번째 포스트 좋아요 카운트 노출 여부 확인
    tc_progress = "ATC_057"
    print("----------------------------- ATC_056 -------------------------------")   
    try :
        if travel_top4_like_count.is_displayed() :
            print("여행·맛집 탭 하단 두번째 포스트 좋아요 Count 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 두번째 포스트 좋아요 Count 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_057.jpg',region=(0,0,1287,900))
    
    #TC_058 여행·맛집 탭 하단 두번째 포스트 댓글 아이콘 노출 여부 확인
    tc_progress = "ATC_058"
    print("----------------------------- ATC_058 -------------------------------")   
    try :
        if travel_top4_reply_icon.is_displayed() :
            print("여행·맛집 탭 하단 두번째 포스트 댓글 아이콘 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 두번째 포스트 댓글 아이콘 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_058.jpg',region=(0,0,1287,900))
    
    #TC_059 여행·맛집 탭 하단 두번째 포스트 댓글 카운트 노출 여부 확인
    tc_progress = "ATC_059"
    print("----------------------------- ATC_059 -------------------------------")   
    try :
        if travel_top4_reply_count.is_displayed() :
            print("여행·맛집 탭 하단 두번째 포스트 댓글 카운트 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 두번째 포스트 댓글 카운트 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_059.jpg',region=(0,0,1287,900))
    
    #TC_060 여행·맛집 탭 하단 두번째 포스트 Date 노출 여부 확인
    tc_progress = "ATC_060"
    print("----------------------------- ATC_060 -------------------------------")   
    try :
        if travel_top4_date.is_displayed() :
            print("여행·맛집 탭 하단 두번째 포스트 Date 노출 성공!")
            result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '여행·맛집 탭 하단 두번째 포스트 Date 노출 실패\n'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
        pyautogui.screenshot(f'./{now}_Fail_shot_TC_060.jpg',region=(0,0,1287,900))

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
