# Track your Day
## Ausgangslage
Herrn Burgener ist aufgefallen, dass er extrem viel Zeit unterwegs oder beim Gamen verbringt. Er möchte deshalb eine Webapplikation entwickeln, die es im ermöglicht, alle seine Zeitdaten in Bezug auf das Gamen und die Reisezeiten zu tracken. 

## Projket-Idee
Die Webapplikation soll es dem Benutzer ermöglichen, seine Reise- und/oder Gamezeiten zu tracken. Bei den Reisezeiten, soll der Benutzer eine Auswahl haben, mit welchem Transportmittel er unterwegs war (zu Fuss/Auto/Zug/Flugzeug). Ebenso sollten die Daten zur Gamingzeit vom Benutzer getrackt werden können. Der Benutzer soll die Möglichkeit haben, verschiedene Spiele nach Belieben hinzuzufügen. Nachdem der Benutzer seine Reise- und/oder Gamezeiten eingeben hat, soll er eine visuelle Darstellung in Form eines Pie-Charts erhalten. 

## Anforderungen
Die Anwendung soll aus einer Startseite und 2 weiteren Seiten bestehen
Auf der Hauptseite soll zwischen der Unterseite "Track your Travels" und "Track your Gaming Time" unterschrieden werden (mittels 2 Cards oder der Auswahl auf der Navigationsleiste).
Sobald auf eine entsprechene Card gedrückt wird soll die Seite geöffnet werden. Auf der geöffneten Seite erscheint eine Übersicht der getrackten Daten (Tabelle und Pie-chart). Es besteht jeweils auch die Möglichkeiten per Click weitere Daten hinzuzüfen (add journey/add game)

## Installation
Um die Anwendung zu starten, müssen folgende Bedingungen erfüllt sein:
- Python 3.6
- Flask
- Jinja2
- Plotly

## Benutzung
Graphische Benutzeranleitung Webapplikation:

![Flowchart Overview](doku/Flowchart_Bedienung.png)

## Neue Reise hinzufügen
Beispiel Hinzufügen einer neuen Reise:

![UML add journey](doku/add_journey.png)

## Bedienung
Die Bedienung der Webapplikation ist sehr intuitiv. Befindet man sich auf der Startseite, kann man via Drücken auf die Cards (Track tavel oder Track gaming) zu den Subpages gelagen, oder man kann via Navigationsbar direkt zur gewünschten Seite navigieren.
![Startseite](doku/startseite.png)

### Track Travels
Möchte man nun die Reiszeit tracken, wählt man auf der Startseite (Track Travel aus) und gelangt somit auf diese Oberfläche (siehe Bild unten). Auf dieser Seite findet man auf einen Überblick alle eingegeben Reisedaten. Die Daten sind in tabellarischer sowie graphischer Form ersichtlich. Um eine neue Zeit hinzuzufügen, klickt man auf den Button (Add new Journey)
![Übersicht Tack Journey](doku/travel_overview.png)

Somit gelangt man auf diese Oberfläche (Bild unten), wo man sein Daten eingeben kann. Ist man mit den Daten zufrieden, können diese mit dem Button (Hinzufügen) hinzugefügt werden. Man gelangt anschliessend direkt wieder auf die Übersichtsseite.
![Add Journey](doku/add_new_journey.png) 

Übersichtsseite neu:
![Neue Übersicht](doku/new_overview_travel.png)

### Track Games
Möchte man die Gamingzeit tracken kann man zurück zur Startseite gehen. Dies gelingt am schnellsten mit einem Klick auf "Track your Day" in der Navigationsbar. Hier wählt man nun die Card "Track Gaming" aus. Von dort gelangt man nun auf die Übersicht der Games.
![Übersicht Games](doku/games_overview.png) 

Hier kann man sich einen Überblick verschaffen, welche Spiele wie lange gespielt wurden. Zudem gibt es zwei Schaltflächen (Add Gamingtime now und Manage Games). 
Wählt man nun "Manage Games" aus, können dort neue Spiele hinzugefügt werden (siehe Bild unten)
![Manage Games](doku/manage_games.png)

Hat man ein gewünschtes Spiel hinzugefügt, kann man sich wieder zurück zur Übersicht navigieren oder man kann über die Navigationsbar --> Gaming Dropdown --> Add Game Session direkt eine neue Spielzeit tracken. Dies sieht so aus:
![Track Gaming Time](doku/track_gaming.png)

Nach dem Hinzufügen des Spiels sowie der Spielzeit kann man sich nochmals die Übersicht anschauen.
![Game overview](doku/games_overview2.png)
