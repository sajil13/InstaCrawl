from bs4 import BeautifulSoup
import requests , shutil , os , re , time

username = input("Instagram Username : ")
filename = input("Filename to put your images in: ")
noofpages = int(input("Number pages you want NOTE: 1 Page = 12 Images: "))
res = requests.get("https://www.instagram.com/" +username)
htmlsoup = BeautifulSoup(res.text,'html.parser')


def images(mid = ''):
    res_i = requests.get("https://www.instagram.com/" + username+mid)
    global htmlsoup_i
    htmlsoup_i = BeautifulSoup(res_i.text,'html.parser')
    pat = r'"display_src": "(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+.jpg)"'
    img_url = re.findall(pat,str(htmlsoup_i))
    if(os.path.exists(filename)):
        pass
    else:
        os.mkdir(filename)
    for i in img_url:
        img = requests.get(i , stream=True)
        data = img.raw
        with open(filename + os.sep + str(time.time()) + ".jpg", 'wb') as insta_file:
            shutil.copyfileobj(img.raw, insta_file)
        del img
    del img_url


posts = re.findall(r'(\d+) Posts',str(htmlsoup))
pages = int(posts[0])/12

if noofpages in range(1,int(pages)+1):
    for j in range(1,noofpages+1):
        if j == 1:
            images()
        else:
            
            pat1 = r'"GraphImage", "id": "(\d*)"'
            maxid = re.findall(pat1,str(htmlsoup_i))
            
            new_url = "/?max_id="+maxid[len(maxid)-1]
            images(new_url)
            del maxid
        
else:
    print("These many number of pages doesn't exist")
