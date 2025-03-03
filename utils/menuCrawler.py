import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver_path = "./chromedriver"

service = Service(executable_path=driver_path)

options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_argument("disable-gpu")

driver = webdriver.Chrome(service=service, options=options)

# 네이버 지도 열기
driver.get("https://map.naver.com")

try:
    # iframe으로 전환
    # iframe = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "iframe#searchIframe"))
    # )
    # driver.switch_to.frame(iframe)
    # print("검색창 찾기 시도 중...")

    # iframe 내부에서 검색창 찾기
    search_box = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.input_search"))
    )
    search_box.send_keys("워낭소리")
    search_box.send_keys(Keys.ENTER)

    # 다시 기본 콘텐츠로 전환
    # driver.switch_to.default_content()
except Exception as e:
    print(f"검색창을 찾을 수 없습니다: {e}")
    driver.quit()

# 페이지 로딩 대기
# time.sleep(3)

# 첫 번째 검색 결과 클릭
# try:
#     search_results = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "div.qbGlu"))
#     )
#     search_results.click()
# except Exception as e:
#     print(f"검색 결과는 있는데 헤멤: {e}")
#     driver.quit()

# 페이지 로딩 대기
# time.sleep(3)

# 드라이버 종료
driver.quit()
