OIMI_R1_txt = '''
0.2225
0.2540
0.2978
0.3302
0.3702
0.3859
0.3975
0.4020
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

IVF2M_R1_txt = '''
0.2548
0.2992
0.3526
0.3805
0.4138
0.4247
0.4323
0.4355
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

IVF4M_R1_txt = '''
0.2855
0.3302
0.3739
0.4020
0.4264
0.4331
0.4412
0.4512
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

IVFG_R1_txt = '''
0.2284
0.2706
0.3323
0.3739
0.4189
0.4301
0.4383
0.4420
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

IVFGP_R1_txt = '''
0.2622
0.3094
0.3670
0.3995
0.4294
0.4373
0.4452
0.4497
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
    plt.yticks(numpy.arange(0.25, 0.46, 0.02))

    plt.axis([0.2, 2.81, 0.25, 0.451])
    plt.xlabel('Time (ms)', fontsize=12)
    plt.ylabel('R@1, 16 bytes', fontsize=12)
    #plt.legend(frameon = True, fontsize=9, loc=4)

    pp = PdfPages('recallR1_PQ16.pdf')
    pp.savefig(bbox_inches='tight')
    pp.close()
