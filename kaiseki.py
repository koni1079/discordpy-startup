from janome.tokenizer import Tokenizer

def analysis(message):
    t=Tokenizer()
    morpheme=[]
    taboo={"タイトル":0,"作者":1,"日付":2} #発売日は辞書登録しなければならないため一応日付
    tabooset = 0

    for token in t.tokenize(message):
        if token.part_of_speech.split(',')[0] == "名詞":
            tabooflag = 0
            if tabooset != 1:
                if token.surface in taboo.keys():
                    morpheme.insert(0,taboo[token.surface])
                    tabooflag = 1
                    tabooset = 1
            if tabooflag != 1:
                morpheme.append(token.surface)
    if tabooset != 1:
        morpheme.insert(0,0)
    return morpheme

def wakati(title):
    t=Tokenizer()
    morpheme=[]
    for token in t.tokenize(title):
        morpheme.append(token.surface)
    return morpheme
