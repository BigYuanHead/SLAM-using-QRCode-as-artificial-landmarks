import math
a = [0.000000,
-0.0001810,
-0.0004225,
-0.0010072,
-0.0021125,
-0.0037291,
-0.0059208,
-0.0082217,
-0.010697,
-0.004871,
0.008716,
0.039192,
0.085473,
0.134076,
0.172065,
0.174285,
0.183659,
0.198843,
0.207029,
0.207972,
0.208021,
0.208076,
0.211877,
0.225798,
0.246923,
0.278120,
0.303741,
0.282113,
0.245127,
0.203731,
0.158892,
0.120080,
0.085122,
0.079554,
0.079131,
0.081262,
0.113117,
0.152933,
0.193229,
0.237464,
0.276757,
0.316514,
0.351124,
0.383007,
0.404550,
0.417801,
0.422449,
0.4178019,
0.4055034,
0.3819181,
0.3509293,
0.3465201,
0.3460738,
0.3380378,
0.2750869,
0.2090839,
0.1658193,
0.1165279,
0.0573138,
0.0059948,
-0.0513821,
-0.0978419,
-0.1472980,
-0.2047140,
-0.2447607,
-0.2375077,
-0.2401512,
-0.2404788,
-0.2375314,
-0.2153654,
-0.1848089,
-0.1497898,
-0.1125241,
-0.0974419,
-0.1423754,
-0.2216667,
-0.2093040,
-0.2059396,
-0.2059396,
-0.2059396,
-0.1974953,
-0.1605525,
-0.1212822,
-0.1463211,
-0.2239827,
-0.3095341,
-0.3861885,
-0.4712214,
-0.5304320,
-0.5748256,
-0.6322732,
-0.6655043,
-0.6638405,
-0.6638383,
-0.6647063,
-0.6647063,
-0.6981830,
-0.7704522,
-0.8304664,
-0.8725048,
-0.8926665,
-0.9000501,
-0.9085674,
-0.9128725,
-0.9122831,
-0.9120884,
-0.9120884,
-0.9120484,
-0.9087318,
-0.9002721,
-0.8875877,
-0.8634493,
-0.8184736,
-0.7660035,
-0.7192353,
-0.6669237,
-0.6042613,
-0.5358840,
-0.4684601,
-0.4247507,
-0.3864375,
-0.3440284,
-0.3213039,
-0.3201734,
-0.3201734,
-0.3201734,
-0.3201734,
-0.3431288,
-0.3830985,
-0.4174403,
-0.4460422,
-0.4467711,
-0.4478565,
-0.4478565,
-0.4478565,
-0.4478565,
-0.4377155,
-0.4198118,
-0.4045746,
-0.3989550,
-0.3985724,
-0.3991528,
-0.3992429,
-0.3992621,
-0.4027965,
-0.4108120,
-0.4269008,
-0.4574786,
-0.5072130,
-0.5471963,
-0.5853742,
-0.6181695,
-0.6216616,
-0.6225357,
-0.6225357,
-0.6185852,
-0.5914135,
-0.5489330,
-0.5085644,
-0.4648417,
-0.4190786,
-0.3849676,
-0.3498663,
-0.3083815,
-0.2669103,
-0.2169564,
-0.1697564,
-0.1222326,
-0.0837653,
-0.0364673,
0.0126489,
0.0532076,
0.0532017,
0.0532017,
0.0532017,
0.0532017,
0.0532017,
0.0532017,
0.0532017,
0.0466395,
0.0005440,
-0.0029926,
-0.0203313,
-0.0329563,
-0.0355042,
-0.0815391,
-0.1238979,
-0.1412412,
-0.1422496,
-0.1487306,
-0.1803581,
-0.2012805,
-0.2024371,
-0.2168761,
-0.2310098,
-0.2313107,
-0.2354729,
-0.2721973,
-0.3172696,
-0.3597578,
-0.3968182,
-0.4345523,
-0.4807729,
-0.5194465,
-0.5564789,
-0.5650820,
-0.5673087,
-0.5720735,
-0.5865089,
-0.5941581,
-0.5920647,
-0.5833274,
-0.5745925,
-0.5655720,
-0.5514931,
-0.5321591 ,
-0.5026544 ,
-0.4680313 ,
-0.4314630 ,
-0.3840358 ,
-0.3732732 ,
-0.3698722 ,
-0.3414257 ,
-0.2805286 ,
-0.2409278 ,
-0.2375789 ,
-0.2375789 ,
-0.2375789 ,
-0.2336729 ,
-0.1952525 ,
-0.1280995 ,
-0.1201278 ,
-0.0996783 ,
-0.0470030 ,
-0.0097312 ,
0.0144708 ,
0.0158512 ,
0.0323614 ,
0.0933016 ,
0.1667211 ,
0.2233222 ,
0.2836074 ,
0.3021843 ,
0.3054252 ,
0.3277492 ,
0.3538114 ,
0.3742468 ,
0.3840443 ,
0.3854788 ,
0.3853505 ,
0.3853505 ,
0.3869715 ,
0.3902965 ,
0.3853272 ,
0.3811790 ,
0.3753313 ,
0.3718396 ,
0.3715028 ,
0.3694930 ,
0.3575803 ,
0.3350470 ,
0.3047695 ,
0.2660220 ,
0.2310259 ,
0.2161547 ,
0.2150446 ,
0.2106107 ,
0.1641767 ,
0.1560642 ,
0.1528323 ,
0.1625177 ,
0.1972177 ,
0.2274803 ,
0.2813990 ,
0.2946135 ,
0.3347066 ,
0.3726883 ,
0.3971903 ,
0.3977537 ,
0.3954986 ,
0.3688270 ,
0.3534556 ,
0.3511809 ,
0.3511809 ,
0.3336015 ,
0.3116473 ,
0.3110858 ,
0.3043437 ,
0.2465406 ,
0.2414163 ,
0.2362909 ,
0.2220533 ,
0.1651121 ,
0.1526252 ,
0.1492196 ,
0.1384235 ,
0.0986812 ,
0.0902508 ,
0.0902508 ,
0.0902508 ]

print max(a)
print min(a)

print max(a)-min(a)
from math import pi
print pi/4