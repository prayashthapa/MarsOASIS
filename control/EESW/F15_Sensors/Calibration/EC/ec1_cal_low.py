# This script calibrates low point (dual pt calibration)
import smbus #import smbus library
import time
bus=smbus.SMBus(2) #assign an object to the SMBus class and mention the interface number
#bus.write_i2c_block_data(0x64,0x43,[0x61,0x6c,0x2c,0x3f]) # Cal, ?
#results=bus.read_i2c_block_data(0x64,0x52) #get calibration info
#print results #print data
# bus.write_i2c_block_data(0x64,0x43,[0x61,0x6C,0x2C,0x63,0x6C,0x65, 0X61, 0x72 ]) #Cal, clear
# time.sleep(5.4)
# results=bus.read_i2c_block_data(0x64,0x52)
#time.sleep(5)
bus.write_i2c_block_data(0x66,0x43,[0x61,0x6C,0x2C,0x6C, 0x6F, 0x77, 0x2C, 0x31, 0x32, 0x38, 0x38, 0x30]) #Cal, low, n
time.sleep(5)
results=bus.read_i2c_block_data(0x66,0x52) #read cal info
print results #print data