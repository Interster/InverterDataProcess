# inpy - module waarmee die Axpert gelykrigter afgelaaide data prosesseer word
#
# Maak leers skoon met die volgende:
# sed '/NAK/d' ./inverterlog_20190725.out > inverterlog_20190725.rep



import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md


# Lees in die lys van metingsleers wat prossesseer moet word
metinglysleernaam = 'metinglys'

dfmetings = pd.read_csv(metinglysleernaam, names=['metings'], 
                     sep=" ", engine='python')


# Lees in 'n meting
leernaam = dfmetings['metings'][2]


class dagMeting:
    def __init__(self, metingleer):
        self.df = pd.read_csv(leernaam, names=['Date', 'Time', 'Grid voltage', 'Grid frequency', 'AC output voltage', 'AC output frequency',
                                 'AC output apparent power', 'AC output active power', 'Output load percent',
                                 'BUS voltage', 'Battery voltage', 'Battery charging current', 'Battery capacity',
                                 'Inverter heat sink temperature', 'PV Input current 1', 'PV Input voltage 1',
                                 'Battery voltage from SCC 1', 'Battery discharge current', 'Device status',
                                 'Battery voltage offset for fans on', 'EEPROM version', 'PV Charging power 1',
                                 'Device status 2'], 
                     sep=" ", engine='python')
        self.df['DateTime'] = self.df['Date'] + ' ' + self.df['Time']
        self.df['DateTime'] = pd.to_datetime(self.df['DateTime'], format='%d/%m/%Y %H:%M:%S')
        self.df['Time'] = pd.to_datetime(self.df['Time'], format='%H:%M:%S')
    
    # Plot 'n parameter op 'n grafiek
    def plotinv(self, lysPlotParameters):
        ax = plt.gca()

        for teller in range(0, len(lysPlotParameters)):
            self.df.plot(kind='line',x='DateTime', y=lysPlotParameters[teller], ax=ax)
        
        plt.xticks(rotation=45)  # Maak die x-as geskrewe gedeelte teen 45 grade
        ax.xaxis.set_major_formatter(md.DateFormatter('%H:%M')) # Formateer die tyd in ure en minute

        plt.show()

    def plotAlleParameters(self):
        # Battery toestand plot:  Antwoord volgende vrae
        # Was die battery heeltemal leeg en hoe het dit ontlaai en gelaai
        self.plotinv(['Battery capacity'])
        self.plotinv(['Battery discharge current', 'Battery charging current'])
        # Kyk hoe die battery kapasiteit lyk vanaf 'n battery spanning oogpunt
        # Wys ook hoe spanning met die las verander
        self.plotinv(['BUS voltage'])
        self.plotinv(['Battery voltage'])
        self.plotinv(['Battery voltage from SCC 1'])
        # Drywing vanaf paneel:  Hoe baie son was daar en hoeveel drywing vanaf die paneel
        self.plotinv(['PV Charging power 1', 'AC output active power'])
        # Energiemeting in kWh op die meettoestel (Owl) is heel waarskynlik skynkrag.  Dit stem die
        # beste ooreen met die energie somtotaal soos bereken.
        self.plotinv(['PV Charging power 1', 'AC output apparent power'])
        # Kyk na die stroom en spanning op die panele.  Dit wys wanneer daar die meeste sonkrag is
        # en wys hoe die stroom en spanning oor die bereik van 'n dag wissel
        self.plotinv(['PV Input voltage 1'])
        self.plotinv(['PV Input current 1'])
        # Plot hoeveel las op die stelsel is:
        self.plotinv(['Output load percent'])
        # Plot die frekwensies om die krag kwaliteit te ondersoek
        self.plotinv(['Grid voltage', 'Grid frequency'])
        # Plot die insetspanning en uitsetspanning om te sien wanneer krag afgegaan het.
        self.plotinv(['AC output voltage', 'AC output frequency'])
        # Kyk of die gelykrigter warm geword het deur hitteruiler temperatuur te plot
        self.plotinv(['Inverter heat sink temperature'])

    def drukAlleBerekeninge(self):
        # Differensieer om delta T te bereken
        self.df['dT'] = self.df['Time'].diff(1)
        # Verander die delta T van 'n tyd data tipe na wisselpunt datatipe
        self.df['dT'] = pd.to_numeric(self.df['dT'].dt.seconds, downcast='float')/3600
        self.df['EnergieGelewer'] = self.df['dT']*self.df['AC output active power']/1000
        self.df['SkynEnergieGelewer'] = self.df['dT']*self.df['AC output apparent power']/1000
        self.df['EnergiePV'] = self.df['dT']*self.df['PV Charging power 1']/1000
        self.df['EnergieLaaiBattery'] = self.df['dT']*self.df['Battery voltage']*self.df['Battery charging current']/1000
        self.df['EnergieOnttrekBattery'] = self.df['dT']*self.df['Battery voltage']*self.df['Battery discharge current']/1000

        # Energie statistiek
        print('Energie gelewer aan las is')
        print(self.df['EnergieGelewer'][1:-1].sum())
        print('Skyn Energie gelewer aan las is')
        print(self.df['SkynEnergieGelewer'][1:-1].sum())

        print('Energie opgewek uit PV is')
        print(self.df['EnergiePV'][1:-1].sum())
        
        # Battery statistiek
        print('Energie gebruik om battery te laai is')
        print(self.df['EnergieLaaiBattery'][1:-1].sum())
        print(self.df['EnergieLaaiBattery'][1:-1].sum()*1000/48)
        print('Energie onttrek uit battery is')
        print(self.df['EnergieOnttrekBattery'][1:-1].sum())
        print(self.df['EnergieOnttrekBattery'][1:-1].sum()*1000/48)





eenDag = dagMeting(leernaam)
eenDag.plotAlleParameters()
eenDag.drukAlleBerekeninge()












                                  
                                 
                                 
                                 





# Te doen:
# Kyk of die OWL nie eintlik verwys na skyndrywing VAR nie.  Miskien is dit wat dit wys en werklike drywing is eers na verliese?
# Stel energiebalans op.  Wat gaan in en wat gaan uit.  En is daar 'n netto voordeel.

# Skryf 'n verslag module wat 'n markdown verslag maak van 'n sekere dag se plot data.
# Skryf 'n plot funksie wat 'n sekere plot maak.

# Berekende energie onttrek uit battery is altyd meer as laai energie.  Hoe is dit moontlik?
# Laai die battery miskien nie heeltemal nie?  Miskien moet laai stroom laer gestel word.
# Miskien is die sampling rate te groot om die groot laaistrome te sien wat die battery laai?

