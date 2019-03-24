import os, sys,logging,re,time,requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
logging.basicConfig(filename='./update_global_ip.log',level=logging.INFO)

opts = Options()
# opts.headless = True

email = "noip email"
password = "noip password"
last_ip_path = './last_ip.txt'
browser = None

def get_global_ip():
    url = 'http://api.ipify.org/'
    res = requests.get(url)
    return res.text

def save_ip(ip:str):
    with open(last_ip_path,'w') as f:
        f.write(ip)
        logging.info(ip)

def read_last_ip():
    if not os.path.isfile(last_ip_path):return ""
    with open(last_ip_path, 'r') as f:
        return  f.read()

def login_noip():
    global browser
    browser = webdriver.Chrome(chrome_options=opts)
    noip = "https://my.noip.com/#!/dynamic-dns"
    browser.get(noip)
    time.sleep(3)
    browser.find_element_by_name("username").send_keys(email)
    browser.find_element_by_name("password").send_keys((password))
    time.sleep(1)
    browser.find_element_by_name("Login").click()
    time.sleep(1)

def update_ip(ip:str):
    global browser
    browser.find_element_by_xpath("//*[@class='btn-label']").click()
    time.sleep(2)
    elms = browser.find_elements_by_xpath("//div[@class='modal-body']//input[@name='target']")
    elms[1].clear()
    elms[1].send_keys(ip)
    browser.find_element_by_xpath("//*[@class='btn btn-170 btn-flat btn-success btn-round-corners pr-sm ml-sm-30']/div").click()
    time.sleep(1)
    browser.quit()


if __name__ == '__main__':
    last_ip = read_last_ip()
    current_ip = get_global_ip()
    if last_ip == current_ip:sys.exit()
    login_noip()
    update_ip(current_ip)
    save_ip(current_ip)
    logging.info("Update to {}".format(current_ip))
    sys.exit()



