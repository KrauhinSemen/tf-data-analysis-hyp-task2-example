import pandas as pd
import numpy as np


chat_id = 1081838572 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы

    f = [[-0.45347663,  0.27220621], [-0.45783903,  0.15800409], [-0.39713278,  0.21315491], [-0.1534459 ,  0.56910535], [-0.23203341,  0.39651871], [-0.23540821,  0.44729791], [-0.28674559,  0.42673496], [-0.31440981,  0.45039466], [-0.10698279,  0.53646296], [-0.31800414,  0.42820409], [-0.32605111,  0.46649218], [-0.29893664,  0.26222243], [-0.44900584,  0.24944462], [-0.42202174,  0.26433779], [-0.23676192,  0.4162817 ], [-0.45768823,  0.12508382], [-0.11609244,  0.62927888], [-0.39410045,  0.46618143], [-0.41362286,  0.35505898], [-0.18099788,  0.47833207], [-0.30989921,  0.43929524], [-0.24845794,  0.25953287], [-0.3856808 ,  0.30843993], [-0.51395253,  0.22298585], [-0.4577331,  0.249706 ], [-0.56299795,  0.17823464], [-0.23786122,  0.39680083], [-0.24878501,  0.30249303], [-0.43868198,  0.47415679], [-0.32602131,  0.25937902], [-0.31513243,  0.3961661 ], [-0.34398339,  0.17536241], [-0.36990796,  0.28293772], [-0.24128132,  0.22718757], [-0.38812648,  0.32005191], [-0.37890852,  0.26181385], [-0.32109324,  0.33661532], [-0.40062323,  0.18366557], [-0.4213322 ,  0.30393602], [-0.30502293,  0.32400561], [-0.30134506,  0.32054132], [-0.11469866,  0.5391073 ], [-0.16018964,  0.55013039], [-0.66944039,  0.09318695], [-0.25031731,  0.50263463], [-0.25578414,  0.51851575], [-0.18992645,  0.37787923], [-0.15355007,  0.33019155], [-0.47299897,  0.4097965 ], [-0.28266009,  0.3847183 ], [-0.39329739,  0.49216967], [-0.22699385,  0.49499269], [-0.34936198,  0.28307444], [-0.53355445,  0.18970354], [-0.30498053,  0.41533671], [-0.16247278,  0.37454006], [-0.269474  ,  0.30794574], [-0.49163123,  0.24217175], [-0.45217431,  0.11620378], [-0.2687485 ,  0.35429193], [-0.35948359,  0.21243245], [-0.34045639,  0.22177259], [-0.32828005,  0.35856204], [-0.37642082,  0.38239703], [-0.22464506,  0.47976912], [-0.19505811,  0.27073614], [-0.36708695,  0.32338283], [-0.34273886,  0.28091236], [-0.31515941,  0.32569886], [-0.40425932,  0.22200934], [-0.25444083,  0.26846595], [-0.36393616,  0.27882373], [-0.36315673,  0.31507875], [-0.12003686,  0.44999281], [-0.51282115,  0.23340435], [-0.2682333 ,  0.50740981], [-0.437483  ,  0.22799816], [-0.50374982,  0.10605548], [-0.22128125,  0.29645266], [-0.06041933,  0.58607161], [-0.27648806,  0.29699562], [-0.35555055,  0.24869428], [-0.20041954,  0.51557175], [-0.21185404,  0.28995976], [-0.02984627,  0.44862183], [-0.19623875,  0.47724555], [-0.4187941 ,  0.33824473], [-0.53755652,  0.29684721], [-0.26897696,  0.36224806], [-0.45083767,  0.10672345], [-0.43797689,  0.30344327], [-0.33235009,  0.32449076], [-0.32862907,  0.3240036 ], [-0.23781731,  0.37562724], [-0.11268159,  0.49865423], [-0.51319912,  0.28365847], [-0.45790761,  0.27912988], [-0.21649112,  0.39175133], [-0.39491126,  0.213458  ], [-0.2960739 ,  0.31313633], [-0.23827371,  0.32135217], [-0.49354873,  0.0885421 ], [-0.26797941,  0.35728668], [-0.28713702,  0.47733567], [-0.38093934,  0.23381065], [-0.27484843,  0.42908331], [-0.44118942,  0.35029355], [-0.31111402,  0.39848138], [-0.38853752,  0.39641557], [-0.34524628,  0.10787902], [-0.30429399,  0.42766306], [-0.18857463,  0.35834556], [-0.30899103,  0.29293028], [-0.29323927,  0.29002943], [-0.19479023,  0.4613925 ], [-0.26751667,  0.32293251], [-0.40536973,  0.3137651 ], [-0.1617383 ,  0.41279856], [-0.58097065,  0.17217395], [-0.42126704,  0.31957903], [-0.41925614,  0.2886639 ], [-0.27920304,  0.51002122], [-0.22614816,  0.28470912], [-0.41878508,  0.37197805], [-0.4568118 ,  0.47044443], [-0.46212056,  0.28036782], [-0.281892  ,  0.36363907], [-0.14566535,  0.50149104], [-0.53048017,  0.27171603], [-0.35079674,  0.4004317 ], [-0.31297053,  0.36714961], [-0.27568271,  0.27385582], [-0.10501666,  0.50671672], [-0.24740321,  0.26865676], [-0.28879646,  0.39788149], [-0.16764008,  0.37033728], [-0.63438491,  0.1591369 ], [-0.2300987 ,  0.36147768], [-0.25152833,  0.39341124], [-0.41144569,  0.32454745], [-0.63415539,  0.223294  ], [-0.43926186,  0.30599821], [-0.36882212,  0.17523306], [-0.37091436,  0.38452984], [-0.28784063,  0.29369451], [-0.22296379,  0.45137699], [-0.25890214,  0.31399014], [-0.2109258 ,  0.45326324], [-0.26543651,  0.41320927], [-0.34865016,  0.35876188], [-0.25099131,  0.29707866], [-0.37604937,  0.18806575], [-0.28345737,  0.24498232], [-0.33694534,  0.33380705], [-0.16957005,  0.41350616], [-0.29985306,  0.31005145], [-0.2187742 ,  0.25523625], [-0.31869976,  0.26651085], [-0.44668299,  0.20191331], [-0.07389751,  0.60010648], [-0.33314416,  0.32454487], [-0.35287518,  0.28382769], [-0.27826654,  0.41142464], [-0.64680004,  0.25863748], [-0.4216422 ,  0.21926132], [-0.16271973,  0.65662102], [-0.28954253,  0.36880695], [-0.59076895,  0.2224798 ], [-0.1252302 ,  0.33916621], [-0.24816725,  0.36154436], [-0.60401137,  0.20666741], [-0.3216365 ,  0.59278149], [-0.43897237,  0.20169567], [-0.19206083,  0.41179363], [-0.35739476,  0.29885191], [-0.53765804,  0.18643218], [-0.20362163,  0.45180901], [-0.24790348,  0.39280364], [-0.30803305,  0.21221927], [-0.28310623,  0.38943168], [-0.40948816,  0.30396212], [-0.41549887,  0.32898279], [-0.41978508,  0.21145919], [-0.45822321,  0.08088075], [-0.27216087,  0.2529614 ], [-0.47923801,  0.23863337], [-0.25526167,  0.37438055], [-0.38706552,  0.17258519], [-0.51621101,  0.31345986], [-0.3728164 ,  0.37425523], [-0.36323668,  0.43904308], [-0.31981399,  0.31028123], [-0.24046212,  0.33928055], [-0.10808667,  0.37537323], [-0.30469255,  0.24929315], [-0.35706266,  0.36912153], [-0.45890795,  0.28417944], [-0.48470638,  0.2521294 ], [-0.31029384,  0.27512815], [-0.46127012,  0.29771623], [-0.37034757,  0.25503066], [-0.26740068,  0.2668725 ], [-0.52897682,  0.14878703], [-0.22982716,  0.42216882], [-0.30799187,  0.34924627], [-0.47376164,  0.17696965], [-0.46151276,  0.26267859], [-0.28816125,  0.42135474], [-0.42502237,  0.38914016], [-0.31135137,  0.44063362], [-0.31853699,  0.32851956], [-0.28319524,  0.3487871 ], [-0.42224336,  0.22568165], [-0.40327002,  0.33213601], [-0.26776216,  0.38763421], [-0.23946904,  0.46302023], [-0.38729292,  0.24536595], [-0.33838365,  0.43438089], [-0.06542725,  0.48907088], [-0.30153687,  0.41616741], [-0.56710406,  0.16158428], [-0.48885349,  0.17224169], [-0.19384662,  0.3947951 ], [-0.43307309,  0.17688385], [-0.56931403,  0.19796857], [-0.14949468,  0.52694189], [-0.27647591,  0.45825028], [-0.27795971,  0.4197487 ], [-0.20502782,  0.35111378], [-0.36630283,  0.20198321], [-0.25318827,  0.32114033], [-0.29046364,  0.34933749], [-0.40841886,  0.14506028], [-0.4217886 ,  0.13337728], [-0.23002564,  0.34602821], [-0.51578569,  0.19710519], [-0.39652068,  0.11385241], [-0.2880946 ,  0.35144798], [-0.4480858,  0.1305326], [-0.34737362,  0.37827225], [-0.48887328,  0.07070486], [-0.18954835,  0.40557852], [-0.28033141,  0.40024367], [-0.42428453,  0.26392352], [-0.50248558,  0.08035272], [-0.17037655,  0.42443548], [-0.59675731,  0.08960792], [-0.17714231,  0.3227227 ], [-0.28450385,  0.29917909], [-0.52554258,  0.13333184], [-0.43207593,  0.14709286], [-0.3202642 ,  0.25201933], [-0.26232532,  0.35272309], [-0.25279977,  0.31549611], [-0.53417346,  0.0713415 ], [-0.40888848,  0.28878608], [-0.445935  ,  0.18069694], [-0.27309215,  0.2771711 ], [-0.24316494,  0.45854147], [-0.43262011,  0.38473131], [-0.52085518,  0.10853955], [-0.30410629,  0.3053747 ], [-0.2256723 ,  0.43237958], [-0.41947546,  0.26695301], [-0.14801578,  0.54073802], [-0.24671093,  0.4633422 ], [-0.37720506,  0.11943046], [-0.41983498,  0.12965383], [-0.32283115,  0.24914337], [-0.32147848,  0.17547486], [-0.54054832,  0.15152153], [-0.47423382,  0.16259385], [-0.41050183,  0.27298287], [-0.29646054,  0.37926778], [-0.19434007,  0.50862396], [-0.12182786,  0.45126417], [-0.22267234,  0.39015677], [-0.62754234,  0.08950448], [-0.23326928,  0.48351041], [-0.18978782,  0.40824623], [-0.16135994,  0.4147245 ], [-0.24291954,  0.50688929], [-0.22158123,  0.5386881 ], [-0.16308511,  0.47151593], [-0.24422439,  0.5513456 ], [-0.16106155,  0.46395776], [-0.43852072,  0.29579807], [-0.00518675,  0.57012565], [-0.20110089,  0.47557013], [-0.34358808,  0.20335774], [-0.17405411,  0.34127967], [-0.50897781,  0.33625025], [-0.4610996 ,  0.21264605], [-0.42184917,  0.22615974], [-0.31657175,  0.32808066], [-0.25504365,  0.37950202], [-0.41889186,  0.37236164], [-0.21411987,  0.49120792], [-0.19615458,  0.45965053], [-0.3064412,  0.4141844]]
    # квантили 0.4 и 0.6 от исторических данных

    tr_x = 0
    fl_x = 0
    for j in range(len(x.tolist())):
      if f[j][1] >= x[j] >= f[j][0]:
           tr_x += 1
      else:
           fl_x += 1

    tr_y = 0
    fl_y = 0
    for j in range(len(y.tolist())):
      if f[j][1] >= y[j] >= f[j][0]:
           tr_y += 1
      else:
           fl_y+=1

    return tr_x/fl_x < tr_y/fl_y  # Ваш ответ, True или False
