
def gpio_list_fmt_cb(val, read, lst, index=0):
    if read:
        return lst[1 if int(val) else 0]
    else:
        return '1' if lst.index(val) else '0'
    
def gpio_cmd_cb(dev, cmd, val=None, index=0):
    gpio_list = dev['gpio'].split(',')
    if index >= len(gpio_list):
        return
    gpio = gpio_list[index]
    if val != None:
        return 'gpio %s %s' % (gpio, val)
    else:
        return 'gpio %s odsr' % gpio
    
def spi_efc_cmd_cb(dev, cmd, val=None, ncpha='1', cpha=None, cpol='1'):
    if val != None:
        if cpha:
            return 'spi %s 0x%s %s %s' % (dev['spi'], val, cpha, cpol)
        else:
            return 'spi %s 0x%s %s %s' % (dev['spi'], val, ncpha, cpol)
    else:
        r = 0
        if cmd[0] == 'R':
            r = int(cmd[1:])
        return 'efc spi %s %d' % (dev['spi'], r)

def strip0x_fmt_cb(val, read=True, sz=8):
    if val[0:2].lower() == '0x':
        val = val[2:]
    if sz != 8 and len(val) > sz:
        val = val[-sz:]
    return val

def mdio_cmd_cb(dev, cmd, val=None):
    r = cmd[1:]
    if val != None:
        return 'mdio %s 0x%s' % (r, val)
    else:
        return 'mdio %s' % r

