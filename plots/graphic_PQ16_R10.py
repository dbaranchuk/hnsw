OIMI_R10_txt = '''
0.3293
0.3901
0.4874
0.5700
0.6859
0.7265
0.7550
0.7710
'''
OIMI_T_txt = '''
1.29
1.37
1.47
1.96
2.99
4.33
8.7
12.9
'''

IVF2M_R10_txt = '''
0.3836
0.4689
0.5886
0.6623
0.7564
0.7861
0.8108
0.8193
'''
IVF2M_T_txt = '''
0.33
0.34
0.45
0.55
1.01
1.52
2.67
3.85
'''

IVF4M_R10_txt = '''
0.4326
0.5213
0.6308
0.7050
0.7774
0.8024
0.8270
0.8470
'''
IVF4M_T_txt = '''
0.66
0.93
2.02
3.66
9.55
16.28
32
50
'''

IVFG_R10_txt = '''
0.3369
0.4164
0.5399
0.6307
0.7477
0.7843
0.8142
0.8263
'''
IVFG_T_txt = '''
0.30
0.34
0.43
0.59
1.14
1.71
3.20
5.1
'''

IVFGP_R10_txt = '''
0.3974
0.4891
0.6192
0.6989
0.7865
0.8099
0.8325
0.8415
'''
IVFGP_T_txt = '''
0.31
0.34
0.46
0.65
1.23
1.96
3.60
5.54
'''

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy
import re
import seaborn as sns
sns.set(style='ticks', palette='Set2')
sns.despine()

dataset = "DEEP"
if dataset == "DEEP":
    OIMI_R10 = re.findall(r"[0-9.]+", OIMI_R10_txt)
    OIMI_T = re.findall(r"[0-9.]+", OIMI_T_txt)

    IVF2M_R10 = re.findall(r"[0-9.]+", IVF2M_R10_txt)
    IVF2M_T = re.findall(r"[0-9.]+", IVF2M_T_txt)

    IVF4M_R10 = re.findall(r"[0-9.]+", IVF4M_R10_txt)
    IVF4M_T = re.findall(r"[0-9.]+", IVF4M_T_txt)

    IVFG_R10 = re.findall(r"[0-9.]+", IVFG_R10_txt)
    IVFG_T = re.findall(r"[0-9.]+", IVFG_T_txt)

    IVFGP_R10 = re.findall(r"[0-9.]+", IVFGP_R10_txt)
    IVFGP_T = re.findall(r"[0-9.]+", IVFGP_T_txt)

    plt.figure(figsize=[5,4])
    #lineOIMI, = plt.plot(OIMI_T, OIMI_R10, 'r', label = 'OIMI-D-OADC $2^{14}$')
    #lineIVF2M, = plt.plot(IVF2M_T, IVF2M_R10, '-g', label = 'IVFOADC $2^{21}$')
    #lineIVF4M, = plt.plot(IVF4M_T, IVF4M_R10, '-m', label = 'IVFOADC $2^{22}$')
    #lineIVFG, = plt.plot(IVFG_T, IVFG_R10, '-c', label = 'IVFOADC+G $2^{20}$')
    #lineIVFGP, = plt.plot(IVFGP_T, IVFGP_R10, '--b', label = 'IVFOADC+G+P $2^{20}$')
    lineOIMI, = plt.plot(OIMI_T, OIMI_R10, 'r', label = 'O-Multi-D-OADC $2^{14}$')
    lineIVF2M, = plt.plot(IVF4M_T, IVF4M_R10, '-m', label = 'IVFOADC $2^{22}$')
    lineIVF4M, = plt.plot(IVF2M_T, IVF2M_R10, '-g', label = 'IVFOADC-fast $2^{21}$')
    lineIVFG, = plt.plot(IVFG_T, IVFG_R10, '-c', label = 'IVFOADC+G $2^{20}$')
    lineIVFGP, = plt.plot(IVFGP_T, IVFGP_R10, '--b', label = 'IVFOADC+G+P $2^{20}$')

    plt.xticks(numpy.arange(0.2, 3.01, 0.2))
    plt.yticks(numpy.arange(0.35, 0.86, 0.05))

    plt.axis([0.2, 2.81, 0.35, 0.85])
    plt.xlabel('Time (ms)', fontsize=12)
    plt.ylabel('R@10, 16 bytes', fontsize=12)
    plt.legend(frameon = True, fontsize=9, loc=4)

    pp = PdfPages('recallR10_PQ16.pdf')
    pp.savefig(bbox_inches='tight')
    pp.close()
