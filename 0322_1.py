# 격자 배치 관리자를 사용하여 레이블과 버튼을 배치한다. 
# 색상의 개수만큼 반복하면서 레이블과 버튼을 생성하고
# 격자형태로 배치하면 된다. 

from tkinter import *

# 약간의 3차원 효과를 낸다. 

window = Tk()
colors = ['green', 'red', 'orange','white','yellow','blue']

r = 0
for c in colors:
	Label(window, text=c, relief=RIDGE, width=15).grid(row=r, column=0)
	Button(window, bg=c, width=10).grid(row=r, column=1)
	r = r + 1

window.mainloop()