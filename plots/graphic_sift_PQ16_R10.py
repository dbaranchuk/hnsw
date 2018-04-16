OIMI_R10_txt = '''
0.4151
0.5195
0.6372
0.7195
0.7956
0.8215
0.8392
0.8442
'''
OIMI_T_txt = '''
1.43
1.59
1.97
2.53
4.24
6.61
12.8
21.1
'''

IVF2M_R10_txt = '''
0.2917
0.3819
0.5262
0.6256
0.7438
0.7845
0.8108
0.8204
'''
IVF2M_T_txt = '''
0.31
0.33
0.44
0.55
1.05
1.56
2.96
4.22
'''

IVF4M_R10_txt = '''
0.3288
0.4297
0.5788
0.6716
0.7691
0.8010
0.8243
0.8313
'''
IVF4M_T_txt = '''
0.35
0.43
0.71
1.10
2.70
4.27
8.36
13.1
'''

IVFG_R10_txt = '''
0.2613
0.3416
0.4772
0.5900
0.7380
0.7858
0.8324
0.8485
'''
IVFG_T_txt = '''
0.29
0.33
0.44
0.57
1.12
1.69
3.10
4.41
'''

IVFGP_R10_txt = '''
0.3216
0.4196
0.5743
0.6778
0.7895
0.8250
0.8492
0.8582
'''
IVFGP_T_txt = '''
0.30
0.33
0.47
0.64
1.25
1.94
3.44
4.72
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
    lineOIMI, = plt.plot(OIMI_T, OIMI_R10, 'r', label = 'O-Multi-D-OADC $2^{14}$')
    lineIVF2M, = plt.plot(IVF4M_T, IVF4M_R10, '-m', label = 'IVFOADC $2^{22}$')
    lineIVF4M, = plt.plot(IVF2M_T, IVF2M_R10, '-g', label = 'IVFOADC-fast $2^{21}$')
    lineIVFG, = plt.plot(IVFG_T, IVFG_R10, '-c', label = 'IVFOADC+G $2^{20}$')
    lineIVFGP, = plt.plot(IVFGP_T, IVFGP_R10, '--b', label = 'IVFOADC+G+P $2^{20}$')

    plt.xticks(numpy.arange(0.2, 2.91, 0.2))
    plt.yticks(numpy.arange(0.28, 0.841, 0.04))

    plt.axis([0.2, 2.81, 0.31, 0.841])
    plt.xlabel('Time (ms)', fontsize=12)
    plt.ylabel('R@10, 16 bytes', fontsize=12)
    plt.legend(frameon = True, fontsize=9, loc=4)

    pp = PdfPages('recallR10_PQ16_sift.pdf')
    pp.savefig(bbox_inches='tight')
    pp.close()
