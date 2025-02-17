import pprint

HEADER_BRIDGE = 1
HEADER_NORMAL = 2

class PCIe_Endpoint:
    def __init__(self):
        self.header = HEADER_NORMAL

    def read(self,offset):
        if offset == 0x00:
            return 12345678
        return 0xFFFFFFFF

    def write(self,offset,value):
        pass

class PCIe_Bridge:
    def __init__(self,devs):
        self.header = HEADER_BRIDGE
        self.devs = devs
        self.command = 0
        self.sub = 0
        self.sec = 0
        self.pri = 0
        self.mem_limit = 0
        self.mem_base = 0

    def route(self,b,d,f):
        if self.sec == b:
            if d < len(self.devs):
                dev = self.devs[d]
                if dev: return dev
        else:
            for dev in self.devs:
                if (dev.sec <= b) and (b <= dev.sub):
                    return dev.route(b,d,f)
        return None

    def read(self,offset):
        if offset == 0x00:
            return 12345678
        elif offset == 0x04:
            return self.command
        elif offset == 0x0C:
            return HEADER_BRIDGE << 16
        elif offset == 0x18:
            return (self.sub << 16) | (self.sec << 8) | self.pri
        elif offset == 0x20:
            return (self.mem_limit << 16) | self.mem_base
        return 0xFFFFFFFF
    
    def write(self,offset,value):
        if offset == 0x04:
            self.command = value & 0xFFFF
        elif offset == 0x18:
            self.sub = (value >> 16) & 0xFF
            self.sec = (value >>  8) & 0xFF
            self.pri = (value >>  0) & 0xFF
        elif offset == 0x20:
            self.mem_limit = (value >> 16) & 0xFFFF
            self.mem_base  = (value >>  0) & 0xFFFF

ep_0 = PCIe_Endpoint()
ep_1 = PCIe_Endpoint()
ep_2 = PCIe_Endpoint()
ep_3 = PCIe_Endpoint()
ep_4 = PCIe_Endpoint()
ep_5 = PCIe_Endpoint()
ep_6 = PCIe_Endpoint()

sw_0_d_0 = PCIe_Bridge([ep_0])
sw_0_d_1 = PCIe_Bridge([ep_1])
sw_0_u   = PCIe_Bridge([sw_0_d_0,sw_0_d_1])
sw_2_u   = PCIe_Bridge([ep_3,ep_4,ep_5])
sw_1_d_0 = PCIe_Bridge([ep_2])
sw_1_d_1 = PCIe_Bridge([sw_2_u])
sw_1_d_2 = PCIe_Bridge([ep_6])
sw_1_u   = PCIe_Bridge([sw_1_d_0,sw_1_d_1,sw_1_d_2])
root_d_0 = PCIe_Bridge([sw_0_u])
root_d_1 = PCIe_Bridge([sw_1_u])
root_u   = PCIe_Bridge([root_d_0, root_d_1])

def pcie_config_read(b,d,f,offset):
    if b == -1:
        dev = root_u
    else:
        dev = root_u.route(b,d,f)

    if dev:
        return dev.read(offset)
    else: 
        return 0xFFFFFFFF

def pcie_config_write(b,d,f,offset,value):
    if b == -1:
        dev = root_u
    else:
        dev = root_u.route(b,d,f)

    if dev:
        dev.write(offset,value)

def pcie_enum():
    
    bus = -1 # imaginary host/pci bridge bus
    stack = [(bus,0,0)]

    while len(stack) > 0:
        b,d,f = stack.pop()
        vendor_device_id = pcie_config_read(b,d,f,0x00)
        if vendor_device_id == 0xFFFFFFFF: continue
        print(f"{b:02X}:{d:02X}:{f:02X}")

        header = (pcie_config_read(b,d,f,0x0C) >> 16) & 0xFF
        if header == HEADER_BRIDGE:
            reg_18h = pcie_config_read(b,d,f,0x18)
            if (reg_18h & 0x00FFFF00) != 0: # sub/sec not zero on second pass
                reg_18h &= 0xFF00FFFF
                reg_18h |= (bus & 0xFF) << 16
                pcie_config_write(b,d,f,0x18,reg_18h)
            else:
                bus += 1
                reg_18h &= 0xFF0000FF
                reg_18h |= (bus & 0xFF) << 8
                reg_18h |= 0x00FF0000
                pcie_config_write(b,d,f,0x18,reg_18h)
                stack.append((b,d,f))
                for dev in reversed(range(3)):
                    reg_18h = pcie_config_read(bus,dev,0,0x18)
                    reg_18h &= 0xFFFFFF00
                    reg_18h |= bus
                    pcie_config_write(bus,dev,0,0x18,reg_18h)
                    stack.append((bus,dev,0))

def show(dev,depth):
    print(depth * "   ",end="")
    if dev.header == HEADER_BRIDGE:
        print(f"{dev.pri} {dev.sec} {dev.sub}")
        for child in dev.devs:
            show(child, depth + 1)
    else:
        print("endpoint")

# pcie_enum_recursive(-1,-1,root_u,0)
# pprint.pprint(root_u)

pcie_enum()
show(root_u,0)