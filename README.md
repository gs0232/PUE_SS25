# PUE_SS25

Hier werden die Sakai-Aufgaben für Programmierübung 2 erstellt.

# Funktionsumfang

Hier liegt ein Skript 'main.py', mit dem wir eine Leistungskurve plotten.

# Anforderungen

- Zum Installieren wird das Projekt gecloned
- Im Terminal werden folgende Befehle in die Powershell geschrieben
    - 'pdm install'
- Zum Starten des Projektes wird ein 'activity.csv' benötigt, welches dann in 'power_curve.py' zu einem Plot gemacht wird

# Sakai Aufgabe 1 - Power Curve Plot
![](figures/power_curve.png)

# EKG-App

## Funktionsbeschreibung

Die app soll es der __Diagnostiker:in__ ermöglichen, EKG-Daten verschiedener __Patient:innen__ zu erfassen, zu speichern und auszuwerten. Die App soll eine einfache und intuitive Benutzeroberfläche bieten, um die Bedienung zu erleichtern. Der __Admin__ kann __Diagnostiker:innen__ anlegen.

![](docs/UML_UseCase.png)

### Use Cases

- UC1: EKG-Daten auswerten
    - bla
- UC2: Daten verwalten

## Implementierung

__Use Case 1__ Die User Journey für die Diagnostiker:in wenn Sie einen Test auswerten möchten, folgt aus dem Activity Diagramm:

![](docs/ekg_data_acticity.svg)

### Design

Hier folgen erste Entwürfe eines UI Designs. Das Design ist für die Darstellung auf einem PC optimiert (Querformat). Keine separaten Frames.


## Bneutzung

` .\.venv\Scripts\activate`
`streamlit run .\main.py`