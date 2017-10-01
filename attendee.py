#!/usr/bin/python


from keyboard_alike import reader


if __name__ == "__main__":
    r = reader.Reader(0xffff, 0x0035, 4, 4, should_reset=True, debug=True)

    dev = r._device
    for cfg in dev:
        sys.stdout.write(str(cfg.bConfigurationValue) + '\n')
        for intf in cfg:
            sys.stdout.write('\t' + \
                             str(intf.bInterfaceNumber) + \
                             ',' + \
                             str(intf.bAlternateSetting) + \
                             '\n')
            for ep in intf:
                sys.stdout.write('\t\t' + \
                                 str(ep.bEndpointAddress) + \
                                 '\n')

    print 'Created reader'
    r.initialize()
    print 'Initialized'
    print(r.read().strip())
    print 'Read'
    r.disconnect()
    print 'Disconnected'

