
from collections import OrderedDict as OD
from ..regs import RegsData, manyregs_cb
from .callbacks import mdio_cmd_cb, strip0x_fmt_cb
from util.columns import get_columns

hex_data = '''
R0||Basic Control
R1||Basic Status
R2||PHY Identifier I
R3||PHY Identifier II
R4||Auto-Negotiation Advertisement
R5||Auto-Negotiation Link Partner Ability
R6||Auto-Negotiation Expansion
R7||Auto-Negotiation Next Page
R8||Link Partner Next Page Ability
R15||RXER Counter
R1b||Interrupt Control/Status
R1f||100BASE-TX PHY Control
'''

binregs_str = '''
R0|15|Reset||1 = software reset. Bit is self-clearing
R0|14|Loop-Back||1 = loop-back mode;0 = normal operation
R0|13|Speed Select (LSB)||1 = 100Mbps;0 = 10Mbps;Ignored if Auto-Neg is enabled (0.12 = 1);Set by SPD100
R0|12|Auto-Neg Enable||1 = enable auto-negotiation process (override 0.13 and 0.8);0 = disable auto-negotiation process;Set by NWAYEN
R0|11|Power Down||1 = power-down mode;0 = normal operation
R0|10|Isolate||1 = electrical isolation of PHY from MII and TX+/TX0 = normal operation;Set by ISO
R0|9|Restart Auto-Neg||1 = restart auto-negotiation process;0 = normal operation. Bit is self-clearing
R0|8|Duplex Mode||1 = FD;0 = HD;Set by DUPLEX
R0|7|Collision Test|0|1 = enable COL test;0 = disable COL test
R0|1|Reserved|1|
R0|0|Disable Transmitter|0|0 = enable transmitter;1 = disable transmitter
R1|15|100BASE-T4|1|1 = T4 capable;0 = not T4 capable
R1|14|100BASE-TX FD|1|1 = capable of 100BASE-X full-duplex;0 = not capable of 100BASE-X full-duplex
R1|13|100BASE-TX HD|1|1 = capable of 100BASE-X half-duplex;0 = not capable of 100BASE-X half-duplex
R1|12|10BASE-T FD|1|1 = 10Mbps with full-duplex;0 = no 10Mbps with full-duplex capability
R1|11|10BASE-T HD|1|1 = 10Mbps with half-duplex;0 = no 10Mbps with half-duplex capability
R1|7|Reserved|1|
R1|6|No Preamble|1|1 = preamble suppression;0 = normal preamble
R1|5|Auto-Neg Complete|1|1 = auto-negotiation process completed;0 = auto-negotiation process not completed
R1|4|Remote flt|1|1 = remote fault;0 = no remote fault
R1|3|Auto-Neg Ability|1|1 = capable to perform auto-negotiation;0 = unable to perform auto-negotiation
R1|2|Link Status|1|1 = link is up;0 = link is down
R1|1|Jabber Detect|1|1 = jabber detected;0 = jabber not detected. Deflt is low
R1|0|Extended Capability|1|1 = supports extended capabilities registers
R2|0|PHY ID|1|Assigned to the 3rd through 18th bits of the organizationally;unique identifier (OUI). Micrel’s OUI is 0010A1 (hex).
R3|0|Revision|1|Four bit manufacturer’s model number
R3|4|Model|1|Six bit manufacturer’s model number
R4|15|Next Page|0|1 = next page capable;0 = no next page capability
R4|14|Reserved|1|
R4|13|Remote flt|0|1 = remote fault supported;0 = no remote fault
R4|11|Reserved|1|
R4|10|Pause|0|1 = pause function supported;0 = no pause function
R4|9|100BASE-T4|1|1 = T4 capable;0 = no T4 capability
R4|8|100BASE-TX FD|0|1 = TX with full-duplex;0 = no TX full-duplex capability;Set by SPD100 & DUPLEX
R4|7|100BASE-TX|0|1 = TX capable;0 = no TX capability;Set by SPD100
R4|6|10BASE-T FD|0|1 = 10Mbps with full-duplex;0 = no 10Mbps full-duplex capability;Set by DUPLEX
R4|5|10BASE-T|0|1 = 10Mbps capable;0 = no 10Mbps capability
R4|0|Selector Field|0|[00001] = IEEE 802.3
R5|15|Next Page|1|1 = next page capable;0 = no next page capability
R5|14|Acknowledge|1|1 = link code word received from partner;0 = link code word not yet received
R5|13|Remote flt|0|1 = remote fault detected; 0 = no remote fault
R5|12|Reserved|1|
R5|10|Pause|1|0 0 - No PAUSE;0 1 - Asymmetric PAUSE (link partner);1 0 - Symmetric PAUSE;1 1 - Symmetric & Asymmetric PAUSE (local device)
R5|9|100 BASE-T4|1|1 = T4 capable;0 = no T4 capability
R5|8|100BASE-TX FD|1|1 = TX with full-duplex;0 = no TX full-duplex capability
R5|7|100BASE-TX|1|1 = TX capable;0 = no TX capability
R5|6|10BASE-T FD|1|1 = 10Mbps with full-duplex;0 = no 10Mbps full-duplex capability
R5|5|10BASE-T|1|1 = 10Mbps capable;0 = no 10Mbps capability
R5|0|Selector Field|1|[00001] = IEEE 802.3
R6|5|Reserved|1|
R6|4|Parallel Detect flt|1|1 = fault detected by parallel detection;0 = no fault detected by parallel detection
R6|3|Next Page Able|1|1 = link partner has next page capability;0 = link partner does not have next page capability
R6|2|Next Page Able|1|1 = local device has next page capability;0 = local device does not have next page capability
R6|1|Page Received|1|1 = new page received;0 = new page not yet received
R6|0|Auto-Neg Able|1|1 = link partner has auto-negotiation capability;0 = link partner does not have auto-negotiation capability
R7|15|Next Page|0|1 = additional next page(s) will follow;0 = last page
R7|14|Reserved|1|
R7|13|Message Page|0|1 = message page;0 = unformatted page
R7|12|Acknowledge 2|0|1 = will comply with message;0 = cannot comply with message
R7|11|Toggle|1|1 = previous value of the transmitted link code word equaled logic One;0 = logic Zero
R7|0|Message Field|0|11-bit wide field to encode 2048 messages
R8|15|Next Page|1|1 = additional next page(s) will follow;0 = last page
R8|14|Acknowledge|1|1 = successful receipt of link word;0 = no successful receipt of link word
R8|13|Message Page|1|1 = Message Page;0 = unformatted page
R8|12|Acknowledge 2|1|1 = able to act on the information;0 = not able to act on the information
R8|11|Toggle|1|1 = previous value of transmitted link code word equal to logic zero;0 = previous value of transmitted link code word equal to logic one
R8|0|Message Field|1|
R15|0|RXER Counter|0|RX Error counter for the RX_ER in each package
R1b|15|Jabber en|0|1 = Enable jabber interrupt;0 = Disable jabber interrupt
R1b|14|Receive Error en|0|1 = Enable receive error interrupt;0 = Disable receive error interrupt
R1b|13|Page Received en|0|1 = Enable page received interrupt;0 = Disable page received interrupt
R1b|12|Parallel Detect flt en|0|1 = Enable parallel detect fault interrupt;0 = Disable parallel detect fault interrupt
R1b|11|Link Partner Ack en|0|1 = Enable link partner acknowledge interrupt;0 = Disable link partner acknowledge interrupt
R1b|10|Link Down en|0|1 = Enable link down interrupt;0 = Disable link down interrupt
R1b|9|Remote flt en|0|1 = Enable remote fault interrupt;0 = Disable remote fault interrupt
R1b|8|Link Up en|0|1 = Enable link up interrupt;0 = Disable link up interrupt
R1b|7|Jabber irq|1|1 = Jabber irq occurred;0 = Jabber irq has not occurred
R1b|6|Receive Error irq|1|1 = Receive error occurred;0 = Receive error has not occurred
R1b|5|Page Receive irq|1|1 = Page receive occurred;0 = Page receive has not occurred
R1b|4|Parallel Detect flt irq|1|1 = Parallel detect fault occurred;0 = Parallel detect fault has not occurred
R1b|3|Link Partner Ack irq|1|1 = Link partner acknowledge occurred;0 = Link partner acknowledge has not occurred
R1b|2|Link Down irq|1|1 = Link down occurred;0 = Link down has not occurred
R1b|1|Remote flt irq|1|1 = Remote fault occurred;0 = Remote fault has not occurred
R1b|0|Link Up irq|1|1 = Link up irq occurred;0 = Link up irq has not occurred
R1f|14|Reserved|1|
R1f|13|Pairswap Disable|0|1 = Disable MDI/MDI-X;0 = Enable MDI/MDI-X
R1f|12|Energy Detect|1|1 = Presence of signal on RX+/RX- analog wire pair;0 = No signal detected on RX+/RX-
R1f|11|Force Link|0|1 = Force link pass;0 = Normal link operation;This bit bypasses the control logic and allow transmitter to;send pattern even if there is no link.
R1f|10|Power-Saving|0|1 = Enable power-saving;0 = Disable
R1f|9|Interrupt Level|0|1 = Interrupt pin active high;0 = Active low
R1f|8|Enable Jabber|0|1 = Enable jabber counter;0 = Disable
R1f|7|Auto-Neg Complete|0|1 = Auto-negotiation complete;0 = Not complete
R1f|6|Enable Pause|1|1 = Flow control capable;0 = No flow control
R1f|5|PHY Isolate|1|1 = PHY in isolate mode;0 = Not isolated
R1f|2|Operation Mode|1|[000] = Still in Auto-Neg;[001] = 10BASE-T HD;[010] = 100BASE-TX half-duplex;[011] = Reserved;[101] = 10BASE-T FD;[110] = 100BASE-TX full-duplex;[111] = PHY/MII isolate
R1f|1|Enable SQE Test|0|1 = Enable SQE test;0 = Disable
R1f|0|Dis Data Scrambling|0|1 = Disable scrambler;0 = Enable
'''

def columns():
    return get_columns()

def get_menu(dev):
    return OD([('Registers', manyregs_cb)])

def get_regs(dev):
    data = RegsData(sz=16)
    data.add_hex_data(hex_data, cmd_cb=mdio_cmd_cb, fmt_cb=strip0x_fmt_cb)
    data.add_bin_data(binregs_str)
    data.columns = 4
    return data

