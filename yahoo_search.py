from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
"""
global driver

def setup():
    global driver
    #chromedriverの設定
    options = Options()
    options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    #options.binary_location = "C:\Users\yoshinobu_konishiike\.vscode\extensions\yzane.markdown-pdf-1.4.2\node_modules\puppeteer\.local-chromium\win64-686378\chrome-win"
    options.add_argument('--headless')
    # 1.操作するブラウザを開く
    #driver = webdriver.Chrome(executable_path=r'C:\Users\yoshinobu_konishiike\Miniconda3\Lib\site-packages\selenium\chromedriver\chromedriver.exe')
    driver = webdriver.Chrome(options = options,executable_path=r'C:\Users\yoshinobu_konishiike\Miniconda3\Lib\site-packages\selenium\chromedriver\chromedriver.exe')

def search(title):
    # 2.操作するページを開く
    driver.get('https://shopping.yahoo.co.jp/')
    #検索したいキーワードを入力
    elem = driver.find_element_by_id("ss_yschsp").send_keys(title)

    #検索の実行
    elem_btn = driver.find_element_by_id("ss_srch_btn")
    elem_btn.click()
    #driver.find_element_by_class_name("aok-inline-block a-spacing-none").click()
    #url取得
    url=driver.current_url
    #print("----------------ここからurl----------------")
    #print(url)
    #print("----------------ここまでurl----------------")
    
    #source=driver.page_source
    #print("----------------ここからソース----------------")
    #print(source)
    #print("----------------ここまでソース----------------")
    
    #driver.save_screenshot("search_results.png")
    driver.quit()
    return url
    """
