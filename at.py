import serial

"""

\dev\ttyACM0
"""

class AT_Master:

    def __init__(self, port):
        self.__serial = serial.Serial(port, 9600, timeout=1)

    def __at(self, cmd=None, args=None):
        self.__serial.reset_output_buffer()
        if cmd is None:
            self.__serial.write(b'AT\r\n')
        else:
            if args is None:
                self.__serial.write(bytes('AT+%s\r\n' % cmd, 'UTF-8'))
            else:
                self.__serial.write(bytes('AT+%s=%s' % (cmd, args), 'UTF-8'))

    def close(self):
        self.__serial.close()

    def purge(self):
        self.__serial.reset_output_buffer()
        return self.__serial.read_all().decode('UTF-8')

    def ping(self):
        self.__at()
        return self.purge()

    def join(self):
        self.__at("JOIN")

    def join_status(self):
        self.__at("NJS", "?")
        return self.purge()

    def send_text(self, port, text):
        self.__at("SEND", str(port) + ":" + text)

    def send_bytes(self, port, data):
        self.__at("SENDB", str(port) + ":" + data)