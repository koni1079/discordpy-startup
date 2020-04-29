import MeCab

def analysis(message):
    morpheme=[]
    taboo={"タイトル":0,"作者":1,"日付":2} #発売日は辞書登録しなければならないため一応日付
    tabooset = 0
    m=MeCab.Tagger("-Ochasen")
    m.parse('')
    #message = message.encode('utf-8')
    node = m.parseToNode(message)
    
    while node:
        word=node.surface
        #print(word)
        #print("----")
        wclass=node.feature.split(",")
        if wclass[0] != u'BOS/EOS':
            if wclass[0] == "名詞":
                tabooflag = 0
                if tabooset != 1:
                    if word in taboo.keys():
                        morpheme.insert(0,taboo[word])
                        tabooflag = 1
                        tabooset = 1

                if tabooflag != 1:    
                    #print(noun)
                    morpheme.append(word)
                    #print(word)
                    #print(word,",",wclass[0])
        #print(word,end=",")
        #print(wclass)   #ここで形態素解析表示できる
        node=node.next
    #print(wclass[0])
    #print(morpheme)
    if tabooset != 1:
        morpheme.insert(0,0)
    return morpheme #リスト型[“名詞1”,”名詞2”,…]
    
    #return m.parse(message)

def wakati(title):
    morpheme=[]
    m=MeCab.Tagger("-Ochasen")
    m.parse('')
    node = m.parseToNode(title)
    while node:
        word=node.surface
        wclass=node.feature.split(",")
        if wclass[0] != u'BOS/EOS':
            morpheme.append(word)
            #print(word)
            #print(word,",",wclass[0])
        node=node.next
    #print(wclass[0])
    #print(morpheme)
    return morpheme #リスト型[“名詞1”,”名詞2”,…]
