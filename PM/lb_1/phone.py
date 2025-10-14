#ПРОБЛЕМА АЛМАЗА

class Device:
    def __init__(self, power):
        self.power = power

    def turn_on(self):
        print('Enabling')


class NetworkedDevice(Device):
    def __init__(self, power, ip_address):
        super().__init__(power)
        self.ip_address = ip_address

    def connect(self):
        print('Internet connection')


class PortableDevice(Device):
    def __init__(self, power, battery_level):
        super().__init__(power)
        self.battery_level = battery_level

    def charge(self):
        print('charging')


class SmartPhone(NetworkedDevice, PortableDevice):
    def __init__(self, power, ip_address, battery_level):
        NetworkedDevice.__init__(self, power, ip_address)
        PortableDevice.__init__(self, power, battery_level)

    def call(self):
        print('сalling')


#РЕШЕНИЕ ПРОБЛЕМЫ АЛМАЗА

class Device:
    def __init__(self, power):
        self.power = power

    def turn_on(self):
        print('Enable')


class NetworkedDevice(Device):
    def __init__(self, power, ip_address):
        super().__init__(power)
        self.ip_address = ip_address

    def connect(self):
        print('Internet connection')


class PortableDevice(Device):
    def __init__(power, battery_level):
        super().__init__(power)
        self.battery_level = battery_level

    def charge(self):
        print('charging')


class SmartPhone(NetworkedDevice, PortableDevice):
    def __init__(self, power, ip_address, battery_level):
        NetworkedDevice.__init__(self, power, ip_address)
        PortableDevice.__init__(self, power, battery_level)

    def call(self):
        print('calling')

