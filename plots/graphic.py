SIFT_O_IMI_16384_txt = '''
0.0029	
0.0054	
0.0099	
0.0175	
0.0326	
0.0531	
0.0874	
0.134	
0.202	
0.2908	
0.3979	
0.5213	
0.6388	
0.7532	
0.8464	
0.9154	
0.9612	
0.9831	
0.9948	
0.999	
0.9999	
'''

SIFT_Hybrid_txt = '''
0.0004	
0.0004	
0.0005	
0.0014	
0.003	
0.0063	
0.0118	
0.0239	
0.0499	
0.0968	
0.1823	
0.301	
0.4321	
0.5706	
0.7045	
0.8142	
0.8903	
0.9447	
0.9743	
0.9906	
0.9969	
'''

SIFT_Pruning_25_txt = '''
0.0001
0.0006
0.0017
0.0031
0.0068
0.0151
0.0322
0.0578
0.1110
0.2000
0.3250
0.4713
0.6125
0.7382
0.8275
0.8909
0.9363
0.9648
0.9819
0.9932
0.9970
'''

SIFT_Pruning_50_txt = '''
0.0001
0.0006
0.0018
0.0032
0.0078
0.0160
0.0304
0.0544
0.1032
0.1828
0.2958
0.4242
0.5629
0.6973
0.8099
0.8901
0.9448
0.9756
0.9916
0.9975
0.9999
'''

SIFT_Pruning_75_txt = '''
0.0001
0.0006
0.0020
0.0037
0.0077
0.0145
0.0283
0.0528
0.0968
0.1646
0.2660
0.3891
0.5175
0.6517
0.7707
0.8621
0.9259
0.9628
0.9837
0.9948
0.9982
'''

DEEP_O_IMI_16384_txt = '''
0.0023	
0.0047	
0.0099	
0.0169	
0.0271	
0.0421	
0.0616	
0.0872	
0.122	
0.1735	
0.2384	
0.3264	
0.429	
0.5503	
0.6711	
0.793	
0.8828	
0.9436	
0.9737	
0.9915	
0.9982
'''

DEEP_Hybrid_txt = '''
0.0003	
0.0012	
0.0018	
0.0035	
0.0059	
0.0109	
0.0199	
0.0368	
0.0717	
0.1415	
0.2611	
0.3886	
0.5109	
0.6402	
0.7506	
0.8442	
0.9105	
0.9524	
0.9786	
0.9915	
0.9967	
'''

DEEP_O_IMI_4096_txt='''
0.0007
0.0014
0.0021
0.0047
0.0069
0.0124
0.0221
0.0353
0.0557
0.0876
0.1292
0.1842
0.2577
0.3575
0.4705
0.5893
0.7179
0.8377
0.922
0.9681
0.989
'''

DEEP_Pruning_25_txt = '''
0.0004
0.0011
0.0019
0.0043
0.0092
0.0220
0.0445
0.0849
0.1618
0.2843
0.4106
0.5418
0.6708
0.7693
0.8428
0.8978
0.9360
0.9623
0.9805
0.9907
0.9959
'''

DEEP_Pruning_50_txt = '''
0.0004
0.0011
0.0019
0.0041
0.0107
0.0215
0.0421
0.0798
0.1482
0.2622
0.3764
0.5015
0.6307
0.7436
0.8366
0.9054
0.9479
0.9760
0.9891
0.9956
0.9987
'''

DEEP_Pruning_75_txt = '''
0.0004
0.0011
0.0019
0.0049
0.0106
0.0221
0.0416
0.0775
0.1381
0.2387
0.3494
0.4674
0.5919
0.7087
0.8067
0.8826
0.9348
0.9653
0.9860
0.9940
0.9983
'''

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy
import re
import seaborn as sns
sns.set(style='ticks', palette='Set2')
sns.despine()

k = range(21)

dataset = "DEEP"
if dataset == "SIFT":
    O_IMI = re.findall(r"[0-9.]+", SIFT_O_IMI_16384_txt)
    Hybrid = re.findall(r"[0-9.]+", SIFT_Hybrid_txt)
    Pruning25 = re.findall(r"[0-9.]+", SIFT_Pruning_25_txt)
    Pruning50 = re.findall(r"[0-9.]+", SIFT_Pruning_50_txt)
    Pruning75 = re.findall(r"[0-9.]+", SIFT_Pruning_75_txt)

    plt.figure(figsize=[5.5,4])
    lineIMI, = plt.plot(k, O_IMI, 'r', label = 'Inverted Multi-Index $K{=}2^{14}$')
    lineHybrid, = plt.plot(k, Hybrid, 'g', label = 'Inverted Index $K{=}2^{20}$')
    #linePruning, = plt.plot(k, Pruning25, '-b', label = 'Inverted Index\nGrouping+Pruning 25%')
    linePruning, = plt.plot(k, Pruning50, 'b', label = 'Inverted Index $K{=}2^{20}$\nGrouping+Pruning')
    #linePruning, = plt.plot(k, Pruning75, '-.b', label = 'Inverted Index\nGrouping+Pruning 75%')

    plt.xticks(range(0, 21, 1))
    plt.yticks(numpy.arange(0., 1.1, 0.1))

    plt.axis([0, 20, 0, 1])
    plt.xlabel('Log$_2$R', fontsize=12)
    #plt.ylabel('Recall@R', fontsize=12)
    plt.legend(frameon = True, fontsize=10, loc=2)

    pp = PdfPages('recallR_SIFT.pdf')
    pp.savefig(bbox_inches='tight')
    pp.close()
else:
    O_IMI = re.findall(r"[0-9.]+", DEEP_O_IMI_16384_txt)
    Hybrid = re.findall(r"[0-9.]+", DEEP_Hybrid_txt)
    Pruning25 = re.findall(r"[0-9.]+", DEEP_Pruning_25_txt)
    Pruning50 = re.findall(r"[0-9.]+", DEEP_Pruning_50_txt)
    Pruning75 = re.findall(r"[0-9.]+", DEEP_Pruning_75_txt)

    plt.figure(figsize=[5.5,4])
    lineIMI, = plt.plot(k, O_IMI, 'r', label = 'Inverted Multi-Index $K{=}2^{14}$')
    lineHybrid, = plt.plot(k, Hybrid, 'g', label = 'Inverted Index $K{=}2^{20}$')
    #linePruning, = plt.plot(k, Pruning25, '-b', label = 'Inverted Index\nGrouping+Pruning 25%')
    linePruning, = plt.plot(k, Pruning50, 'b', label = 'Inverted Index $K{=}2^{20}$\nGrouping+Pruning')
    #linePruning, = plt.plot(k, Pruning75, '-.b', label = 'Inverted Index\nGrouping+Pruning 75%')

    plt.xticks(range(0, 21, 1))
    plt.yticks(numpy.arange(0., 1.1, 0.1))

    plt.axis([0, 20, 0., 1.])
    plt.xlabel('Log$_2$R', fontsize=12)
    plt.ylabel('Recall@R', fontsize=12)
    plt.legend(frameon = True, fontsize=10, loc=2)

    pp = PdfPages('recallR_DEEP.pdf')
    pp.savefig(bbox_inches='tight')
    pp.close()
