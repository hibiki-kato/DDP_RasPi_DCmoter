import tkinter as tk
import MoterClass as mc
from typing import List, Tuple
import asyncio

async def main_async():
    # pinの設定
    pins: List[int] = [17, 18, 27, 22]

    # モータークラスのインスタンス化
    motors: List[mc.Motor] = []
    for i in range(4):
        motors.append(mc.Motor(pins[i], "instruction.csv"))

    # GUIの作成
    root: tk.Tk = tk.Tk()
    root.title("一教祭2023")

    # ボタンとラベルの作成と配置
    buttons: List[Tuple[tk.Button, tk.Button, tk.Label]] = []
    state_labels: List[tk.Label] = []  # Store the state_label widgets in a list
    for motor in motors:
        frame: tk.Frame = tk.Frame(root)
        frame.pack(side=tk.LEFT, padx=10)

        state_label: tk.Label = tk.Label(frame, height=10, width=20, text="停止中", bg="red", font=("", 20))
        state_label.pack()

        play_button: tk.Button = tk.Button(frame, text="再生", height=10, width=20, command=lambda m=motor, l=state_label: asyncio.create_task(play_async(m, l)), bg="green", font=("", 20))
        play_button.pack()

        stop_button: tk.Button = tk.Button(frame, text="停止", height=10, width=20, command=lambda m=motor, l=state_label: asyncio.create_task(stop_async(m, l)), bg="red", font=("", 20))
        stop_button.pack()

        buttons.append((play_button, stop_button, state_label))
        state_labels.append(state_label)  # Add the state_label widget to the list

    # 下に一斉再生と一斉停止のボタンを作成
    frame: tk.Frame = tk.Frame(root)
    frame.pack(side=tk.LEFT, padx=10)
    play_all_button: tk.Button = tk.Button(frame, text="一斉再生", height=10, width=20, command=lambda: [asyncio.create_task(play_async(m, l)) for (m, l) in zip(motors, state_labels)], bg="green", font=("", 20))
    play_all_button.pack()
    stop_all_button: tk.Button = tk.Button(frame, text="一斉停止", height=10, width=20, command=lambda: [asyncio.create_task(stop_async(m, l)) for (m, l) in zip(motors, state_labels)], bg="red", font=("", 20))
    stop_all_button.pack()

    # GUIの更新を強制する関数
    def update_gui():
        for motor, state_label in zip(motors, state_labels):
            if motor.is_playing:
                state_label["text"] = "再生中"
                state_label["bg"] = "green"
            else:
                state_label["text"] = "停止中"
                state_label["bg"] = "red"
        root.after(100, update_gui)

    # GUIの更新を開始
    root.after(100, update_gui)
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