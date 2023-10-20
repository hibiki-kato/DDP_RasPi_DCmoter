import time
import tkinter.ttk as ttk

class MotorControl:
    def __init__(self, motor: Moter, progressbar: ttk.Progressbar):
        self.motor = motor
        self.progressbar = progressbar
        self.playing = False
        self.progressbar["maximum"] = self.motor.instructions[-1][0] + 1

    def run_motor(self):
        if not self.playing:
            self.playing = True
            self.progressbar["value"] = 0
            self.motor.run()
            self.playing = False

    def stop_motor(self):
        self.motor.stop()

    def update_progressbar(self):
        if self.playing:
            self.progressbar["value"] = self.motor.current_step
            if self.motor.current_step >= self.motor.instructions[-1][0]:
                self.playing = False

def main() -> None:
    # GPIOピンの設定
    motor_pins: List[int] = [18, 19, 20, 21]  # モーターのGPIOピン番号
    moter1: Moter = MoterClass.Motor(motor_pins[0], "instruction.csv")
    moter2: Moter = MoterClass.Motor(motor_pins[1], "instruction.csv")
    moter3: Moter = MoterClass.Motor(motor_pins[2], "instruction.csv")
    moter4: Moter = MoterClass.Motor(motor_pins[3], "instruction.csv")

    # GUIの作成
    root: tk.Tk = tk.Tk()

    # モーターコントロールの作成
    motor_controls = []
    for motor in [moter1, moter2, moter3, moter4]:
        frame = tk.Frame(root)
        frame.pack(side=tk.LEFT, padx=10, pady=10)
        label = tk.Label(frame, text=f"Motor {motor_pins.index(motor.pin) + 1}")
        label.pack()
        progressbar = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
        progressbar.pack()
        motor_control = MotorControl(motor, progressbar)
        motor_controls.append(motor_control)
        button_frame = tk.Frame(frame)
        button_frame.pack(pady=10)
        run_button = tk.Button(button_frame, text="Run", command=motor_control.run_motor)
        run_button.pack(side=tk.LEFT, padx=5)
        stop_button = tk.Button(button_frame, text="Stop", command=motor_control.stop_motor)
        stop_button.pack(side=tk.LEFT, padx=5)

    # プログレスバーの更新
    def update_progressbars():
        for motor_control in motor_controls:
            motor_control.update_progressbar()
        root.after(10, update_progressbars)

    root.after(10, update_progressbars)
    root.mainloop()
