from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        var items = document.querySelector('downloads-manager')
            .shadowRoot.getElementById('downloadsList').items;
        if (items.every(e => e.state === "COMPLETE"))
            return items.map(e => e.fileUrl || e.file_url);
        """)

def get_iodd(product_name):
    driver = webdriver.Chrome(executable_path = '/usr/lib/chromium-browser/chromedriver')
    driver.get("https://ioddfinder.io-link.com/productvariants/search?page=0&vendorName=Festo&productName=" + product_name)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-product-variant-search/div[3]/div[2]/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper/datatable-body-row/div[2]/datatable-body-cell[1]/div/div/span'))).click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/ngb-modal-window/div/div/app-terms-of-use-modal/div[3]/button[1]'))).click()
    wait = WebDriverWait(driver, 120, 1).until(every_downloads_chrome)
    driver.close()