# Experimente

Dieses Verzeichnis enthält alle Datensätze, Logdateien und Messergebnisse für die Evaluation der entwickelten Microsegmentierung.

## Struktur

```text
experiments/
├── star/
├── tree/
├── mesh/
├── logs/
└── results.csv
```

## Datensätze

Für die Evaluation wurden synthetische Netzwerke mit drei unterschiedlichen Topologien erzeugt:

- **Star** – ein zentraler Switch mit allen Hosts als Baseline.
- **Tree** – hierarchische Core-, Distribution- und Access-Switches als realistische Unternehmensstruktur.
- **Mesh** – vollständig vermaschtes Switch-Netzwerk mit hoher Pfadvielfalt.

Für jede Topologie existieren Datensätze mit den Netzwerkgrößen:

- 5
- 10
- 20
- 40
- 60
- 80
- 100
- 120 Hosts

Zusätzlich werden drei Constraint-Dichten verwendet:

- **Low** – wenige Kommunikationsregeln
- **Medium** – mittlere Anzahl Kommunikationsregeln
- **High** – hohe Anzahl Kommunikationsregeln

Alle Datensätze sind konsistent erzeugt und besitzen eine gültige (SAT) Segmentierung.

## Ergebnisse

Während der Experimente werden für jeden Datensatz:

- eine Logdatei im Verzeichnis `logs/`
- sowie alle relevanten Messwerte in `results.csv`

gespeichert. Diese Ergebnisse dienen als Grundlage für die Auswertung und die Erstellung der Diagramme.