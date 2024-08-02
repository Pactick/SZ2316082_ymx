from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 初始化WebDriver
driver = webdriver.Chrome()

try:
    # 1. 打开搜狐网站
    driver.get("https://www.baidu.com")

    # 2. 在输入框中搜索深度强化学习
    search_box = EC.presence_of_element_located((By.NAME, "query"))
    search_box.send_keys("深度强化学习")
    search_box.send_keys(Keys.RETURN)

    # 3. 打开搜索到的第一个结果
    first_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".results h3 a"))
    )
    first_result.click()

    # 切换到新标签页
    driver.switch_to.window(driver.window_handles[1])

    # 4. 向下滑动翻阅后退出
    time.sleep(2)  # 等待页面加载
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

finally:
    # 5. 退出浏览器
    driver.quit()
