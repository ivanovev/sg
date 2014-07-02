data = '''
R00|0|SOFT_RESET||
R00|1|RESERVED|1|
R01|0|UNUSED|1|
R01|1|VCO_LDO_EN||
R01|2|CP_EN||
R01|3|DIV_EN||
R01|4|VCO_EN||
R01|5|REF_BUF_EN||
R01|6|VCO_MUX_EN||
R01|7|LO_DRV1X_EN||
R01|8|LO_DRV2X_EN||
R01|9|QUAD_DIV_EN||
R01|10|DMOD_EN||
R01|11|UNUSED|1|
R02|0|INT_DIV[7:0]||
R02|8|INT_DIV[10:8]||
R02|11|DIV_MODE||
R02|12|RESERVED|1|
R03|0|FRAC_DIV[7:0]||
R03|8|FRAC_DIV[15:8]||
R04|0|MOD_DIV[7:0]||
R04|8|MOD_DIV[15:8]||
R10|0|UNUSED|1|
R10|1|VCO_LDO_MASK||
R10|2|CP_MASK||
R10|3|DIV_MASK||
R10|4|VCO_MASK||
R10|5|REF_BUF_MASK||
R10|6|VCO_MUX_MASK||
R10|7|LO_DRV1X_MASK||
R10|8|LO_DRV2X_MASK||
R10|9|QUAD_DIV_MASK||
R10|10|DMOD_MASK||
R10|11|UNUSED|1|
R20|0|BLEED||
R20|6|RESERVED|1|
R20|8|RESERVED|1|
R20|10|CSCALE||
R20|14|CPSEL||
R20|15|RESERVED|1|
R21|0|REFSEL||
R21|3|PFD_POLARITY||
R21|4|REF_MUX_SEL||
R21|7|RESERVED|1|
R21|8|RESERVED|1|
R22|0|VCO_SEL||
R22|3|DIV4_EN||
R22|4|DIV8_EN||
R22|5|DRVDIV2_EN||
R22|6|LO_DRV_LVL||
R22|8|RESERVED|1|
R22|12|RESERVED|1|
R23|0|RESERVED|1|
R23|5|RFDSA_SEL[2:0]||
R23|8|RFDSA_SEL[3]||
R23|9|RFSW_SEL||
R23|10|RESERVED|1|
R23|11|RFSW_MUX||
R23|12|RESERVED|1|
R30|0|BAL_CIN||
R30|4|BAL_COUT||
R30|8|RESERVED|1|
R31|0|DEMOD_CDAC||
R31|4|RESERVED|1|
R31|5|DEMOD_RDAC[2:0]||
R31|8|DEMOD_RDAC[3]||
R31|9|RESERVED|1|
R31|10|MIX_BIAS||
R31|13|RESERVED|1|
R32|0|ILO||
R32|4|QLO||
R32|8|POLI||
R32|10|POLQ||
R32|12|RESERVED|1|
R33|0|DCOFFQ||
R33|8|DCOFFI||
R34|0|RESERVED|1|
R34|4|RESERVED|1|
R34|8|BWSEL||
R34|10|BB_BIAS||
R34|12|RESERVED|1|
R40|0|CLKEDGE||
R40|2|CPCTRL||
R40|5|ABLDLY||
R40|7|RESERVED|1|
R40|8|RESERVED|1|
R42|0|DITH_VAL||
R42|1|DITH_MAG||
R42|3|DITH_EN||
R42|4|RESERVED|1|
R42|8|RESERVED|1|
R43|0|DITH_VAL[7:0]||
R43|8|DITH_VAL[15:8]||
R45|0|BAND||
R45|7|VCO_BAND_SRC||
R45|8|VTUNE_CTRL||
R45|10|RESERVED|1|
R49|0|SET_0[7:0]||
R49|8|SET_0[8]||
R49|9|SET_1[13:9]||
R49|14|RESERVED|1|
'''