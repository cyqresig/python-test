import time
import logging
logging.basicConfig(level=10)

import undetected_chromedriver as uc
def main(args=None):
    TAKE_IT_EASY = True

    if args:
        TAKE_IT_EASY = (
            args.no_sleeps
        )  # so the demo is 'follow-able' instead of some flashes and boom => done. set it how you like

    if TAKE_IT_EASY:
        sleep = time.sleep
    else:
        sleep = lambda n: print(
            "we could be sleeping %d seconds here, but we don't" % n
        )

    driver = uc.Chrome(headless=False,use_subprocess=False)
    driver.get('https://nowsecure.nl')
    # driver.get('https://s01-test.wxmovie.com/test/captcha/captcha.staging.html')

    sleep(3600)
    driver.quit()

if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--no-sleeps", "-ns", action="store_false")
    a = p.parse_args()
    main(a)
