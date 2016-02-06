# need this to wait
import time

# need this for UART
import Adafruit_BBIO.UART as UART

# need this to read serial buffer
import serial

# what is this?
import struct 

class UART_sensor:

	def __init__(self, UART_number):

		# initiate sensor with a UART value
		UART.setup("UART" + str(UART_number))

		# terminal number corresponds to terminal number (convenient)
		self.tty = UART_number

class CO2_sensor(UART_sensor):

	def read(self):

		# what determines this list of hexadecimel numbers?
		data = [0xfe, 0x44, 0x00, 0x08, 0x02, 0x9f, 0x25]

		# what does struct do? why 7B? what's the asterisk do?
		d = struct.pack("7B", *data)

		# is this a port to a terminal somewhere? why? why does the baudrate = 9600?
		ser = serial.Serial(port = "/dev/ttyO" + str(self.tty), baudrate = 9600)

		# this was commented out. why was it ultimately unnecessary to initialize the serial class?
		#serial.begin(9600)

		# why is this delay necessary?
		time.sleep(1)

		# wait for some buffer to be non empty?
		while(ser.inWaiting() == 0):

			# write one byte at a time? why are we writing? a request?
			ser.write(d)

			# why is this delay necessary?
			time.sleep(1)

		# read in some buffer?
		A = ser.read(ser.inWaiting())

		# third bit times 2^8 (a byte) + fourth bit divided by 10^4
		percent = (ord(A[3])*256 + ord(A[4]))/10000.0

		# never closes serial port, potential problems with that

		# return percentage, probably shouldn't be a string
		return str(percent)

class flow_meter(UART_sensor):

	def read(self):

		# need to setup UART1 at boot, does not set up immediately
		# UART1 corresponds to ttyO1 in adafruit libraries
		# to manually enable use:
		# echo BB-UART1 > /sys/devices/bone_capemgr.*/slots 
		# ls /dev/tty*   in terminal 

		# need to setup UART1 at boot, does not set up immediately
		# UART1 corresponds to ttyO1 in adafruit libraries
		# to manually enable use:
		# echo BB-UART1 > /sys/devices/bone_capemgr.*/slots 
		# ls /dev/tty*   in terminal 

		# baudrate corresponds to flow meter circuit baud rate 
		ser = serial.Serial(port = "/dev/ttyO" + str(self.tty), baudrate = 38400)

		# open serial port
		ser.open()

		# turn on LEDs. Green = power, red = instruction received/data transmit, 
		# amber = one rotation of meter blades
		ser.write("L1\r")

		# why is this delay necessary?
		time.sleep(.4)

		# write model number TurboFlow 226000
		ser.write("T1\r")

		# why is this delay neccesary?
		time.sleep(0.4)

		# return num of chars in receive buffer
		num = ser.inWaiting()

		# read Turboflow
		model_num = ser.read(num)

		# why is this delay necessary?
		time.sleep(0.4)

		# what are we writing?
		ser.write("R\r")

		# why is this delay necessary?
		time.sleep(2)

		# return num of chars in receive buffer
		num = ser.inWaiting()

		# returns entire serial buffer?
		single_flow_reading = ser.read(num)
		
		# is this just a diagnostic thing?
		# print "Model Num is ", model_num

		# close serial port
		ser.close()

		# flow rate [total vol] [LPM] [LPH]
		return single_flow_reading

# flow meters
flow_meter = {1: flow_meter(1),
	      2: flow_meter(4)}

# CO2 sensor
CO2 = CO2_sensor(5)