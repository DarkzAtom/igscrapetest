from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from pprint import pprint
import json
# from zyte_smartproxy_selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
import random
from extension import proxies


# stop_status = False
# zyte_api_key = "2ff54daf4042456d9b99ef2946fee95c"
# proxy_url = f"{zyte_api_key}:@proxy.crawlera.com:8011/"
# output = {}

smartproxy_username = "spu2u4zn32"
smartproxy_password = "12345678"

# smartproxy_proxies = [
#     "gate.smartproxy.com:10000",
#     "gate.smartproxy.com:10001",
#     "gate.smartproxy.com:10002",
#     "gate.smartproxy.com:10003",
#     "gate.smartproxy.com:10004",
#     "gate.smartproxy.com:10005",
#     "gate.smartproxy.com:10006",
#     "gate.smartproxy.com:10007",
#     "gate.smartproxy.com:10008",
#     "gate.smartproxy.com:10009",
# ]

username = "shalomslavyanie"
password = "13m9aVpbV3hhdl~XNf"
endpoint = "gate.smartproxy.com"
port = "7000"

def prepare_browser():
    # PROXY = "https://spu2u4zn32:111222333@gate.smartproxy.com:7000"
    # proxy_str = '{hostname}:{port}'.format(hostname=HOSTNAME, port=PORT)
    options = webdriver.ChromeOptions()
    # options.add_argument(f'--proxy-server={PROXY}')
    proxies_extension = proxies(username, password, endpoint, port)
    options.add_extension(proxies_extension)
    # options.add_argument('--proxy-server={}'.format(proxy_str))
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    stealth(driver,
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
            languages=["en-US", "en"],
            vendor= "Google Inc.",
            platform= "Win32",
            webgl_vendor= "Intel Inc.",
            renderer= "Intel Iris OpenGL Engine",
            fix_hairline= False,
            run_on_insecure_origins= False,
            )
    return driver

def main():
    stop_status = None
    url = "https://www.instagram.com/reels/audio/249517056921774/"
    # url = "https://www.instagram.com/reels/audio/676302309391102/"
    # options = webdriver.ChromeOptions
    # driver = webdriver.Chrome()
    driver = prepare_browser()
    driver.get(url)

    # fedsakolsk

    # try:
    #     WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "svg[aria-label='Загрузка…']")))
    #     nested_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xl565be.x1s688f.x9bdzbf.x1tu3fi.x3x7a5m.x10wh9bi.x1wdrske.x8viiok.x18hxmgj")))
    #     larger_container_element = nested_element.find_element(By.XPATH, "./ancestor::div[12]")
    #     larger_container_element_html = larger_container_element.get_attribute('outerHTML')
    # except (Exception, AttributeError) as e:
    #     return None
    # finally:
    #     driver.quit()

    try:
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._abq3._al5p")))

    except(Exception, AttributeError) as e:
        return None


    # this is the test part to implement loading the whole elements with the infinite scrolling

    items=[]

    last_height = driver.execute_script("return document.body.scrollHeight")

    numberofreels = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[2]/div[1]/div/div[2]/div[2]/span').text

    parts = numberofreels.split()

    itemTargetCount  = int(parts[0])

    try:
        accept_button = driver.find_element(By.CSS_SELECTOR, 'button._a9--._ap36._a9_0')
    except NoSuchElementException:
        accept_button = None

    if accept_button:
        accept_button.click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'button._a9--._ap36._a9_0')))
    else:
        pass

    try:
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x972fbf.xcfux6l.x1qhh985.xm0m39n.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x18d9i69.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x9bdzbf.x1ypdohk.x1f6kntn.xwhw2v2.x10w6t97.xl56j7k.x17ydfre.x1swvt13.x1pi30zi.x1n2onr6.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.x1tu34mt.xzloghq.xe81s16.x3nfvp2')))
    except NoSuchElementException:
        login_button = None

    if login_button:
        login_button.click()
        enter_username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input._aa4b._add6._ac4d._ap35')))
        enter_password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        enter_username.send_keys('cocojumbo123123')
        enter_password.send_keys('cocojumbo123123pass')
        enter_password.send_keys(Keys.RETURN)
    else:
        pass
    # button for accepting cookies is button._a9--._ap36._a9_0

    # the class to save the credentials: button._acan._acap._acas._aj1-._ap30

    try:
        save_credentials_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._acan._acap._acas._aj1-._ap30')))
    except (NoSuchElementException, TimeoutException):
        save_credentials_button = None

    if save_credentials_button:
        save_credentials_button.click()
    else:
        pass

    collected_hrefs = set()

    while itemTargetCount > len(items):

        # it ends here

        #button for closing the proposition to log in:  div.x1i10hfl.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x6s0dn4.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x1ypdohk.x78zum5.xl56j7k.x1y1aw1k.x1sxyh0.xwib8y2.xurb0ha.xcdnw81

        try:
            close_button = driver.find_element(By.CSS_SELECTOR, 'div.x1i10hfl.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x6s0dn4.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x1ypdohk.x78zum5.xl56j7k.x1y1aw1k.x1sxyh0.xwib8y2.xurb0ha.xcdnw81')
        except NoSuchElementException:
            close_button = None

        if close_button:
            close_button.click()
        else:
            pass


        reels = driver.find_elements(By.CSS_SELECTOR, 'div._abq3._al5p')
        amountofitems = 0
        for i, reel in enumerate(reels):
            link = reel.find_element(By.CSS_SELECTOR,'a.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._a6hd').get_attribute('href')
            collected_hrefs.add(link)
            amountofitems += 1

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")


        if new_height == last_height:
            if stop_status:
                break
            else:
                if len(collected_hrefs) < itemTargetCount:
                    time.sleep(15)
                    stop_status = True
                else:
                    break
        else:
            pass

        last_height = new_height

    collected_hrefs_list = list(collected_hrefs)
    print(collected_hrefs_list)
    print('\n')
    print(len(collected_hrefs_list))
    amount_of_repetitions = 0
    for i in range(len(collected_hrefs_list)):
        for j in range(i + 1, len(collected_hrefs_list)):
            if i != j and collected_hrefs_list[i] == collected_hrefs_list[j]:
                amount_of_repetitions += 1
            else:
                continue

    print(amount_of_repetitions)



#     numberofreels = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[2]/div[1]/div/div[2]/div[2]/span').text
#
#     parts = numberofreels.split()
#
#     number = int(parts[0])
#
#     reels = driver.find_elements(By.CSS_SELECTOR, 'div._abq3._al5p')
#     views = []
#     for reel in reels:
#
#         view = reel.find_elements(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/a/div[2]/div[2]/div/div/div/span/span")
#         views.append(view)
#     for i in range(len(views)):
#         print(views[i])
#         print('\n')
#
#
#
#
#
#
#
#
#
#     print(number, '\n', reels[0])
#
if __name__ == "__main__":
    main()