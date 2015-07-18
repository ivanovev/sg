
from collections import OrderedDict as OD
from ..regs import RegsData, manyregs_cb
from .callbacks import mdio_cmd_cb
from util.callbacks import util_io_cb
from util.columns import *

hex_data = '''
R00||Basic Control
R01||Basic Status
R02||PHY Identifier 1
R03||PHY Identifier 2
R04||Auto Negotiation Advertisement
R05||Auto Negotiation Link Partner Ability
R06||Auto Negotiation Expansion
R16||Silicon Revision
R17||Mode Control/Status
R18||Special Modes
R26||Symbol Error Counter
R27||Special Control/Status Indications
R28||Special Internal Testability Controls
R29||Interrupt Source Flags
R30||Interrupt Mask
R31||PHY Special Control/Status
'''

binregs_str = '''
R00|15|Reset|0|1 = software reset. Bit is self-clearing.
R00|14|Loopback|0|1 = loopback mode,;0 = normal operation
R00|13|Speed Select|0|1 = 100Mbps,;0 = 10Mbps.;Ignored if Auto Negotiation is enabled (0.12 = 1).
R00|12|AutoNegotiation Enable|0|1 = enable auto-negotiate process;(overrides 0.13 and 0.8);0 = disable auto-negotiate process
R00|11|Power Down|0|1 = General power down mode,;0 = normal operation
R00|10|Isolate|0|1 = electrical isolation of transceiver from MII;0 = normal operation
R00|9|Restart AutoNegotiate|0|1 = restart auto-negotiate process;0 = normal operation. Bit is self-clearing.
R00|8|Duplex Mode|0|1 = Full duplex,;0 = Half duplex.;Ignored if Auto Negotiation is enabled (0.12 = 1).
R00|7|Collision Test|0|1 = enable COL test,;0 = disable COL test
R00|0|Reserved|1|RO
R01|15|100Base-T4|0|
R01|14|100Base-TX Full Duplex|0|1 = TX with full duplex,;0 = no TX full duplex ability
R01|13|100Base-TX Half Duplex|0|1 = TX with half duplex,;0 = no TX half duplex ability
R01|12|10Base-T Full Duplex|0|1 = 10Mbps with full duplex;0 = no 10Mbps with full duplex ability
R01|11|10Base-T Half Duplex|0|1 = 10Mbps with half duplex;0 = no 10Mbps with half duplex ability
R01|6|Reserved|1|
R01|5|Auto-Negotiate Complete|0|1 = auto-negotiate process completed;0 = auto-negotiate process not completed
R01|4|Remote Fault|0|
R01|3|Auto-Negotiate Ability|0|
R01|2|Link Status|0|
R01|1|Jabber Detect|0|
R01|0|Extended Capabilities|0|
R02|0|PHY ID Number|1|Assigned to the 3rd through 18th bits of the;Organizationally Unique Identifier (OUI), respectively.;OUI=00800Fh
R03|10|PHY ID Number|1|
R03|4|Model Number|1|
R03|0|Revision Number|1|
R04|15|Next Page|0|
R04|14|Reserved|1|
R04|13|Remote Fault|0|
R04|12|Reserved|1|
R04|10|Pause Operation|0|00 = No PAUSE;01= Symmetric PAUSE;10= Asymmetric PAUSE toward link partner;11 = Both Symmetric PAUSE and Asymmetric;PAUSE toward local device
R04|9|100Base-T4|0|1 = T4 able,;0 = no T4 ability;This Phy does not support 100Base-T4
R04|8|100Base-TX Full Duplex|0|1 = TX with full duplex,;0 = no TX full duplex ability
R04|7|100Base-TX|0|1 = TX able,;0 = no TX ability
R04|6|10Base-T Full Duplex|0|1 = 10Mbps with full duplex;0 = no 10Mbps with full duplex ability
R04|5|10Base-T|0|1 = 10Mbps able,;0 = no 10Mbps ability
R04|0|Selector Field|0|[00001] = IEEE 802.3
R05|15|Next Page|0|1 = “Next Page” capable,;0 = no “Next Page” ability;This Phy does not support next page ability.
R05|14|Acknowledge|0|1 = link code word received from partner;0 = link code word not yet received
R05|13|Remote Fault|0|1 = remote fault detected,;0 = no remote fault
R05|11|Reserved|1|RO
R05|10|Pause Operation|0|1 = Pause Operation is supported by remote MAC,;0 = Pause Operation is not supported by remote MAC
R05|9|100Base-T4|0|1 = T4 able,;0 = no T4 ability.;This Phy does not support T4 ability.
R05|8|100Base-TX Full Duplex|0|1 = TX with full duplex,;0 = no TX full duplex ability
R05|7|100Base-TX|0|1 = TX able,;0 = no TX ability
R05|6|10Base-T Full Duplex|0|1 = 10Mbps with full duplex;0 = no 10Mbps with full duplex ability
R05|5|10Base-T|0|1 = 10Mbps able,;0 = no 10Mbps ability
R05|0|Selector Field|0|[00001] = IEEE 802.3
R06|5|Reserved|1|RO
R06|4|Parallel Detection Fault|0|1 = fault detected by parallel detection logic;0 = no fault detected by parallel detection logic
R06|3|Link Partner Next Page Able|0|1 = link partner has next page ability;0 = link partner does not have next page ability
R06|2|Next Page Able|0|1 = local device has next page ability;0 = local device does not have next page ability
R06|1|Page Received|0|1 = new page received;0 = new page not yet received
R06|0|Link Partner AutoNegotiation Able|0|1 = link partner has auto-negotiation ability;0 = link partner does not have auto-negotiation ability
R16|10|Reserved|1|RO
R16|6|Silicon Revision|0|Four-bit silicon revision identifier.
R16|0|Reserved|1|RO
R17|14|Reserved|1|
R17|13|EDPWRDOWN|0|
R17|12|Reserved|1|
R17|11|LOWSQEN|0|The Low_Squelch signal is equal to LOWSQEN AND;EDPWRDOWN.;Low_Squelch = 1 implies a lower threshold;(more sensitive).;Low_Squelch = 0 implies a higher threshold;(less sensitive).
R17|10|MDPREBP|0|Management Data Preamble Bypass:;0 – detect SMI packets with Preamble;1 – detect SMI packets without preamble
R17|9|FARLOOPBACK|0|Force the module to the FAR Loop Back mode, i.e. all;the received packets are sent back simultaneously (in 100Base-TX only).;This bit is only active in RMII mode.
R17|7|Reserved|1|Write as 0, ignore on read.
R17|6|ALTINT|0|Alternate Interrupt Mode.;0 = Primary interrupt system enabled (Default).;1 = Alternate interrupt system enabled.;See Section 5.2, "Interrupt Management," on page 47.
R17|4|Reserved|1|Write as 0, ignore on read.
R17|3|PHYADBP|0|1 = PHY disregards PHY address in SMI access;write.
R17|2|Force Good Link Status|0|0 = normal operation;;1 = force 100TX- link active;
R17|1|ENERGYON|0|
R17|0|Reserved|1|This bit should be set only during lab testing
R18|15|Reserved|1|Write as 0, ignore on read.
R18|14|MIIMODE|0|MII Mode: set the mode of the digital interface, as;described in Section 5.3.9.3:;0 – MII interface.;1 – RMII interface
R18|8|Reserved|1|Write as 0, ignore on read.
R18|5|Mode|0|Transceiver Mode of operation.
R18|0|PHYAD|0|PHY Address.
R26|0|Sym_Err_Cnt|0|100Base-TX receiver-based error register
R27|15|AMDIXCTRL|0|HP Auto-MDIX control;0 - Auto-MDIX enable;1 - Auto-MDIX disabled (use 27.13 to control channel)
R27|14|Reserved|1|Reserved
R27|13|CH_SELECT|0|Manual Channel Select;0 - MDI -TX transmits RX receives;1 - MDIX -TX receives RX transmits
R27|12|Reserved|1|Write as 0. Ignore on read.
R27|5|Reserved|1|Write as 0. Ignore on read.
R27|4|XPOL|0|Polarity state of the 10Base-T:;0 - Normal polarity;1 - Reversed polarity
R27|0|Reserved|1|Reserved
R28|0|Reserved|1|Do not write to this register. Ignore on read.
R29|8|Reserved|1|
R29|7|INT7|0|1 = ENERGYON generated;0 = not source of interrupt
R29|6|INT6|0|1 = Auto-Negotiation complete;0 = not source of interrupt
R29|5|INT5|0|1 = Remote Fault Detected;0 = not source of interrupt
R29|4|INT4|0|1 = Link Down (link status negated);0 = not source of interrupt
R29|3|INT3|0|1 = Auto-Negotiation LP Acknowledge;0 = not source of interrupt
R29|2|INT2|0|1 = Parallel Detection Fault;0 = not source of interrupt
R29|1|INT1|0|
R29|0|Reserved|1|
R30|8|Reserved|1|Write as 0; ignore on read.
R30|1|Mask Bits|0|1 = interrupt source is enabled;0 = interrupt source is masked
R30|0|Reserved|1|Write as 0; ignore on read
R31|13|Reserved|1|Write as 0, ignore on read.
R31|12|Autodone|0|Auto-negotiation done indication:;0 = Auto-negotiation is not done or disabled (or not;active);1 = Auto-negotiation is done
R31|10|Reserved|1|Write as 0, ignore on Read.
R31|7|GPO[2:0]|0|General Purpose Output connected to signals;GPO[2:0]
R31|6|Enable 4B5B|0|0 = Bypass encoder/decoder.;1 = enable 4B5B encoding/decoding.;MAC Interface must be configured in MII mode.
R31|5|Reserved|1|Write as 0, ignore on Read.
R31|2|Speed Indication|0|HCDSPEED value:;[001]=10Mbps Half-duplex;[101]=10Mbps Full-duplex;[010]=100Base-TX Half-duplex;[110]=100Base-TX Full-duplex
R31|1|Reserved|1|Write as 0; ignore on Read
R31|0|Scramble Disable|0|0 = enable data scrambling;1 = disable data scrambling,
'''

def columns():
    return get_columns([c_ip_addr])

def get_menu(dev):
    return OD([('Registers', manyregs_cb)])

def get_regs(dev):
    data = RegsData(sz=16, io_cb=util_io_cb)
    data.add_hex_data(hex_data, cmd_cb=mdio_cmd_cb)
    data.add_bin_data(binregs_str)
    data.columns = 4
    return data

