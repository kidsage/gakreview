import os
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# test
base_dir = Path(__file__).resolve().parent
driver_path = os.path.join(base_dir, "chromedriver")

service = Service(executable_path=driver_path)

options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_argument("disable-gpu")

driver = webdriver.Chrome(service=service, options=options)

# 네이버 지도 열기
driver.get("https://map.naver.com")

searchFrame = "searchIframe"
entryFrame = "entryIframe"

try:
    search_box = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.input_search"))
    )
    search_box.send_keys("주나수산")
    search_box.send_keys(Keys.ENTER)

except Exception as e:
    print(f"검색창을 찾을 수 없습니다: {e}")
    driver.quit()

try:
    driver.switch_to.default_content()
    WebDriverWait(driver, 1.5).until(
        EC.presence_of_element_located((By.ID, searchFrame))
    )
    driver.switch_to.frame(searchFrame)

    first_result = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "#_pcmap_list_scroll_container > ul > li:nth-child(1) > div.qbGlu > div.ouxiq > a > div",
            )
        )
    )
    # print(first_result)
    time.sleep(1)
    first_result.click()

    time.sleep(1)
    driver.switch_to.default_content()

    driver.switch_to.frame(entryFrame)
    menu = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "#app-root > div > div > div > div.place_fixed_maintab > div > div > div > div > a:nth-child(3) > span",
            )
        )
    )
    menu.click()
    time.sleep(1)

    # 메뉴 항목 추출
    menu_items = menu.find_elements(
        By.CSS_SELECTOR,
        "#app-root > div > div > div > div:nth-child(6) > div:nth-child(2) > div.place_section.no_margin > div.place_section_content > ul",
    )
    print(menu_items)
    menu_list = []

    for item in menu_items:
        try:
            # 메뉴 이름 추출
            menu_name = item.find_element(By.CSS_SELECTOR, "span.lPzHi").text
            # 메뉴 가격 추출
            menu_price = item.find_element(By.CSS_SELECTOR, "div.GXS1X em").text
            menu_list.append((menu_name, menu_price))
        except Exception as e:
            print(f"메뉴 정보 추출 중 오류 발생: {e}")

    # 메뉴 정보 출력
    for menu in menu_list:
        print(f"메뉴: {menu[0]}, 가격: {menu[1]}")

    driver.switch_to.default_content()
    time.sleep(3)

    print("done")
except Exception as e:
    print(e, "failed")
    # pass

# 드라이버 종료
driver.quit()


# class NaverMapCrawler:
#     def __init__(self, driver_path):
#         """
#         초기화 메서드: 웹 드라이버 설정
#         """
#         self.driver = webdriver.Chrome(executable_path=driver_path)
#         self.driver.implicitly_wait(10)  # 암시적 대기 시간 설정

#     def search_place(self, keyword):
#         """
#         네이버 맵에서 키워드로 검색
#         """
#         self.driver.get("https://map.naver.com/")
#         time.sleep(2)  # 페이지 로딩 대기

#         # 검색창 찾기
#         search_box = self.driver.find_element(By.CSS_SELECTOR, "input#search-input")
#         search_box.send_keys(keyword)  # 키워드 입력
#         search_box.send_keys(Keys.RETURN)  # 엔터 키 입력
#         time.sleep(2)  # 검색 결과 대기

#     def select_first_store(self):
#         """
#         검색 결과 중 첫 번째 가게 선택
#         """
#         # 첫 번째 검색 결과 클릭
#         first_store = self.driver.find_element(By.CSS_SELECTOR, "li.lsnx")
#         first_store.click()
#         time.sleep(2)  # 가게 페이지 로딩 대기

#     def crawl_menu(self):
#         """
#         가게의 메뉴 정보 크롤링
#         """
#         # 메뉴 탭 클릭 (네이버 맵의 메뉴 탭 선택자)
#         menu_tab = self.driver.find_element(By.CSS_SELECTOR, "div._tab_menu a[data-tab='MENU']")
#         menu_tab.click()
#         time.sleep(2)  # 메뉴 로딩 대기

#         # 메뉴 목록 크롤링
#         menu_items = self.driver.find_elements(By.CSS_SELECTOR, "div._1ZDCG ul li")
#         menu_list = []

#         for item in menu_items:
#             try:
#                 menu_name = item.find_element(By.CSS_SELECTOR, "span.lPzHi").text
#                 menu_price = item.find_element(By.CSS_SELECTOR, "div._3yfZ1").text
#                 menu_list.append((menu_name, menu_price))
#             except:
#                 continue

#         return menu_list

#     def close(self):
#         """
#         브라우저 종료
#         """
#         self.driver.quit()
