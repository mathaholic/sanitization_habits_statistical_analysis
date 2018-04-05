import numpy as np

np.random.seed(5271009)
a = ['car-lobby', 'car-gym', 'con-3', 'con-5', 'con-10', 'con-12', 'con-16', 'yarn', 'eca']
for loc in a:
   print(loc, np.random.choice(['C', 'T']))

#results
#car-lobby C
#car-gym C
#con-3 T
#con-5 T
#con-10 C
#con-12 T
#con-16 C
#yarn C
#eca T