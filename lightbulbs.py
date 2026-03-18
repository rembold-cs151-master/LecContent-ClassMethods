class SmartBulb:
    def __init__(self, room_name):
        self.room_name = room_name
        self._is_on = False
        self._brightness = 0  # Percent between 0 and 100


if __name__ == "__main__":
    kitchen = SmartBulb("Kitchen")
    lroom = SmartBulb("Living Room")
    broom = SmartBulb("Bathroom")
    all = [kitchen, lroom, broom]

    ## Part A Testing
    # print(kitchen._is_on)
    # kitchen.turn_on()
    # print(kitchen._is_on)
    # kitchen.turn_on()
    # print(kitchen._is_on)
    # kitchen.turn_off()
    # print(kitchen._is_on)
    # kitchen.turn_off()
    # print(kitchen._is_on)

    ## Part B Testing, uncomment when ready
    # broom.turn_on()
    # print(all)

    ## Part C Testing, uncomment when ready
    # print(kitchen)
    # kitchen.toggle()
    # print(kitchen)
    # kitchen.toggle()
    # print(kitchen)
    # kitchen.set_brightness(50)
    # kitchen.toggle()
    # print(kitchen)

    ## Part D Testing, uncomment when ready
    # print(lroom)
    # lroom.set_brightness(50)
    # print(lroom)
    # lroom.set_brightness(-50)
    # print(lroom)
    # lroom.set_brightness(500)
    # print(lroom)
