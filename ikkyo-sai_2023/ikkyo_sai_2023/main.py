import tkinter as tk
import MoterClass as mc
from typing import List
import asyncio

async def main_async():
    # pinの設定
    pins: List[int] = [17, 18, 27, 22]

    # モータークラスのインスタンス化
    motors: List[mc.Motor] = []
    motors.append(mc.Motor(pins[0], "instruction.csv"))
    motors.append(mc.Motor(pins[1], "instruction.csv"))
    motors.append(mc.Motor(pins[2], "instruction.csv"))
    motors.append(mc.Motor(pins[3], "instruction.csv"))

    # GUIの作成
    root: tk.Tk = tk.Tk()
    root.title("一教祭2023")

    # ボタンとラベルの作成と配置
    frame1: tk.Frame = tk.Frame(root)
    frame1.pack(side=tk.LEFT, padx=10)

    state_label1: tk.Label = tk.Label(frame1, height=10, width=20, text="停止中", bg="red", font=("", 20))
    state_label1.pack()

    play_button1: tk.Button = tk.Button(frame1, text="再生", height=10, width=20, command=lambda: asyncio.create_task(play_async(motors[0], state_label1)), bg="green", font=("", 20))
    play_button1.pack()

    stop_button1: tk.Button = tk.Button(frame1, text="停止", height=10, width=20, command=lambda: asyncio.create_task(stop_async(motors[0], state_label1)), bg="red", font=("", 20))
    stop_button1.pack()

    frame2: tk.Frame = tk.Frame(root)
    frame2.pack(side=tk.LEFT, padx=10)

    state_label2: tk.Label = tk.Label(frame2, height=10, width=20, text="停止中", bg="red", font=("", 20))
    state_label2.pack()

    play_button2: tk.Button = tk.Button(frame2, text="再生", height=10, width=20, command=lambda: asyncio.create_task(play_async(motors[1], state_label2)), bg="green", font=("", 20))
    play_button2.pack()

    stop_button2: tk.Button = tk.Button(frame2, text="停止", height=10, width=20, command=lambda: asyncio.create_task(stop_async(motors[1], state_label2)), bg="red", font=("", 20))
    stop_button2.pack()

    frame3: tk.Frame = tk.Frame(root)
    frame3.pack(side=tk.LEFT, padx=10)

    state_label3: tk.Label = tk.Label(frame3, height=10, width=20, text="停止中", bg="red", font=("", 20))
    state_label3.pack()

    play_button3: tk.Button = tk.Button(frame3, text="再生", height=10, width=20, command=lambda: asyncio.create_task(play_async(motors[2], state_label3)), bg="green", font=("", 20))
    play_button3.pack()

    stop_button3: tk.Button = tk.Button(frame3, text="停止", height=10, width=20, command=lambda: asyncio.create_task(stop_async(motors[2], state_label3)), bg="red", font=("", 20))
    stop_button3.pack()

    frame4: tk.Frame = tk.Frame(root)
    frame4.pack(side=tk.LEFT, padx=10)

    state_label4: tk.Label = tk.Label(frame4, height=10, width=20, text="停止中", bg="red", font=("", 20))
    state_label4.pack()

    play_button4: tk.Button = tk.Button(frame4, text="再生", height=10, width=20, command=lambda: asyncio.create_task(play_async(motors[3], state_label4)), bg="green", font=("", 20))
    play_button4.pack()

    stop_button4: tk.Button = tk.Button(frame4, text="停止", height=10, width=20, command=lambda: asyncio.create_task(stop_async(motors[3], state_label4)), bg="red", font=("", 20))
    stop_button4.pack()

    # 下に一斉再生と一斉停止のボタンを作成
    frame5: tk.Frame = tk.Frame(root)
    frame5.pack(side=tk.LEFT, padx=10)

    play_all_button: tk.Button = tk.Button(frame5, text="一斉再生", height=10, width=20, command=lambda: [asyncio.create_task(play_async(m, l)) for (m, l) in zip(motors, [state_label1, state_label2, state_label3, state_label4])], bg="green", font=("", 20))
    play_all_button.pack()

    stop_all_button: tk.Button = tk.Button(frame5, text="一斉停止", height=10, width=20, command=lambda: [asyncio.create_task(stop_async(m, l)) for (m, l) in zip(motors, [state_label1, state_label2, state_label3, state_label4])], bg="red", font=("", 20))
    stop_all_button.pack()

    # GUIの更新を開始
    root.mainloop()

async def play_async(motor: mc.Motor, state_label: tk.Label) -> None:
    state_label["text"] = "再生中"
    state_label["bg"] = "green"
    motor.play()

async def stop_async(motor: mc.Motor, state_label: tk.Label) -> None:
    state_label["text"] = "停止中"
    state_label["bg"] = "red"
    motor.stop()

if __name__ == "__main__":
    asyncio.run(main_async())