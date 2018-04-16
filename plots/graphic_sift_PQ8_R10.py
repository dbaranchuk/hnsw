OIMI_PQ8_R10_txt = '''
0.3571
0.4255
0.4853
0.5198
0.5477
0.5545
0.5583
0.5596
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
IVF2M_PQ8_R10_txt = '''
0.2566
0.3248
0.4155
0.4648
0.5152
0.5284
0.5353
0.5392
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
IVF4M_PQ8_R10_txt = '''
0.2925
0.3606
0.4482
0.4901
0.5232
0.5328
0.5385
0.5394
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
IVFG_PQ8_R10_txt = '''
0.2383
0.3028
0.4007
0.4713
0.5495
0.5689
0.5864
0.5916
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

IVFGP_PQ8_R10_txt = '''
0.2884
0.3622
0.4639
0.5212
0.5717
0.5838
0.5926
0.5952
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
    lineOIMI, = plt.plot(OIMI_PQ8_T, OIMI_PQ8_R10, 'r', label = 'OIMI-D-OADC $2^{14}$')
    lineIVF2M, = plt.plot(IVF4M_PQ8_T, IVF4M_PQ8_R10, '-m', label = 'IVFOADC $2^{22}$')
    lineIVF4M, = plt.plot(IVF2M_PQ8_T, IVF2M_PQ8_R10, '-g', label = 'IVFOADC-fast $2^{21}$')
    lineIVFG, = plt.plot(IVFG_PQ8_T, IVFG_PQ8_R10, '-c', label = 'IVFOADC $2^{20}$\nGrouping')
    lineIVFGP, = plt.plot(IVFGP_PQ8_T, IVFGP_PQ8_R10, '--b', label = 'IVFOADC $2^{20}$\nGrouping+Pruning')

    plt.xticks(numpy.arange(0.2, 2.01, 0.2))
    plt.yticks(numpy.arange(0.23, 0.601, 0.03))

    plt.axis([0.2, 2.0, 0.23, 0.591])
    #plt.xlabel('Time (ms)', fontsize=12)
    plt.ylabel('R@10, 8 bytes', fontsize=12)
    
    pp = PdfPages('recallR10_PQ8_sift.pdf')
    pp.savefig(bbox_inches='tight')
    pp.close()
