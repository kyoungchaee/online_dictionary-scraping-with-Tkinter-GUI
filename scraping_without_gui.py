from urllib.request import *              ###필요한 외부 패키지 호출
from bs4 import BeautifulSoup
import re

def search(english_word):  ##기본 함수
    cam_search(english_word)
    long_search(english_word)
    YBM_search(english_word)


def long_search(english_word): ##각 사전 함수
    long_url = urlopen("https://www.ldoceonline.com/ko/dictionary/english-korean/" + english_word)
    bs = BeautifulSoup(long_url.read(), 'html.parser') ##bs4 사용 url 불러오기, 파싱 실시

    definitionList = str(bs.find_all(class_= ("freq lejEntry koreanEntry"and "TRAN") ##단어 의미 찾기 - 사이트별 태그 활용
                                     or ("lejEntry koreanEntry" and "TRAN") , limit=4))
    parced_def = re.sub('<.+?>', '', definitionList, 0).strip() ##단어 의미에서 정규화 기호들 없애기
    exampleList = str(bs.find_all(class_="Examples" and "exagr", limit=1)) ##해당 단어의 예문 찾기 - 사이트별 태그 활용
    parced_ex = re.sub('<.+?>', '', exampleList, 0).strip() ##예문에서 정규화 기호들 없애기
    
    return print("Longman Dictionary 검색결과......\n뜻 : %s \n예문 : %s\n"%(parced_def, parced_ex))

def cam_search(english_word):
    cam_url = urlopen("https://dictionary.cambridge.org/dictionary/english-korean/"
    + english_word)
    bs = BeautifulSoup(cam_url.read(), 'html.parser')

    definitionList = str(bs.find_all(class_="def ddef_d db", limit=3))
    parced_def = re.sub('<.+?>', '', definitionList, 0).strip()
    exampleList = str(bs.find_all(class_="examp dexamp", limit=2))
    parced_ex = re.sub('<.+?>', '', exampleList, 0).strip()

    return print("Cambirdge Dictionary 검색결과......\n뜻 : %s \n예문 : %s\n"%(parced_def, parced_ex))

def YBM_search(english_word):
    YBM_url = urlopen("http://www.ybmallinall.com/styleV2/dicview.asp?kwdseq=0&kwdseq2=0&DictCategory=Dict" 
                      + "Eng&DictNum=1&ById=0&PageSize=5&StartNum=0&GroupMode=0&cmd=0&kwd="
                      + english_word + "&x=0&y=0")
    bs = BeautifulSoup(YBM_url.read(), 'html.parser')

    definitionList= str(bs.find_all(class_="Explain ybm", limit=6))
    parced_def = re.sub('<.+?>', '', definitionList, 0).strip()

    return print("YBM 영한사전  검색결과......\n뜻 : %s\n"%(parced_def))

print("\t\t파이썬 단어 검색기")
   
while(True) :
    print("\n***종료하시려면 1을 입력하세요 /  예문이 없는 단어는 []로 출력됩니다")
    english_word = input("검색하실 단어를 입력하세요 : ")

    if english_word.isalpha() == True :

            print("검색 중입니다.........\n")
            print("")      
            search(english_word)

    elif english_word.isalpha() == False :
        if english_word == '1' :
            print("\n프로그램을 종료합니다......")
            break
        else :
            print("\n숫자 및 기호를 입력하셨습니다\n입력할 단어(문자)를 입력하세요")

    






