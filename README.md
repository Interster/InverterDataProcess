# Data Prosessering vir die Axpert Gelykrigter

Python pakket met standaard funksie wat die energievloei van 'n Axpert  gelykrigter analiseer.

Die vloei van energie word met die volgende vloeidiagram analiseer:

![EnergieVloei](Prente/EnergieVloei.png)

Die funksies in die pakket moet die volgende vrae beantwoord:

- Hoeveel energie kan battery werklik stoor en lewer.  Dit is moontlik dat 'n battery wat 400Ah kapasiteit het glad nie naby hierdie kapasiteit kan lewer nie.  Ondersoek hierdie stelling.
- Hoeveel energie word uit lynkrag gebruik.
- Hoeveel kWh lewer die sonpanele en hoe vergelyk dit met die spesifikasie van die panele.  Dus:  Lewer 'n 330W paneel werklike 330W en hoe varieer die lewering tussen seisoene in die jaar.
- Wat is die drywing van al die laste tans en wat is die energie wat deur die las gebruik word.  Hoe varieer dit met tyd.

Doel van berekenings

- Bepaal hoeveel battery krag is gebruik in Ampere uur. Bepaal hoe lank die yskaste op battery kan loop
- Bepaal hoeveel siklusse die battery gedoen het.  Hoeveel keer is die battery laat afloop na die limiet spanning toe.  Gebruik 'n rainflow counter indien nodig om die siklusse te tel.  Dit is moontlik dat gedurende gewone gebruik dat die battery afloop na 'n lae spanning toe omdat die sonkrag te min is.  Maak 'n grafiek van hoeveel keer die battery afgeloop het.
- Meet hoeveel sonkrag kan per dag opgegaar word. En of dit genoeg is om las te trek
- As dit nie genoeg sonkrag verskaf nie, hoeveel is die bydrae van die lynkrag in Rand
- Teen watter battery Volts moet die inverter teruggaan na lyn krag om nie die battery se lewe te verkort nie?
- Werk uit die gelykbreek tydperk van die stelsel deur die kragbesparing met panele te bepaal
- Bepaal hoeveel krag is beskikbaar vanaf panele op 'n bewolkte dag


Die volgende plot funksies is beskikbaar:

- Plot drywing teen die tyd in die dag vir verskillende items
- Plot drywing vir verskillende dae in die jaar.

Data word met die Axpert gemeer per dag.  Die data word in 'n tekslêer gestoor wat ongeveer 1MB groot is vir elke dag.

Die data het partykeer foute in.  Daar is Linux opdragte wat voor die tyd op die data uitgevoer word om dit skoon te maak.

Die daaglikse data word dan ingelees in Python.

Dit word dan in 'n groter binêre databasis gestoor vir verder verwerking.