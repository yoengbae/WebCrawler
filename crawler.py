from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Crawl:
    def __init__(self):
        super().__init__()
        option = Options()
        option.headless = True
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=option)
        self.driver.set_window_size(1600, 1024)
        self.driver.get('http://my.knu.ac.kr/stpo/stpo/cour/lectReqCntEnq/list.action')
        self.driver.implicitly_wait(3)
        self.maxNumber = 'default'
        self.nowNumber = 'default'
        self.nm = 'default'

    def crawling(self, str):
        self.driver.find_element_by_name('search_subj_class_cde').clear()
        self.driver.find_element_by_name('search_subj_class_cde').send_keys(str)
        self.driver.find_element_by_tag_name('button').click()
        courses = self.driver.find_elements_by_css_selector('#contents > div > div > table.resultT.form > tbody:nth-child(2) > tr')
        for course in courses:
            if course.text != '조회된 자료가 없습니다.':
                self.checknumber(course)
                break
                # 결과 2개이상 띄우려면 수정 필요
            else:
                print('에러')
                break

    def checknumber(self, course):
        self.maxNumber = course.find_element_by_class_name('lect_quota').text  # 최대 수강인원
        self.nowNumber = course.find_element_by_class_name('lect_req_cnt').text  # 현재 수강인원
        self.nm = course.find_element_by_class_name('subj_nm').text
        #print(self.maxNumber+self.nowNumber+self.nm)
        if int(self.maxNumber) - int(self.nowNumber) > 0:
            print("알람")
            # gui 처리 추가


# https://selenium.dev/documentation/en/webdriver/browser_manipulation/
# selenium DOC
