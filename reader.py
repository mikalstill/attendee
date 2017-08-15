#!/usr/bin/python


from keyboard_alike import reader


if __name__ == "__main__":
    reader = reader.Reader(0xffff, 0x0035, 84, 16, should_reset=False,
                           debug=False)
    reader.initialize()
    print(reader.read().strip())
    reader.disconnect()

