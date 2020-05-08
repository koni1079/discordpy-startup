import sys
import kaiseki
book_list = []
wakati_list = []
path_r = "./book_data.txt"
path_r2 = "./wakati_data.txt"

def setup_list():
    f = open(path_r,"r",encoding = 'utf-8')
    for line in f:
        line = line.strip()
        line = line.replace("\n","")
        line = line.split(",")
        book_list.append(line)
    f.close()

    f = open(path_r2,"r",encoding = 'utf-8')
    one_book = []
    for line in f:
        line = line.strip()
        line = line.replace("\n","")
        line = line.split(",")
        one_book.append(line)
        if len(one_book) == 3:
            wakati_list.append(one_book)
            one_book = [] 
    f.close()
    #print(wakati_list)


def search(book):
    if book[0] == 0:
        book.pop(0)
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
        for i,book in enumerate(wakati_list):
            #print(title[0])
            if set(book_name) <=  set(book[0]): #i[0]タイトル検索 i[1]日付検索 i[2]著者検索
                serched_list.append(book_list[i])
                result=1
    if result != 1:
        #print(kaiseki.wakati(book_list[-1][0]))
        return False
    return serched_list

def search_date(book_date):
    result=0
    serched_list=[]
    for i,book in enumerate(wakati_list):
        if set(book_date) <=  set(book[1]): #i[0]タイトル検索 i[1]日付検索 i[2]著者検索
            serched_list.append(book_list[i])
            result=1
    if result != 1:
        return False       
    return serched_list

def search_author(book_author):
    result=0
    serched_list=[]
    for i,book in enumerate(wakati_list):
        if set(book_author) <=  set(book[2]): #i[0]タイトル検索 i[1]日付検索 i[2]著者検索
            serched_list.append(book_list[i])
            result=1    
    if result != 1:
        return False
    return serched_list
