
from inpy import *

# Lees in die lys van metingsleers wat prossesseer moet word
metinglysleernaam = 'metinglys'

dfmetings = pd.read_csv(metinglysleernaam, names=['metings'], 
                     sep=" ", engine='python')


# Lees in 'n meting
leernaam = dfmetings['metings'][6]


eenDag = dagMeting(leernaam)
eenDag.plotAlleParameters()
eenDag.drukAlleBerekeninge()