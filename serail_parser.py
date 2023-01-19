import serial
import argparse
import time, datetime


if __name__ == '__main__':

	parser = argparse.ArgumentParser(
                    prog = 'Serail reader',
                    description = 'Template for serial parser',
                    epilog = 'Author: Yuan-Wei Pi :)')

	
	t = datetime.datetime.now()
	today = f"{t.year}{t.month:02d}{t.day}"
	
	parser.add_argument('-b', '--baudrate', default=9600, type=int, help='baudrate, default=9600')
	parser.add_argument('-p', '--port', default="/dev/ttyUSB0", help='device port, default=/dev/ttyUSB0')
	parser.add_argument('-r', '--rate', default=1, type=int, help='sample rate, default=1sec')
	parser.add_argument('-o', '--output_file', default=f"logfile_{today}.log", help='default=slogfile_today_date.log')
	parser.add_argument('-path', default="", help='default: local path')

	args = parser.parse_args()

	logfile = args.path + "/" + args.output_file
	port = args.port
	br = args.baudrate
	rate = args.rate
	ser = serial.Serial(port=port, baudrate=br)


	while True:
		t = str(datetime.datetime.now())
		line = ser.readline().decode('utf-8')   # read a '\n' terminated line
		
		print(f"[{t}] {line}")
		
		with open(logfile, "a") as ofile:
			ofile.write(f"[{t}] {line}")

		time.sleep(rate)
