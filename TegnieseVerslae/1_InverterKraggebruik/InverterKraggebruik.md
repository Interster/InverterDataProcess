# Gelykrigter kraggebruik

Bereken inverter kraggebruik met battery data en die inverter logs.



Twee metodes sal gevolg word om gelykrigter kraggebruik te bereken.

1. Battery logs en gelykrigter logs van die warmwater ligte stelsel wat isoleerd is van die lynkrag.  'n Energiebalans sal gebruik word om die gelykrigter kraggebruik te bepaal.
2. Die gelykrigter met die yskasstelsel sal op sy eie op die voorafbetaalde kragmeter gesit word en die kraggebruik sal bepaal word.  Die krag gelewer aan die gebruikers sal uit die gelykrigter logs gekry word.  Die verskil tussen die twee syfers is die gelykrigter kraggebruik.



## Probleemstelling

Die gebruikershandleiding van die Axpert beweer dat die geen-las gebruik van die Axpert 5kVa model minder as 50W is.  Dit is gemeet met 'n Owl drywingsmeter en is bepaal om sowat 500W te  wees.

Dit blyk dat die Axpert 'n groot induktiewe las trek as hy nie 'n ordentlike las op het nie.  Die laaier blyk nie 'n pf-korreksie in te hê nie, met  die gevolg dat die meeste drywingsmeters 'n groot meetfout maak.

Na vermoede is die gestadigde meting van 'n voorafbetaalde meterstelsel baie meer akkuraat as 'n goedkoop drywingsmeter.

Die doel van hierdie ondersoek is om te bepaal wat die werklike energiekoste is van 'n Axpert 5kVa gelykrigter in normale gebruik.  Aan die een kant dui eenvoudige metings aan dat dit nie weglaatbaar is nie en aan die ander kant beweer die gebruikershandleiding dat die energieverbruik van die Axpert laag is.



## Metings

### Warmwater ligte stelsel meting



### Voorafbetaalde meter meting

#### Inleiding

Die volgende gesprek bespreek die eksperiment van die meting:

[21:02, 6/29/2020] Gideon: Die prepaid meters is meer akkuraat, maar nie met oombliklike drywingsverbruik nie, maar akkumulatiewe energieverbruik
[21:03, 6/29/2020] Gideon: Jy moet mbv jou prepaidmeter ‘n eksperiment oornag doen (minstens 8 ure of so)
[21:03, 6/29/2020] Gideon: En vgl met Axpert log
[21:03, 6/29/2020] Gideon: Dan doen jy aftreksom en bereken gem drywingverlies

Mmmm. Ek gaan hierdie naweek vereeniging toe. Ek dink dit is goeie geleentheid vir so 'n toets. Goeie idee. Ek sit dan alles af behalwe die Axpert op die yskaste.
In parallel gebruik ek die goedkoop drywingsmeter as ekstra toets.
[21:06, 6/29/2020] Gideon: Ok sy onakkuraatheid te bevestig ja
[21:06, 6/29/2020] Gideon: Om
Ok dit is dan die beste wat ons vir nou kan doen.
Dit sal dalk seker beter wees om vir die eksperiment die Axpert se panele af te dit en dit net op eskom krag te loop die hele naweek. Dan is die krag na batterye basies net "float". Stem jy saam
Dan is die verskil tussen wat die Axpert lewer aan die las en die kragmeter se syfer die Axpert se eie gebruik.
Ja jy sal sonpanele moet afhaal
Reg so.
Vir die eksperiment inverter
Ja die ander een se lynkrag gaan ek afsit. Die een met die ligte is buitendien van die grid af tegnies omdat ligte so min krag vat.

Belangrik vir ons meting is dat ons net regte drywing gaan meet met die prepaid. Blykbaar is die drywingsfaktor nie so groot faktor vir eskom nie. Dus vra hulle jou as huis nie geld vir die skynkrag wat jy gebruik nie. Vir komersiële gebruikers vra hulle geld vir die skynkrag sodat hulle forseer word om PF korreksies te doen.
So al is daar baie VAR in die stroombaan gaan ons nie kyk daarna nie want ons metertjies meet net regte drywing in kW.
Ek sê dit want ek gaan net die kW logs van Axpert gebruik.
Dis wat ek sê dis wat ek sê
OK dis mooi. Ek het nie geweet ons is so klein dat ons VAR verniet is nie.
So as die Owl metertjie sleg is gaan ons groot verskil tussen hom en die prepaid sien.
Dis die eerste afleiding wat ons wil maak: hoe sleg is die goedkoop metertjie.
Die tweede ding wat ons wil weet is wat is die delta tussen die kWh van die prepaid en die kWh regte drywing wat die Axpert aan sy netwerk lewer.
[23:13, 6/29/2020] Gideon: Dis die vermoede. Onthou dat skynkrag nie noodwendig drywing kos nie. Mens kan groot vAR’e opwek maar die turbines kom dit nie agter nie, maar dis onbruikbaar. Slegs die weerstand in die drade/klosse is die koste
[23:13, 6/29/2020] Gideon: Van die generator
Ek log elke 10 sekondes. So daar gaan 'n klein foutjie wees. Want ek gaan die 0.1Hz kW sein integreer om die energie te kry.
Skuus, VAr’e

[23:17, 6/29/2020] Gideon: Jou metertjie meet die skyndrywing, wat glad nie akkuraat is is die pf ver van 1 af is nie
[23:17, 6/29/2020] Gideon: *is as



#### Meterlesings


Begin Axpert meting 301.3 op 2020-07-03 15:00

Eindig Axpert meting 284.4 op 2020-07-05 18:54

![20200703_145918](Prente/20200703_145918.jpg)

Die DB het die volgende instellings gehad.  Net die Axpert het krag gekry met die muurproppe.  Alle ander toestelle is uitgeprop uit die muurproppe.  Net die yskaste en TV is ingeprop op die gelykrigter se proppe.

![20200703_145928](Prente/20200703_145928.jpg)



![20200705_185407](Prente/20200705_185407.jpg)



Die lesing op die OWL drywingsmeter was as volg:

![20200705_185726](Prente/20200705_185726.jpg)

Die voorafbetaalde meter het dus 16.9kWh gelees in 51.9 uur en die OWL drywingsmeter het 24.22kWh gelees in dieselfde tydperk.  Die voorafbetaalde meter word geneem as die maatstaf omdat die energie betaal word op die basis van hierdie meter se lesing.  Dus het die OWL drywingsmeter 7.32kWh te veel gelees oor die tydperk en dit werk uit op 'n gemiddeld  van 141W wat te veel gelees word op enige gegewe tyd.

Die lesingsfout wat die OWL maak kan toegeskryf word aan die feit dat die OWL net stroom gelewer meet en nie ook die spanning meet nie.  Dit kan dus nie onderskei tussen skyndrywing en ware drywing nie.  Die drywingsfaktor van die laste gekoppel tydens die eksperiment is laer as 0.8 omdat die laste meestal induktiewe laste is.  Die laste was oorwegend yskaste wat kompressormotors het wat 'n induktiewe las veroorsaak.  Die OWL meter lees dus die totale drywing wat 'n groot komponent skyndrywing bevat en dus oorskat die lesing die werklike drywing.  Die OWL vereis dat die gebruiker 'n spanning intik wat die gemiddeld is wat verwag word, naamlik 240V in hierdie spesifieke geval.  Dit lei tot die oorskatting.  Die OWL kan dus net vir vergelykende metings en AAN/AF tipe metings gebruik word, of in die onwaarskynlike geval dat daar 'n suiwer weerstandslas is.  Die mengsel van laste in 'n huis is meestal induktief van aard, dus is dit nie baie prakties vir die toepassing nie.

#### Axpert drywing leweringslesing

Hier is die logs van die Axpert oor die tydperk.