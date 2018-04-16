OIMI_R1_txt = '''
0.2540
0.2879
0.3245
0.3455
0.3625
0.3675
0.3712
0.3723
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

IVF2M_R1_txt = '''
0.1942
0.2353
0.2764
0.3165
0.3476
0.3574
0.3635
0.3660
'''
IVF2M_T_txt = '''
0.30
0.32
0.43
0.54
1.04
1.55
2.95
4.21
'''

IVF4M_R1_txt = '''
0.2188
0.2615
0.3133
0.3386
0.3629
0.3698
0.3743
0.3750
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

IVFG_R1_txt = '''
0.1840
0.2240
0.2814
0.3212
0.3591
0.3825
0.3977
0.3908
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

IVFGP_R1_txt = '''
0.2179
0.2608
0.3200
0.3549
0.3878
0.3972
0.4022
0.4030
'''
IVFGP_T_txt = '''
0.30
0.33
0.47
0.64
1.25
1.94
3.44
4.73
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
    OIMI_R1 = re.findall(r"[0-9.]+", OIMI_R1_txt)
    OIMI_T = re.findall(r"[0-9.]+", OIMI_T_txt)

    IVF2M_R1 = re.findall(r"[0-9.]+", IVF2M_R1_txt)
    IVF2M_T = re.findall(r"[0-9.]+", IVF2M_T_txt)

    IVF4M_R1 = re.findall(r"[0-9.]+", IVF4M_R1_txt)
    IVF4M_T = re.findall(r"[0-9.]+", IVF4M_T_txt)

    IVFG_R1 = re.findall(r"[0-9.]+", IVFG_R1_txt)
    IVFG_T = re.findall(r"[0-9.]+", IVFG_T_txt)

    IVFGP_R1 = re.findall(r"[0-9.]+", IVFGP_R1_txt)
    IVFGP_T = re.findall(r"[0-9.]+", IVFGP_T_txt)

    plt.figure(figsize=[5,4])
    lineOIMI, = plt.plot(OIMI_T, OIMI_R1, 'r', label = 'OIMI-D-OADC $2^{14}$')
    lineIVF2M, = plt.plot(IVF2M_T, IVF2M_R1, '-g', label = 'IVFOADC $2^{21}$')
    lineIVF4M, = plt.plot(IVF4M_T, IVF4M_R1, '-m', label = 'IVFOADC $2^{22}$')
    lineIVFG, = plt.plot(IVFG_T, IVFG_R1, '-c', label = 'IVFOADC+G $2^{20}$')
    lineIVFGP, = plt.plot(IVFGP_T, IVFGP_R1, '--b', label = 'IVFOADC+G+P $2^{20}$')

    plt.xticks(numpy.arange(0.2, 2.91, 0.2))
    plt.yticks(numpy.arange(0.18, 0.411, 0.02))

    plt.axis([0.2, 2.81, 0.18, 0.403])
    plt.xlabel('Time (ms)', fontsize=12)
    plt.ylabel('R@1, 16 bytes', fontsize=12)
    #plt.legend(frameon = True, fontsize=9, loc=4)

    pp = PdfPages('recallR1_PQ16_sift.pdf')
    pp.savefig(bbox_inches='tight')
    pp.close()
