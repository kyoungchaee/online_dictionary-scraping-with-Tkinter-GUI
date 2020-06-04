from tkinter.scrolledtext import ScrolledText
from tkinter import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re



##크롤링 기능 추가
def search():
    global english_word 
    english_word = search_entry.get()
    print("english_word", english_word)
    cam_search(english_word)
    YBM_search(english_word)
    long_search(english_word)


def long_search(english_word):
    long_url = urlopen("https://www.ldoceonline.com/ko/dictionary/english-korean/" + english_word)
    bs = BeautifulSoup(long_url.read(), 'html.parser')

    definitionList = str(bs.find_all(class_="Translation" and "TRAN", limit=3))
    parced_def = re.sub('<.+?>', '', definitionList, 0).strip()
    exampleList = str(bs.find_all(class_="Examples" and "exagr", limit=2))
    parced_ex = re.sub('<.+?>', '', exampleList, 0).strip()
    long_def.replace("1.0", END, "뜻 : %s \n\n예문 : %s" % (parced_def, parced_ex))
    return 

def cam_search(english_word):
    cam_url = urlopen("https://dictionary.cambridge.org/dictionary/english-korean/" + english_word)
    bs = BeautifulSoup(cam_url.read(), 'html.parser')

    definitionList = str(bs.find_all(class_="def ddef_d db", limit=3))
    parced_def = re.sub('<.+?>', '', definitionList, 0).strip()
    exampleList = str(bs.find_all(class_="examp dexamp", limit=2))
    parced_ex = re.sub('<.+?>', '', exampleList, 0).strip()
    cam_def.replace("1.0", END, "뜻 : %s \n\n예문 : %s" % (parced_def, parced_ex))
    
    return 

def YBM_search(english_word):
    YBM_url = urlopen("http://www.ybmallinall.com/styleV2/dicview.asp?kwdseq=0&kwdseq2=0&"
                      + "DictCategory=DictEng&DictNum=1&ById=0&PageSize=5&StartNum=0&GroupMode=0&cmd=0&kwd="
                      + english_word + "&x=0&y=0")
    bs = BeautifulSoup(YBM_url.read(), 'html.parser')

    definitionList= str(bs.find_all(class_="Explain ybm", limit=3))
    parced_def = re.sub('<.+?>', '', definitionList, 0).strip()
    YBM_def.replace("1.0", END, "뜻 : %s " %(parced_def))
    return

# 기본 설정
window = Tk()  ##보통 다이얼로그(레이블, 텍스트박스, 버튼)은 tk생성 함수와 mainloop함수 사이에 집어 넣음
window.title('파이썬 영단어 검색기')
window.resizable(True, True)  ##사용자가 창 사이즈 늘리기 기능 허용##

# 인터페이스 추가
# 프레임추가
frame1 = Frame(window, relief="solid", bd=2, padx=15, pady=10)
frame1.pack(side="top", fill="both", expand=False)
frame2 = Frame(window, relief="solid", bd=2)
frame2.pack(side="bottom", fill="both", expand=True)
frame3 = Frame(frame2, relief="solid", bd=2)
frame3.pack(side="left", fill="both", expand=True)
frame4 = Frame(frame2, relief="solid", bd=2)
frame4.pack(side="left", fill="both", expand=True)
frame5 = Frame(frame2, relief="solid", bd=2)
frame5.pack(side="right", fill="both", expand=True)

# 검색 입력 창 구현
frame1_1 = Frame(frame1)
frame1_1.pack(anchor='c')
search_label = Label(frame1_1, text=" 단어 검색기: ", font=("배달의민족주아", 15, 'bold'), fg="black")
search_label.pack(side="left", pady=5, padx=5)

## 라벨은 주로 이미지,  글 등에 주석문으로 사용
## 라벨 추가 방법 :위젯이름=tkinter.Label(윈도우창, text="내용") 사용해서 위젯 설정

# 빈간(entry) 구현
search_entry = Entry(frame1_1, width=40, text="")
search_entry.bind("<Return>")
search_entry.pack(side="left", pady=5, padx=5)

# 검색 버튼 구현
search_button = Button(frame1_1, text="검색", font=("배달의민족 주아", 10), command=search)  # command=search()
search_button.pack(side="left", pady=5, padx=5)

# 종료 버튼 구현
quit_button = Button(frame1_1, text="종료", font=("배달의민족주아", 10), fg='red', command=window.destroy)
quit_button.pack(side="left", pady=5, padx=5)

# 1. Cambridge Dictionary
cam_label = Label(frame3, text="Cambridge Dictionary", font=("배달의민족 주아", 10, "bold"))
cam_label.pack(side="top")
cam_def = ScrolledText(frame3, width=40, height=20, background="SystemButtonFace")
cam_def.pack(side="top",expand=True, fill="both")

# 2. YBM 영한사전 검색
YBM_label = Label(frame4, text="YBM 영한사전", font=("배달의민족 주아", 10, "bold"))
YBM_label.pack(side="top")
YBM_def = ScrolledText(frame4, width=40, height=20, background="SystemButtonFace")
YBM_def.pack(side="top",expand=True, fill="both")

# 3. Longman Dictionary
long_label = Label(frame5, text="Longman Dictionary", font=("배달의민족 주아", 10, "bold"))
long_label.pack(side="top")
long_def = ScrolledText(frame5, width=40, height=20, background="SystemButtonFace")
long_def.pack(side="top", expand=True, fill="both")

window.mainloop()
