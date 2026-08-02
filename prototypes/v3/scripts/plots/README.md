# Diagramme der Evaluation

Dieses Verzeichnis enthält alle Skripte zur automatischen Erstellung der Diagramme für die Evaluation der Bachelorarbeit. Grundlage aller Auswertungen ist die Datei `experiments/results.csv`, welche durch `run_experiments.py` erzeugt wird.

Die Diagramme dienen dazu, die beiden Segmentierungsverfahren

- Heuristischer Ansatz
- SMT-Solver (Z3)

hinsichtlich **Laufzeit**, **Skalierbarkeit**, **Lösungsqualität** und **Robustheit** miteinander zu vergleichen.

Alle Diagramme werden automatisch durch `run_plots.py` erzeugt und im Verzeichnis `output/` gespeichert.

---

# Verzeichnisstruktur

```text
plots/
│
├── run_plots.py          # Einstiegspunkt zum Erzeugen aller Diagramme
├── style.py              # Gemeinsame Farben, Layout und Formatierung
│
├── runtime.py            # Laufzeitvergleich
├── vlans.py              # Vergleich der Segmentierungsqualität
├── success.py            # Robustheit der Verfahren
├── constraints.py        # Laufzeit in Abhängigkeit der Constraint-Anzahl
│
└── output/               # Generierte Diagramme
```

---

# Gestaltungsprinzipien

Alle Diagramme verwenden bewusst dieselbe visuelle Sprache, um Vergleiche zwischen den Abbildungen zu erleichtern.

## Farben

Die Farben repräsentieren die Constraint-Dichte.

| Farbe     | Bedeutung |
| --------- | --------- |
| 🟢 Grün   | Low       |
| 🟠 Orange | Medium    |
| 🔴 Rot    | High      |

## Linienstile

Die Linienstile unterscheiden die beiden Segmentierungsverfahren.

| Stil         | Verfahren |
| ------------ | --------- |
| Durchgezogen | Heuristik |
| Gestrichelt  | Z3 Solver |

## Diagrammaufbau

Sämtliche Diagramme bestehen aus drei synchronisierten Teilgrafiken.

- Star
- Tree
- Mesh

Dadurch lassen sich Unterschiede zwischen den Topologien direkt vergleichen.

---

# Diagramme

## runtime.py

**Ziel**

Vergleicht die Laufzeiten beider Verfahren in Abhängigkeit von der Netzwerkgröße.

**Achsen**

- X: Anzahl Netzwerkknoten
- Y: Laufzeit in Sekunden (logarithmische Skala)

**Erkenntnisse**

Das Diagramm beantwortet unter anderem folgende Fragestellungen:

- Wie skaliert die Laufzeit mit zunehmender Netzwerkgröße?
- Welchen Einfluss besitzt die Constraint-Dichte?
- Wie unterscheiden sich Heuristik und SMT-Solver hinsichtlich ihrer Skalierbarkeit?

Ausgabedatei:

```text
01_runtime_comparison.png
```

---

## vlans.py

**Ziel**

Vergleicht die Qualität der erzeugten Segmentierung anhand der Anzahl verwendeter VLANs.

**Achsen**

- X: Anzahl Netzwerkknoten
- Y: Anzahl verwendeter VLANs

Die Heuristik wird als gefüllter Marker dargestellt, während der SMT-Solver als ungefüllter Marker dargestellt wird.

**Erkenntnisse**

Das Diagramm zeigt,

- ob beide Verfahren vergleichbare Segmentierungen erzeugen,
- ob der Solver zusätzliche VLANs benötigt,
- wie sich die Segmentierungsqualität mit wachsender Netzwerkgröße verändert.

Ausgabedatei:

```text
02_vlan_usage.png
```

---

## success.py

**Ziel**

Vergleicht die Robustheit beider Verfahren.

Dargestellt wird der prozentuale Anteil erfolgreicher Segmentierungen für jede Constraint-Dichte.

**Achsen**

- X: Constraint-Dichte
- Y: Erfolgreiche Segmentierungen [%]

Die Farben repräsentieren die Constraint-Dichte, während schraffierte Balken den SMT-Solver kennzeichnen.

**Erkenntnisse**

Das Diagramm beantwortet unter anderem folgende Fragen:

- Bei welcher Constraint-Dichte scheitert die Heuristik?
- Löst der SMT-Solver sämtliche SAT-Instanzen?
- Welchen Einfluss besitzen Topologie und Problemkomplexität auf die Erfolgsrate?

Ausgabedatei:

```text
03_solver_robustness.png
```

---

## constraints.py

**Ziel**

Analysiert den Einfluss der Anzahl Constraints auf die Laufzeit.

**Achsen**

- X: Anzahl Constraints
- Y: Laufzeit in Sekunden (logarithmische Skala)

**Erkenntnisse**

Das Diagramm zeigt,

- ob die Laufzeit primär von der Netzwerkgröße oder von der Anzahl Constraints beeinflusst wird,
- wie empfindlich beide Verfahren auf steigende Problemkomplexität reagieren,
- ob sich Unterschiede zwischen den Topologien erkennen lassen.

Ausgabedatei:

```text
04_runtime_constraints.png
```

---

# Ausführung

Alle Diagramme können mit folgendem Befehl automatisch erzeugt werden:

```bash
python run_plots.py
```

Die erzeugten Diagramme werden automatisch im Verzeichnis

```text
plots/output/
```

gespeichert.

---
