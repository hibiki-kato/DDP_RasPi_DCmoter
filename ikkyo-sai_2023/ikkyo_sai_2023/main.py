import time
import tkinter as tk
import MoterClass as mc
from typing import List, Tuple
import asyncio

async def play_async(motor: mc.Motor, state_label: tk.Label, stop_label: tk.Label) -> None:
    motor.play()
    state_label.config(text="再生中", bg="green")

async def stop_async(motor: mc.Motor, state_label: tk.Label, stop_label: tk.Label) -> None:
    motor.stop()
    state_label.config(text="停止中", bg="red")

async def main_async():
    #pinの設定
    pins: List[int] = [17, 18, 27, 22]

    #モータークラスのインスタンス化
    moters: List[mc.Motor] = []
    for i in range(4):
        moters.append(mc.Motor(pins[i], "instruction.csv"))


    # GUIの作成
    root: tk.Tk = tk.Tk()
    root.title("一教祭2023")

    # ボタンとラベルの作成と配置
    buttons: List[Tuple[tk.Button, tk.Button, tk.Label]] = []
    for motor in moters:
        frame: tk.Frame = tk.Frame(root)
        frame.pack(side=tk.LEFT, padx=10)
        
        play_button: tk.Button = tk.Button(frame, text="再生", height=10, width=10, command=lambda m=motor: asyncio.create_task(play_async(m, state_label, stop_label)), bg="green", font=("", 20))
        play_button.pack()

        stop_button: tk.Button = tk.Button(frame, text="停止",height=10, width=15, command=lambda m=motor: asyncio.create_task(stop_async(m, state_label, stop_label)), bg="red", font=("", 20))
        stop_button.pack()

        state_label: tk.Label = tk.Label(frame, height=10, width=10, text="停止中", bg="red", font=("", 20))
        state_label.pack()

        buttons.append((play_button, stop_button, state_label))
        
    root.mainloop()

if __name__ == "__main__":
    asyncio.run(main_async())
