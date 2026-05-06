# Network Builder

Ein leichtgewichtiges Web-Tool zum Erstellen, Bearbeiten und Exportieren von Netzwerk-Topologien und Zugriffsregeln.

Die Anwendung basiert auf:

- Python
- Flask
- HTML
- CSS
- Vanilla JavaScript

Es werden bewusst keine komplexen Frontend-Frameworks oder Datenbanken verwendet.



# Funktionen

## Nodes erstellen

Hosts oder Endgeräte können erstellt werden.

Beispiel:

```json
"nodes": [
    "User1",
    "User2",
    "Printer1"
]
```



## Switches erstellen

Netzwerk-Switches können erstellt werden.

Beispiel:

```json
"switches": [
    "Switch1",
    "Switch2"
]
```



## Switches verbinden

Switches können untereinander verbunden werden.

Beispiel:

```json
{
    "type": "CONNECTED",
    "node_a": "Switch1",
    "node_b": "Switch2"
}
```



## Gruppen erstellen

Nodes können Gruppen zugeordnet werden.

Beispiel:

```json
"groups": [
    {
        "name": "ICT",
        "members": ["User1", "User2"]
    }
]
```



## Zugriffsregeln definieren

Unterstützte Regeln:

- `ALLOW`
- `DENY`

Beispiele:

```json
{
    "type": "ALLOW",
    "src": "User1",
    "dst": "Printer1"
}
```

```json
{
    "type": "DENY",
    "src": "ICT",
    "dst": "Office"
}
```



## Node-zu-Switch Verbindungen

Nodes können physisch einem Switch zugeordnet werden.

Beispiel:

```json
{
    "type": "LOCATED_AT",
    "node": "User1",
    "switch": "Switch1"
}
```



# JSON Vorschau

Die Anwendung zeigt jederzeit eine Live-Vorschau des erzeugten JSONs auf der rechten Seite der Oberfläche.



# JSON kopieren

Die aktuelle Konfiguration kann direkt über den Button:

```text
Copy JSON
```

in die Zwischenablage kopiert werden.



# JSON herunterladen

Die aktuelle Konfiguration kann als Datei exportiert werden.

Dateiformat:

```text
network.json
```



# JSON importieren

Bereits exportierte Konfigurationen können wieder geladen werden.

Dadurch können bestehende Netzwerke:

- bearbeitet
- erweitert
- erneut exportiert

werden.



# Löschen von Objekten

Folgende Elemente können gelöscht werden:

- Nodes
- Switches
- Gruppen
- Regeln
- Switch-Verbindungen
- Node-zu-Switch Zuordnungen

Abhängige Referenzen werden automatisch entfernt.



# Duplikat-Schutz

Die Anwendung verhindert doppelte:

- Nodes
- Switches
- Gruppen
- Switch-Verbindungen



# Benutzeroberfläche

Die Oberfläche bietet:

- modernes helles Design
- responsives Layout
- Sticky JSON-Vorschau
- Live-Updates
- Formulare mit ENTER-Unterstützung



# Projektstruktur

```text
project/
├── app.py
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        ├── app.js
        ├── attachments.js
        ├── export.js
        ├── groups.js
        ├── nodes.js
        ├── render.js
        ├── rules.js
        ├── state.js
        └── switches.js
```



# Installation

## Voraussetzungen

Benötigt wird:

- Python 3.10 oder neuer



## Flask installieren

```bash
pip install flask
```



# Anwendung starten

Im Projektordner ausführen:

```bash
python app.py
```

Danach im Browser öffnen:

```text
http://127.0.0.1:5000
```



# Wichtiger Hinweis

Die Anwendung prüft aktuell NICHT:

- Syntaxfehler
- semantische Korrektheit
- Konflikte zwischen Regeln
- technische Validität
- logische Konsistenz
- Erreichbarkeit im Netzwerk

Die erzeugte Konfiguration muss vor produktiver Nutzung manuell überprüft werden.



# Technologien

Verwendete Technologien:

- Flask
- HTML5
- CSS3
- Vanilla JavaScript
- ES Modules

Keine Datenbank.
Keine Build-Tools.
Keine Frontend-Frameworks.
Keine externen UI-Bibliotheken.
