import tkinter as tk
import tkinter.font
import sys
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

# Set LED pins
ledRed = 18
ledGreen = 15
ledBlue = 7

GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledBlue, GPIO.OUT)

GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledGreen, GPIO.LOW)
GPIO.output(ledBlue, GPIO.LOW)

pwm_redLED = GPIO.PWM(ledRed, 100)
pwm_greenLED = GPIO.PWM(ledGreen, 100)
pwm_blueLED = GPIO.PWM(ledBlue, 100)

def update_led_brightness(pwmLED, value):
    pwmLED.ChangeDutyCycle(value)

# Start PWM
pwm_redLED.start(0)
pwm_greenLED.start(0)
pwm_blueLED.start(0)

# Create GUI window
win = tk.Tk()
win.title('5.1GUI Task')
win.geometry('350x450+700+200')

def cleanup_and_exit():
    pwm_redLED.stop()
    pwm_greenLED.stop()
    pwm_blueLED.stop()
    GPIO.cleanup()
    win.destroy()

def update_red_brightness(value):
    brightness = 100 - int(value)
    update_led_brightness(pwm_redLED, brightness)

def update_green_brightness(value):
    brightness = 100 - int(value)
    update_led_brightness(pwm_greenLED, brightness)

def update_blue_brightness(value):
    brightness = 100 - int(value)
    update_led_brightness(pwm_blueLED, brightness)

# Set up sliders for each LED
redLabel = tk.Label(win, text='Red')
redLabel.pack()
redSlider = tk.Scale(win, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: update_red_brightness(int(value)))
redSlider.pack(pady=20, padx=10)

greenLabel = tk.Label(win, text='Green')
greenLabel.pack()
greenSlider = tk.Scale(win, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: update_green_brightness(int(value)))
greenSlider.pack(pady=20, padx=10)

blueLabel = tk.Label(win, text='Blue')
blueLabel.pack()
blueSlider = tk.Scale(win, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: update_blue_brightness(int(value)))
blueSlider.pack(pady=20, padx=10)

exitButton = tk.Button(win, text="Exit", command=cleanup_and_exit, width=10, height=2)
exitButton.pack()


win.mainloop()
