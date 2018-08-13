
# -*- coding: utf-8 -*-
import re
from urllib import request
import urllib
import os
import ssl
#Catch the webpage images


#According to the given web address to get the details of the web page, get the html is the source code of the web page.
def getHtml(url):
    #Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36
    #Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0
    #headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    page1=urllib.request.Request(url,headers=headers)
    page=urllib.request.urlopen(page1)
    html = page.read()
    return html

#Create folder to save pictures
def mkdir(path):
    path = path.strip()
    # Check whether the path exists
    # exist    True
    # not exist  Flase
    isExists = os.path.exists(path)
    if not isExists:
        print(u'New folder',path,u'created')
        # Create directory operation function
        os.makedirs(path)
        return True
    else:
        # If the directory exists, show the info:the directory already exists
        print(u'Named',path,u'a folder was existed')
        return False

# Input the file name and save the images
def saveUrl(imglist,name):
    for imageURL in imglist:
        imageURL = "https://www.baidu.com" + imageURL
        imageURL = imageURL.replace('th/', 'fm/')
        print
        try:
            f = open('thefile.txt','a')
            f.write(imageURL+"\n")
            f.close()
        except urllib.error.URLError as e:
            print (e.reason)

# Input the file name and save the images
def saveImages(imglist,name):
    number = 1
    for imageURL in imglist:
        imageURL = "https://www.baidu.com" + imageURL
        imageURL = imageURL.replace('th/', 'fm/')
        #headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        #pageimg1=urllib.request.Request(imageURL,headers=headers)
        #pageimg=urllib.request.urlopen(pageimg1)
        #pageimgUrl=pageimg.read()
        #print(pageimgUrl)
        headers = [('Host','www.baidu.com'),
                    ('Connection', 'keep-alive'),
                    ('Cache-Control', 'max-age=0'),
                    ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
                    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'),
                    ('Accept-Encoding','gzip,deflate,sdch'),
                    ('Accept-Language', 'zh-CN,zh;q=0.8'),
                    ('If-None-Match', '90101f995236651aa74454922de2ad74'),
                    ('Referer','http://image.baidu.com'),
                    ('If-Modified-Since', 'Thu, 01 Jan 1970 00:00:00 GMT')]
        picNamelist = imageURL.split("/")
        if picNamelist[-1].startswith("Issue") == True:
            picName = picNamelist[-2] + "_" + picNamelist[-1]
        else:
            picName = picNamelist[-1]
        fileName = name + "/" + picName +"A0" + str(number) + ".jpg" #+ fTail
        if os.path.exists(fileName):
            number += 1
        else:
            print
            try:
                opener = urllib.request.build_opener()
                opener.addheaders = headers
                data = opener.open(imageURL)
                data = data.read()
                f = open(fileName,'wb+')
                f.write(data)
                print('Saving image is ',fileName)
                f.close()
            except urllib.error.URLError as e:
                print(e.reason)
            number += 1

#Get the address of all the pictures in the web page
def getAllImg(html):
    #Filter out the picture address in the source code using regular expressions
    reg = r'data-src="(.+?\.jpg)"'
    #reg = r'id=\"imageName\" value="(.+?\.jpg)"'
    imgre = re.compile(reg)
    #print(reg)
    #print(imgre)
    #Indicates that the address of all pictures is filtered in the entire web page and placed in imglist.
    imglist = imgre.findall(str(html))
    #print(imglist)
    return imglist


#Create local save folder and download and save pictures.
#ssl._create_default_https_context = ssl._create_unverified_context
if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    path = u'Images'
    #Create local folder
    mkdir(path)
    n = 1
    for line in open("aa.txt"):
        #Get the web page details, and the html is the source code of the web page
        html = getHtml(line + "/"+str(n))
        #Get the address list of the images
        imglist = getAllImg(html.decode('utf-8'))
        #Save the image address
        saveUrl(imglist,path)
        #Save images
        saveImages(imglist,path)