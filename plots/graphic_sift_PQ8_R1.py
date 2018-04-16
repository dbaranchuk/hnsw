OIMI_PQ8_R1_txt = '''
0.1507
0.1673
0.1758
0.1820
0.1849
0.1860
0.1862
0.1870
'''
OIMI_PQ8_T_txt = '''
1.28
1.40
1.64
2.04
3.11
4.76
8.90
13.1
'''
IVF2M_PQ8_R1_txt = '''
0.1150
0.1357
0.1560
0.1648
0.1727
0.1746
0.1755
0.1755
'''
IVF2M_PQ8_T_txt = '''
0.26
0.28
0.39
0.48
0.87
1.31
2.33
3.32
'''
IVF4M_PQ8_R1_txt = '''
0.1321
0.1491
0.1648
0.1724
0.1771
0.1779
0.1785
0.1790
'''
IVF4M_PQ8_T_txt = '''
0.33
0.38
0.58
0.85
1.95
3.14
6.58
9.7
'''
IVFG_PQ8_R1_txt = '''
0.1161
0.1356
0.1628
0.1802
0.2001
0.2029
0.2048
0.2053
'''
IVFG_PQ8_T_txt = '''
0.26
0.28
0.39
0.50
0.97
1.46
2.60
3.78
'''

IVFGP_PQ8_R1_txt = '''
0.1310
0.1532
0.1784
0.1933
0.2048
0.2051
0.2052
0.2057
'''
IVFGP_PQ8_T_txt = '''
0.27
0.31
0.43
0.56
1.09
1.70
3.01
4.51
'''

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy
import re
import seaborn as sns
sns.set(style='ticks', palette='Set2')
sns.despine()

dataset = "SIFT"
if dataset == "SIFT":
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
    plt.yticks(numpy.arange(0.11, 0.32, 0.01))

    plt.axis([0.2, 2.0, 0.11, 0.211])
    #plt.xlabel('Time (ms)', fontsize=12)
    plt.ylabel('R@1, 8 bytes', fontsize=12)
    
    pp = PdfPages('recallR1_PQ8_sift.pdf')
    pp.savefig(bbox_inches='tight')
    pp.close()
