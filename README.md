# Data Prosessering vir die Axpert Gelykrigter

Python pakket met standaard funksie wat die energievloei van 'n Axpert  gelykrigter analiseer.

Die vloei van energie word met die volgende vloeidiagram analiseer:

![EnergieVloei](F:\Rugsteun\Projekte\Huis\Verbeteringe\Sonpanele\Logs\dataproses\Prente\EnergieVloei.png)

Die funksies in die pakket moet die volgende vrae beantwoord:

- Hoeveel energie kan battery werklik stoor en lewer.  Dit is moontlik dat 'n battery wat 400Ah kapasiteit het glad nie naby hierdie kapasiteit kan lewer nie.  Ondersoek hierdie stelling.
- Hoeveel energie word uit lynkrag gebruik.
- Hoeveel kWh lewer die sonpanele en hoe vergelyk dit met die spesifikasie van die panele.  Dus:  Lewer 'n 330W paneel werklike 330W en hoe varieer die lewering tussen seisoene in die jaar.
- Wat is die drywing van al die laste tans en wat is die energie wat deur die las gebruik word.  Hoe varieer dit met tyd.

Die volgende plot funksies is beskikbaar:

- Plot drywing teen die tyd in die dag vir verskillende items
- Plot drywing vir verskillende dae in die jaar.

Data word met die Axpert gemeer per dag.  Die data word in 'n tekslêer gestoor wat ongeveer 1MB groot is vir elke dag.

Die data het partykeer foute in.  Daar is Linux opdragte wat voor die tyd op die data uitgevoer word om dit skoon te maak.

Die daaglikse data word dan ingelees in Python.

Dit word dan in 'n groter binêre databasis gestoor vir verder verwerking.