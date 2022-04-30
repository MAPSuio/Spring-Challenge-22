# Vaksiner i ballene 2
Basert på en historie fra en tidligere [fredagsprat](https://www.instagram.com/tv/CV5VD_SjItl/) (spol til 1:06).

<br>

<img src="img/generations.png" align="right" width="350px" style="margin: 10px;">

Noen år har gått, og enkelte vaksineskeptikere hadde dessverre rett: Man er ikke lenger fullvaksinert med mindre man har fått `d` doser! Derimot er det ikke sikkert at du må belage deg på såpass, da noen av forfedrene dine (heldigvis) fikk vaksinen i ballene. Før i tiden trodde man at barna ble fullvaksinerte om man utførte dåden innen 6 måneder, men nyere forskning har vist en annen effekt: _Alle_ barn trenger én færre dose enn faren!

Gitt en beskrivelse av familietreet ditt, og hvorvidt dine forfedre fikk vaksina i høyre arm, venstre arm, eller, vel, ballene, hvor mange doser trenger du før du er fullvaksinert og igjen kan nyte utepils uten munnbind?

### Input
Input består av to heltall `n` og `d` separert med linjeskift, hvor `n` er antall personer og `d` er antall doser man trenger. Deretter følger `n` linjer, som består av to strenger `a` og `b`: et navn og hvor de fikk vaksinen satt. Deretter kommer en tom linje, etterfulgt av linjer frem til EOF, som alle beskriver en far-sønn relasjon på formatet `far` `sønn`. Det er garantert at "Deg" vil forekomme her et sted.

### Output
Hvor mange doser du trenger å ta før du er fullvaksinert.

### Sample input
```
5
3
Tord venstre
Evan høyre
Finn ballene
Sarek ballene
Deg venstre

Evan Tord
Finn Evan
Sarek Deg
Tord Sarek
```

### Sample output
```
1
```
