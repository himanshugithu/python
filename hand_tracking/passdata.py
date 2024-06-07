import serial
arduinoData = serial.Serial("com3",9600)

while True:
    cmd = input("enter no")
    cmd =  cmd+"\r"
    arduinoData.write(cmd.encode())
    print(cmd)