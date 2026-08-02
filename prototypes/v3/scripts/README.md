# Skripte

Dieses Verzeichnis enthält alle ausführbaren Skripte zur Durchführung der Experimente sowie zur automatischen Auswertung der Ergebnisse.

## Verzeichnisstruktur

```text
scripts/
├── plots/
│   ├── README.md
│   ├── run_plots.py
│   └── ...
├── run_experiments.py
└── run_pipeline.py
```

## Skripte

### run_pipeline.py

Führt die vollständige Segmentierungspipeline für ein einzelnes Netzwerk aus.

Der Ablauf umfasst:

- Laden und Erweitern der Constraints
- Aufbau des Digital Twin
- Ausführung der Heuristik
- Ausführung des Z3-Solvers
- Validierung der Ergebnisse
- Optionale Visualisierung
- Ausgabe aller relevanten Metriken

### run_experiments.py

Führt automatisiert alle Datensätze im Verzeichnis `experiments/` aus.

Dabei werden:

- alle Experimente nacheinander gestartet,
- Logdateien erzeugt,
- die gemessenen Metriken extrahiert,
- sowie die Ergebnisse in `experiments/results.csv` gespeichert.

Diese CSV-Datei bildet die Grundlage für sämtliche Diagramme der Evaluation.

### plots/

Enthält alle Skripte zur automatischen Erstellung der Diagramme für die Evaluation.

Die Diagramme werden auf Basis von `experiments/results.csv` erzeugt und im Unterverzeichnis `plots/output/` gespeichert.

Weitere Informationen befinden sich in der README des Unterverzeichnisses `plots/`.

## Typischer Ablauf

1. Experimente ausführen

```bash
python run_experiments.py
```

2. Diagramme erzeugen

```bash
python plots/run_plots.py
```

Nach Abschluss liegen sämtliche Messergebnisse in `experiments/results.csv` sowie alle erzeugten Diagramme im Verzeichnis `plots/output/` vor.
