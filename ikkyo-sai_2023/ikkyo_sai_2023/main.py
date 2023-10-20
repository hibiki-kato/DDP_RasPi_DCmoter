import time
import tkinter as tk


# GUIの作成
root: tk.Tk = tk.Tk()

# ボタンの作成と配置
buttons: List[Tuple[tk.Button, tk.Button, tk.Button]] = []
for i in range(4):
    frame: tk.Frame = tk.Frame(root)
    frame.pack(side=tk.LEFT, padx=10)

    play_button: tk.Button = tk.Button(frame, text="再生")
    play_button.pack()

    pause_button: tk.Button = tk.Button(frame, text="一時停止")
    pause_button.pack()

    reset_button: tk.Button = tk.Button(frame, text="リセット")
    reset_button.pack()

    buttons.append((play_button, pause_button, reset_button))