OIMI_PQ8_R10_txt = '''
0.2790
0.3233
0.3838
0.4227
0.4701
0.4844
0.4984
0.5040
'''
OIMI_PQ8_T_txt = '''
1.10
1.12
1.35
1.65
2.65
3.73
6.79
10.8
'''

IVF2M_PQ8_R10_txt = '''
0.3329
0.3926
0.4625
0.5019
0.5413
0.5531
0.5615
0.5648
'''
IVF2M_PQ8_T_txt = '''
0.22
0.24
0.33
0.42
0.79
1.22
2.15
3.10
'''

IVF4M_PQ8_R10_txt = '''
0.3754
0.4351
0.4981
0.5321
0.5591
0.5684
0.5743
0.5772
'''
IVF4M_PQ8_T_txt = '''
0.32
0.37
0.60
0.88
1.90
3.15
6.15
9.14
'''

IVFG_PQ8_R10_txt = '''
0.2997
0.3607
0.4497
0.5054
0.5669
0.5805
0.5924
0.5961
'''
IVFG_PQ8_T_txt = '''
0.22
0.24
0.34
0.45
0.92
1.36
2.50
3.64
'''

IVFGP_PQ8_R10_txt = '''
0.3493
0.4152
0.4996
0.5440
0.5819
0.5908
0.5987
0.6037
'''
IVFGP_PQ8_T_txt = '''
0.25
0.28
0.39
0.53
1.10
1.65
2.91
4.26
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
    OIMI_PQ8_R10 = re.findall(r"[0-9.]+", OIMI_PQ8_R10_txt)
    OIMI_PQ8_T = re.findall(r"[0-9.]+", OIMI_PQ8_T_txt)

    IVF2M_PQ8_R10 = re.findall(r"[0-9.]+", IVF2M_PQ8_R10_txt)
    IVF2M_PQ8_T = re.findall(r"[0-9.]+", IVF2M_PQ8_T_txt)

    IVF4M_PQ8_R10 = re.findall(r"[0-9.]+", IVF4M_PQ8_R10_txt)
    IVF4M_PQ8_T = re.findall(r"[0-9.]+", IVF4M_PQ8_T_txt)

    IVFG_PQ8_R10 = re.findall(r"[0-9.]+", IVFG_PQ8_R10_txt)
    IVFG_PQ8_T = re.findall(r"[0-9.]+", IVFG_PQ8_T_txt)

    IVFGP_PQ8_R10 = re.findall(r"[0-9.]+", IVFGP_PQ8_R10_txt)
    IVFGP_PQ8_T = re.findall(r"[0-9.]+", IVFGP_PQ8_T_txt)

    plt.figure(figsize=[5,4])
    lineOIMI, = plt.plot(OIMI_PQ8_T, OIMI_PQ8_R10, 'r', label = 'OIMI-D-OADC $K{=}2^{14}$')
    lineIVF2M, = plt.plot(IVF2M_PQ8_T, IVF2M_PQ8_R10, '-g', label = 'IVFOADC $K{=}2^{21}$')
    lineIVF4M, = plt.plot(IVF4M_PQ8_T, IVF4M_PQ8_R10, '-m', label = 'IVFOADC $K{=}2^{22}$')
    lineIVFG, = plt.plot(IVFG_PQ8_T, IVFG_PQ8_R10, '-c', label = 'IVFOADC+G $K{=}2^{20}$')
    lineIVFGP, = plt.plot(IVFGP_PQ8_T, IVFGP_PQ8_R10, '--b', label = 'IVFOADC+G+P $K{=}2^{20}$')

    plt.xticks(numpy.arange(0.2, 2.01, 0.2))
    plt.yticks(numpy.arange(0.3, 0.61, 0.05))

    plt.axis([0.2, 2.0, 0.30, 0.601])
    #plt.xlabel('Time (ms)', fontsize=12)
    plt.ylabel('R@10, 8 bytes', fontsize=12)
    #plt.legend(frameon = True, fontsize=9, loc=4)

    pp = PdfPages('recallR10_PQ8.pdf')
    pp.savefig(bbox_inches='tight')
    pp.close()
