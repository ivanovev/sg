data = '''
R000|00|SPI Configuration
R001|00|Multi-Chip Sync and TX Mon Control
R002|5F|TX Enable & Filter Control
R003|5F|Rx Enable & Filter Control
R004|00|Input Select
R005|00|RFPLL Dividers
R006|00|RX Clock & Data Delay
R007|00|TX Clock & Data Delay
R009|10|Clock Enable
R00A|03|BBPLL
R00B|00|Offset
R00C|00|Start Temp Reading
R00D|03|Temp Sense2
R00E|00|Temperature
R00F|04|Temp Sensor Con g
R010|00|Parallel Port Configuration 1
R011|00|Parallel Port Configuration 2
R012|04|Parallel Port Configuration 3
R013|01|ENSM Mode
R014|13|ENSM Config 1
R015|08|ENSM Config 2
R016|00|Calibration Control
R017|00|State
R018|00|AuXDAC 1 Word
R019|00|AuXDAC 2 Word
R01A|00|AuXDAC 1 Con g
R01B|00|AuXDAC 2 Con g
R01C|10|AuXADC Clock Divider
R01D|01|AuXADC Con g
R01E|00|AuXADC Word MSB
R01F|00|AuXADC LSB
R020|33|Auto GPO
R021|00|AGC Gain Lock Delay
R022|00|AGC Attack Delay
R023|3F|AuXDAC Enable Control
R024|02|RX Load Syn th Delay
R025|02|TX Load Syn th Delay
R026|00|External LNA con trol
R027|03|GPO Force and lnit
R028|00|GPO0 RX delay
R029|00|GPO 1 RX delay
R02A|00|GPO2 RX delay
R02B|00|GPO3 RX delay
R02C|00|GPO0 TX Delay
R02D|00|GPO 1 TX Delay
R02E|00|GPO2 TX Delay
R02F|00|GPO3 TX Delay
R030|00|AuXDAC1 RX Delay
R031|00|AuXDAC2 TX Delay
R032|00|AuXDAC2 RX Delay
R033|00|AuXDAC2 TX Delay
R035|00|Control Output Pointer
R036|FF|Control Output Enable
R037|00|Product ID
R038|80|DCXO Output Buffer Config
R03A|00|Reference Clock Cycles
R03B|00|Digital V0 Control
R03C|03|LVDS Bias con trol
R03D|00|LVDS Invert con trol 1
R03E|00|LVDS In vert con troI2
R03F|01|SDM Control 1
R040|00|SDM Control 2
R041|00|Fractional BB Freq Word 1
R042|00|Fractional BB Freq Word 2
R043|00|Fractional BB Freq Word 3
R044|10|Integer BB Freq Word
R045|00|Clock Control
R046|09|CP Current
R047|00|CP Bleed Current
R048|C5|Loop Filter 1
R049|B8|Loop Filter 2
R04A|2E|Loop Filter 3
R04B|00|VCO Control
R04C|00|VCO Program 1
R04D|00|VCO Program 2
R04E|00|SDM Control
R04F|00|BBPLL External Clock
R050|00|RX Syn th Power Down Override
R051|00|TX Syn th Power Down Override
R052|03|Rx Analog Power Down Override 1
R053|00|Rx Analog Power Down Override 2
R054|00|RX1 ADC Power Down Override
R055|00|RXZ ADC Power Down Override
R056|00|TX Analog Power Down Override 1
R057|3C|Analog Power Down Override
R058|30|Misc Power Down Override
R05E|00|CH 1 Overflow
R05F|00|CH 2 Overflow
R060|00|TX Filter Coefficient Address
R061|00|TX Filter Coefficient Write Data 1
R062|00|TX Filter Coefficient Write Data 2
R063|00|TX Filter Coefficient Read Data 1
R064|00|TX Filter Coefficient Read Data 2
R065|00|TX Filter Configuration
R073|00|Tx1Atten 0
R074|00|Tx1 Atten 1
R075|00|TX2 Atten 0
R076|00|Tx2 Atten 1
R077|40|TxAtten Offset
R078|3C|TxAtten Threshold
R079|00|Tx1 Dig Attenuation
R07A|00|Tx1 LWHP Atten
R07B|00|Tx1 LP Atten
R07C|00|Tx2 Dig Attenuation
R07D|00|Tx2 LWHP Atten
R07E|00|Tx2 LP Atten
R07F|00|TX 1 Symbol Attenuation
R080|00|TX2 Symbol Attenuation
R081|00|TX Symbol Atten Config
R08E|00|TX1 Out 1 Phase Corr
R08F|00|TX1 Out 1 Gain Corr
R090|00|TX2 Out 1 Phase Corr
R091|00|TX2 Out 1 Gain Corr
R092|00|TX1 Out 1 Offsetl
R093|00|TX1 Out 1 Offset Q
R094|00|TX2 Out 1 Offset I
R095|00|TX2 Out 1 Offset Q
R096|00|TX1 Out2 Phase Corr
R097|00|TX1 Out 2 Gain Corr
R098|00|TX2 Out 2 Phase Corr
R099|00|TX2 Out 2 Gain Corr
R09A|00|TX1 Out2 Offsetl
R09B|00|TX1 Out2 Offset Q
R09C|00|TX2 Out 2 Offset I
R09D|00|TX2 Out 2 Offset Q
R09E|00|Open
R09F|00|Force Bits
R0A0|00|Quad Cal NCO Freq & Phase Offset
R0A1|78|Quad Cal Control
R0A2|1F|Kexp 1
R0A3|00|Kexp 2
R0A4|10|Settle count
R0A5|06|Mag. Ftest Thresh
R0A6|06|Mag. Ftest Thresh 2
R0A7|00|Quad cal status TX1
R0A8|00|Quad cal status TX2
R0A9|20|Quadcal Count
R0AA|00|TX Quad FUIVLMT Gain
R0AB|00|Squarer Con g
R0AC|00|TX Quad Cal Atten
R0AD|00|Thresh Accum
R0AE|18|Tx Quad LPF Gain
R0B0|00|TXDAC Vds I
R0B1|00|TXDAC Vds Q
R0B2|00|TXDA C gn I
R0B3|00|TXDAC gn Q
R0C0|6F|TXBBF OpA mp A
R0C1|EF|TXBBF OpAmp B
R0C2|1F|TX BBF R 1
R0C3|1F|TX BBF R2
R0C4|1F|TX BBF R3
R0C5|1F|TX BBF R4
R0C6|1F|TX BBF RP
R0C7|2A|TX BBF C 1
R0C8|2A|TX BBF C2
R0C9|2A|TX BBF
R0CA|20|TX Tune Control
R0CB|00|TX BBF R2b
R0CC|00|Tx BBF Tune
R0D0|55|Config0
R0D1|00|Resistor
R0D2|1F|Capacitor
R0D3|60|LO CM
R0D6|12|TX BBF Tune Divider
R0D7|1E|TX BBF Tune Mode
R0F0|00|RX Filter CoeffAddr
R0F1|00|RX Filter CoeffData 1
R0F2|00|RX Filter CoeffData 2
R0F3|00|RX Filter CoeffRead Data 1
R0F4|00|Rx Filter Coeff Read Data 2
R0F5|00|RX Filter Con g
R0F6|00|Rx Filter Gain
R0FA|00|AGC Configl
R0FB|08|AGC config2
R0FC|03|AGC Config3
R0FD|4C|Max LMWFUII Gain
R0FE|44|Peak Wait Time
R0FF|00|N/A
R100|6F|Digital Gain
R101|00|AGC Lock Level
R102|00|ADC noise Correction Factor
R103|08|Gain Step Con g1
R104|2F|ADC Small Overload Threshold
R105|3A|ADC Large Overload Threshold
R106|25|Gain Step Config 2
R107|3F|Small LM T Overload Threshold
R108|1F|Large LM T Overload Threshold
R109|4C|RX1 Manual LMWFUII Gain
R10A|58|RX1 Manual LPF gain
R10B|00|RX1 Manual DigitaVForced Gain
R10C|4C|RX2 ManuaILMWF ull Gain
R10D|18|RX2 Manual LPF Gain
R10E|00|RX2 Manual DigitaVForced Gain
R110|02|Config 1
R111|CA|Config 2 & Settling Delay
R112|4A|Energy Lost Threshold
R113|4A|Stronger Signal Threshold
R114|80|Low Power Threshold
R115|64|Strong Signal Freeze
R116|65|Final Over Range and Opt Gain
R117|08|Energy Detect Count
R118|3F|AGCLL Upper Limit
R119|08|Gain Lock Exit Count
R11A|1C|Initial LM T Gain Limit
R11B|00|Increment Time
R120|00|AGC Inner Low Threshold
R121|00|LMT Overload Counters
R122|00|ADC Overload Counters
R123|00|Gain Step1
R124|00|Gain Update Counter1
R125|00|Gain Update Counter2
R126|00|N/A
R127|00|N/A
R128|00|Digital Sat Counter
R129|00|Outer Power Thresholds
R12A|00|Gain Step 2
R12C|00|Ext LNA High Gain
R12D|00|Ext LNA Low Gain
R130|00|Gain Table Address
R131|00|Gain Table Write Data 1
R132|00|Gain Table Write Data2
R133|00|Gain Table Write Data 3
R134|00|Gain Table Read Data 1
R135|00|Gain Table Read Data 2
R136|00|Gain Table Read Data 3
R137|08|Gain Table Con g
R138|00|Gm Sub Table Address
R139|00|Gm Sub Table Gain Word Write
R13A|00|Gm Sub Table Bias Word Write
R13B|00|Gm Sub Table Control Word Write
R13C|00|Gm Sub Table Gain Word Read
R13D|00|Gm Sub Table Bias Word Read
R13E|00|Gm Sub Table Control Word Read
R13F|00|Gm Sub Table Config
R140|00|Word Address
R141|00|Gain Diff WordiError Write
R142|00|Gain Error Read
R143|00|Con g
R144|00|LNA Gain Diff Read Back
R145|00|Max Mixer Calibration Gain Index
R146|00|Temp Gain Coefficient
R147|10|Settle Time
R148|04|Measure Duration
R149|00|Cal Temp sensor word
R150|08|Measure Duration 0&1
R151|00|Measure Duration 2&3
R152|00|Weight 0
R153|00|Weight 1
R154|00|Weight 2
R155|00|Weight 3
R156|00|RSSI delay
R157|00|RSSI wait time
R158|01|RSSI Config
R159|22|ADC Measure Duration 0&1
R15A|00|Weight 0
R15B|00|Weight 1
R15C|15|Dec Power Measure Duration 0
R15D|B1|LNA Gain
R160|00|CH1 ADC Power
R161|00|CH1 Rx filter Power
R162|00|CH2 ADC Power
R163|00|CH2 Rx filter Power
R168|00|RX Quad Cal Level
R169|00|Calibration Config 1
R16A|08|Calibration con g2
R16B|08|Calibration con g3
R16C|FF|Calib count
R16D|00|Settle count
R16E|00|RX Quad gain 1
R16F|18|RX Quad gain2
R170|00|RX1 lnputA Phase Corr
R171|00|RX1 lnputA Gain Corr
R172|00|RX2 lnputA Phase Corr
R173|00|RX2 lnputA Gain Corr
R174|00|RX1 lnputA Q Offset
R175|00|RX1 lnputA Offsets
R176|00|lnputA Offsets 1
R177|00|RX2 lnputA Offsets
R178|00|RX2 lnputA W Offset
R179|00|RX1 Input B&C Phase Corr
R17A|00|RX1 Input B&C Gain Corr
R17B|00|RXZ Input B&C Phase Corr
R17C|00|RXZ Input B&C Gain Corr
R17D|00|RX1 Input IIQII Offset
R17E|00|RX1 Input B&C Offsets
R17F|00|Input B&C Offsets 1
R180|00|RXZ Input B&C Offsets
R181|00|RXZ Input B&C l Offset
R182|00|Force Bits
R185|10|Wait Count
R186|B4|RF DC Offset Count
R187|1C|RF DC Offset Con g1
R188|05|RF DC Offset Attenuation
R189|30|In vert Bits
R18A|FF|N/A
R18B|8D|DC Offset Config2
R18C|00|RF Cal Gain Index
R18D|64|SOI Threshold
R18E|00|N/A
R18F|00|N/A
R190|00|BB DC Offset Shift
R191|06|BB DC Offset Fast Settle Shift
R192|03|BB Fast Settle Dur
R193|3F|BB DC Offset Count
R194|01|BB DC Offset Attenuation
R19A|00|RX 1 BB DC word I MSB
R19B|00|RX 1 BB DC word I LSB
R19C|00|RX 1 BB DC word Q MSB
R19D|00|RX 1 BB DC word Q LSB
R19E|00|RX2 BB DC word I MSB
R19F|00|RX2 BB DC word I LS B
R1A0|00|RX2 BB DC word Q MSB
R1A1|00|RX2 BB DC word Q LSB
R1A2|00|BB Track corr word I MSB
R1A3|00|BB Track corr word I LS B
R1A4|00|BB Track corr word Q MSB
R1A5|00|BB Track corr word Q LSB
R1A7|00|Rx1 RSSI Symbol
R1A8|00|Rx1 RSSI preamble
R1A9|00|RX2 RSSI symbol
R1AA|00|RX2 RSSI preamble
R1AB|00|Symbol LSB
R1AC|00|Preamble LSB
R1AD|00|RX Path Gain
R1AE|00|RX Path Gain
R1B0|00|Rx Diff LNA Force
R1B1|07|Rx LNA Bias Coarse
R1B2|00|RX LNA Bias Fine 0
R1B3|03|Rx LNA Bias Fine 1
R1C0|43|RX Mix Gm Con g
R1C1|00|RX1 Mix Gm Force
R1C2|00|RX1 Mix Gm Bias Worcd
R1C3|00|RX2 Mix Gm Force
R1C4|00|RX2 Mix Gm Bias Worcd
R1C8|00|lnputA MSBS
R1C9|00|lnputA RX 1 I
R1CA|00|lnputA RX 1 Q
R1CB|00|lnputA RXZI
R1CC|00|lnputA RX2 Q
R1CD|00|Inputs B&C RX 1 I
R1CE|00|Band1RX1Q
R1CF|00|Inputs B&C RX2 I
R1D0|00|Inputs B&C RX2 Q
R1D1|00|Inputs B&C M535
R1D2|00|Force 05 DAC
R1D5|28|RX Mix LO CM
R1D6|4F|RX CGB Seg Enable
R1D7|13|RX Mix InpuVBias
R1DB|60|RX TIA Config
R1DC|03|TlA1 CLSB
R1DD|00|TIA1 CMSB
R1DE|03|TlA2 C LSB
R1DF|00|TlA2 C MSB
R1E0|03|RX1BBFR1A
R1E1|03|RX2 BBF R 1A
R1E2|00|RX1 Tune Control
R1E3|00|RX2 Tune Control
R1E4|01|RX1 BBF R5
R1E5|01|RX2 BBF R5
R1E6|01|RX BBF R2346
R1E7|00|RX BBF C1 MSB
R1E8|60|RX BBF C1 LSB
R1E9|00|RX BBF C2 MSB
R1EA|60|RX BBF C2 LSB
R1EB|00|RX BBF C3 MSB
R1EC|60|RX BBF C3 LSB
R1ED|07|Rx BBF CC 1 Ctr
R1EE|60|RX BBF Pow R2 Byte0
R1EF|07|Rx BBF CC2 Ctr
R1F0|CC|RX BBF Pow R2 Byte1
R1F1|07|Rx BBF CC3 Ctr
R1F2|00|Rx BBF R5 Tune
R1F3|20|RX BBF Tune
R1F4|00|RX1 BBF Man Gain
R1F5|00|RXZ BBF Man Gain
R1F8|14|RX BBF Tune Divide
R1F9|1E|RX BBF Tune Con g
R1FA|01|Pole gain
R1FB|05|RX BBBWMHZ
R1FC|00|RX BBB WkHz
R200|00|Not Used
R201|00|FB DAC Clk Delayi
R202|00|FB DAC Clk Delay2
R203|24|Flash Sample Clk Delay 3p
R204|24|Flash Sample Clk Delay 3p
R205|00|Test MUX2i
R206|00|Test M UX 2q
R207|28|Integrator 1 Resistance
R208|14|Integrator 1 Capacitance
R209|20|In tegrator 23 Resistance
R20A|28|In tegrator 2 Resistance
R20B|14|In tegrator 2 Capacitance
R20C|28|In tegrator 3 Resistance
R20D|14|In tegrator 3 Capacitance
R20E|00|lntegratorAmp Cc
R20F|29|Int 1 FB DAC NMOS Current Source
R210|29|Int 1 FB DAC NMOS Casoade Bias Current
R211|29|Int 1 FB DAC PMOS Current Source
R212|27|lnt2 FB DAC NMOS Currentsource
R213|27|lnt2 FB DAC NMOS Cascode Bias Current
R214|27|lnt2 FB DAC PMOS Current Source
R215|27|Int 3 FB DAC NMOS Currentsource
R216|27|Int 3 FB DAC NMOS Cascode Bias Current
R217|27|Int 3 FB DAC PMOS Current Source
R218|2E|FB DAC Bias Current
R219|90|Int 1 ISI Stage Current
R21A|15|Int 1 15f Stage Cascode Current
R21B|10|Int 1 2nd Stage Current
R21C|90|lntegrator2 15f Stage Current
R21D|15|lnt2 15f Stage Cascode Current
R21E|10|Int 2 2nd Stage Current
R21F|90|Int 3 15f Stage Current
R220|15|Int 3 15f Stage Cascode Current
R221|20|Int 3 2nd Stage Current
R222|20|Flash Bias Current
R223|40|Flash Ladder Bias
R224|40|Flash Ladder Cascode Current
R225|2C|Flash Ladder Bias2
R226|00|Reset
R230|54|PFD Config
R231|00|In teger Byte 0
R232|00|In teger Byte 1
R233|00|Fractional Byte 0
R234|00|Fractional Byte 1
R235|00|Fractional Byte 2
R236|00|Force ALC
R237|00|Force VCO Tune 0
R238|00|Force VCO Tune 1
R239|82|ALOVaract or
R23A|00|VCO Output
R23B|00|CP Current
R23C|00|CP Offset
R23D|80|CP Config
R23E|00|Loop Filter 1
R23F|00|Loop Filter 2
R240|00|Loop Filter 3
R241|00|DitheMCP Cal
R242|04|VCO Bias 1
R243|00|VCO Bias 2
R244|00|Cal Status
R245|00|VCO Cal Ref
R246|00|VCO Pd Overrides
R247|00|CP<3ver RangeA 3D Lock
R248|07|VCO LDO
R249|02|VCO Cal
R24A|02|Lock LDetect Con g
R24B|17|CP Level Detect
R24C|00|DSM Setup
R24D|00|DSM Setup
R24E|00|Correction Word0
R24F|00|Correction Word 1
R250|63|VCO Varactor Control 0
R251|08|VCO Varactor Control 1
R25A|00|RX Fast Lock Setup
R25B|00|RX Fast Lock Setup lnit Delay
R25C|00|RX Fast Lock Program Addr
R25D|00|RX Fast Lock Program Data
R25E|00|RX Fast Lock Program Read
R25F|00|RX Fast Lock Program Control
R261|00|RX LO Gen Power Mode
R270|54|PFD Config
R271|00|In teger Byte 0
R272|00|In teger Byte 1
R273|00|Fractional Byte 0
R274|00|Fractional Byte 1
R275|00|Fractional Byte 2
R276|00|Force ALC
R277|00|Force VCO Tune 0
R278|00|Force VCO Tune 1
R279|82|ALOVaract or
R27A|00|VCO Output
R27B|00|CP Current
R27C|00|CP Offset
R27D|80|CP Config
R27E|00|Loop Filter 1
R27F|00|Loop Filter 2
R280|00|Loop Filter 3
R281|00|DitheMCP Cal
R282|04|VCO Bias 1
R283|00|VCO Bias 2
R284|00|Cal Status
R285|00|VCO Cal Ref
R286|00|VCO Pd Overrides
R287|00|CP<3ver RangeA 3D Lock
R288|07|VCO LDO
R289|02|VCO Cal
R28A|02|Lock LDetect Con g
R28B|40|CP Level Detect
R28C|00|DSM Setup
R28D|80|DSM Setup
R28E|00|Correction Word0
R28F|00|Correction Word 1
R290|63|VCO Varactor Control 0
R291|08|VCO Varactor Control 1
R292|00|DCXO Coarse Tune
R293|00|DCXO Fine Tune2
R294|00|DCXO Fine Tune 1
R295|14|DCXO Config
R296|00|DCXO Tempco Write
R297|00|DCXO Tempco Read
R298|00|DCXO Tempco Addr
R299|00|Delta TRead
R29A|00|TX Fast Lock Setup
R29B|00|TX Fast Lock Setup Init Delay
R29C|00|TX Fast Lock Program Addr
R29D|00|TX Fast Lock Program Data
R29E|00|TX Fast Lock Program Read
R29F|00|TX Fast Lock Program C trl
R2A1|00|Tx LO Gen Power Mode
R2A6|04|Bandgap Config0
R2A8|00|Bandgap Config1
R2AB|04|Ref Divide Config 1
R2AC|00|Ref Divide Config 2
R2B0|00|Gain RX1
R2B1|00|LPF Gain RX1
R2B2|00|Dig gain RX1
R2B3|00|FastAttack State
R2B4|00|Slow Loop State
R2B5|00|Gain RX2
R2B6|00|LPF Gain RX2
R2B7|00|Dig Gain RX2
R2B8|00|Ovrg Sigs RX1
R2B9|00|Ovrg Sigs RX2
R3DF|00|Control
R3F4|00|BIST Config
R3F5|00|Observe Con g
R3F6|00|BIS Tand Data Port Test Config
R3FC|FF|DAC Test 0
R3FD|FF|DAC Test 1
R3FE|3F|DAC Test 2
'''
