import requests as ur 
from bs4 import BeautifulSoup
f1 = open('my1.txt','a')#create a text file and locate here
f1.truncate(0)
f1.close() 
def fun(x):#for updating products in txt file
    x= str(x)
    f = open('my1.txt','a',encoding="utf-8")
    f.write(str(x))
    f.write('\n')
    f.close()
while 1:
    u = input('enter product')
    url='https://www.flipkart.com/search?q='+u+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    print(url)
    resp=ur.get(url)
    soup=BeautifulSoup(resp.content,'html.parser')
    #print(soup)
    #s1 for prouduct name &s2 for cost
    s1 =  soup.findAll('div',{'class':'_3wU53n'})
    s2 = soup.findAll('div',{'class':'_1vC4OE _2rQ-NK'})
    print(len(s1))
    if len(s1)== 0:#if no results found for s1 & s2
        s1 =  soup.findAll('a',{'class':'_2cLu-l'})
        s2 = soup.findAll('div',{'class':'_1vC4OE'})
    data = []
    x=0
    try:
        for j in s2:
            data.append(j.get_text())
        #print(data)
        for i in s1:
            r=i.get_text()
            r1=r.split('(')
            r1 = r1[0]+' : RS='+data[x]+'\n'
            print(r1)
            fun(r1)
            x +=1
        fun('-----------------******--------------')
    except:
        fun('-----------------******--------------')
        pass
