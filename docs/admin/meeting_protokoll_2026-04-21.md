# Meetingprotokoll

**Datum:** 21.04.2026  

## Teilnehmer

- Luc  
- Christopher  
- Martin  

## Besprechung

Der aktuelle Stand der Implementierung wurde präsentiert und gemeinsam diskutiert.  
Der Fokus lag auf der Vorstellung der bisherigen Ergebnisse im Bereich Solver-Modellierung sowie der Einordnung des aktuellen Gesamtansatzes.

## Fortschritt

- Durchführung von Test Runs zur Validierung des aktuellen Ansatzes  
  <https://github.com/FHNW-Security-Lab-Student-Projects/ip6-automatisierte-microsegmentierung/issues/25>  

- Erstellung und Dokumentation eines Solver-Modells  
  <https://github.com/FHNW-Security-Lab-Student-Projects/ip6-automatisierte-microsegmentierung/blob/main/docs/knowledge-base/ideas/solver_model.md>  

- Aktueller Stand der Segmentierungsansätze:
  - Constraint-basierte Segmentierung
    - Solver-basierter Ansatz (formal korrekt, optimierbar)
    - Heuristischer Ansatz (greedy)

- Struktur und Aufbau eines Digital Twins wurde definiert

## Aktueller Ansatz

Der derzeitige Systementwurf basiert auf zwei komplementären Paradigmen:

- Constraint-basierte Microsegmentierung mittels SMT (Solver)
- Kombination aus:
  - Graph Analytics
  - Constraint Solving

Ziel ist es, sowohl formale Korrektheit als auch praktische Skalierbarkeit und Interpretierbarkeit zu erreichen.

## Ideen & Weiteres Vorgehen

### Feature-Erweiterungen

- Einführung von Node-Gruppen
- Definition von Regeln auf Gruppenebene
- Erweiterung des Constraint-Modells:
  - Neben „Allow“ und „Deny“ auch Service-basierte Regeln
  - Ermöglichen spezifischer Kommunikation über VLAN-Grenzen hinweg

### Vergleich & Evaluation

Geplante Evaluationsdimensionen:

- Qualität der Segmentierung (z. B. Isolation)
  - Beispielvergleich:
    - Heuristik: 8 VLANs
    - Solver: 5 VLANs  

- Laufzeit und Skalierbarkeit:
  - Tests mit:
    - 10 Nodes  
    - 100 Nodes  
    - 1000 Nodes  

- Vollständige Erfüllung aller Constraints  
- Anzahl benötigter VLANs  

### Analyse & Erweiterte Methoden

- Analyse von UNSAT-Fällen zur Identifikation von Konflikten im Constraint-System
- Einsatz von Community Detection zur Generierung von Segment-Vorschlägen
- Integration von Graph-Metriken in die Segmentierungslogik:
  - Degree Centrality:
    - Identifikation zentraler Systeme
    - Vermeidung unnötiger Isolation kritischer Nodes
  - Betweenness Centrality:
    - Identifikation kritischer Kommunikationsknoten
    - gezielte Schutzmaßnahmen

## Nächste Schritte

- Implementierung zusätzlicher Features (Gruppen, Service-basierte Regeln)
- Durchführung systematischer Evaluationen (Heuristik vs. Solver)
- Skalierungstests mit größeren Netzwerken
- Analyse und Behandlung von UNSAT-Fällen
- Integration von Graph-Analytics-Methoden in den Segmentierungsansatz

## Offene Punkte

- Konkrete Definition und Modellierung von Service-basierten Constraints  
- Methodik zur Kombination von Graph Analytics und Constraint Solving  
- Bewertungskriterien für „optimale“ Segmentierung  
- Umgang mit Zielkonflikten (z. B. Sicherheit vs. Funktionalität)
