import tkinter as tk
from datetime import datetime

class Clock():
    def __init__(self):
        self.sub_win = tk.Toplevel()
        self.label_sub = tk.Label(self.sub_win, text="hello", font=('Helvetica', 48), fg='black')
        self.sub_win.geometry("500x65")
        self.sub_win.title("寿命カウントダウン")
        self.label_sub.pack()
        self.update_clock()
        self.sub_win.mainloop()

    def update_clock(self):
        dt_now = datetime.now()
        dt_end = datetime(bir_year + life_span, bir_mon, bir_day)
        re_day = dt_end - dt_now
        hour = 23 - dt_now.hour
        minute = 59 - dt_now.minute
        second = 59 - dt_now.second
        now =str(re_day.days) + 'Day ' + str(hour) + 'h ' + str(minute) + 'm ' + str(second) + 's '
        self.label_sub.configure(text=now)
        self.sub_win.after(1000, self.update_clock)

def count():
    global bir_day, bir_year, bir_mon, life_span
    bir_year = int(entry1.get())
    bir_mon = int(entry2.get())
    bir_day = int(entry3.get())
    life_span = int(entry4.get())
    Clock()

# rootフレームの設定
root = tk.Tk()
root.title("寿命カウントダウンアプリ")
root.geometry("300x280")
# 入力画面ラベルの設定
label1 = tk.Label(root,text="【生年月日入力画面】",font=("",16),height=2)
label1.pack(fill="x")

# 年のラベルとエントリーの設定
frame1 = tk.Frame(root,pady=10)
frame1.pack()
label1 = tk.Label(frame1,font=("",14),text="年")
label1.pack(side="left")
entry1 = tk.Entry(frame1,font=("",14),justify="center",width=15)
entry1.pack(side="left")

# 月のラベルとエントリーの設定
frame2 = tk.Frame(root,pady=10)
frame2.pack()
label2 = tk.Label(frame2,font=("",14),text="月")
label2.pack(side="left")
entry2 = tk.Entry(frame2,font=("",14),justify="center",width=15)
entry2.pack(side="left")

# 日のラベルとエントリーの設定
frame3 = tk.Frame(root,pady=10)
frame3.pack()
label3 = tk.Label(frame3,font=("",14),text="日")
label3.pack(side="left")
entry3 = tk.Entry(frame3,font=("",14),justify="center",width=15)
entry3.pack(side="left")

# 寿命のラベルとエントリーの設定
life = tk.Frame(root,pady=10)
life.pack()
label4 = tk.Label(life,font=("",14),text="推定寿命")
label4.pack(side="left")
entry4 = tk.Entry(life,font=("",14),justify="center",width=15)
entry4.pack(side="left")

# 開始ボタンの設定
button = tk.Button(root,text="開始",font=("",16),width=10,bg="gray",command=count)
button.pack()

# メインループ
root.mainloop()
