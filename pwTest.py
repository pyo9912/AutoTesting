import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.docx.co.kr"

# Chromedriver 연결
browser = webdriver.Chrome('chromedriver')
browser.get(url)

time.sleep(1)

# 최초 관리자 계정으로 로그인
# ID 입력
try:
    id_name = 'login_id'
    id_field = browser.find_element(By.ID, id_name)
    id_field.send_keys("admin5")

    time.sleep(1)

    # PW 입력
    base_pw = "1111"
    pw_name = 'login_pw'
    pw_field = browser.find_element(By.ID, pw_name)
    pw_field.send_keys(base_pw)

    time.sleep(1)

    # 로그인 버튼 클릭
    login_button_name = 'btn_submit btn'
    login_button = browser.find_element(By.XPATH, '//*[@id="login_frm"]/input[3]')
    login_button.click()

    time.sleep(1)
except Exception as error:
    print("로그인 기능 오류")

# 비밀번호 보안 규칙 확인
cur_pw = base_pw
pw_list = ["qwert!@#$%", "qwert12345", "qwe!@#12", "1111"]

for pw in pw_list:
    # 정보수정 페이지 진입
    profile_button_name = 'prf_btn'
    profile_button = browser.find_element(By.CLASS_NAME, profile_button_name)
    profile_button.click()

    time.sleep(1)

    register_button = browser.find_element(By.XPATH, '//*[@id="ol_after_private"]/li[1]/a')
    register_button.click()

    time.sleep(1)

    # 기존 비밀번호 입력
    confirm_pw = 'mb_confirm_pw'
    confirm_pw_field = browser.find_element(By.ID, confirm_pw)
    confirm_pw_field.send_keys(cur_pw)

    time.sleep(1)

    # 확인 버튼 클릭
    confirm_button = browser.find_element(By.XPATH, '//*[@id="btn_submit"]')
    confirm_button.click()

    time.sleep(1)
    try:
        # 새 비밀번호 입력
        register_pw = "reg_mb_password"
        register_pw_field = browser.find_element(By.ID, register_pw)
        register_pw_field.send_keys(pw)

        time.sleep(1)

        # 비밀번호 확인

        re_register_pw = "reg_mb_password_re"
        re_register_pw_field = browser.find_element(By.ID, re_register_pw)
        re_register_pw_field.send_keys(pw)

        time.sleep(1)

        # 정보수정 버튼 클릭
        change_button = browser.find_element(By.XPATH, '//*[@id="btn_submit"]')
        change_button.click()

        time.sleep(1)
    
    except Exception as error:
        print("비밀번호 점검기능 동작")

    # 로그아웃
    profile_button_name = 'prf_btn'
    profile_button = browser.find_element(By.CLASS_NAME, profile_button_name)
    profile_button.click()

    time.sleep(1)

    logout_button = browser.find_element(By.XPATH, '//*[@id="ol_after_private"]/li[2]/a')
    logout_button.click()

    # 로그인 확인
    # ID 입력
    try:        
        id_name = 'login_id'
        id_field = browser.find_element(By.ID, id_name)
        id_field.send_keys("admin5")

        time.sleep(1)

        # PW 입력
        cur_pw = pw
        pw_name = 'login_pw'
        pw_field = browser.find_element(By.ID, pw_name)
        pw_field.send_keys(cur_pw)

        time.sleep(1)

        # 로그인 버튼 클릭
        login_button_name = 'btn_submit btn'
        login_button = browser.find_element(By.XPATH, '//*[@id="login_frm"]/input[3]')
        login_button.click()

        time.sleep(1)
    except Exception as error:
        print("비밀번호 변경 기능 오류")


