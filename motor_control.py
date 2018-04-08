
import RPi.GPIO as GPIO
import time


LEFT_MOTOR_PIN = 23
RIGHT_MOTOR_PIN = 18

SLEEP_TIMER = 0.25


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LEFT_MOTOR_PIN, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_PIN, GPIO.OUT)


def go_straight():
	# print("Going straight")

	GPIO.output(LEFT_MOTOR_PIN, GPIO.HIGH)
	GPIO.output(RIGHT_MOTOR_PIN, GPIO.HIGH)

	time.sleep(SLEEP_TIMER)
	stop()

def go_left():
	# print("To the left!")

	GPIO.output(LEFT_MOTOR_PIN, GPIO.LOW)
	GPIO.output(RIGHT_MOTOR_PIN, GPIO.HIGH)

	time.sleep(SLEEP_TIMER)
	stop()


def go_right():
	# print("To the right!")

	GPIO.output(LEFT_MOTOR_PIN, GPIO.HIGH)
	GPIO.output(RIGHT_MOTOR_PIN, GPIO.LOW)

	time.sleep(SLEEP_TIMER)
	stop()

def stop():
	# print("Stopping")

	GPIO.output(LEFT_MOTOR_PIN, GPIO.LOW)
	GPIO.output(RIGHT_MOTOR_PIN, GPIO.LOW)

