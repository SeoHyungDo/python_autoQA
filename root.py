# 변수명 camelcase 기법

# class root:
    
 # def url(By, browser) :
 #  browser.get("https://www.tistory.com/")

# tistory 우측 상단 시작하기 버튼 클릭
# def start_button(By, browser) :
# browser.findElement(By.xpath('//*[@id="kakaoHead"]/div/div[3]/div/a')).click()

# 카카오로 로그인 버튼
# def login_button(By, browser) :
# browser.findElement(By.xpath('//*[@id="cMain"]/div/div/div/a[2]/span[2]')).click()

# ID / PW 화면 ID 버튼 클릭
# def loginId(By, browser) :
#  browser.findElement(By.xpath('//*[@id="loginId--1"]')).click()

# ID / PW 화면 ID 입력
# def inputId(By, browser) :
# browser.findElement(By.id("loginId--1")).sendKeys('id') # ID 전송, git에선 가림

# ID / PW 화면 PW 입력
# def inputPw(By, browser) :
  #browser.findElement(By.id("password--2")).sendKeys('password') # ID 전송, git에선 가림

# 로그인 버튼 클릭
# def clickLogin(By, browser) :
#  browser.findElement(By.xpath('//*[@id="mainContent"]/div/div/form/div[4]/button[1]')).click() # 로그인 버튼 클릭

# 우측 상단 글로벌 버튼
# def globalbuttonclick(By, browser) :
#  browser.findElement(By.xpath('//*[@id="kakaoHead"]/div/div[3]/div/a[2]/img')).click() # 글로벌 버튼 클릭

# 우측 상단 글로벌 버튼 -> 이름
# def globalbuttonname (By, browser) :
# browser.findElement(By.xpath('//*[@id="kakaoHead"]/div/div[3]/div/div/div/div[1]/div/a')) # 글로벌 버튼 클릭

# By 안에 함수가 있어 By랑 Click을 분리할 수 없음 -> TypeError: Cannot read properties of undefined (reading 'findElement'), 
# TypeError: kakaoLogin(...).click is not a function등 타입 에러 유발

#BannerGroup = browser.find_element(By.XPATH,'//*[@id="mFeature"]/div/div/div[2]/div[2]/div/div')
#BannerText = BannerGroup.text
#print("현재 배너 정보는" + BannerText)