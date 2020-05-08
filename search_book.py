import sys
import kaiseki
book_list = []
path_r = "./book_data.txt"

def setup_list():
    f = open(path_r,"r",encoding = 'utf-8')
    for line in f:
        line = line.strip()
        line = line.replace("\n","")
        line = line.split(",")
        book_list.append(line)
    f.close()
    
def search(book):
    if book[0] == 0:
        book.pop(0)
        return book_list
        return search_title(book)
    elif book[0] == 1:
        book.pop(0)
        return search_author(book)
    elif book[0] == 2:
        book.pop(0)
        return search_date(book)
        

def search_title(book_name):  
    result=0
    serched_list=[]
    if book_name != []:
        for i in book_list:
             if set(book_name) <=  set(kaiseki.wakati(i[0])): #i[0]タイトル検索 i[1]日付検索 i[2]著者検索
                serched_list.append(i)
                result=1
    if result != 1:
       return False
    return serched_list

def search_date(book_date):
    result=0
    serched_list=[]
    for i in book_list:
        if set(book_date) <=  set(kaiseki.wakati(i[1])): #i[0]タイトル検索 i[1]日付検索 i[2]著者検索
            serched_list.append(i)
            result=1
    if result != 1:
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
        return False

    return serched_list
