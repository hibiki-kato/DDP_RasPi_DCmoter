import time
import tkinter as tk
import MoterClass as mc
from typing import List, Tuple

def main():
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

    # ボタンとラベルの作成と配置
    buttons: List[Tuple[tk.Button, tk.Button, tk.Label]] = []
    for motor in moters:
        frame: tk.Frame = tk.Frame(root)
        frame.pack(side=tk.LEFT, padx=10)

        play_button: tk.Button = tk.Button(frame, text="再生", command=lambda m=motor: play(m, play_label, stop_label))
        play_button.pack()

        stop_button: tk.Button = tk.Button(frame, text="停止", command=lambda m=motor: stop(m, play_label, stop_label))
        stop_button.pack()

        play_label: tk.Label = tk.Label(frame, text="停止中")
        play_label.pack()

        stop_label: tk.Label = tk.Label(frame, text="")
        stop_label.pack()

        buttons.append((play_button, stop_button, play_label, stop_label))
        
    # メインループ
    tk.mainloop()

def play(motor: mc.Motor, play_label: tk.Label, stop_label: tk.Label) -> None:
    motor.play()
    motor.is_playing = True
    play_label.config(text="再生中")
    stop_label.config(text="")

def stop(motor: mc.Motor, play_label: tk.Label, stop_label: tk.Label) -> None:
    motor.stop()
    motor.is_playing = False
    play_label.config(text="停止中")
    stop_label.config(text="停止中")
    
if __name__ == "__main__":
    main()

