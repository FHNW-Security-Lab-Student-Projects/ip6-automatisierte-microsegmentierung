# Meetingprotokoll

**Datum:** 12.05.2026  

## Teilnehmer

- Luc  
- Christopher  
- Martin  

## Besprechung

Der aktuelle Fortschritt der Implementierung sowie erste Evaluationen wurden vorgestellt und diskutiert.  
Der Schwerpunkt lag auf der Analyse von UNSAT-Fällen, Performance-Messungen sowie der Weiterentwicklung der Netzwerkmodellierung und Gruppenlogik.

Zusätzlich wurden mögliche Optimierungen des Constraint-Modells sowie Visualisierungs- und Evaluationsideen für kommende Iterationen besprochen.

## Fortschritt

- Analyse und Behandlung von UNSAT-Fällen implementiert
- Durchführung von Tests mit Netzwerken unterschiedlicher Größe:
  - 60 Hosts
  - 80 Hosts
  - 100 Hosts

- Messung der Laufzeiten während der Solver-Ausführung
- Implementierung eines Network Builders
- Einführung und Umsetzung eines Gruppen-Features

## Aktueller Ansatz

Der aktuelle Segmentierungsansatz kombiniert weiterhin:

- Constraint-basierte Segmentierung mittels Solver
- Heuristische Segmentierung
- Netzwerkmodellierung über Graphstrukturen

Die Implementierung unterstützt inzwischen Gruppen-basierte Modellierungen und größere Netzwerkszenarien zur Evaluation von Skalierbarkeit und Laufzeitverhalten.

## Ideen & Weiteres Vorgehen

### Visualisierung von UNSAT-Fällen

Bei nicht lösbaren Netzwerkkonfigurationen könnte dennoch ein physischer Netzwerk-Graph erzeugt werden, um Konflikte visuell darzustellen.

Mögliche Erweiterungen:

- Markierung problematischer Nodes und Kommunikationspfade
- Hervorhebung von Konflikten mittels Farbcodierung (z. B. rot)
- Integration der Solver-/Terminal-Fehlermeldungen in die Visualisierung

Ziel ist eine bessere Nachvollziehbarkeit von Constraint-Konflikten und deren Ursachen.

### Erweiterte Performance-Analyse

Weitere Evaluationen wurden diskutiert:

- Untersuchung des Laufzeitverhaltens bei steigender Anzahl von Constraints
- Entwicklung eines Helpers zur automatischen Generierung von Netzwerken mit definierter Constraint-Anzahl
- Vergleich des Skalierungsverhaltens verschiedener Segmentierungsansätze

### Optimierung der Gruppenmodellierung

Ein möglicher Optimierungsansatz besteht darin, Gruppen im Constraint-System als einzelne abstrahierte Knoten zu behandeln.

Dadurch könnte vermieden werden, dass zwischen allen Gruppenmitgliedern vollständige Constraint-Graphen erzeugt werden.

Erwartete Vorteile:

- Reduktion der Constraint-Anzahl
- Verbesserte Skalierbarkeit
- Geringere Solver-Laufzeiten

### Erweiterung der Optimierungsziele

Diskutiert wurde eine zusätzliche Betriebsoption:

- „Erfülle alle Constraints und segmentiere maximal“

Ziel wäre eine möglichst restriktive Segmentierung unter vollständiger Einhaltung aller definierten Regeln.

### Edge-Case-Analysen

Zur Untersuchung möglicher Schwächen der Heuristik sollen spezielle Netzwerkstrukturen erzeugt werden:

- Kettenstrukturen
- Ringstrukturen

Dadurch könnten Szenarien identifiziert werden, die:

- vom Solver korrekt gelöst werden,
- vom heuristischen Ansatz jedoch nicht optimal behandelt werden.

## Nächste Schritte

- Erweiterung der Visualisierung für UNSAT-Fälle
- Entwicklung automatisierter Constraint-Generatoren für Performance-Tests
- Optimierung der Gruppenmodellierung im Constraint-System
- Durchführung weiterer Skalierungs- und Laufzeittests
- Analyse von Edge Cases mit speziellen Netzwerkstrukturen
- Vorbereitung des Midterm Meetings am 16.06.2026

## Midterm Meeting

Das Midterm Meeting findet am 16.06.2026 statt.  
Der genaue Zeitpunkt muss noch definiert werden, damit die Planung während des Militärdienstes berücksichtigt werden kann.

Geplante Inhalte des Meetings:

- Strukturierte Präsentation des aktuellen Projektstands
- Vorstellung der bisherigen Ergebnisse
- Diskussion erfolgreicher und problematischer Aspekte des Projekts
- Überblick über geplante nächste Entwicklungsschritte

## Offene Punkte

- Konkrete Umsetzung der Visualisierung von UNSAT-Konflikten
- Effiziente Modellierung von Gruppen im Constraint-System
- Definition geeigneter Metriken für maximale Segmentierung
- Vergleich der Skalierbarkeit zwischen Solver- und Heuristik-Ansatz
- Identifikation weiterer relevanter Edge Cases für die Evaluation