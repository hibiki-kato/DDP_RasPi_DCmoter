import time
import tkinter as tk
import MoterClass as mc
from typing import List, Tuple

#pinの設定
pins: List[int] = [17, 18, 27, 22]

#モータークラスのインスタンス化
moters: List[mc.Motor] = []
for i in range(4):
    moters.append(mc.Motor(pins[i], "instruction.csv"))


# GUIの作成
root: tk.Tk = tk.Tk()
root.geometry("1200x900")
root.title("一教祭2023")

# ボタンの作成と配置
buttons: List[Tuple[tk.Button, tk.Button]] = []
for motor in moters:
    frame: tk.Frame = tk.Frame(root)
    frame.pack(side=tk.LEFT, padx=10)

    play_button: tk.Button = tk.Button(frame, text="再生", width=10, height=5, command = motor.play())
    play_button.pack()

    reset_button: tk.Button = tk.Button(frame, text="リセット", width=10, height=5, command = motor.stop())
    reset_button.pack()

    buttons.append((play_button, reset_button))
        
# BEGIN: 8zj5t3d7f2q1
root.mainloop()
