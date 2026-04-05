# ⚠️ Frozen / Archived

# Microsegmentation Prototype

Dieses Verzeichnis enthält den **prototypischen Implementierungsteil** der Bachelorarbeit
**„Automatisierte Microsegmentierungsstrategie basierend auf Digital Twin Netzwerk-Mapping“**.

---

# Systemübersicht

Der Prototyp implementiert eine Verarbeitungspipeline zur Analyse von Netzwerkkommunikation.

```
Netzwerkkommunikationsdaten
            ↓
       Traffic Parsing
            ↓
   Normalisiertes Datenset
            ↓
  Digital Twin Netzwerkgraph
            ↓
      Graphanalyse
            ↓
   Community Detection
            ↓
Policy-Synthese (Microsegmentierung)
            ↓
   Generiertes Regelset
```

Die einzelnen Komponenten sind modular implementiert, sodass unterschiedliche Algorithmen und Methoden getestet werden können.

---

# Repository-Struktur

```
prototype/
│
├── datasets
│   ├── synthetic
│   └── real
│
├── experiments
│
├── scripts
│
└── src
    └── microseg
        ├── ingestion
        ├── graph
        ├── analysis
        ├── segmentation
        ├── policy
        └── visualization
```

Die wichtigsten Komponenten werden im Folgenden kurz beschrieben.

---

# src/microseg

Der Ordner `src/microseg` enthält die eigentliche Implementierung des Prototyps.

Die Architektur orientiert sich an der Analysepipeline des Systems.

## ingestion

Verarbeitung und Import von Netzwerkkommunikationsdaten.

Diese Komponente übernimmt das Einlesen verschiedener Datenquellen wie z.B.:

- CSV Datensätze
- JSON Datensätze
- (optional später) NetFlow oder Zeek Logs

Das Ergebnis ist ein **normalisiertes Kommunikationsdatenset**, das als Grundlage für den Aufbau des Graphmodells dient.

---

## graph

Implementierung des **Digital Twin Netzwerkmodells**.

Das Netzwerk wird als gerichteter Graph modelliert:

**Nodes**

repräsentieren Netzwerkelemente wie:

- Hosts
- virtuelle Maschinen
- Container
- Services

**Edges**

repräsentieren beobachtete Kommunikationsbeziehungen.

Kanten können zusätzliche Attribute enthalten wie:

- Protokoll
- Port
- Kommunikationsfrequenz
- Trafficvolumen

Die Graphstruktur wird mit **NetworkX** implementiert.

---

## analysis

Graphbasierte Analyse der Netzwerkstruktur.

Implementierte Analysemetriken:

- Degree (in/out)
- Weighted Degree (Verbindungsstärke)
- Betweenness Centrality
- Edge Weight Analyse inkl. Importance-Klassifikation (low / medium / high)
- Abhängigkeitsanalyse zwischen Systemen

Diese Metriken dienen dazu, wichtige Systeme und Kommunikationszentren im Netzwerk zu identifizieren.

---

## segmentation

Automatische Erkennung von **logischen Netzwerksegmenten**.

Hier werden Community-Detection-Algorithmen angewendet, um Gruppen von Hosts zu identifizieren, die stark miteinander kommunizieren.

Geplante Algorithmen:

- Louvain
- Leiden
- Label Propagation

Die resultierenden Communities bilden **Kandidaten für Microsegmentierungsgruppen**.

---

## policy

Generierung von Microsegmentierungsrichtlinien auf Basis der erkannten Kommunikationsbeziehungen und Segmentstrukturen.

Ziel ist die Ableitung eines minimalen Regelsets, das:

- notwendige Kommunikation erlaubt
- unnötige Kommunikation blockiert
- eine **Deny-by-Default Strategie** unterstützt

Beispiel:

```
ALLOW segment_web → segment_api port 443
ALLOW segment_api → segment_db port 5432
DENY ALL
```

---

## visualization

Einfache Visualisierung des Kommunikationsgraphen und der erkannten Segmente.

Die Visualisierung dient primär zur:

- Analyse der Netzwerkstruktur
- Darstellung der erkannten Communities
- Demonstration der Ergebnisse

Mögliche Technologien:

- NetworkX
- PyVis
- Graphviz

---

# datasets

Dieser Ordner enthält Datensätze zur Evaluation des Systems.

```
datasets/

synthetic/
    synthetisch generierte Testnetzwerke

real/
    reale oder realitätsnahe Netzwerkdaten
```

Synthetische Datensätze werden verwendet, um reproduzierbare Experimente durchführen zu können.

---

# experiments

Der Ordner enthält experimentelle Skripte zur Evaluation verschiedener Ansätze.

Beispiele:

```
experiment_graph_metrics.py
experiment_community_detection.py
experiment_policy_generation.py
```

Diese Skripte dienen insbesondere zur Generierung von Daten und Diagrammen für die Bachelorarbeit.

---

# scripts

Hilfsskripte zur Ausführung der Pipeline.

Beispiel:

```
source .venv/bin/activate
python3 scripts/run_pipeline.py
```

Dieses Skript führt die grundlegende Verarbeitungskette aus:

```
Dataset → Graph → Analyse → Segmentierung
```

---

# Status

Der Prototyp befindet sich in aktiver Entwicklung im Rahmen der Bachelorarbeit.

Geplante Implementierungsschritte:

1. Import von Netzwerkkommunikationsdaten
2. Aufbau des Digital Twin Graphmodells
3. Graphbasierte Kommunikationsanalyse
4. Community Detection zur Segmentierung
5. Generierung von Microsegmentierungsrichtlinien
6. Evaluation der generierten Policies
