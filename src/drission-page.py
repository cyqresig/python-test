import time
import logging
logging.basicConfig(level=10)

from DrissionPage import ChromiumPage

driver = ChromiumPage()
driver.get('https://nowsecure.nl')
# driver.get('https://s01-test.wxmovie.com/test/captcha/captcha.staging.html')

time.sleep(3600)
driver.quit()