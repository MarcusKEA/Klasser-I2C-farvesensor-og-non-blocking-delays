from machine import Pin
import dht

class Sensor:
    def __init__(self) -> None:
        self.temp = 0
        self. moist = 0

    def set_temp(self, val:int):
        self.temp = val

    def set_moist(self, val:int):
        self.moist = val

dhtsensor = dht.DHT11(Pin(14))
mySensor = Sensor()



def main():
    dhtsensor.measure()
    mySensor.set_moist(dhtsensor.temperature())
    mySensor.set_temp(dhtsensor.humidity())
    
    print(mySensor.temp, "Celcius")
    print(mySensor.moist, "Moist")

if __name__ == "__main__":
    main()