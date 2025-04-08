class Device:
    def __init__(self):
        self.power = 100

    def turn_on(self):
        print('включен')

class NetworkedDevice(Device):
    def __init__(self):
        super().__init__()
        self.ip_adress = '4.224.197.46'

    def connect(self):
        print('подключен')

class PortableDevice(Device):
    def __init__(self):
        super().__init__()
        self.battery_lvl = 100

    def charge(self):
        print('устройство заряжается')

class SmartPhone(NetworkedDevice, PortableDevice):
    pass

    def call(self):
        print('Соединение')

    def turn_on(self):
        Device.turn_on(self)

a = SmartPhone()
a.charge()
a.turn_on()
a.connect()
a.call()
