from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
html=urlopen('https://ko.wikipedia.org/wiki/%EC%9C%A0%EC%9E%AC%EC%84%9D#%EC%B6%9C%EC%97%B0%EC%9E%91')
soup=BeautifulSoup(html,'lxml')
p=re.compile("\w\w\w")
program=soup.find_all('a',{'title':p})
program2=[]
for program1 in program:
    program2.append(program1.get_text())
program3=program2[175:391]
program4=[]
for i in range(0,len(program3)):
    if program3[i]!='KBS':
        if program3[i]!='SBS':
            if program3[i]!='MBC':
                if program3[i]!='tvN':
                    if program3[i]!='넷플릭스':
                        if program3[i]!='JTBC':
                            if program3[i]!='KBS2':
                                if program3[i]!='KBS1':
                                    program4.append(program3[i])
    else:
        pass

html2=urlopen('https://ko.wikipedia.org/wiki/%EA%B0%95%ED%98%B8%EB%8F%99#%EC%88%98%EC%83%81_%EA%B2%BD%EB%A0%A5_2')
soup=BeautifulSoup(html2,'lxml')
program5=soup.find_all('a',{'title':p})
program6=[]
for program7 in program5:
    program6.append(program7.get_text())
program8=program6[156:325]
program9=[]
for i in range(0,len(program8)):
    if program8[i]!='KBS':
        if program8[i]!='SBS':
            if program8[i]!='MBC':
                if program8[i]!='tvN':
                    if program8[i]!='넷플릭스':
                        if program8[i]!='JTBC':
                            if program8[i]!='KBS2':
                                if program8[i]!='KBS1':
                                    program9.append(program8[i])
    else:
        pass


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("https://ko.wikipedia.org/wiki/%EC%9C%A0%EC%9E%AC%EC%84%9D#%EC%88%98%EC%83%81")
soup=BeautifulSoup(html,'lxml')
p=re.compile("\w\w")
prize=soup.find_all("table",{"class":"wikitable"})
prize_tbody=prize[-1].find_all("tr")

big_prize=[]

for li in prize_tbody:
    li=li.find_all('li')
    for i in li:
        i=i.get_text()
        big_prize.append(i)

html2=urlopen("https://ko.wikipedia.org/wiki/%EA%B0%95%ED%98%B8%EB%8F%99")
soup=BeautifulSoup(html2,'lxml')
prize2=soup.find_all("table",{"class":"wikitable"})
prize_Tbody=prize2[1].find_all("tr")

Big_prize=[]

for Li in prize_Tbody:
    Li=Li.find_all('li')
    for I in Li:
        I=I.get_text()
        Big_prize.append(I)

import numpy as np
x=np.arange(2)
x1=['유재석','강호동']
programs=[len(program4),len(program9)+6]
수=[51,22]
print('유재석의 프로그램 출연 횟수: '+str(len(program4)))
print('강호동의 프로그램 출연 횟수: '+str(len(program9)+6))
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
plt.bar(x, programs, label='프로그램 수', color='b',width=0.3)
plt.bar(x+0.4,수,label='수상 횟수',color='r',width=0.3)
plt.xticks(x,x1)
plt.xlabel('연예인')
plt.suptitle('출연 프로그램 횟수와 수상 횟수 비교')
plt.legend()
plt.show()


