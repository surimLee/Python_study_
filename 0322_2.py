# 레이블을 사용하여 간단한 스톱워치를 작성하여 보자. 
# 시작 버튼을 누르면 시작되고 중지 버튼을 누르면
# 스톱워치가 중지된다. 

import tkinter as tk

def startTimer():
	if (running):
		global timer
		timer += 1
		timeText.configure(text=str(timer))
	window.after(10, startTimer)

def start():
	global running
	running = True

def stop():
	global running
	running = False

running = False

window = tk.Tk()

timer = 0

timeText = tk.Label(window, text="0", font=("Helvetica", 80))
timeText.pack()

startButton = tk.Button(window, text='시작', bg="yellow", command=start)
startButton.pack(fill=tk.BOTH)

stopButton = tk.Button(window, text='중지', bg="yellow", command=stop)
stopButton.pack(fill=tk.BOTH)

startTimer()
window.mainloop()