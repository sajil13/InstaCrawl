from bs4 import BeautifulSoup
import requests , shutil , os , re

username = input("Enter the user name of the Instagram account holder: ")
res = requests.get("https://www.instagram.com/" + username)

htmlsoup = BeautifulSoup(res.text,'html.parser')

pat = r'"display_src": "(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+.jpg)"'

img_url = re.findall(pat,str(htmlsoup))
pic = 0
for i in img_url:
    
    img = requests.get(i , stream=True)
    data = img.raw
    with open("Insta" + os.sep + str(pic) + ".jpg", 'wb') as insta_file:
        shutil.copyfileobj(r.raw, insta_file)
        pic+=1
    del r

