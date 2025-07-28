import os
import zipfile
#import undetected_chromedriver.v2 as uc
from selenium import webdriver
import json
PROXY_HOST = 'x.botproxy.net'  # rotating proxy
PROXY_PORT = 8080
PROXY_USER = 'pxu18829-0'
PROXY_PASS = 'z5uglHJthAcKOAqd0MUM'


manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
          },
          bypassList: ["localhost"]
        }
      };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

path2 = 'fl_orange/spiders'

jobid = ""


def get_chromedriver(use_proxy=False, user_agent=None, ji=jobid):
    #path2 = r'D:\OPERATOOL_TOOL_RPC\fl_orange\fl_orange\download\%s\\' % ji
    #path2 = r'D:\OPERATOOL_TOOL_RPC\fl_orange\fl_orange\download\%s\\' % ji
    #path2 = r'/Users/vishalsharma/Desktop/new/%s//' % ji
    # path2 = path2.replace("\\x0c","\\f")
    #print(path2)
    path = 'D:/GENERAL_OUTPUT/FL/fl_flagler'
    if not os.path.exists(path):
        os.mkdir(path)

    path2 = r'D:\GENERAL_OUTPUT\FL\fl_flagler\%s\\' % ji
    path = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists(path2):
        pass
    else:
        os.mkdir(path2)
    settings = {
        "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', {
        "download.default_directory": path2,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
        'printing.print_preview_sticky_settings.appState': json.dumps(settings),
        'savefile.default_directory': path2
    })
    #chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--kiosk-printing')
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'
        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)
    if user_agent:
        chrome_options.add_argument('--user-agent=%s' % user_agent)

    driver = webdriver.Chrome(
        executable_path='../chromedriver.exe',
        options=chrome_options)
    return driver

# def main():
#     driver = get_chromedriver(use_proxy=True)
#     #driver.get('https://www.google.com/search?q=my+ip+address')
#     driver.get('https://httpbin.org/ip')
#
#
# if __name__ == '__main__':
#     main()
