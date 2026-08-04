# Meetingprotokoll

**Datum:** 04.08.2026

## Teilnehmer

- Christopher
- Martin

## Besprechung

Im Meeting wurde der aktuelle Stand der Bachelorarbeit besprochen. Der Fokus lag auf der fachlichen Einordnung der implementierten Ansätze, der Aussagekraft der Evaluation sowie auf noch fehlenden Inhalten und formalen Bestandteilen der Arbeit.

## Besprochene Punkte

### Gruppenmodellierung

- Die aktuelle Gruppenmodellierung ist aufgrund der quadratischen Expansion der Gruppenbeziehungen nicht ausreichend effizient.
- Gruppen wurden deshalb in den Experimenten nicht verwendet.
- In der Arbeit soll klarer beschrieben werden, dass die aktuelle Implementierung bei grösseren Gruppen zu einer starken Zunahme der erzeugten Constraints führt und deshalb nur eingeschränkt skalierbar ist.

### Besonderheiten und Designentscheidungen

- Die wesentlichen Besonderheiten und Designentscheidungen der entwickelten Lösung sollen deutlicher beschrieben werden.
- Dabei sollen insbesondere getroffene Vereinfachungen, technische Abwägungen und deren Auswirkungen auf die Resultate erläutert werden.

### Heuristischer Ansatz

- Die Aussagekraft der Heuristik ist eingeschränkt, da sie zahlreiche Szenarien nicht erfolgreich lösen kann.
- Dieser Umstand soll in der Evaluation klar dargestellt und kritisch analysiert werden.
- Die Ergebnisse der Heuristik dürfen nicht isoliert anhand der Laufzeit beurteilt werden, sondern müssen gemeinsam mit der Erfolgsrate und der Gültigkeit der erzeugten Segmentierungen betrachtet werden.

### Z3-Solver

- Die Optimierung des Z3-Solvers zur Minimierung der verwendeten VLANs soll beschrieben und ausgewertet werden.
- Es soll erläutert werden, wie sich die Optimierung auf die Anzahl der VLANs und die Laufzeit des Solvers auswirkt.

### UNSAT-Fälle

- Nicht lösbare Szenarien mit dem Ergebnis **UNSAT** sollen genauer untersucht werden.
- In der Arbeit soll analysiert werden, welche Kombinationen aus Topologie und Kommunikationsanforderungen zu widersprüchlichen Constraints führen.
- Nach Möglichkeit sollen ausgewählte UNSAT-Fälle beispielhaft erklärt werden.

### Anhang

Für den Anhang beziehungsweise die ergänzenden Verzeichnisse sollen folgende Inhalte geprüft und aufgenommen werden:

- Hilfsmittelverzeichnis
  - Verwendung von ChatGPT
  - Verwendung des Overleaf AI Assistant
- Meetingprotokolle
- Planung und Projektvereinbarung
- Glossar
- Abkürzungsverzeichnis

### Organisatorisches

- Michael Faes ist als zuständige Ansprechperson für alle Module festgehalten.
- Alle offenen Verbesserungsvorschläge aus dem Kapitel **„Future Work“** wurden bereits als GitHub Issues erfasst.

## Termine

- **Abgabe der Bachelorarbeit:** 07.08.2026, 23:59 Uhr
- **Präsentation der Bachelorarbeit:** 01.09.2026, 09:00 Uhr

## Nächste Schritte

- Abschnitt zur Gruppenmodellierung überarbeiten und die eingeschränkte Skalierbarkeit der aktuellen Implementierung erläutern.
- Besonderheiten und zentrale Designentscheidungen der Lösung dokumentieren.
- Aussagekraft und Erfolgsrate der Heuristik kritisch analysieren.
- Optimierung des Z3-Solvers zur VLAN-Minimierung beschreiben und auswerten.
- Ausgewählte UNSAT-Fälle untersuchen und in der Arbeit erläutern.
- Hilfsmittelverzeichnis und weitere Bestandteile des Anhangs ergänzen.
- Bachelorarbeit bis spätestens 07.08.2026, 23:59 Uhr fertigstellen und abgeben.
- Präsentation für den 01.09.2026 um 09:00 Uhr vorbereiten.

## Offene Punkte

- Auswahl geeigneter UNSAT-Fälle für die detaillierte Analyse.
- Umfang der Beschreibung zur VLAN-Minimierung durch den Z3-Solver.
- Finale Zusammenstellung und Reihenfolge der Bestandteile des Anhangs.
- Klärung, ob Glossar und Abkürzungsverzeichnis beide benötigt werden.
