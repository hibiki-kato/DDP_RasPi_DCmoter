import csv
import time
import RPi.GPIO as GPIO
from typing import List

class Motor:
    def __init__(self, pin: int, filepath: str) -> None:
        """
        Initialize the Motor class.

        Args:
        - pin (int): The GPIO pin number to which the motor is connected.
        - filepath (str): The path to the CSV file containing the motor instructions.
        """
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 1000)
        self.pwm.start(0) # 0% duty cycle
        
        self.instructions = self.read_motor_instructions(filepath)

    def set_duty_cycle(self, duty_cycle: float) -> None:
        """
        Set the duty cycle of the PWM signal.

        Args:
        - duty_cycle (float): The duty cycle of the PWM signal.
        """
        self.pwm.ChangeDutyCycle(duty_cycle)

    def stop(self) -> None:
        """
        Stop the motor.
        """
        self.pwm.stop()

    def cleanup(self) -> None:
        """
        Clean up the GPIO pins.
        """
        GPIO.cleanup()

    def drive_for_time(self, n: float, v: float) -> None:
        """
        Drive the motor for a specified amount of time.

        Args:
        - n (float): The duration for which the motor should be driven.
        - v (float): The duty cycle of the PWM signal.
        """
        self.set_duty_cycle(v)
        time.sleep(n)
        self.stop()

    def read_motor_instructions(self, filepath: str) -> List[List[float]]:
        """
        Read motor instructions from a CSV file.

        Args:
        - filepath (str): The path to the CSV file.

        Returns:
        - A list of lists containing the motor instructions.
        """
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            instructions = []
            for row in reader:
                instructions.append([float(x) for x in row])
        return instructions

    def play(self) -> None:
        """
        Run the motor according to the instructions.

        Args:
        - instructions (List[List[float]]): A list of lists containing the motor instructions.
        """
        start_time = time.time()
        for instruction in self.instructions:
            timestamp = instruction[0]
            duration = instruction[1]
            duty_cycle = instruction[2]
            while time.time() - start_time < timestamp:
                pass
            self.drive_for_time(duration, duty_cycle)

