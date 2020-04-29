i=15

"""import requests
from bs4 import BeautifulSoup
import sys
import kaiseki

book_list=[]
def setup_book():
    response_zenhan=requests.get("https://hon-hikidashi.jp/enjoy/103170/")
    response_zenhan.encoding=response_zenhan.apparent_encoding
    response_kouhan=requests.get("https://hon-hikidashi.jp/enjoy/103171/")
    response_kouhan.encoding=response_kouhan.apparent_encoding

    #data=BeautifulSoup(response.content,"html.parser")
    data_zenhan=BeautifulSoup(response_zenhan.text,"html.parser")
    data_kouhan=BeautifulSoup(response_kouhan.text,"html.parser")

    #print(info.headers)
    #print(info.content)
    #print(data.text)
    #print(data.find_all("td"))
    #print(data.find(text="ジャンプコミックス"))
    count_title=-3
    count_date=-1
    count_author=-4
    #book_list = []

    for tag in data_zenhan("td"):
        count_title+=1
        count_date+=1
        count_author+=1

        if count_date % 5 == 0:
            date=tag.text
            #print(tag.text)

        if count_author % 5 == 0:
            author=tag.text
            book=[]
            book.append(title[-1])
            book.append(date)
            book.append(author)
            book_list.append(book)

        if count_title % 5 == 0:
            #if tag.find(text="ジャンプコミックス"):
            #print(tag.text)
        
            title=tag.text.splitlines()
            #title.pop(0)

    #print(book_list)

    count_title=-3
    count_date=-1
    count_author=-4

    for tag in data_kouhan("td"):
        count_title+=1
        count_date+=1
        count_author+=1

        if count_date % 5 == 0:
            date=tag.text
            #print(tag.text)

        if count_author % 5 == 0:
            author=tag.text
            book=[]
            book.append(title[-1])
            book.append(date)
            book.append(author)
            book_list.append(book)

        if count_title % 5 == 0:
            #if tag.find(text="ジャンプコミックス"):
            #print(tag.text)
        
            title=tag.text.splitlines()
            #title.pop(0)

def search(book):
    if book[0] == 0:
        book.pop(0)
        #print(book)
        return search_title(book)
    elif book[0] == 1:
        book.pop(0)
        return search_author(book)
    elif book[0] == 2:
        book.pop(0)

        return search_date(book)
        

def search_title(book_name):  
    #print(book_list)
    #if (text="人妻肉人形"):
    #print("（成）人妻肉人形さつき" in book_list[[1]])
    #print(book_list)
    result=0
    serched_list=[]
    #print("調べたい本はなあに？")
    #book_name=input()
    #print(book_list)
    if book_name != []:
        for i in book_list:
            #l_in = [s for s in i if book_name in s]
            #print(kaiseki.wakati(i[0]))
            #if l_in != []:

            if set(book_name) <=  set(kaiseki.wakati(i[0])): #i[0]タイトル検索 i[1]日付検索 i[2]著者検索
                #print("著者:"+i[2])
                #print(i[1]+"日発売です。")
                #print()
                serched_list.append(i)
                result=1

    if result != 1:
        #print("ありません。")
        return False
    #print(serched_list)
    return serched_list

def search_date(book_date):
    result=0
    serched_list=[]
    for i in book_list:
        if set(book_date) <=  set(kaiseki.wakati(i[1])): #i[0]タイトル検索 i[1]日付検索 i[2]著者検索
            serched_list.append(i)
            result=1
    
    if result != 1:
        #print("ありません。")
        return False
        
    return serched_list

def search_author(book_author):
    result=0
    serched_list=[]
    for i in book_list:
        if set(book_author) <=  set(kaiseki.wakati(i[2])): #i[0]タイトル検索 i[1]日付検索 i[2]著者検索
            serched_list.append(i)
            result=1
    
    if result != 1:
        #print("ありません。")
        return False

    return serched_list
"""
