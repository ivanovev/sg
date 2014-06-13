
data = '''
R00|6|Not used|1|
R00|0|DC_REGVAL[5:0]||
R01|5|RCCAL_LPFCAL[2:0]||
R01|2|DC_LOCK[2:0]||Lock pattern register
R01|1|DC_CLBR_DONE||indicates calibration status
R01|0|DC_UD||
R02|6|Not used|1|
R02|0|DC_CNTVAL[5:0]||
R03|6|Not used|1|
R03|5|DC_START_CLBR||
R03|4|DC_LOAD||
R03|3|DC_SRESET||resets all DC Calibration modules
R03|0|DC_ADDR[2:0]||Active calibration module address
R04|4|VER[3:0]|1|Chip version
R04|0|REV[3:0]|1|Chip revision
R05|7|DECODE||
R05|6|Not used|1|
R05|5|SRESET||DSM soft reset
R05|4|EN||Top modules enable
R05|3|STXEN||Soft transmit enable
R05|2|SRXEN||Soft receive enable
R05|1|TFWMODE||Serial port mode
R05|0|Not used|1|
R06|4|Not used|1|
R06|3|CLKSEL_LPFCAL||
R06|2|PD_CLKLPFCAL||
R06|1|ENF_EN_CAL_LPFCAL||Enables the enforce mode
R06|0|RST_CAL_LPFCAL||
R07|7|EN_CAL_LPFCAL||
R07|4|FORCE_CODE_CAL_LPFCAL[2:0]||
R07|0|BWC_LPFCAL[3:0]||
R08|7|Reserved|1|
R08|6|LBEN_LPFIN||
R08|5|LBEN_VGA2IN||
R08|4|LBEN_OPIN||
R08|0|LBRFEN[3:0]||
R09|7|RXOUTSW||RX out/ADC in high-Z switch control
R09|6|CLK_EN[6:0]||PLLCLKOUT
R09|5|CLK_EN[6:0]||LPF CAL clock
R09|4|CLK_EN[6:0]||Rx VGA2 DCCAL clock
R09|3|CLK_EN[6:0]||Rx LPF DCCAL clock
R09|2|CLK_EN[6:0]||Rx DSM SPI clock
R09|1|CLK_EN[6:0]||Tx LPF SPI DCCAL clock
R09|0|CLK_EN[6:0]||Tx DSM SPI clock
R0A|2|Not used|1|
R0A|1|FDDTDD||Frequency/Time division duplexing selection
R0A|0|TDDMOD||TDD mode selection if FDDTDD=1
R0B|5|Not used|1|
R0B|4|PDXCOBUF||XCO buffer power down
R0B|3|SLFBXCOBUF||XCO buffer self biasing control
R0B|2|BYPXCOBUF||XCO buffer bypass
R0B|0|PD[1:0]||Power down control for top modules
R0E|0|SPARE0[7:0]||Spare configuration register
R0F|0|SPARE1[7:0]||Spare configuration register
R10|0|NINT[8:1]||Integer part of the divider (MSBs)
R11|7|NINT[0]||Integer part of the divider (LSB)
R11|0|NFRAC[22:16]||Fractional part of the divider
R12|0|NFRAC[15:8]||Fractional part of the divider
R13|0|NFRAC[7:0]||Fractional part of the divider
R14|7|DITHEN||Dithering control
R14|4|DITHN[2:0]||
R14|3|EN||PLL enable
R14|2|AUTOBYP||
R14|1|DECODE||
R14|0|Reserved|1|
R15|2|FREQSEL[5:0]||
R15|0|Not used|1|
R16|7|EN_PFD_UP||Enable PFD UP pulses
R16|6|OEN_TSTD_SX||
R16|5|PASSEN_TSTOD_SD||
R16|0|ICHP[4:0]||
R17|7|BYPVCOREG||Bypass VCO regulator
R17|6|PDVCOREG||VCO regulator power down
R17|5|FSTVCOBG||
R17|0|OFFUP[4:0]||
R18|5|VOVCOREG[3:1]||
R18|0|OFFDOWN[4:0]||
R19|7|VOVCOREG[0]||VCO regulator output voltage control LSB
R19|6|Not used|1|
R19|0|VCOCAP[5:0]||Switch capacitance programming Binary coded
R1A|7|VTUNE_H|1|Value from Vtune comparator
R1A|6|VTUNE_L|1|Value from Vtune comparator
R1A|0|Reserved|1|
R1B|4|Reserved|1|
R1B|3|PD_VCOCOMP_SX||VCO Comparator Enable
R1B|2|Reserved|1|
R1B|1|Reserved|1|
R1B|0|Reserved|1|
R1C|0|Reserved|1|
R1D|0|Reserved|1|
R1E|0|Reserved|1|
R1F|0|Reserved|1|
R20|0|NINT[8:1]||Integer part of the divider (MSBs)
R21|7|NINT[0]||Integer part of the divider (LSB)
R21|0|NFRAC[22:16]||Fractional part of the divider
R22|0|NFRAC[15:8]||Fractional part of the divider
R23|0|NFRAC[7:0]||Fractional part of the divider
R24|7|DITHEN||Dithering control
R24|4|DITHN[2:0]||
R24|3|EN||PLL enable
R24|2|AUTOBYP||
R24|1|DECODE||
R24|0|Reserved|1|
R25|2|FREQSEL[5:0]||
R25|0|SELOUT[1:0]||Select output buffer in RX PLL
R26|7|EN_PFD_UP||Enable PFD UP pulses
R26|6|OEN_TSTD_SX||
R26|5|PASSEN_TSTOD_SD||
R26|0|ICHP[4:0]||
R27|7|BYPVCOREG||Bypass VCO regulator
R27|6|PDVCOREG||VCO regulator power down
R27|5|FSTVCOBG||
R27|0|OFFUP[4:0]||
R28|5|VOVCOREG[3:1]||
R28|0|OFFDOWN[4:0]||
R29|7|VOVCOREG[0]||VCO regulator output voltage control LSB
R29|6|Not used|1|
R29|0|VCOCAP[5:0]||Switch capacitance programming Binary coded
R2A|7|VTUNE_H|1|Value from Vtune comparator
R2A|6|VTUNE_L|1|Value from Vtune comparator
R2A|0|Reserved|1|
R2B|4|Reserved|1|
R2B|3|PD_VCOCOMP_SX||VCO Comparator Enable
R2B|2|Reserved|1|
R2B|1|Reserved|1|
R2B|0|Reserved|1|
R2C|0|Reserved|1|
R2D|0|Reserved|1|
R2E|0|Reserved|1|
R2F|0|Reserved|1|
R30|6|Not used|1|
R30|0|DC_REGVAL[5:0]||
R31|5|Not used|1|
R31|2|DC_LOCK[2:0]||Lock pattern register
R31|1|DC_CLBR_DONE||indicates calibration status
R31|0|DC_UD||
R32|6|Not used|1|
R32|0|DC_CNTVAL[5:0]||
R33|6|Not used|1|
R33|5|DC_START_CLBR||
R33|4|DC_LOAD||
R33|3|DC_SRESET||
R33|0|DC_ADDR[2:0]||
R34|6|Not used|1|
R34|2|BWC_LPF[3:0]||LPF bandwidth control
R34|1|EN||LPF modules enable
R34|0|DECODE||
R35|7|Not used|1|
R35|6|BYP_EN_LPF||LPF bypass enable
R35|0|DCO_DACCAL[5:0]||
R36|7|TX_DACBUF_PD||TX data DAC buffers power down
R36|4|RCCAL_LPF[2:0]||Calibration value| coming from TRX_LPF_CAL module
R36|3|PD_DCOCMP_LPF||
R36|2|PD_DCODAC_LPF||
R36|1|PD_DCOREF_LPF||
R36|0|PD_FIL_LPF||Power down for the filter
R3E|0|SPARE0[7:0]||Spare configuration register
R3F|0|SPARE1[7:0]||Spare configuration register
R40|2|Not used|1|
R40|1|EN||TXRF modules enable
R40|0|DECODE||
R41|5|Not used|1|
R41|0|VGA1GAIN[4:0]||TXVGA1 gain| log-linear control
R42|0|VGA1DC_I[7:0]||
R43|0|VGA1DC_Q[7:0]||
R44|5|Not used|1|
R44|2|PA_EN[2:0]||VGA2 power amplifier (TX output) selection
R44|1|PD_DRVAUX||AUXPA auxiliary (RF loop back) PA power down
R44|0|PD_PKDET||Power down for envelop/peak detectors
R45|3|VGA2GAIN[4:0]||TXVGA2 gain control| log-linear control
R45|0|ENVD[2:0]||Controls envelop/peak detector analogue MUX
R46|4|PKDBW[3:0]||
R46|2|LOOPBBEN[1:0]||Base band loop back switches control
R46|1|FST_PKDET||
R46|0|FST_TXHFBIAS||
R47|4|ICT_TXLOBUF[3:0]||
R47|0|VBCAS_TXDRV[3:0]||
R48|5|Not used|1|
R48|0|ICT_TXMIX[4:0]||
R49|5|Not used|1|
R49|0|ICT_TXDRV[4:0]||
R4A|5|Not used|1|
R4A|4|PW_VGA1_I||VGA1| I channel power control
R4A|3|PW_VGA1_Q||VGA1| Q channel power control
R4A|2|PD_TXDRV||Power down for PAs and AUXPA
R4A|1|PD_TXLOBUF||Power down for TXLOBUF
R4A|0|PD_TXMIX||Power down for TXMIX
R4B|0|VGA1GAINT[7:0]||TXVGA1 gain control raw access
R4C|0|G_TXVGA2[8:1]||
R4D|7|G_TXVGA2[0]||
R4D|0|Not used|1|
R4E|0|SPARE0[7:0]||Spare configuration register
R4F|0|SPARE1[7:0]||Spare configuration register
R50|6|Not used|1|
R50|0|DC_REGVAL[5:0]||
R51|5|Not used|1|
R51|2|DC_LOCK[2:0]||Lock pattern register
R51|1|DC_CLBR_DONE||indicates calibration status
R51|0|DC_UD||
R52|6|Not used|1|
R52|0|DC_CNTVAL[5:0]||
R53|6|Not used|1|
R53|5|DC_START_CLBR||
R53|4|DC_LOAD||
R53|3|DC_SRESET||resets all DC Calibration modules
R53|0|DC_ADDR[3:0]||Active calibration module address
R54|6|Not Used|1|
R54|2|BWC_LPF[3:0]||LPF bandwidth control
R54|1|EN_LPF||LPF modules enable
R54|0|DECODE||
R55|7|Not Used|1|
R55|6|BYP_EN_LPF||LPF bypass enable
R55|0|DCO_DACCAL[5:0]||
R56|7|Not Used|1|
R56|4|RCCAL_LPF[2:0]||Calibration value| coming from TRX_LPF_CAL module
R56|3|PD_DCOCMP_LPF||
R56|2|PD_DCODAC_LPF||
R56|1|PD_DCOREF_LPF||
R56|0|PD_FIL_LPF||Power down for the filter
R57|7|EN_ADC_DAC||ADC/DAC modules enable
R57|6|DECODE||
R57|3|TX_CTRL1[6:4].||
R57|2|TX_CTRL1[3].||DAC Reference Current Resistor
R57|0|TX_CTRL1[1:0].||
R58|6|RX_CTRL1[7:6].||Reference bias resistor adjust
R58|4|RX_CTRL1[5:4].||Reference bias UP
R58|0|RX_CTRL1[3:0].||Reference bias DOWN
R59|7|Not Used|1|
R59|5|RX_CTRL2[7:6].||Reference Gain Adjust
R59|3|RX_CTRL2[5:4].||Common Mode Adjust
R59|1|RX_CTRL2[3:2].||Reference Buffer Boost
R59|0|RX_CTRL2[0].||ADC Input Buffer Disable
R5A|7|MISC_CTRL[9]||Rx Fsync Polarity frame start
R5A|6|MISC_CTRL[8]||Rx Interleave Mode; 1 – Q,I; 0 – I,Q (default)
R5A|5|MISC_CTRL[7]||Dac Clk Edge Polarity; 1 – negative (default); 0 – positive
R5A|4|MISC_CTRL[6]||Tx Fsync Polarity frame start
R5A|3|MISC_CTRL[5]||Tx Interleave Mode; 1 – Q,I; 0 – I,Q (default)
R5A|2|RX_CTRL3[7]||ADC Sampling Phase Select; 1 – falling edge; 0 – rising edge (default)
R5A|0|RX_CTRL3[1:0]||Clock Non-Overlap Adjust
R5B|6|RX_CTRL4[7:6]||ADC bias resistor adjust
R5B|4|RX_CTRL4[5:4]||Main bias DOWN
R5B|2|RX_CTRL4[3:2]||ADC Amp1 stage1 bias UP
R5B|0|RX_CTRL4[1:0]||ADC Amp2-4 stage1 bias UP
R5C|6|RX_CTRL5[7:6]||ADC Amp1 stage2 bias UP
R5C|4|RX_CTRL5[5:4]||ADC Amp2-4 stage2 bias UP
R5C|2|RX_CTRL5[3:2]||Quantizer bias UP
R5C|0|RX_CTRL5[1:0]||Input Buffer bias UP
R5D|4|REF_CTRL0[7:4]||Bandgap Temperature Coefficient Control
R5D|0|REF_CTRL0[3:0]||Bandgap Gain Control
R5E|6|REF_CTRL1[7:6]||Reference Amps bias adjust
R5E|4|REF_CTRL1[5:4]||Reference Amps bias UP
R5E|0|REF_CTRL1[3:0]||Reference Amps bias DOWN
R5F|5|SPARE00[7:5]||Spare configuration bits
R5F|4|MISC_CTRL[4]||Enable DAC
R5F|3|MISC_CTRL[3]||Enable ADC1 (I Channel)
R5F|2|MISC_CTRL[2]||Enable ADC2 (Q Channel)
R5F|1|MISC_CTRL[1]||Enable ADC reference
R5F|0|MISC_CTRL[0]||Enable master reference
R60|6|Not used|1|
R60|0|DC_REGVAL[5:0]||
R61|5|Not used|1|
R61|2|DC_LOCK[2:0]||Lock pattern register
R61|1|DC_CLBR_DONE||indicates calibration status
R61|0|DC_UD||
R62|6|Not used|1|
R62|0|DC_CNTVAL[5:0]||
R63|6|Not used|1|
R63|5|DC_START_CLBR||
R63|4|DC_LOAD||
R63|3|DC_SRESET||resets all DC Calibration modules
R63|0|DC_ADDR[3:0]||Active calibration module address
R64|6|Not used|1|
R64|2|VCM[3:0]||RXVGA2 output common mode voltage control
R64|1|EN||RXVGA2 modules enable
R64|0|DECODE||
R65|5|Not used|1|
R65|0|VGA2GAIN[4:0]||RXVGA2 gain control
R66|6|Not used|1|
R66|5|PD[9]||DC current regulator
R66|4|PD[8]||DC calibration DAC for VGA2B
R66|3|PD[7]||DC calibration comparator for VGA2B
R66|2|PD[6]||DC calibration DAC for VGA2A
R66|1|PD[5]||DC calibration comparator for VGA2A
R66|0|PD[4]||Band gap
R67|4|Not used|1|
R67|3|PD[3]||Output buffer in both RXVGAs
R67|2|PD[2]||RXVGA2B
R67|1|PD[1]||RXVGA2A
R67|0|PD[0]||Current reference
R68|4|VGA2GAINB||
R68|0|VGA2GAINA||
R6E|0|SPARE0[7:0]||Spare configuration register
R6F|0|SPARE1[7:0]||Spare configuration register
R70|2|Not used|1|
R70|1|DECODE||
R70|0|EN||RXFE modules enable
R71|7|IN1SEL_MIX_RXFE||Selects the input to the mixer; 1 - LNA; 0 - PADS
R71|0|DCOFF_I_RXFE[6:0]||DC offset cancellation I channel
R72|7|INLOAD_LNA_RXFE||
R72|0|DCOFF_Q_RXFE[6:0]||DC offset cancellation Q channel
R73|7|XLOAD_LNA_RXFE||
R73|0|IP2TRIM_I_RXFE[6:0]||IP2 cancellation I channel
R74|7|Not used|1|
R74|0|IP2TRIM_Q_RXFE[6:0]||IP2 cancellation Q channel
R75|6|G_LNA_RXFE[1:0]||LNA gain mode control
R75|4|LNASEL_RXFE[1:0]||Selects the active LNA
R75|0|CBE_LNA_RXFE[3:0]||
R76|7|Not used|1|
R76|0|RFB_TIA_RXFE[6:0]||
R77|7|Not used|1|
R77|0|CFB_TIA_RXFE[6:0]||
R78|6|Not used|1|
R78|0|RDLEXT_LNA_RXFE[5:0]||
R79|6|Not used|1|
R79|0|RDLINT_LNA_RXFE[5:0]||
R7A|4|ICT_MIX_RXFE[3:0]||
R7A|0|ICT_LNA_RXFE[3:0]||
R7B|4|ICT_TIA_RXFE[3:0]||
R7B|0|ICT_MXLOB_RXFE[3:0]||
R7C|7|Not used|1|
R7C|3|LOBN_MIX_RXFE[3:0]||
R7C|2|RINEN_MIX_RXFE||
R7C|0|G_FINE_LNA3_RXFE[1:0]||LNA3 fine gain adjustment
R7D|4|Not used|1|
R7D|0|Reserved|1|
R7E|0|SPARE0[7:0]||
R7F|0|SPARE1[7:0]||
'''
