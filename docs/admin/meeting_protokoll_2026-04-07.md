# Meetingprotokoll

**Datum:** 07.04.2026  

## Teilnehmer
- Luc  
- Christopher  
- Martin  

## Besprechung
Der aktuelle Fortschritt wurde gemeinsam besprochen und als insgesamt zufriedenstellend bewertet.

## Fortschritt
- Erste Variante der Heuristic Synthesis **ohne Z3 Solver** wurde implementiert und getestet
- Ergebnis: Funktionierender erster Ansatz als Grundlage für weitere Iterationen

## Neuer Ansatz
Als nächster Schritt soll eine Variante **mit Solver-Unterstützung (Z3)** umgesetzt werden.

- Feature Set für den neuen Ansatz wurde erarbeitet
- Dokumentation:  
  https://github.com/FHNW-Security-Lab-Student-Projects/ip6-automatisierte-microsegmentierung/blob/main/docs/knowledge-base/ideas/feature_set_definition_v2.md

## Weiterführende Ressourcen
Folgende Inhalte wurden als potenziell hilfreich identifiziert:

- Advanced Topics in Communication Networks (BGP Fokus)  
  https://adv-net.ethz.ch/transcripts/verification/

Ziel: Relevante Konzepte und Methoden extrahieren und ggf. in den eigenen Ansatz integrieren.

## Tools Evaluation
Luc hat eine Übersicht möglicher Tools zusammengestellt, die bis zum nächsten Meeting evaluiert werden sollen:

| Goal                          | Best Tool        |
|------------------------------|------------------|
| Flexible research modeling    | Z3               |
| Built-in synthesis            | CVC5             |
| Natural rule-based modeling   | Clingo (ASP)     |
| Scalable reachability analysis| Soufflé (Datalog)|
| Optimization-heavy problems   | OR-Tools         |
| Real network configs          | Batfish          |

## Nächste Schritte
- Implementierung eines Solver-basierten Ansatzes mit Z3
- Analyse und ggf. Integration von Erkenntnissen aus den BGP-Verifikationsmaterialien
- Evaluation der identifizierten Tools hinsichtlich Eignung für das Projekt

## Offene Punkte
- Entscheidung für finalen Toolstack
- Abgrenzung des Feature Sets für die nächste Iteration