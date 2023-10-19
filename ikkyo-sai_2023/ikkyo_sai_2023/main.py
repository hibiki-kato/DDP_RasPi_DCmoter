import RPi.GPIO as GPIO
import tkinter as tk
from typing import List, Tuple

def main() -> None:
    # GPIOピンの設定
    motor_pins: List[int] = [18, 19, 20, 21]  # モーターのGPIOピン番号
    GPIO.setmode(GPIO.BCM)
    for pin in motor_pins:
        GPIO.setup(pin, GPIO.OUT)

    # PWMの設定
    frequency: int = 1000  # PWMの周波数
    duty_cycle: int = 50  # デューティサイクル（0〜100の範囲で指定）
    pwm_list: List[GPIO.PWM] = [GPIO.PWM(pin, frequency) for pin in motor_pins]
    for pwm in pwm_list:
        pwm.start(duty_cycle)

    # GUIの作成
    root: tk.Tk = tk.Tk()

    # ボタンの作成と配置
    buttons: List[Tuple[tk.Button, tk.Button, tk.Button]] = []
    for i in range(4):
        frame: tk.Frame = tk.Frame(root)
        frame.pack(side=tk.LEFT, padx=10)

        play_button: tk.Button = tk.Button(frame, text="再生", command=lambda i=i: play_motor(i))
        play_button.pack()

        pause_button: tk.Button = tk.Button(frame, text="一時停止", command=lambda i=i: pause_motor(i))
        pause_button.pack()

        reset_button: tk.Button = tk.Button(frame, text="リセット", command=lambda i=i: reset_motor(i))
        reset_button.pack()

        buttons.append((play_button, pause_button, reset_button))

    # 終了処理
    def on_closing() -> None:
        for pwm in pwm_list:
            pwm.stop()
        GPIO.cleanup()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


# モーターの制御関数
def play_motor(index: int) -> None:
    pwm_list[index].ChangeDutyCycle(duty_cycle)

def pause_motor(index: int) -> None:
    pwm_list[index].ChangeDutyCycle(0)

def reset_motor(index: int) -> None:
    pwm_list[index].ChangeDutyCycle(0)
    
if __name__ == "__main__":
    main()