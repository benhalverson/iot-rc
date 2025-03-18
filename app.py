import pigpio
import time
import datetime

ESC_GPIO_PIN = 18
SERVO_GPIO_PIN = 17
LOG_FILE_PATH = "/home/pi/pwn_log.txt"
ERROR_LOG_FILE_PATH = "/home/pi/pwn_error_log.txt"

pi = pigpio.pi()

if not pi.connected:
    exit()

def log_pwn(gpio: int, level: int, tick: int):
    print(f"GPIO {gpio} changed to {level} at {tick}")
    if level == 1:
      pulse_width = pigpio.tickDiff(log_pwn.lask_tick[gpio], tick)

      with open(LOG_FILE_PATH, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - GPIO {gpio} changed to {level} at {tick} with pulse width {pulse_width}\n")

      log_pwn.lask_tick[gpio] = tick

log_pwn.lask_tick = {ESC_GPIO_PIN: 0, SERVO_GPIO_PIN: 0}

pi.set_mode(ESC_GPIO_PIN, pigpio.INPUT)
pi.set_mode(SERVO_GPIO_PIN, pigpio.INPUT)

pi.callback(ESC_GPIO_PIN, pigpio.EITHER_EDGE, log_pwn)
pi.callback(SERVO_GPIO_PIN, pigpio.EITHER_EDGE, log_pwn)

try:
    while True:
        time.sleep(60)
except Exception as e:
    with open(ERROR_LOG_FILE_PATH, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {e}\n")
