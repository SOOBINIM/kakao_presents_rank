from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter.tix import *
from presents import *


root = Tk()
root.title("카카오 선물하기 랭킹 확인")
root.geometry("540x380")
root.option_add("*Font", "궁서 20")

progress_complete = DoubleVar()

win_scroll = ScrolledWindow(root, width=320, height=240)
win_scroll.pack()


def test():
    for i in range(1, 3):
        print(i)


def dateGet():
    print(text_date.get())


btn_search = Button(root, fg="white", bg="green", padx=10,
                    pady=3, text="검색", command=rank)
btn_search.pack()

Label(win_scroll.window, text=rank)
# Label.configure(text=name)

label_info = Label(root, text="xx주차 핫아이템 광고")
label_info.pack()


text_date = Entry(root, width=10)
text_date.insert(0, "예)8/9")
text_date.pack()

# progressbar = ttk.Progressbar(
#     root, maximum=100, length=150, mode="indeterminate", variable=progress_complete)
# progressbar.pack()


def complete():
    msgbox.showinfo("검색 완료", "xx개의 값을 찾았습니다.")


# Button(root, command=complete, text="검색").pack()
# text_date.grid(row=0, column=0)
# label_info.grid(row=1, column=1)

root.mainloop()
