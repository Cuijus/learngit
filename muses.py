
# -*- coding: utf-8 -*-
import re
from urllib import request
import urllib
import os
import ssl
#抓取网页图片


#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
def getHtml(url):
    #Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36
    #Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0
    #headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    page1=urllib.request.Request(url,headers=headers)
    page=urllib.request.urlopen(page1)
    #page = request.urlopen(url)
    html = page.read() #.decode("utf-8")
    return html

#创建保存图片的文件夹
def mkdir(path):
    path = path.strip()
    # 判断路径是否存在
    # 存在    True
    # 不存在  Flase
    isExists = os.path.exists(path)
    if not isExists:
        print(u'New folder',path,u'created')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已经存在
        print(u'Named',path,u'a folder was existed')
        return False

# 输入文件名，保存多张图片
def saveUrl(imglist,name):
    for imageURL in imglist:
        imageURL = "https://www.baidu.com" + imageURL
        imageURL = imageURL.replace('th/', 'fm/')
        #print(imageURL)
        print
        try:
            f = open('thefile.txt','a')
            f.write(imageURL+"\n")
            f.close()
        except urllib.error.URLError as e:
            print (e.reason)

# 输入文件名，保存多张图片
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
                    ('Referer','http://image.baidu.com/i?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&word=%E4%BA%A4%E9%80%9A&ie=utf-8'),
                    ('If-Modified-Since', 'Thu, 01 Jan 1970 00:00:00 GMT')]
        
        picNamelist = imageURL.split("/")
        if picNamelist[-1].startswith("Issue") == True:
            picName = picNamelist[-2] + "_" + picNamelist[-1]
        else:
            picName = picNamelist[-1]
        #PicName2 = picNamelist[-2]
        fileName = name + "/" + picName +"00" + str(number) + ".jpg" #+ fTail
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

#获取网页中所有图片的地址
def getAllImg(html):
    #利用正则表达式把源代码中的图片地址过滤出来
    reg = r'data-src="(.+?\.jpg)"'
    #reg = r'id=\"imageName\" value="(.+?\.jpg)"'
    imgre = re.compile(reg)
    #print(reg)
    #print(imgre)
    imglist = imgre.findall(str(html)) #表示在整个网页中过滤出所有图片的地址，放在imglist中
    #print(imglist)
    return imglist


#创建本地保存文件夹，并下载保存图片
#ssl._create_default_https_context = ssl._create_unverified_context
if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    path = u'Images'
    #创建本地文件夹
    mkdir(path)
    n = 1
    for line in open("aa.txt"):
        #获取该网址网页详细信息，得到的html就是网页的源代码
        html = getHtml(line + "/"+str(n))
        #获取图片的地址列表
        imglist = getAllImg(html.decode('utf-8'))
        #保存图片地址
        saveUrl(imglist,path)
        #保存图片
        saveImages(imglist,path)