# inpy - module waarmee die Axpert gelykrigter afgelaaide data prosesseer word

import pandas as pd

# Leernaam:  Hierdie moet as 'n inset gestel word
leernaam = 'inverterlog_20190417.out'

df = pd.read_csv(leernaam, names=['Date', 'Time', 'Grid voltage', 'Grid frequency', 'AC output voltage', 'AC output frequency',
                                 'AC output apparent power', 'AC output active power', 'Output load percent',
                                 'BUS voltage', 'Battery voltage', 'Battery charging current', 'Battery capacity',
                                 'Inverter heat sink temperature', 'PV Input current 1', 'PV Input voltage 1',
                                 'Battery voltage from SCC 1', 'Battery discharge current', 'Device status',
                                 'Battery voltage offset for fans on', 'EEPROM version', 'PV Charging power 1',
                                 'Device status 2'], 
                     sep=" ", engine='python')

df['DateTime'] = df['Date'] + ' ' + df['Time']
df['DateTime'] = pd.to_datetime(df['DateTime'], format='%d/%m/%Y %H:%M:%S')
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')

import matplotlib.pyplot as plt
import matplotlib.dates as md

ax = plt.gca()

df.plot(kind='line',x='DateTime', y='Battery discharge current',ax=ax)
plt.xticks(rotation=45)  # Maak die x-as geskrewe gedeelte teen 45 grade
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M')) # Formateer die tyd in ure en minute

plt.show()

ax = plt.gca()

df.plot(kind='line',x='DateTime',y='PV Charging power 1',ax=ax)
df.plot(kind='line',x='DateTime',y='AC output active power', color='red', ax=ax)

fig = ax.get_figure()

plt.xticks(rotation=45)  # Changed here
ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M'))

plt.show()



