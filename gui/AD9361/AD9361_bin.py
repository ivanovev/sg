data = '''
R000|0|Soft reset||
R000|1|3-Wire SPI||
R000|2|LSB First||
R000|3|Open||
R000|5|LSB First||
R000|6|3-Wire SPI||
R000|7|Soft Reset||
R001|0|MCS BB Enable||
R001|1|MCS Digital CLK||MCS Digital CLK Enable
R001|2|MCS BBPLL enable||
R001|3|MCS RF Enable||
R001|4|Open||
R001|5|TX1 Monitor Enable||
R001|6|Tx2 Monitor Enable||
R001|7|Open||
R002|0|Tx FIR Enable &||Tx FIR Enable & InterpoIation<1:O>
R002|2|THB1 Enable||
R002|3|THB2 Enable||
R002|4|THB3 Enable &||THB3 Enable & Interp<1:O>
R002|6|Txchannel||Txchannel EnabIe<1:O>
R003|0|Rx FIR Enable &||Rx FIR Enable & Decimation<1:O>
R003|2|RHB1 Enable||
R003|3|RHB2 Enable||
R003|4|DEC3 Enable &||DEC3 Enable & Decimation<1:O>
R003|6|Rxchannel||Rxchannel EnabIe<1:O>
R004|0|RX Input <5:O>||
R004|6|TX Output||
R004|7|N/A||
R005|0|RX VCO Divider<3:O>||
R005|4|TX VCO Divider<3:O>||
R006|0|Rx Data Delay <3:O>||
R006|4|DATA CLK DeIay<3:O>||
R007|0|Tx Data Delay <3:O>||
R007|4|FB CLK DeIay<3:O>||
R009|0|BBPLL Enable||
R009|1|Set to||
R009|2|Digital Power Up||
R009|3|Set to O||
R009|4|XO Bypass||
R009|5|Set to O||
R009|6|Open||
R00A|0|BBPLL Divider <2:O>||
R00A|3|DAC Clk div2||
R00A|4|CLKOUT Enable||
R00A|5|CLKOUT SeIect<2:O>||
R00B|0|Temp Sense Offset||Temp Sense Offset <7:O>
R00C|0|Start Temp Reading||
R00C|1|Open||
R00D|0|Temp Sense Periodic||Temp Sense Periodic Enable
R00D|1|Measurement Time||Measurement Time IntervaI<6:O>
R00E|0|Temperature<7:O>||
R00F|0|Temp Sensor||Temp Sensor Decimation<2:O>
R00F|3|Open||
R010|0|Inven DATA CLK||
R010|1|Invert data bus||
R010|2|2R2T Timing||
R010|3|Rx Frame Pulse Mode||
R010|4|Rx Channel swap||
R010|5|Tx Channel swa p||
R010|6|PP Rx Swap IQ||
R010|7|PP Tx Swap IQ||
R011|0|Delay Rx Data<1:O>||
R011|2|Invert Rx Frame||
R011|3|Invert Tx2||
R011|4|Invert TX1||
R011|5|Invert Rx2||
R011|6|Invert RX1||
R011|7|FDD Alt Word Order||
R012|0|Full Duplex Swap||Full Duplex Swap Bits
R012|1|Full Port||
R012|2|Single Port Mode||
R012|3|Half Duplex Mode||
R012|4|LVDS Mode||
R012|5|Single Data Rate||
R012|6|Swap Ports||
R012|7|FDD Rx Rate : 29eTx||FDD Rx Rate : 29eTx Rate
R013|0|FDD Mode||
R013|1|Open||
R014|0|To Alert||
R014|1|Auto Gain Lock||
R014|2|Force Alert State||
R014|3|Level Mode||
R014|4|Enable ENSM Pin||Enable ENSM Pin Control
R014|5|Force Tx On||
R014|6|Force Rx On||
R014|7|Enable Rx Data Port||Enable Rx Data Port for Cal
R015|0|Tx Synth Ready Mask||
R015|1|Rx Synth Ready Mask||
R015|2|Dual Synth Mode||
R015|3|Synth Enable Pin||Synth Enable Pin Control Mode
R015|4|TXN RX SPI Control||
R015|5|Power Down Tx Synth||
R015|6|Power Down Rx Synth||
R015|7|FDD External||FDD External Control Enable
R016|0|DC cal BB Start||
R016|1|DC Cal RF Start||
R016|2|Open||
R016|3|Rx Gain Step Cal||
R016|4|Tx Quad Cal||
R016|5|Rx Quad Cal||
R016|6|Tx BB Tune||
R016|7|RXBB Tune||
R017|0|ENSM State<3:O>||
R017|4|Calibration||Calibration Sequence State<3:O>
R018|0|AuxDAC 1 Word<9:2>||
R019|0|AuxDAC 2 Word<9:2>||
R01A|0|AuXDAC 1 Word <1 :O>||
R01A|2|AuXDAC 1 Vref<1:O>||
R01A|4|AuXDAC1 Step Factor||
R01A|5|Comp Ctrl 1||
R01A|6|Open||
R01B|0|AuXDAC 2 Word <1 :O>||
R01B|2|AuXDAC 2 Vref<1:O>||
R01B|4|AuXDAC2 Step Factor||
R01B|5|Comp Ctrl 2||
R01B|6|Open||
R01C|0|AuxADC Clock||AuxADC Clock Divider<5:O>
R01C|6|Open||
R01D|0|AuxADC Power Down||
R01D|1|Aux ADC||Aux ADC Decimation<2:O>
R01D|4|Open||
R01E|0|AUXADC Word||AUXADC Word MSB<11:4>
R01F|0|AuXADC Word LSB<3:O>||
R01F|4|Open||
R020|0|GPO Enable Auto||GPO Enable Auto Tx<3:O>
R020|4|GPO Enable Auto||GPO Enable Auto Rx<3:O>
R021|0|Gain Lock DeIay<7:O>||
R022|0|AGC Attack||AGC Attack DeIay<5:O>
R022|6|Invert Bypassed LNA||Invert Bypassed LNA Polarity
R022|7|Open||
R023|0|AuxDAC Init Bar<1:O>||
R023|2|AuXDAC Auto Rx||AuXDAC Auto Rx Bar<1:O>
R023|4|AuxDAC Auto Tx||AuxDAC Auto Tx Bar<1 20>
R023|6|AuxDac Manual||AuxDac Manual Bar<1:O>
R024|0|Rx Load Synthesizer||Rx Load Synthesizer DeIay<7:O>
R025|0|Tx Load Synthesizer||Tx Load Synthesizer DeIay<7:O>
R026|0|Open<3:O>||
R026|4|GPO manual select||
R026|5|External LNA1||External LNA1 control
R026|6|External LNA2||External LNA2 control
R026|7|AuxDAC Manual Select||
R027|0|GPO Init State<3:O>||
R027|4|GPO Manual||GPO Manual ControI<3:O>
R028|0|GPOO Rx DeIay<7:O>||
R029|0|GPO1 Rx DeIay<7:O>||
R02A|0|GPO2 Rx DeIay<7:O>||
R02B|0|GPO3 Rx DeIay<7:O>||
R02C|0|GPOO Tx DeIay<7:O>||
R02D|0|GPOO Tx DeIay<7:O>||
R02E|0|GPOO Tx DeIay<7:O>||
R02F|0|GPOO Tx DeIay<7:O>||
R030|0|AuXDAC 1 Rx Delay||AuXDAC 1 Rx Delay <7:O>
R031|0|AuXDAC 1 TX Delay||AuXDAC 1 TX Delay <7:O>
R032|0|AuXDAC 2 Rx Delay||AuXDAC 2 Rx Delay <7:O>
R033|0|AuXDAC 2 TX Delay||AuXDAC 2 TX Delay <7:O>
R035|0|Control Output||Control Output Pointer<7:O>
R036|0|En ctrIO||
R036|1|En ctrI1||
R036|2|En ctrI2||
R036|3|En ctrI3||
R036|4|En ctrI4||
R036|5|En ctrI5||
R036|6|En ctrI6||
R036|7|En ctrI7||
R037|0|RevI2:01||
R037|3|9361||
R037|4|Open||
R038|0|Output Buffer||Output Buffer Drive<4:O>
R038|5|Open||
R038|6|Output Buffer Enable||
R038|7|Open||
R03A|0|Reference Clock||Reference Clock Cycles per us<6:O>
R03A|7|open||
R03B|0|Data Port SIew<1:O>||
R03B|2|Data Port Drive||
R03B|3|N/A||
R03B|4|DATACLK slew <1 :O>||
R03B|6|DATACLK drive||
R03B|7|CLK Out Drive||
R03C|0|LVDS Bias <2:O>||
R03C|3|LVDS TX LO VCM||
R03C|4|Bypass Bias R||
R03C|5|Rx On Chip Term||
R03C|6|CLK Out SIew<1:O>||
R03D|0|LVDS pn Invert<7:O>||
R03E|0|LVDS pn Invert<15:8>||
R03F|0|BBPLL Reset Bar||
R03F|1|BBPLL SDAA Bypass||
R03F|2|Init BB FO CAL||
R03F|3|BBPLL SDM CLK||BBPLL SDM CLK Enable Bar
R03F|4|SDM SIF Data<3:O>||
R040|0|SIF Addr<4:O>||
R040|5|SIF Clk||
R040|6|Dither<1:O>||
R041|0|Fractional BB||Fractional BB Frequency Word<23:1 6>
R042|0|Fractional BB||Fractional BB Frequency Word<1 5:8>
R043|0|Fractional BB||Fractional BB Frequency Word<7:O>
R044|0|Integer BB||Integer BB Frequency Word<7:O>
R045|0|Ref Frequency Scaler||
R045|2|PFD Clk Edge||
R045|3|PFD Reset Delay||
R045|5|Ref Clk Inv||
R045|6|FB Clk Inv||
R045|7|PLL FB Inv||
R046|0|Charge Pump||Charge Pump Current<5:O>
R046|6|CP Test Mode<1 :O>||
R047|0|Charge Pump Bleed||Charge Pump Bleed Current<5:O>
R047|6|Bleed Enable||
R047|7|MCS refclk Scale En||
R048|0|R1 Word<4:O>||
R048|5|C1 Word<2:O>||
R049|0|C1 Word<4:3>||
R049|2|C2 Word <4:O>||
R049|7|R2 Word <O>||
R04A|0|R2 Word<2:1>||
R04A|2|C3 Word<3:O>||
R04A|6|Bypass R2||
R04A|7|Bypass C3||
R04B|0|Forced VCO band||Forced VCO band word<2:O>
R04B|3|Force VCO band||Force VCO band enable
R04B|4|Freq Cal Reset||
R04B|5|Freq Cal Count||Freq Cal Count Length<1:O>
R04B|7|Freq Cal Enable||
R04C|0|SIF Data<5:O>||
R04C|6|SIF Addr<1:0>||
R04D|0|SIF Addr<3:2>||
R04D|2|SIF Clk||
R04D|3|SIF Reset||
R04D|4|POR Overri||
R04D|5|Doubler DeIay<1:O>||
R04D|7|Open||
R04E|0|SDM SIF Reset||
R04E|1|SDM Divider Reset||
R04E|2|Lock Detect Reset||
R04E|3|SDM Reset||
R04E|4|Cal Clock div 4||
R04E|5|VCO Cal Tol||
R04E|6|MCS Pulse DeIay<1:O>||
R04F|0|OTA1 CCAP<4:O>||
R04F|4|Force OTA CCAP||
R04F|5|Bypas s Bias Filter||
R04F|6|Force Freq Cal State||
R04F|7|BBPLL Ext Clock||BBPLL Ext Clock Enable
R050|0|Rx Synth VCO LDO||Rx Synth VCO LDO Power Down
R050|1|Rx Synth VCO Power||Rx Synth VCO Power Down
R050|2|Rx Synth PTAT Power||Rx Synth PTAT Power Down
R050|3|Rx Synth VCO ALC||Rx Synth VCO ALC Power Down
R050|4|Rx LO Power Down||
R050|5|Open||
R051|0|Tx Synth VCO LDO||Tx Synth VCO LDO Power Down
R051|1|Tx Synth VCO Power||Tx Synth VCO Power Down
R051|2|Tx Synth PTAT Power||Tx Synth PTAT Power Down
R051|3|Tx Synth VCO ALC||Tx Synth VCO ALC Power Down
R051|4|TX LO Power Down||
R051|5|Open||
R052|0|Rx CGB Power||Rx CGB Power Down<1:O>
R052|2|Rx Mixer Gm Power||Rx Mixer Gm Power Down<1:O>
R052|4|Rx LMT Overload||Rx LMT Overload Power Down<1:O>
R052|6|Rx Offset DAC CGin||Rx Offset DAC CGin Power Down<1:O>
R053|0|Rx Offset DAC CGOut||Rx Offset DAC CGOut Power Down<1:O>
R053|2|Rx Mixer Power||Rx Mixer Power Down<1:O>
R053|4|Rx TIA Power||Rx TIA Power Down<1:O>
R053|6|Rx BBF Power||Rx BBF Power Down<1:O>
R054|0|RX1 ADC Power||RX1 ADC Power Down<7:O>
R055|0|Rx2 ADC Power||Rx2 ADC Power Down<7:O>
R056|0|Tx DAC Bias Power||Tx DAC Bias Power Down<1:O>
R056|2|Tx DAC Power||Tx DAC Power Down<1:O>
R056|4|Tx BBF Power||Tx BBF Power Down<1:O>
R056|6|Tx Secondary Filter||Tx Secondary Filter Power Down<1:O>
R057|0|Tx Upconverter||Tx Upconverter Power Down<1 20>
R057|2|Tx Monitor Power||Tx Monitor Power Down<1:O>
R057|4|TX Ext VCO Buffer||TX Ext VCO Buffer Power Down
R057|5|Rx Ext VCO Buffer||Rx Ext VCO Buffer Power Down
R057|6|Open||
R058|0|Master Bias Power||Master Bias Power Down
R058|1|DCXO Power Down||
R058|2|Rx Calibration||Rx Calibration Power Down<1:O>
R058|4|Open||
R058|6|RX LNA Power Down||
R058|7|N/A||
R05E|0|CH1 RFIR||
R05E|1|CH1 TFIR||
R05E|2|CH1 HB1||
R05E|3|CH1 QEC||
R05E|4|CH1 HB2||
R05E|5|CH1 HB3||
R05E|6|CH 1 INT3||
R05E|7|BBPLL Lock||
R05F|0|CH2 RFIR||
R05F|1|CH2 TFIR||
R05F|2|CH2 HB1||
R05F|3|CH2 QEC||
R05F|4|CH2 HB2||
R05F|5|CH2 HB3||
R05F|6|CH2 INT3||
R05F|7|Open||
R060|0|TX Filter||TX Filter Coefficient Address<7:O>
R061|0|TX Filter||TX Filter coefficient Write Data <7:O>
R062|0|TX Filter||TX Filter coefficient Write Data <15:8>
R063|0|TX Filter||TX Filter coefficient Read Data<7:O>
R064|0|TX Filter||TX Filter coefficient Read Data<15:8>
R065|0|Filter Gain||
R065|1|Start Tx Clock||
R065|2|Write TX||
R065|3|Select Tx CH<1:O>||
R065|5|Number ofTaps<2:O>||
R073|0|Tx1 Attenuation<7:O>||
R074|0|Tx 1 Atten <8>||
R074|1|Open||
R075|0|Tx2 Attenuation<7:O>||
R076|0|Tx 2 Atten <8>||
R076|1|Open||
R077|0|Tx Atten Offset<5:O>||
R077|6|Mask Clr Atten||Mask Clr Atten Update
R077|7|Open||
R078|0|Tx Atten Thresh<7:O>||
R079|0|TX1 Digital||TX1 Digital Attenuation<4:O>
R079|5|TPC Mode TX1||
R079|6|Sel TX1 & TtX2||
R079|7|Open||
R07A|0|TX1 HP Atten<5:O>||
R07A|6|TX1 LO Atten<1:O>||
R07B|0|TX1 LP Atten<7:O>||
R07C|0|TX2 Digital||TX2 Digital Attenuation<4:O>
R07C|5|TPC Mode Tx2||
R07C|6|Immediately U pd||Immediately U pd ate TPC Atten
R07C|7|Open||
R07D|0|Tx2 HP Atten<5:O>||
R07D|6|Tx2 LO Atten<1:O>||
R07E|0|Tx2 LP||Tx2 LP Attenuation<7:O>
R07F|0|Tx 1 Symbol||Tx 1 Symbol Attenuation<6:O>
R07F|7|Open||
R080|0|Tx 2 Symbol||Tx 2 Symbol Attenuation<6:O>
R080|7|Open||
R081|0|Enable Symbol Atten||
R081|1|Use CTRL IN for||Use CTRL IN for symbol Atten
R081|2|Open||
R081|3|Use TX1 Pin &||Use TX1 Pin & Symbol Atten
R081|4|Open||
R08E|0|Tx1 Output1 Phase||Tx1 Output1 Phase Correction<7:O>
R08F|0|TX1 Output1 Gain||TX1 Output1 Gain Correction<7:O>
R090|0|Tx2 Output 1 Phase||Tx2 Output 1 Phase Correction<7:O>
R091|0|Tx2 Output1 Gain||Tx2 Output1 Gain Correction<7:O>
R092|0|TX1 Output 1 Offset||TX1 Output 1 Offset I<7:O>
R093|0|Ttx1 Output1 Offset||Ttx1 Output1 Offset Q<7:O>
R094|0|Tx2 Output 1 Offset||Tx2 Output 1 Offset I<7:O>
R095|0|Tx2 Output 1 Offset||Tx2 Output 1 Offset Q<7:O>
R096|0|Tx1 Output 2 Phase||Tx1 Output 2 Phase Correction<7:O>
R097|0|TX1 Output 2 Gain||TX1 Output 2 Gain Correction<7:O>
R098|0|Tx2 Output 2 Phase||Tx2 Output 2 Phase Correction<7:O>
R099|0|Tx2 Output 2 Gain||Tx2 Output 2 Gain Correction<7:O>
R09A|0|TX1 Output 2 Offset||TX1 Output 2 Offset I<7:O>
R09B|0|Ttx1 Output 2||Ttx1 Output 2 Offset Q<7:O>
R09C|0|Tx2 Output 2 Offset||Tx2 Output 2 Offset I<7:O>
R09D|0|Tx2 Output 2 Offset||Tx2 Output 2 Offset Q<7:O>
R09E|0|Open||
R09F|0|Force Out 1 TX1||Force Out 1 TX1 Phase & Gain
R09F|1|Force Out 1 Tx2||Force Out 1 Tx2 Phase & Gain
R09F|2|Force Out 1 TX1||Force Out 1 TX1 Offset
R09F|3|Force Out 1 Tx2||Force Out 1 Tx2 Offset
R09F|4|Force Out 2 TX1||Force Out 2 TX1 Phase & Gain
R09F|5|Force Out 2 Tx2||Force Out 2 Tx2 Phase & Gain
R09F|6|Force Out 2 TX1||Force Out 2 TX1 Offset
R09F|7|Force Out 2 Tx2||Force Out 2 Tx2 Offset
R0A0|0|Rx NCO Phase||Rx NCO Phase Offset<4:O>
R0A0|5|RXNCO Frequency<1:O>||
R0A0|7|open||
R0A1|0|M<1:0>||
R0A1|2|Quad Cal Soft Reset||
R0A1|3|Phase Enable||
R0A1|4|Gain Enable||
R0A1|5|DC Offset Enable||
R0A1|6|Settle Main Enable||
R0A1|7|Free Run Enable||
R0A2|0|Kexp DC Q <1 :O>||
R0A2|2|Kexp DC I <1:O>||
R0A2|4|Kexp Tx comp <1:0>||
R0A2|6|Kexp Tx<1 20>||
R0A3|0|Kexp Amp <1:O>||
R0A3|2|Kexp Phase <1 :O>||
R0A3|4|Invert Q data||
R0A3|5|Invert I data||
R0A3|6|TX NCO||TX NCO frequency<1:O>
R0A4|0|Settle Count<7:O>||
R0A5|0|Mag Ftest||Mag Ftest Thresh<7:O>
R0A6|0|Mag Ftest||Mag Ftest Thresh2<7:O>
R0A7|0|TX1 SSB Conv||
R0A7|1|TX1 LO Conv||
R0A7|2|Tx1 Convergence||Tx1 Convergence Count<5:O>
R0A8|0|TXZSSB Conv||
R0A8|1|Tx2 LO Conv||
R0A8|2|Tx2 Convergence||Tx2 Convergence Count<5:O>
R0A9|0|Quad Cal Count<7:O>||
R0AA|0|RX Full tabIeAMT||RX Full tabIeAMT table gain<6:O>
R0AA|7|Open||
R0AB|0|Bypass Bias R||
R0AB|1|Vbias ControI<1:O>||
R0AB|3|Gm Stage Lower CM||
R0AB|4|Gm Stage MV HP Pole||
R0AB|5|Gm Stage Time Con||Gm Stage Time Con Override
R0AB|6|Open||
R0AC|0|TX quad Cal Atten||TX quad Cal Atten Word<7:O>
R0AD|0|Threshold||Threshold AccumuIator<3:O>
R0AD|4|Open||
R0AE|0|RX LPF gain<4:O>||
R0AE|5|Open||
R0B0|0|TXDAC Vds I<5:O>||
R0B0|6|Open||
R0B1|0|TXDAC Vds Q<5:O>||
R0B1|6|Open||
R0B2|0|txDAC gn I<5:O>||
R0B2|6|Open||
R0B3|0|tXDAC g n Q<5:0>||
R0B3|6|Open||
R0C0|0|OpAmp A CC<2:O>||
R0C0|3|OpAmpA RZ<1:O>||
R0C0|5|OPAmpA Output||OPAmpA Output Bias<1:O>
R0C0|7|Open||
R0C1|0|OpAmp B CC<2:O>||
R0C1|3|OpAmpB RZ<1:O>||
R0C1|5|OPAmpB Output||OPAmpB Output Bias<1:O>
R0C1|7|Open||
R0C2|0|R1 <4:O>||
R0C2|5|Open||
R0C2|7|Override enable||
R0C3|0|R2<4:O>||
R0C3|5|Open||
R0C4|0|R3<4:O>||
R0C4|5|Open||
R0C5|0|R4<4:O>||
R0C5|5|Open||
R0C6|0|Rp<4:O>||
R0C6|5|Open||
R0C7|0|C1<5:O>||
R0C7|6|Open||
R0C8|0|C2<5:O>||
R0C8|6|Open||
R0C9|0|Cp<5:O>||
R0C9|6|Open||
R0CA|0|Tuner Resample Phase||
R0CA|1|Tuner Resample||
R0CA|2|PD Tune||
R0CA|3|Open||
R0CA|5|Tune Control<1:O>||
R0CA|7|Open||
R0CB|0|R2b<4:O>||
R0CB|5|R2b Ovr||
R0CB|6|Open||
R0CB|7|Bypass Bias R||
R0CC|0|BBF2 Comp Q||
R0CC|1|BBF2 Comp I||
R0CC|2|BBF1 Comp||
R0CC|3|BBF1 Comp I||
R0CC|4|Open||
R0D0|0|AmpBias<1:O>||
R0D0|2|Cc<1:o>||
R0D0|4|Rgm<1:O>||
R0D0|6|Bias<1:O>||
R0D1|0|Resistor<3:O>||
R0D1|4|Open||
R0D2|0|Capacitor<5:O>||
R0D2|6|Open||
R0D3|0|Open||
R0D3|5|LO Common Mode<1:O>||
R0D3|7|Open||
R0D6|0|TX BBF Tune||TX BBF Tune Divider<7:O>
R0D7|0|TX BBF Tune||TX BBF Tune Divider<8>
R0D7|1|Tuner Mode<2:O>||
R0D7|4|EvaITime||
R0D7|5|Tune Comp Mask<1:O>||
R0D7|7|Open||
R0F0|0|Rx Filter Addr<7:O>||
R0F1|0|Rx Filter||Rx Filter Coefficient Write Data<7:O>
R0F2|0|Rx Filter||Rx Filter Coefficient Write Data<15:8>
R0F3|0|Rx Filter||Rx Filter Coefficient Read Back Data<7:O>
R0F4|0|Rx Filter||Rx Filter Coefficient Read Back Data<15:8>
R0F5|0|open||
R0F5|1|Start Chock||
R0F5|2|Write RX||
R0F5|3|Select Rx Ch<1:O>||
R0F5|5|Number ofTaps||
R0F6|0|Filter gain<1:O>||
R0F6|2|Open||
R0FA|0|RX1 Gain Control||RX1 Gain Control Setup<1:O>
R0FA|2|Rx 2 Gain Control||Rx 2 Gain Control Setup<1:O>
R0FA|4|Slow Attack HybHd||Slow Attack HybHd Mode
R0FA|5|Dec Pwr for Gain||Dec Pwr for Gain Lock Exit
R0FA|6|Dec Pwr for Lock||Dec Pwr for Lock Level
R0FA|7|Dec Pwr for Low Pwr||
R0FB|0|Manual Gain Control||Manual Gain Control RX1
R0FB|1|Manual Gain Control||Manual Gain Control Rx 2
R0FB|2|Enable Digital Gain||
R0FB|3|Use Full Gain Table||
R0FB|4|Open||
R0FB|6|Gain Unlock Control||
R0FB|7|Soft Reset||
R0FC|0|ADC Overrange||ADC Overrange Sample Size<2:0>
R0FC|3|Use AGC for LMWLPF||Use AGC for LMWLPF Gain
R0FC|4|IndDec LMT Gain||
R0FC|5|Manual KTRLJM Incr||Manual KTRLJM Incr Gain Step Size<2:O>
R0FD|0|Maximum Full||Maximum Full TabIeAMT Table Index<6:O>
R0FD|7|Open||
R0FE|0|Peak Overload Wait||Peak Overload Wait Time<4:O>
R0FE|5|Manual KTRLJM Decr||Manual KTRLJM Decr Gain Step Size<2:O>
R0FF|0|Open||
R100|0|Maximum Digital||Maximum Digital Gain<4:O>
R100|5|Dig Gain Step||Dig Gain Step Size<2:O>
R101|0|AGC Lock Level||AGC Lock Level Gastv AGC Inner High Threshold Glow <6:O>
R101|7|Enable Dig Sat Ovrg||
R102|0|ADC Noise||ADC Noise Correction Factor<9:2>
R103|0|ADC Noise||ADC Noise Correction Factor<1:O>
R103|2|Dec Step Size for:||Dec Step Size for: Large LMT Overloade Full Table Case 1i3 <2:O>
R103|5|LMT Detector||LMT Detector Settling Time<2:O>
R104|0|ADC Small Overload||ADC Small Overload Threshold<7:O>
R105|0|ADC Large Overload||ADC Large Overload ThreshoId<7:O>
R106|0|Decrement Step Size||Decrement Step Size for: Large LPF Gain Change a Full Table Case 4i1<3:O>
R106|4|Fast Attack Only.||Fast Attack Only. Decrement Step Size for: Small LPF Gain Change l Full Table Case 1t2 <2:O>
R106|7|Open||
R107|0|Small LMT Overload||Small LMT Overload Threshold<5:O>
R107|6|For PD Reset RX1||
R107|7|Force PD Reset Rx2||
R108|0|Large LMT Overload||Large LMT Overload ThreshoId<5:O>
R108|6|Open||
R109|0|Rx1 Manual Full||Rx1 Manual Full tabIeAMT table Gain Index<6:O>
R109|7|Power Meas in State||Power Meas in State 5<3>
R10A|0|RX1 Manual LPF Gain||RX1 Manual LPF Gain <4:O>
R10A|5|Power Meas in State||Power Meas in State 5<2:O>
R10B|0|Rx1 ManuaVForced||Rx1 ManuaVForced Digital Gain<4:O>
R10B|5|Force RX1 Digital||Force RX1 Digital Gain
R10B|6|Open||
R10C|0|Rx2 Manual Full||Rx2 Manual Full tablea LMT table Gain Index<6:O>
R10C|7|Open||
R10D|0|Rx2 Manual LPF||Rx2 Manual LPF Gain<4:O>
R10D|5|Open||
R10E|0|Rx2 ManuaVForced||Rx2 ManuaVForced Digital Gain<4:O>
R10E|5|Force Rx2 Digital||Force Rx2 Digital Gain
R10E|6|Open||
R110|0|Enable Incr Gain||
R110|1|Don Unlock Gain If||Don Unlock Gain If Lg ADC or LMT Ovrg
R110|2|Goto Optimized Gain||Goto Optimized Gain if Exit Rx State
R110|3|DonT Unlock Gain if||DonT Unlock Gain if Energy Lost
R110|4|Goto Set Gain if||Goto Set Gain if Exit Rx State
R110|5|Goto Set Gain if EN||Goto Set Gain if EN AGC High
R110|6|Goto Opt Gain if||Goto Opt Gain if Energy Lost or EN AGC High
R110|7|Enable Gahwlnc||Enable Gahwlnc after Gain Lock
R111|0|Settling DeIay<4:O>||
R111|5|Goto Max Gahwor||Goto Max Gahwor OptGam EN AGC High
R111|6|Enable LAAT Gain||Enable LAAT Gain Inc for Lock Level
R111|7|Use Last Lock Level||Use Last Lock Level for Set Gain
R112|0|Energy lost||Energy lost threshoId<5:O>
R112|6|Post Lock Level||Post Lock Level Step Size for: LPF Tablee Full Table <1 :O>
R113|0|Stronger Signal||Stronger Signal ThreshoId<5:O>
R113|6|Post Lock Level||Post Lock Level Step for LMT Table <1:O>
R114|0|Low Power||Low Power ThreshoId<6:O>
R114|7|DonT unlock gain if||DonT unlock gain if ADC Ovrg
R115|0|Open||
R115|7|DonT unlock gain if||DonT unlock gain if Stronger Signal
R116|0|Optimize Gain||Optimize Gain Offset<3:O>
R116|4|Open||
R116|5|Final Over Range||Final Over Range Count<2:O>
R117|0|Energy Detect||Energy Detect count<4:O>
R117|5|Increment Gain Step||Increment Gain Step eLPHLMD<2:O>
R118|0|AGCLL Max||AGCLL Max Increase<5:O>
R118|6|Open||
R119|0|Gain Lock Exit||Gain Lock Exit Count<5:O>
R119|6|Open||
R11A|0|Initial LMT Gain||Initial LMT Gain Limit<6:O>
R11A|7|Open||
R11B|0|Increment Time<7:O>||
R120|0|AGC Inner Low||AGC Inner Low ThreshoId<6:O>
R120|7|Prevent Gain Inc||
R121|0|Small LMT Overload||Small LMT Overload Exceeded Counter<3:O>
R121|4|Large LMT Overload||Large LMT Overload Exceeded Counter<3:O>
R122|0|Small ADC Overload||Small ADC Overload Exceeded Counter<3:O>
R122|4|Large ADC Overload||Large ADC Overload Exceeded Counter<3:O>
R123|0|AGC Inner Low||AGC Inner Low Threshold Exceeded Step Size<2:O>
R123|3|lmmed. Gain Change||lmmed. Gain Change if Lg ADC Overload
R123|4|AGC Inner High||AGC Inner High Threshold Exceeded Step Size<2:O>
R123|7|lmmed. Gain Change||lmmed. Gain Change if Lg LMT Overload
R124|0|Gain update||Gain update counter<7:O>
R125|0|Gain update||Gain update counter<15:8>
R126|0|Open||
R127|0|Open||
R128|0|Dig Saturation||Dig Saturation Exceeded Counter<3:O>
R128|4|Enable Sync for||Enable Sync for Gain Counter
R128|5|Double Gain Counter||
R128|6|Open||
R129|0|AGC Outer Low||AGC Outer Low ThreshoId<3:O>
R129|4|AGC Outer High||AGC Outer High ThreshoId<3:O>
R12A|0|AGC Outer Low||AGC Outer Low Threshold Exceeded Step Size<3:O>
R12A|4|AGC Outer High||AGC Outer High Threshold Exceeded Step Size<3:O>
R12C|0|Ext LNA High||Ext LNA High Gain<5:O>
R12C|6|Open||
R12D|0|Ext LNA LOW||Ext LNA LOW Gain<5:O>
R12D|6|Open||
R130|0|Gain Table||Gain Table Address<6:O>
R130|7|Open||
R131|0|Mixer Gm Gain <4:O>||
R131|5|LNA Gain <1 :O>||
R131|7|Ext LNA Ctrl||
R132|0|LPF Gain <4:O>||
R132|5|TIA Gain||
R132|6|Open||
R133|0|Digital Gain <4:O>||
R133|5|RF DC Cal||
R133|6|Open||
R134|0|Mixer Gm Gain <4:O>||
R134|5|LNA Gain <1:O>||
R134|7|Ext LNA Ctrl||
R135|0|LPF Gain <4:O>||
R135|5|TIA Gain||
R135|6|Open||
R136|0|Digital Gain <4:O>||
R136|5|RF DC Cal||
R136|6|Open||
R137|0|Open||
R137|1|Start Gain Table||Start Gain Table Clock
R137|2|Write Gain Table||
R137|3|Receiver SeIect<1:O>||
R137|5|Open||
R138|0|Gm Sub Table||Gm Sub Table Address<7:O>
R139|0|Gm Sub Table Gain||Gm Sub Table Gain Word Write<6:O>
R139|7|Open||
R13A|0|Gm Sub Table Bias||Gm Sub Table Bias Word Write<4:O>
R13A|5|Open||
R13B|0|Gm Sub Table||Gm Sub Table Control Word Write<5:O>
R13B|6|Open||
R13C|0|Gm Sub Table Gain||Gm Sub Table Gain Word Read<6:O>
R13C|7|Open||
R13D|0|Gm Sub Table Bias||Gm Sub Table Bias Word Read<4:O>
R13D|5|Open||
R13E|0|Gm Sub Table||Gm Sub Table Control Word Read<5:O>
R13E|6|Open||
R13F|0|Open||
R13F|1|Start Gm Sub Table||Start Gm Sub Table Clock
R13F|2|Write Gm Sub Table||
R13F|3|Open||
R140|0|Calibration Table||Calibration Table Addr<7:O>
R141|0|Calib Table Gain||Calib Table Gain DifVError Word<5:O>
R141|6|Open||
R142|0|Calib Table Gain||Calib Table Gain Error<4:O>
R142|5|Open||
R143|0|Start Calib Table||Start Calib Table Clock
R143|1|Write LNA Gain Diff||
R143|2|Write LNA Error||Write LNA Error Table
R143|3|Write Mixer Error||Write Mixer Error Table
R143|4|Read Select||
R143|5|Calib Table||Calib Table SeIect<1:O>
R143|7|Open||
R144|0|LNA Calib Table||LNA Calib Table Gain Difference Word<5:O>
R144|6|Open||
R145|0|Max Mixer||Max Mixer Calibration Gain Index<4:O>
R145|5|Open||
R146|0|Temp Gain||Temp Gain Coefficient<7:O>
R147|0|Settle Time<5:O>||
R147|6|Force Temp Sensor||Force Temp Sensor for Cal
R147|7|Enable Dig Gain Corr||
R148|0|Gain Cal Meas||Gain Cal Meas Duration<3:O>
R148|4|Open||
R149|0|Cal Temp Sense||Cal Temp Sense word<7:O>
R150|0|Measurement||Measurement duration 0 <3:O>
R150|4|Measurement||Measurement duration 1 <3:O>
R151|0|Measurement||Measurement duration 2 <3:O>
R151|4|Measurement||Measurement duration 3 <3:O>
R152|0|Weighted Multiplier||Weighted Multiplier O <7:O>
R153|0|Weighted multiplier||Weighted multiplier 1 <7:O>
R154|0|Weighted Multiplier||Weighted Multiplier 2 <7:O>
R155|0|Weighted Multiplier||Weighted Multiplier 3 <7:O>
R156|0|RSSI DeIay<7:O>||
R157|0|RSSI Wait<7:O>||
R158|0|Default RSSI Meas||Default RSSI Meas Mode
R158|1|Enable ADCPower||Enable ADCPower Meas.
R158|2|RSSI Mode||RSSI Mode SeIect<2:O>
R158|5|Start RSSI Meas||Start RSSI Meas Node M
R158|6|RFIR for RSSI||RFIR for RSSI measurement<1:O>
R159|0|ADC Power||ADC Power Measurement Duration 0 <3:0>
R159|4|ADC Power||ADC Power Measurement Duration 1<3:O>
R15A|0|Weighted ADC Power||Weighted ADC Power Multiplier O <7:O>
R15B|0|Weighted ADC Power||Weighted ADC Power Multiplier 1 <7:O>
R15C|0|Dec Power||Dec Power Measurement Duration <3:O>
R15C|4|Default Mode ADC||Default Mode ADC Power
R15C|5|Enable Dec Pwr Meas||
R15C|6|Use HB1 Out for Dec||Use HB1 Out for Dec pwr Meas
R15C|7|Use HB3 Out for ADC||Use HB3 Out for ADC Pwr Meas
R15D|0|dBGam Read-back||dBGam Read-back Channel
R15D|1|Max LNA Gain<6:O>||
R160|0|CH1 ADC power <7:O>||
R161|0|CH1 Rx filter power||CH1 Rx filter power <7:O>
R162|0|CH2 ADC power <7:O>||
R163|0|CH2 Rx filter power||CH2 Rx filter power <7:O>
R168|0|Rx Quad Cal Level||Rx Quad Cal Level <3 :O>
R168|4|Open||
R169|0|Enable Tracking||Enable Tracking Mode CH1
R169|1|Enable Tracking||Enable Tracking Mode CH 2
R169|2|Enable Corr Word||Enable Corr Word Decimation
R169|3|Free Run Mode||
R169|4|Fixed DC Cal Wait||Fixed DC Cal Wait Time
R169|5|Use Settle Count||Use Settle Count for DC Cal Wait
R169|6|Enable Gain Corr||
R169|7|Enable Phase Corr||
R16A|0|K exp Phase<4:O>||
R16A|5|Must be 2 b11||
R16A|7|Soft Reset||
R16B|0|K exp AmpIitude<4:O>||
R16B|5|Open||
R16B|7|Prevent Pos Loop||Prevent Pos Loop Gain
R16C|0|Calibration||Calibration count<7:O>
R16D|0|Settle count<7:O>||
R16E|0|Rx Full tabIeAMT||Rx Full tabIeAMT table gain<6:O>
R16E|7|Open||
R16F|0|Rx LPF gain<4:O>||
R16F|5|Correction Word||Correction Word Decimation M<2:0>
R170|0|Rx1 Input A Phase||Rx1 Input A Phase Correction<7:O>
R171|0|Rx1 Input A Gain||Rx1 Input A Gain Correction<7:O>
R172|0|Rx2 Input A Phase||Rx2 Input A Phase Correction<7:O>
R173|0|Rx2 Input A Gain||Rx2 Input A Gain Correction<7:O>
R174|0|Rx1 Input A Q DC||Rx1 Input A Q DC Offset<7:O>
R175|0|RX1 Input A Q DC||RX1 Input A Q DC Offset<9:8>
R175|2|RX1 Input AW DC||RX1 Input AW DC Offset<5:O>
R176|0|RX1 Input AW DC||RX1 Input AW DC Offset<9:6>
R176|4|Rx2 Input A Q DC||Rx2 Input A Q DC Offset<3:O>
R177|0|Rx2 Input A Q DC||Rx2 Input A Q DC Offset<9:4>
R177|6|Rx2 Input AW DC||Rx2 Input AW DC Offset<1:O>
R178|0|Rx2 Input A W DC||Rx2 Input A W DC Offset<9:2>
R179|0|Rx1 Input B&C Phase||Rx1 Input B&C Phase Correction<7:O>
R17A|0|Rx1 Input B&C Gain||Rx1 Input B&C Gain Correction<7:O>
R17B|0|Rx2 Input B&C Phase||Rx2 Input B&C Phase Correction<7:O>
R17C|0|Rx2 Input B&C Gain||Rx2 Input B&C Gain Correction<7:O>
R17D|0|RX1 Input B&C Q DC||RX1 Input B&C Q DC Offset<7:O>
R17E|0|RX1 Input B&C Q DC||RX1 Input B&C Q DC Offset<9:8>
R17E|2|RX1 Input B&C I DC||RX1 Input B&C I DC Offset<5:O>
R17F|0|RX1 Input B&C I DC||RX1 Input B&C I DC Offset<9:6>
R17F|4|Rx2 Input B&C Q DC||Rx2 Input B&C Q DC Offset<3:O>
R180|0|RX2 Input B&C Q DC||RX2 Input B&C Q DC Offset<9:4>
R180|6|Rx2 Input B&C I DC||Rx2 Input B&C I DC Offset<1:O>
R181|0|RX2 Input B&C I DC||RX2 Input B&C I DC Offset<9:2>
R182|0|RX1 Input A Force||RX1 Input A Force PWGain
R182|1|Rx2 Input A Force||Rx2 Input A Force PWGain
R182|2|RX1 Input A Force||RX1 Input A Force offset
R182|3|Rx2 Input A Force||Rx2 Input A Force offset
R182|4|RX1 Input B&C Force||RX1 Input B&C Force Ph GaH1
R182|5|Rx2 Input B&C Force||Rx2 Input B&C Force Ph GaH1
R182|6|RX1 Input B&C Force||RX1 Input B&C Force offset
R182|7|Rx2 Input B&C Force||Rx2 Input B&C Force offset
R185|0|Wait Count<7:O>||
R186|0|RF DC Offset||RF DC Offset Count<7:O>
R187|0|RF DC Calibration||RF DC Calibration Count<3:O>
R187|4|DAC FS<1:O>||
R187|6|Open||
R188|0|RF DC Offset||RF DC Offset Attenuation<4:O>
R188|5|RF DC Offset Table||RF DC Offset Table Update Count<2:O>
R189|0|Open||
R189|4|Invert RX1 RF DC||Invert RX1 RF DC CGout mkwd
R189|5|Invert Rx2 RF DC||Invert Rx2 RF DC CGout Word
R189|6|Invert RX1 RF DC||Invert RX1 RF DC CGin Word
R189|7|Invert Rx2 RF DC||Invert Rx2 RF DC CGin Word
R18A|0|Open||
R18B|0|DC Offset||DC Offset Update<2:O>
R18B|3|Enable RF Offset||Enable RF Offset Tracking
R18B|4|Reset Acc on Gain||Reset Acc on Gain Change
R18B|5|Enable BB DC Offset||Enable BB DC Offset Tracking
R18B|6|Enable Fast Settle||Enable Fast Settle Mode
R18B|7|Use Wait Counter||Use Wait Counter for RF DC Init Cal
R18C|0|RF Minimum||RF Minimum Calibration Gain Index<6:O>
R18C|7|Open||
R18D|0|RF SOI||RF SOI Thresh0Id<6:O>
R18D|7|Open||
R18E|0|Open||
R18F|0|Open||
R190|0|BB DC M Shift<4:O>||
R190|5|BB Tracking||BB Tracking Decimate<1:O>
R190|7|Increase Count||Increase Count Duration
R191|0|BB DC Tracking Fast||BB DC Tracking Fast Settle M Shift<4:O>
R191|5|Force Rx Null||
R191|6|Update Tracking Word||
R191|7|Read Back CH Sel||
R192|0|BB DC Tracking Fast||BB DC Tracking Fast Settle Duration<7:O>
R193|0|BB DC Offset||BB DC Offset Count<7:O>
R194|0|BB DC Offset||BB DC Offset Atten<3:O>
R194|4|Open||
R19A|0|RX1 BB DC Offset||RX1 BB DC Offset Correction word I<14:8>
R19A|7|Open||
R19B|0|RX1 BB DC Offset||RX1 BB DC Offset Correction word l<7:O>
R19C|0|RX1 BB DC Offset||RX1 BB DC Offset Correction word Q<14:8>
R19C|7|Open||
R19D|0|RX1 BB DC Offset||RX1 BB DC Offset Correction word Q<7:O>
R19E|0|RX2 BB DC Offset||RX2 BB DC Offset Correction word I<14:8>
R19E|7|Open||
R19F|0|RX2 BB DC Offset||RX2 BB DC Offset Correction word l<7:O>
R1A0|0|RX2 BB DC Offset||RX2 BB DC Offset Correction word Q<14:8>
R1A0|7|Open||
R1A1|0|RX2 BB DC Offset||RX2 BB DC Offset Correction word Q<7:O>
R1A2|0|RXVRX2 BB DC Offset||RXVRX2 BB DC Offset Tracking correction word I<14:8>
R1A2|7|Open||
R1A3|0|RXURX2 BB DC Offset||RXURX2 BB DC Offset Tracking correction word I<7:O>
R1A4|0|RXVRX2 BB DC Offset||RXVRX2 BB DC Offset Tracking correction word Q<14:8>
R1A4|7|Open||
R1A5|0|RXVRX2 BB DC Offset||RXVRX2 BB DC Offset Tracking correction word Q<7:O>
R1A7|0|Rx1 RSSI SymboI<8:1>||
R1A8|0|Rx1 RSSI||Rx1 RSSI preambIe<8:1>
R1A9|0|Rx2 RSSI symboI<8:1>||
R1AA|0|Rx2 RSSI||Rx2 RSSI preambIe<8:1>
R1AB|0|Rx1 RSSI symbol <O>||
R1AB|1|Rx2 RSSI symbol <O>||
R1AB|2|Open||
R1AC|0|Rx1 RSSI preamble||Rx1 RSSI preamble <O>
R1AC|1|Rx2 RSSI preamble||Rx2 RSSI preamble <O>
R1AC|2|Open||
R1AD|0|Rx Path Gain<8:1>||
R1AE|0|Rx Path Gain<O>||
R1AE|1|Open||
R1B0|0|RX1 LNA Gain<1 10>||
R1B0|2|Rx1 LNA Bypass||
R1B0|3|Force RX1 LNA Gain||
R1B0|4|Rx2 LNA Gain<1 10>||
R1B0|6|Rx2 LNA Bypass||
R1B0|7|Force Rx2 LNA Gain||
R1B1|0|Rx LNA Bias||Rx LNA Bias Coarse<3:O>
R1B1|4|Open||
R1B2|0|RX LNA BiaS<4:O>||
R1B2|5|Rx LNA p-Cascode||Rx LNA p-Cascode Bias<2:O>
R1B3|0|Rx LNA p- Cascode||Rx LNA p- Cascode Bias Fine<4:3>
R1B3|2|Open||
R1C0|0|Rx Mix Gm pload||Rx Mix Gm pload <1:O>
R1C0|2|Open||
R1C0|5|Rx Mix Gm CM||Rx Mix Gm CM Out<2:O>
R1C1|0|RX1 Mix Gm Gain<5:O>||
R1C1|6|Force RX1 Mix Gm||
R1C1|7|Open||
R1C2|0|RX1 Mix Gm Bias<4:O>||
R1C2|5|Open||
R1C3|0|Rx2 Mix Gm Gain<5:O>||
R1C3|6|Force Rx2 Mix Gm||
R1C3|7|Open||
R1C4|0|Rx2 Mix Gm Bias<4:O>||
R1C4|5|Open||
R1C8|0|Input A RX2 Q<9:8>||
R1C8|2|Input A RX2 I<9:8>||
R1C8|4|Input A RX1 I<9:8>||
R1C8|6|Input A RX1 Q<9:8>||
R1C9|0|Input A RX1 I<7:O>||
R1CA|0|Input A RX1 Q<7:O>||
R1CB|0|Input A RX2 I<7:O>||
R1CC|0|Input A RX2 Q<7:O>||
R1CD|0|Inputs B&C RX1||Inputs B&C RX1 I<7:O>
R1CE|0|Inputs B&C RX1||Inputs B&C RX1 Q<7:O>
R1CF|0|Inputs B&C RX2||Inputs B&C RX2 I<7:O>
R1D0|0|Inputs B&C RX2||Inputs B&C RX2 Q<7:O>
R1D1|0|Inputs B&C RX2||Inputs B&C RX2 Q<9:8>
R1D1|2|Inputs B&C RX2||Inputs B&C RX2 l<9:8>
R1D1|4|Inputs B&C RX1||Inputs B&C RX1 l<9:8>
R1D1|6|Inputs B&C RX1||Inputs B&C RX1 Q<9:8>
R1D2|0|Open||
R1D2|2|Force CGin DAC||
R1D2|3|Open||
R1D5|0|Rx Mix LO CM<5:O>||
R1D5|6|Open||
R1D6|0|Rx CGB Seg||Rx CGB Seg EnabIe<5:O>
R1D6|6|Open||
R1D7|0|RX CGB Bias<3:O>||
R1D7|4|Rx CGB Input CM||Rx CGB Input CM SeI<1:O>
R1D7|6|Open||
R1DB|0|TIA1 Override R||
R1DB|1|TIA1 Override C||
R1DB|2|TIA2 Override R||
R1DB|3|TIA2 Override C||
R1DB|4|Open||
R1DB|5|TIA Sel CC<2:O>||
R1DC|0|TIA1 C LSB<5:O>||
R1DC|6|TIA1 RF<1:O>||
R1DD|0|TIA1 C MSB<6:O>||
R1DD|7|Open||
R1DE|0|TIA2 C LSB<5:O>||
R1DE|6|TIA2 RF<1:O>||
R1DF|0|TIA2 C MSB<6:O>||
R1DF|7|Open||
R1E0|0|RX1 BBF R1A<5:O>||
R1E0|6|Open||
R1E0|7|Force RX1 Resistors||
R1E1|0|RX2 BBF R1A<5:O>||
R1E1|6|Open||
R1E1|7|Force Rx2 Resistors||
R1E2|0|RX1 PD Tune||
R1E2|1|RX1 Tune Resampl e||
R1E2|2|RX1 Tune Resann pm||RX1 Tune Resann pm Phase
R1E2|3|Open||
R1E3|0|Rx2 PD Tune||
R1E3|1|Rx2 Tune Resampl e||
R1E3|2|Rx2 Tune Resann pm||Rx2 Tune Resann pm Phase
R1E3|3|Open||
R1E4|0|RX1 BBF R5<7:O>||
R1E5|0|RX2 BBF R5<7:O>||
R1E6|0|RX BBF R2346<2:O>||
R1E6|3|Open||
R1E6|7|Tune Override||
R1E7|0|RX BBF C1 MSB<5:O>||
R1E7|6|Open||
R1E8|0|RX BBF C1 LSB<6:O>||
R1E8|7|Open||
R1E9|0|RX BBF C2 MSB<5:O>||
R1E9|6|Open||
R1EA|0|RX BBF C2 LSB<6:O>||
R1EA|7|Open||
R1EB|0|RX BBF C3 MSB<5:O>||
R1EB|6|Open||
R1EC|0|RX BBF C3 LSB<6:O>||
R1EC|7|Open||
R1ED|0|RX BBF CC1 Ctr<6:O>||
R1ED|7|Open||
R1EE|0|Open||
R1EE|3|Rx BBF R21 Ctr<1:O>||
R1EE|5|RX1 BBF Pow Ctr<1:O>||
R1EE|7|Must be zero||
R1EF|0|RX BBF CC2 Ctr<6:O>||
R1EF|7|Open||
R1F0|0|Rx BBF R22 Ctr<1:O>||
R1F0|1|RX BBF POW2 Ctr<1||RX BBF POW2 Ctr<1 10>
R1F0|4|Rx BBF RZ3 Ctr<1:O>||
R1F0|6|Rx BBF Pow3 Ctr<1:O>||
R1F1|0|RX BBF CC3 Ctr<6:O>||
R1F1|7|Open||
R1F2|0|RX BBF R5 Tune<7:O>||
R1F3|0|Rx2 BBF Tune Comp||
R1F3|1|Rx2 BBF Tune Comp I||
R1F3|2|RX1 BBF Tune Comp||
R1F3|3|RX1 BBF Tune Comp I||
R1F3|4|Rx BBF R5 Tune||
R1F3|5|Rx BBF Tune Ctr<1:O>||
R1F3|7|RXBBF Bypass Bias R||
R1F4|0|RX1 BBF Pole||RX1 BBF Pole Gain<2:O>
R1F4|3|RX1 BBF BQ Gain<1:O>||
R1F4|5|RX1 BBF Force Gain||
R1F4|6|Open||
R1F5|0|Rx2 BBF Pole||Rx2 BBF Pole Gain<2:O>
R1F5|3|Rx2 BBF BQ Gain<1:O>||
R1F5|5|Rx2 BBF Force Gain||
R1F5|6|Open||
R1F8|0|RX BBF Tune||RX BBF Tune Divide<7:O>
R1F9|0|RX BBF Tune||RX BBF Tune Divide<8>
R1F9|1|Rx Tune Mode<2:O>||
R1F9|4|RxTune Evaltime||
R1F9|5|Tune Comp Mask <1:O>||
R1F9|7|Open||
R1FA|0|Pole Gain Tune<1:O>||
R1FA|2|Open||
R1FB|0|RX Tune BBBW||RX Tune BBBW MHz<4::O>
R1FB|5|Open||
R1FC|0|RX Tune BBBW||RX Tune BBBW kHz<6:O>
R1FC|7|Open||
R200|0|Not Used||
R201|0|FB DAC Clk||FB DAC Clk DeIay1<7:O>
R202|0|FB DAC Clk||FB DAC Clk DeIay2<7:O>
R203|0|Flash Sample Clk||Flash Sample Clk Delay 3p<7:O>
R204|0|Flash Sample Clk||Flash Sample Clk Delay 3n<7:O>
R205|0|Test MUX 2i<7:O>||
R206|0|Test MUX 2q<7:O>||
R207|0|Integrator 1||Integrator 1 Resistance<7:O>
R208|0|Integrator 1||Integrator 1 Capacitance<7:O>
R209|0|Integrator 23||Integrator 23 Resistance<7:O>
R20A|0|Integrator 2||Integrator 2 Resistance<7:O>
R20B|0|Integrator 2||Integrator 2 Capacitance<7:O>
R20C|0|Integrator 3||Integrator 3 Resistance<7:O>
R20D|0|Integrator 3||Integrator 3 Capacitance<7:O>
R20E|0|Integrator||Integrator Amplifier Compensation Capacitor<7:O>
R20F|0|Integrator 1 FB DAC||Integrator 1 FB DAC Current Source<7:O>
R210|0|Integrator 1 FB DAC||Integrator 1 FB DAC Cascade Bias Current<7:O>
R211|0|Integrator 1 FB DAC||Integrator 1 FB DAC Current Source<7:O>
R212|0|Integrator 2 FB DAC||Integrator 2 FB DAC Current Source<7:O>
R213|0|Integrator 2 FB DAC||Integrator 2 FB DAC Cascade Bias Current<7:O>
R214|0|Integrator 2 FB DAC||Integrator 2 FB DAC Current Source<7:O>
R215|0|Integrator 3 FB DAC||Integrator 3 FB DAC Current Source<7:O>
R216|0|Integrator 3 FB DAC||Integrator 3 FB DAC Cascade Bias Current<7:O>
R217|0|Integrator 3 FB DAC||Integrator 3 FB DAC Current Source<7:O>
R218|0|FB DAC Bias||FB DAC Bias Current<7:O>
R219|0|Integrator 1 1st||Integrator 1 1st Stage Current<7:O>
R21A|0|Integrator 1 1st||Integrator 1 1st Stage Cascode Current<7:O>
R21B|0|Integrator 1 2m||Integrator 1 2m Stage Current<7:O>
R21C|0|Integrator 2 1st||Integrator 2 1st Stage Current<7:O>
R21D|0|Integrator 2 1st||Integrator 2 1st Stage Cascode Current<7:O>
R21E|0|Integrator 2 2m||Integrator 2 2m Stage Current<7:O>
R21F|0|Integrator 3 1st||Integrator 3 1st Stage Current<7:O>
R220|0|Integrator 3 1st||Integrator 3 1st Stage Cascode Current<7:O>
R221|0|Integrator 3 2m||Integrator 3 2m Stage Current<7:O>
R222|0|Flash Bias||Flash Bias Current<7:O>
R223|0|Flash Ladder||Flash Ladder Bias<7:O>
R224|0|Flash Ladder||Flash Ladder Cascode Current<7:O>
R225|0|Flash Ladder||Flash Ladder Bias<7:O>
R226|0|Reset<7:O>||
R230|0|Bypass Ld Synth||
R230|1|PFD Clk Edge||
R230|2|PFD Width <1 :0>||
R230|4|Open||
R230|5|Div Test En||
R230|6|Open||
R231|0|Synthesizer Integer||Synthesizer Integer Word<7:O>
R232|0|Synthesizer Integer||Synthesizer Integer Word<10:8>
R232|3|Open||
R232|6|SDM Power Down||
R232|7|SDM Bypass||
R233|0|Synthesizer||Synthesizer Fractional Word<7:O>
R234|0|Synthesizer||Synthesizer Fractional Word <15:8>
R235|0|Synthesizer||Synthesizer Fractional Word <22:16>
R235|7|Open||
R236|0|Force ALC Word<6:O>||
R236|7|Force ALC Enable||
R237|0|Force VCO Tune<7:O>||
R238|0|Force VCO Tune<8||
R238|1|Force VCO Tune||Force VCO Tune Enable
R238|2|Open||
R238|3|VCO Cal Offset<3:O>||
R238|7|Bypass Load Dekn||
R239|0|VCO Varactor<3:O>||
R239|4|Init ALC VaIue<3:O>||
R23A|0|VCO Output||VCO Output LeveI<3:O>
R23A|4|Open||
R23A|6|PORb VCO Logic||
R23A|7|Open||
R23B|0|Charge Pump||Charge Pump Current<5:O>
R23B|6|Vtune Out||
R23B|7|Set to 1||
R23C|0|Charge Pump||Charge Pump Offset<5:O>
R23C|6|Open||
R23C|7|Synth Re-Cal||
R23D|0|Cp Test <1 :O>||
R23D|2|Cp Cal Enable||
R23D|3|F Cpcal||
R23D|4|Offset Off||
R23D|5|Open||
R23D|6|Dither Mode||
R23D|7|Half Vco Cal Clk||
R23E|0|Loop Filter C1 <3:O>||
R23E|4|Loop Filter C2<3:O>||
R23F|0|Loop Filter C3<3:O>||
R23F|4|Loop Filter R1 <3:O>||
R240|0|Loop Filter R3<3:O>||
R240|4|Loop Hher Bypass C1||
R240|5|Loop Hher Bypass C2||
R240|6|Loop Hher Bypass R1||
R240|7|Loop Hher Bypass R3||
R241|0|Forced CP Cal||Forced CP Cal Word<3:O>
R241|4|Number SDM Dither||Number SDM Dither Bits<3:O>
R242|0|VCO Bias Ref<2:O>||
R242|3|VCO Bias Tcf<1:O>||
R242|5|Must be zeros||
R242|7|Open||
R243|0|Prescale Bias <1:O>||
R243|2|ALC Enable||
R243|3|Bypass Prescale R||
R243|4|VCC> Comp Bypass||VCC> Comp Bypass BBSFR
R243|5|Open||
R243|7|VCO Bypass BBSDAC||
R244|0|CP Cal Word<3:O>||
R244|4|VCO Cal Busy||
R244|5|CP Cal Done||
R244|6|Comp Out||
R244|7|CP Cal Valid||
R245|0|VCO Cal Ref Tcf<2:O>||
R245|3|VCO Cal Ref Monitor||
R245|4|Open||
R246|0|Power Down VCO||Power Down VCO Bufffer
R246|1|Power Down Cal Tcf||
R246|2|Pwr Down Varact Ref||Pwr Down Varact Ref Tcf
R246|3|Power Down Varactor||Power Down Varactor Ref
R246|4|Open||
R247|0|Open||
R247|1|Lock||
R247|2|Open||
R247|6|CP Ovrg Low||
R247|7|CP Ovrg High||
R248|0|VCO LDO Vdrop||VCO LDO Vdrop SeI<1:O>
R248|2|VCO LDO SeI<2:O>||
R248|5|VCO LDO Inrush<1:O>||
R248|7|VCO LDO Bypass||
R249|0|FB clock adv <1 :O>||
R249|2|VCO Cal Count <1 :O>||
R249|4|VCO Cal ALC Wait||VCO Cal ALC Wait <2:0>
R249|7|VCO Cal||
R24A|0|Lock Detect Mode<1||Lock Detect Mode<1 :O>
R24A|2|Lock Detect||Lock Detect Count<1:O>
R24A|4|Open||
R24B|0|CP Level Threshold||CP Level Threshold High<2:O>
R24B|3|CP Level Threshold||CP Level Threshold Low<2:O>
R24B|6|CP Level Detect||CP Level Detect Power Down
R24B|7|Open||
R24C|0|DSM Prog<3:O>||
R24C|4|Open||
R24D|0|SIF Addr<4:0>||
R24D|5|SIF Reset Bar||
R24D|6|SIF clock||
R24D|7|Open||
R24E|0|Frequency||Frequency Correction Word<11:7>
R24E|5|Read Effective||Read Effective Tuning Word
R24E|6|Open||
R24E|7|Update Freq Word||
R24F|0|Frequency||Frequency Correction Word <6:O>
R24F|7|Update Freq Word||
R250|0|VCO Va ractor||VCO Va ractor Offset<3:O>
R250|4|VCO Varactor||VCO Varactor Reference Tcf<2:O>
R250|7|Open||
R251|0|VCO Varactor||VCO Varactor Reference<3:O>
R251|4|Open||
R25A|0|Rx Fast Lock Mode||Rx Fast Lock Mode Enable
R25A|1|Rx Fast Lock||Rx Fast Lock Profile Pin Select
R25A|2|Rx Fast Lock||Rx Fast Lock Profile Init
R25A|3|Rx Fast Lock Load||Rx Fast Lock Load Synth
R25A|4|Open||
R25A|5|Rx Fast Lock||Rx Fast Lock ProfiIe<2:O>
R25B|0|Rx Fast Lock Init||Rx Fast Lock Init DeIay<7:O>
R25C|0|Rx Fast Lock||Rx Fast Lock Program Address<7:O>
R25D|0|Rx Fast Lock||Rx Fast Lock Program Data<7:O>
R25E|0|Rx Fast Lock||Rx Fast Lock Program Read Data<7:O>
R25F|0|Rx Fast Lock||Rx Fast Lock Program Clock Enable
R25F|1|Rx Fast Lock||Rx Fast Lock Program Write
R25F|2|Open||
R261|0|Open||
R261|4|Power Mode<1:O>||
R261|6|Open||
R270|0|Bypass Ld Synth||
R270|1|PFD Clk Edge||
R270|2|PFD Width <1 :0>||
R270|4|Open||
R270|5|Div Test||
R270|6|Open||
R271|0|Synthesizer Integer||Synthesizer Integer Word<7:O>
R272|0|Synthesizer Integer||Synthesizer Integer Word<10:8>
R272|3|Open||
R272|6|SDM Power Down||
R272|7|SDM Bypass||
R273|0|Synthesizer||Synthesizer Fractional Word<7:O>
R274|0|Synthesizer||Synthesizer Fractional Word <15:8>
R275|0|Synthesizer||Synthesizer Fractional Word <22:16>
R275|7|Open||
R276|0|Force ALC Word<6:O>||
R276|7|Force ALC Enable||
R277|0|Force VCO Tune<7:O>||
R278|0|Force VCO Tune<8||
R278|1|Force VCO Tune||Force VCO Tune Enable
R278|2|Open||
R278|3|VCO Cal Offset<3:O>||
R278|7|Bypass Load Dekn||
R279|0|VCO Varactor<3:O>||
R279|4|Init ALC VaIue<3:O>||
R27A|0|VCO Output||VCO Output LeveI<3:O>
R27A|4|Open||
R27A|6|PORb VCO Logic||
R27A|7|Open||
R27B|0|Charge Pump||Charge Pump Current<5:O>
R27B|6|Vtune Force||
R27B|7|Set to 1||
R27C|0|Charge Pump||Charge Pump Offset<5:O>
R27C|6|Open||
R27C|7|Synth Re-Cal||
R27D|0|Cp Test <1 :O>||
R27D|2|Cp Cal Enable||
R27D|3|F Cpcal||
R27D|4|Offset Off||
R27D|5|Open||
R27D|6|Dither Mode||
R27D|7|HaIfVco Cal Clk||
R27E|0|Loop Filter C1 <3:O>||
R27E|4|Loop Filter C2<3:O>||
R27F|0|Loop Filter C3<3:O>||
R27F|4|Loop Filter R1 <3:O>||
R280|0|Loop Filter R3<3:O>||
R280|4|Loop Hher Bypass C1||
R280|5|Loop Hher Bypass C2||
R280|6|Loop Hher Bypass R1||
R280|7|Loop Hher Bypass R3||
R281|0|Forced CP Cal||Forced CP Cal Word<3:O>
R281|4|Number SDM Dither||Number SDM Dither Bits<3:O>
R282|0|VCO Bias Ref<2:O>||
R282|3|VCO Bias Tcf<1:O>||
R282|5|Must be zeros||
R282|7|Open||
R283|0|Prescale Bias <1:O>||
R283|2|ALC Enable||
R283|3|Bypass Prescale R||
R283|4|VCC> Comp Bypass||VCC> Comp Bypass BBSFR
R283|5|Open||
R283|7|VCO Bypass BBSDAC||
R284|0|CP Cal Word<3:O>||
R284|4|VCO Cal Busy||
R284|5|CP Cal Done||
R284|6|Comp Out||
R284|7|CP Cal Valid||
R285|0|VCO Cal Ref Tcf<2:O>||
R285|3|VCO Cal Ref Monitor||
R285|4|Open||
R286|0|Power Down VCO||Power Down VCO Bufffer
R286|1|Power Down Cal Tcf||
R286|2|Power Down Varact||Power Down Varact Ref Tcf
R286|3|Power Down Varactor||Power Down Varactor Ref
R286|4|Open||
R287|0|Open||
R287|1|Lock||
R287|2|Open||
R287|6|CP Ovrg Low||
R287|7|CP Ovrg High||
R288|0|VCO LDO Vdrop||VCO LDO Vdrop SeI<1:O>
R288|2|VCO LDO Vout||VCO LDO Vout SeI<2:O>
R288|5|VCO LDO Inrush<1:O>||
R288|7|VCO LDO Bypass||
R289|0|FB Clock Adv<1:O>||
R289|2|VCO Cal Count<1:O>||
R289|4|VCO Cal ALC Wait<2:m||
R289|7|VCO Cal||
R28A|0|Lock Detect Mode<1||Lock Detect Mode<1 :O>
R28A|2|Lock Detect||Lock Detect Count<1:O>
R28A|4|Open||
R28B|0|CP Level Detect||CP Level Detect Threshold High<2:O>
R28B|3|CP Level Detect||CP Level Detect Threshold Low<2:0>
R28B|6|CP Level Detect||CP Level Detect Power Down
R28B|7|Open||
R28C|0|DSM Prog<3:O>||
R28C|4|Open||
R28D|0|SIF Addr<4:O>||
R28D|5|SIF Reset Bar||
R28D|6|SIF clock||
R28D|7|Open||
R28E|0|Frequency||Frequency Correction Word<11:7>
R28E|5|Read Effective Tu||Read Effective Tu ning Word
R28E|6|Open||
R28E|7|Update Freq Word||
R28F|0|Frequency||Frequency Correction Word<6:O>
R28F|7|Update Freq Word||
R290|0|VCO Varactor||VCO Varactor Offset<3:O>
R290|4|VCO Varactor||VCO Varactor Reference Tcf<2:O>
R290|7|Open||
R291|0|VCO Varactor||VCO Varactor Reference<3:O>
R291|4|Open||
R292|0|DCXO Tune||DCXO Tune Coarse<5:O>
R292|6|Open||
R293|0|DCXO Tune Fine<12:5>||
R294|0|Open||
R294|3|DCXO Tune Fine<4:O>||
R295|0|Open||
R295|2|DCXO Rd<1:O>||
R295|4|DCXO RtaiI<2:O>||
R295|7|Must be zero||
R296|0|DCXO Temperature||DCXO Temperature Coefficient Write <7:O>
R297|0|DCXO Temperature||DCXO Temperature Coefficient Read <7:O>
R298|0|DCXO Temperature||DCXO Temperature Coefficient Add ress<5:O>
R298|6|DCXO Tempco Clk||
R298|7|DCXO Tempco En||
R299|0|Delta T Read||Delta T Read Back<7:O>
R29A|0|Tx Fast Lock Mode||Tx Fast Lock Mode Enable
R29A|1|Tx Fast Lock||Tx Fast Lock Profile Pin Select
R29A|2|Tx Fast Lock||Tx Fast Lock Profile Init
R29A|3|Tx Fast Lock Load||Tx Fast Lock Load Synth
R29A|4|Open||
R29A|5|Tx Fast Lock||Tx Fast Lock ProfiIe<2:O>
R29B|0|Tx Fast Lock Init||Tx Fast Lock Init DeIay<7:O>
R29C|0|Tx Fast Lock||Tx Fast Lock Program Address<7:O>
R29D|0|Tx Fast Lock||Tx Fast Lock Program Data<7:O>
R29E|0|Tx Fast Lock||Tx Fast Lock Program Read Data<7:O>
R29F|0|Tx Fast Lock||Tx Fast Lock Program Clock Enable
R29F|1|Tx Fast Lock||Tx Fast Lock Program Write
R29F|2|Open||
R2A1|0|Open||
R2A1|4|Power Mode<3:O>||
R2A6|0|Master Bias||Master Bias Trim<4:O>
R2A6|5|Master Bias Ref Sel||
R2A6|6|Master Bias Filter||Master Bias Filter Bypass
R2A6|7|Power Down Bandgap||Power Down Bandgap Ref
R2A8|0|Bandgap Temp||Bandgap Temp Trim<4:O>
R2A8|5|Bandgap Ref Reset||
R2A8|6|VCO LDO Ref Sel||
R2A8|7|VCO LDO Filter||VCO LDO Filter Bypass
R2AB|0|Rx Ref Divider<||
R2AB|1|Rx Ref Reset Bar||
R2AB|2|Set to 1||
R2AB|3|Open||
R2AC|0|Tx Ref Doubler FB||Tx Ref Doubler FB Delay<1:O>
R2AC|2|TX Ref Divider<1:O>||
R2AC|4|Tx Ref Reset Bar||
R2AC|5|Rx Ref Doubler FB||Rx Ref Doubler FB Delay<1:O>
R2AC|7|Rx Ref Divider<||
R2B0|0|Full Table Gain||Full Table Gain Index RXVLMT Gain Rx1<6:O>
R2B0|7|Open||
R2B1|0|LPF gain Rx1<4:O>||
R2B1|5|Open||
R2B2|0|Digital gain||Digital gain Rx1<4:O>
R2B2|5|Open||
R2B3|0|Fast Attack State||Fast Attack State Rx1<2:O>
R2B3|3|Open||
R2B3|4|Fast Attack State||Fast Attack State Rx2<2:O>
R2B3|7|Open||
R2B4|0|Slow Loop State||Slow Loop State Rx1<2:O>
R2B4|3|Open||
R2B4|4|Slow Loop State||Slow Loop State Rx2<2:O>
R2B4|7|Open||
R2B5|0|Full Table Gain||Full Table Gain IndexRx2AMT Gain Rx1<6:O>
R2B5|7|Open||
R2B6|0|LPF gain Rx2<4:O>||
R2B6|5|Open||
R2B7|0|Digital gain||Digital gain Rx2<4:O>
R2B7|5|Open||
R2B8|0|Dig Sat||
R2B8|1|Small ADC OL||
R2B8|2|Large ADC OL||
R2B8|3|Small LMT OL||
R2B8|4|Large LMT OL||
R2B8|5|Low Power 1||
R2B8|6|Gain Lock1||
R2B8|7|Open||
R2B9|0|Dig Sat||
R2B9|1|Small ADC OL||
R2B9|2|Large ADC OL||
R2B9|3|Small LMT OL||
R2B9|4|Large LMT OL||
R2B9|5|Low Power 2||
R2B9|6|Gain Lock1||
R2B9|7|Open||
R3DF|0|Set to 1||
R3DF|1|Open||
R3F4|0|BIST Enable||
R3F4|1|Tony PRBS||
R3F4|2|BIST Control Point||BIST Control Point <1 :O>
R3F4|4|Tone LeveI<1:O>||
R3F4|6|Tone Frequency<1:O>||
R3F5|0|Data Port Loop Test||Data Port Loop Test Enable
R3F5|1|Observation||Observation Point<2:O>
R3F5|5|Channel||
R3F5|6|Mask||
R3F5|7|Data Port SP, HD||Data Port SP, HD Loop Test OE
R3F6|0|Use Data Port||
R3F6|1|Data Port H V Low||
R3F6|2|BIST hAask Channel||BIST hAask Channel 1 Idata
R3F6|3|BIST Mask Channel 1||BIST Mask Channel 1 Q data
R3F6|4|BIST Mask Channel 2||BIST Mask Channel 2 I data
R3F6|5|BIST Mask Channel 2||BIST Mask Channel 2 Q data
R3F6|6|Temp Sense Vbe||Temp Sense Vbe Test<1:O>
R3FC|0|DAC test Word <7:O>||
R3FD|0|DAC test Word <15:8>||
R3FE|0|DAC test Word <22:||DAC test Word <22: 1 6>
R3FE|7|DAC Test Enable||
'''
