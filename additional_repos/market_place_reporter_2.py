###
"""
상권 정보 웹사이트 크롤링 로직 (https://sg.sbiz.or.kr/godo/analysis.sg)
"""
import time
import traceback

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome, ChromeOptions
import pandas as pd


###

def main():
    get_site_and_login(787)


def convert_txt_file():
    lines = None
    with open("../backup_dummy/search_analysis_report.txt", "r", encoding="utf-8") as file:
        lines = file.read().split("\n")[:-1]
    assert isinstance(lines, list)
    for line in lines:
        temp_list = list()
        elements = line.split('|')
        for e in elements:
            if "'" in e:
                data = e.replace("'", "").split(",")[1].strip()
                temp_list.append(data)
            else:
                if "만원" in e:
                    e = e.replace("원", "")
                    temp_word = korean_to_number(e)
                else:
                    temp_word = e.replace("개", "").replace(",", "").replace("명", "").replace("만원", "").strip()
                temp_list.append(temp_word)
        with open("../backup_dummy/result_report.txt", "a", encoding="utf-8") as file:
            new_line = "|".join(temp_list)
            file.write(f"{new_line}\n")

def korean_to_number(korean_str):
    num_map = {
        '일': 1, '이': 2, '삼': 3, '사': 4, '오': 5,
        '육': 6, '칠': 7, '팔': 8, '구': 9, '십': 10,
        '백': 100, '천': 1000, '만': 10000, '억': 100000000
    }

    number = 0
    partial_sum = 0

    for word in korean_str.split():
        if word in num_map:
            if num_map[word] >= 10000:
                number += partial_sum * num_map[word]
                partial_sum = 0
            else:
                partial_sum += num_map[word]

    number += partial_sum

    return str(number)


def get_site_and_login(start_idx):
    # 화면 작으면 분석 안보임, 크기 키우기
    opts = ChromeOptions()
    opts.add_argument("--window-size=1200,800")

    # 창 띄우기
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(20)
    driver.get("https://sg.sbiz.or.kr/godo/index.sg")

    # 일주일 안보기
    driver.find_element(By.CSS_SELECTOR, "#help_guide > div > div.foot > div:nth-child(2) > label").click()
    driver.find_element(By.CSS_SELECTOR, "#help_guide > div > div.foot > a").click()

    # 로그인 버튼화면 이동
    page_login_btn = driver.find_element(By.CSS_SELECTOR,
                                         "#menu > div.lay.scrollbarView > div > div.head > div > ul > li > a > span")
    page_login_btn.click()
    time.sleep(1)

    # 로그인 정보 입력
    login_id = "mun0392"
    login_pw = "qkrrhkdgus123!"
    edit_line_id = driver.find_element(By.ID, "id")
    edit_line_pw = driver.find_element(By.ID, "pass")
    login_btn = driver.find_element(By.CSS_SELECTOR, "body > div > div.l_content > form > div > input")

    edit_line_id.send_keys(login_id)
    edit_line_pw.send_keys(login_pw)
    login_btn.click()

    container = driver.find_element(By.ID, "container")
    # 첫번째 팝업 끄기
    try:
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container'] and contains(.,'한달')]"))).click()
        x_btn = driver.find_element(By.CLASS_NAME, "option-wrap")
        x_btn.click()
    except:
        traceback.print_exc()
        while True:
            pass
    # 상세분석 버튼 클릭
    detail_btn = container.find_element(By.CSS_SELECTOR, "#toLink > a > h4")
    detail_btn.click()
    time.sleep(3)

    # 좌상단 음식 버튼 클릭
    container = driver.find_element(By.ID, "container")
    food_btn = container.find_element(By.CSS_SELECTOR, "#upjong > ul > li:nth-child(2)")
    food_btn.click()
    time.sleep(0.5)

    # 빵/도넛 클릭
    container = driver.find_element(By.ID, "container")
    bread_btn = container.find_element(By.CSS_SELECTOR,
                                       "#container > div:nth-child(17) > div > div.midd > div.midd > div.searchview.scrollbarView > div > ul > li:nth-child(9) > div > ul > li:nth-child(3) > label > span")
    bread_btn.click()
    time.sleep(0.5)

    # 확인 클릭
    container = driver.find_element(By.ID, "container")
    confirm_btn = container.find_element(By.CSS_SELECTOR, "#checkTypeConfirm > span")
    confirm_btn.click()
    time.sleep(3)

    read_file = pd.read_excel("_dummy_src/final_paris_adding_data.xlsx", engine="openpyxl", index_col=0)
    df = pd.DataFrame(read_file)
    for idx, row in df.iterrows():
        if idx < start_idx:
            continue

        searching_address = row["PARIS_ADDRESS"]
        # 검색창 클릭
        container = driver.find_element(By.ID, "container")
        search_box = container.find_element(By.CSS_SELECTOR, "#searchAddress")
        search_box.clear()
        search_box.send_keys(f"{searching_address}")
        search_box.send_keys(Keys.ENTER)
        time.sleep(1.5)

        # 검색 결과 최상단 선택
        searched_label = container.find_element(By.CSS_SELECTOR, "#adrsList > li > label > span")
        searched_label.click()

        # 상권 분석 버튼 클릭
        analysis_sector_btn = container.find_element(By.CSS_SELECTOR,
                                                     "#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(2) > div > ul > li.child > label")
        analysis_sector_btn.click()

        radius_sector_btn = container.find_element(By.CSS_SELECTOR,
                                                   "#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(2) > div > ul > li.child > div > ul > li:nth-child(2) > label")
        radius_sector_btn.click()

        # 500m 클릭
        distance_btn = container.find_element(By.CSS_SELECTOR,
                                              "#auto_circle > div > div.midd > ul > li:nth-child(5) > label")
        distance_btn.click()
        time.sleep(0.5)

        confirm_btn = container.find_element(By.CSS_SELECTOR, "#auto_circle > div > div.foot > a:nth-child(2) > span")
        confirm_btn.click()
        time.sleep(0.5)

        # 분석 버튼 클릭
        start_analysis = container.find_element(By.CSS_SELECTOR,
                                                "#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(3) > img")
        start_analysis.click()
        time.sleep(10)
        container = driver.find_element(By.ID, "page1")
        rival_count_near_500 = container.find_element(By.CSS_SELECTOR,
                                                      "#page1 > div.report-pop-layer > div.analysis-section.analysis-01 > div.analysis-content > div:nth-child(1) > div > div > span").text
        rival_count_near_1000 = container.find_element(By.CSS_SELECTOR,
                                                       "#page1 > div.report-pop-layer > div.analysis-section.analysis-01 > div.analysis-content > div:nth-child(3) > div > div > span").text
        monthly_shop_revenue = container.find_element(By.CSS_SELECTOR, "#salesSmryInfoCurSaleAmt").text
        monthly_shop_sale_transaction_count = container.find_element(By.CSS_SELECTOR, "#salesSmryInfoCurSaleCnt").text
        daily_floating_population = container.find_element(By.CSS_SELECTOR, "#flowPopSmryInfoFlowPop").text
        living_worker_population = container.find_element(By.CSS_SELECTOR, "#empAbodePopSmryInfoEmpPop").text
        living_worker_avg_revenue = container.find_element(By.CSS_SELECTOR, "#empAbodePopSmryInfoEmpAvgCo").text
        living_population = container.find_element(By.CSS_SELECTOR, "#empAbodePopSmryInfoAbodePop").text
        living_population_avg_revenue = container.find_element(By.CSS_SELECTOR, "#empAbodePopSmryInfoAbodeAvgCo").text

        print('rival_count_near_500: ', rival_count_near_500)
        print('rival_count_near_1000: ', rival_count_near_1000)
        print('monthly_shop_revenue: ', monthly_shop_revenue)
        print('monthly_shop_sale_transaction_count: ', monthly_shop_sale_transaction_count)
        print('daily_floating_population: ', daily_floating_population)
        print('living_worker_population: ', living_worker_population)
        print('living_worker_avg_revenue: ', living_worker_avg_revenue)
        print('living_population: ', living_population)
        print('living_population_avg_revenue: ', living_population_avg_revenue)

        driver.find_element(By.CSS_SELECTOR, "#bind > div.lay > a").click()

        temp_list = list()
        for item in row.items():
            temp_list.append(f"{item}")
        temp_list.append(rival_count_near_500)
        temp_list.append(rival_count_near_1000)
        temp_list.append(monthly_shop_revenue)
        temp_list.append(monthly_shop_sale_transaction_count)
        temp_list.append(daily_floating_population)
        temp_list.append(living_worker_population)
        temp_list.append(living_worker_avg_revenue)
        temp_list.append(living_population)
        temp_list.append(living_population_avg_revenue)
        line = "|".join(temp_list)
        with open("../backup_dummy/search_analysis_report.txt", "a", encoding="utf-8") as file:
            file.write(f"{line}\n")

    while True:
        pass


if __name__ == '__main__':
    main()
