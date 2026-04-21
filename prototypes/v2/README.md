# Microsegmentation Prototype

Dieses Verzeichnis enthält den **prototypischen Implementierungsteil** der Bachelorarbeit
**„Automatisierte Microsegmentierungsstrategie basierend auf Digital Twin Netzwerk-Mapping“**.

---

# Quickstart

```bash
cd prototypes/v2
source .venv/bin/activate
python scripts/run_pipeline.py
```

---

# Systemübersicht

Der Prototyp implementiert eine Verarbeitungspipeline zur Analyse von Netzwerkkommunikation.

```
Constraints (High-Level)
        ↓
Constraint Model
        ↓
Topology (Digital Twin)
        ↓
Heuristic Synthesis
        ↓
Constraint Solver (Z3)
        ↓
Solution:
  - VLANs
  - Paths
  - Rule Set
```

Die einzelnen Komponenten sind modular implementiert, sodass unterschiedliche Ansätze
(heuristisch vs. solver-basiert) verglichen werden können.

---

# Repository-Struktur

```
prototypes/v2
│
├── datasets
│   └── scenarios
│
├── experiments
│
├── scripts
│
└── src
    └── microseg
        ├── constraints
        ├── topology
        ├── graph
        ├── synthesis
        ├── validation
        └── visualization
```

Die wichtigsten Komponenten werden im Folgenden kurz beschrieben.

---

## src/microseg

Der Ordner src/microseg enthält die Implementierung des Systems.

Die Architektur folgt einer Constraint → Graph → Synthesis Pipeline.

## constraints

Definition und Verarbeitung von High-Level Constraints (ALLOW, DENY, Topologie).

## topology

Abbildung des Netzwerks als Digital Twin (Hosts, Switches, Verbindungen).

## graph

Graphbasierte Funktionen wie Pfadberechnung und Reachability.

## synthesis

Erzeugung der Segmentierung:

heuristische Initiallösung
solver-basierte Optimierung (Z3)
validation

Überprüfung der Constraint-Erfüllung und Konsistenz der Lösung.

## visualization

Einfache Darstellung der Topologie und Segmentierung.

## Status

Der Prototyp befindet sich in aktiver Entwicklung im Rahmen der Bachelorarbeit.

Geplante Implementierungsschritte:

1. Constraint-Modell und Szenarien definieren
2. Digital Twin Topologie implementieren
3. Graph & Pfadanalyse entwickeln
4. Heuristische Segmentierungslogik implementieren
5. Integration eines Constraint Solvers (Z3)
6. Validierung und Vergleich der Ansätze
7. Experimente und Evaluation