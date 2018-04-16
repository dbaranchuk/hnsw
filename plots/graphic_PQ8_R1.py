OIMI_PQ8_R1_txt = '''
0.1602
0.1747
0.1944
0.2064
0.2224
0.2294
0.2345
0.2370
'''
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

IVF2M_PQ8_R1_txt = '''
0.1829
0.2063
0.2336
0.2436
0.2552
0.2582
0.2611
0.2623
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

IVF4M_PQ8_R1_txt = '''
0.2080
0.2280
0.2486
0.2586
0.2669
0.2694
0.2706
0.2716
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

IVFG_PQ8_R1_txt = '''
0.1702
0.1951
0.2289
0.2464
0.2646
0.2691
0.2716
0.2724
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

IVFGP_PQ8_R1_txt = '''
0.1921
0.2173
0.2450
0.2586
0.2697
0.2717
0.2740
0.2744
'''
IVFGP_PQ8_R10_txt = '''
0.3473
0.4132
0.4976
0.5420
0.5799
0.5888
0.5967
0.6017
'''
IVFGP_PQ8_T_txt = '''
0.24
0.28
0.38
0.52
1.10
1.64
2.90
4.25
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
    OIMI_PQ8_R1 = re.findall(r"[0-9.]+", OIMI_PQ8_R1_txt)
    OIMI_PQ8_T = re.findall(r"[0-9.]+", OIMI_PQ8_T_txt)

    IVF2M_PQ8_R1 = re.findall(r"[0-9.]+", IVF2M_PQ8_R1_txt)
    IVF2M_PQ8_T = re.findall(r"[0-9.]+", IVF2M_PQ8_T_txt)

    IVF4M_PQ8_R1 = re.findall(r"[0-9.]+", IVF4M_PQ8_R1_txt)
    IVF4M_PQ8_T = re.findall(r"[0-9.]+", IVF4M_PQ8_T_txt)

    IVFG_PQ8_R1 = re.findall(r"[0-9.]+", IVFG_PQ8_R1_txt)
    IVFG_PQ8_T = re.findall(r"[0-9.]+", IVFG_PQ8_T_txt)

    IVFGP_PQ8_R1 = re.findall(r"[0-9.]+", IVFGP_PQ8_R1_txt)
    IVFGP_PQ8_T = re.findall(r"[0-9.]+", IVFGP_PQ8_T_txt)

    plt.figure(figsize=[5,4])
    lineOIMI, = plt.plot(OIMI_PQ8_T, OIMI_PQ8_R1, 'r', label = 'OIMI-D-OADC $2^{14}$')
    lineIVF2M, = plt.plot(IVF4M_PQ8_T, IVF4M_PQ8_R1, '-m', label = 'IVFOADC $2^{22}$')
    lineIVF4M, = plt.plot(IVF2M_PQ8_T, IVF2M_PQ8_R1, '-g', label = 'IVFOADC-fast $2^{21}$')
    lineIVFG, = plt.plot(IVFG_PQ8_T, IVFG_PQ8_R1, '-c', label = 'IVFOADC $2^{20}$\nGrouping')
    lineIVFGP, = plt.plot(IVFGP_PQ8_T, IVFGP_PQ8_R1, '--b', label = 'IVFOADC $2^{20}$\nGrouping+Pruning')

    plt.xticks(numpy.arange(0.2, 2.01, 0.2))
    plt.yticks(numpy.arange(0.16, 0.31, 0.02))

    plt.axis([0.2, 2.0, 0.16, 0.28])
    #plt.xlabel('Time (ms)', fontsize=12)
    plt.ylabel('R@1, 8 bytes', fontsize=12)
    #plt.legend(frameon = True, fontsize=9, loc=4)

    pp = PdfPages('recallR1_PQ8.pdf')
    pp.savefig(bbox_inches='tight')
    pp.close()
