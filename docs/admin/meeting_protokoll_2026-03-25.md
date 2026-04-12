# Meetingprotokoll

**Datum:** 25.03.2025  

## Teilnehmer
- Luc  
- Christopher  
- Martin  

## Besprechung
Aktueller Stand wurde mit Luc und Christopher besprochen.

## Fortschritt
Von Martin wurden die folgenden Issues mit einem 30-Node-Netzwerk umgesetzt und erfolgreich getestet:

- Create prototype project structure
- Define network communication dataset format
- Create synthetic network dataset
- Implement csv traffic loader
- Implement digital twin graph builder
- Implement basic graph visualisation
- Implement graph metrics analysis

## Neuer Ansatz
Es soll ein neuer Ansatz verfolgt werden:

- Start mit einem kleineren Netzwerk (~2–3 Switches und 8–10 User)
- Definition von „High-Level Constraints“ in einem geeigneten Datenformat

### Beispiel Constraints
- User 1 und User 7 sind am gleichen Switch 01
- User 8 ist am Switch 02
- Switch 01 und Switch 02 sind verbunden

### Kommunikationsregeln
- User 1 ↔ User 8: Kommunikation erlaubt
- User 8 ↔ User 7: Kommunikation erlaubt
- User 1 ↔ User 7: Kommunikation **nicht erlaubt**

Die Netzwerktopologie soll dabei berücksichtigt werden.

## Ziel
Das System soll selbst erkennen:

- Wo VLANs eingesetzt werden müssen
- Wo ggf. zusätzliche Netzwerkkomponenten benötigt werden

### Beispiel
- User 1 und User 8 müssen miteinander kommunizieren können
- → VLAN erforderlich
- → Alle Netzwerkgeräte zwischen den beiden Usern müssen dieses VLAN unterstützen

## Einschränkungen
- Redundanzen müssen bei der Problemlösung nicht berücksichtigt werden

## Offene Punkte
- Definition des minimalen Netzwerks zur Demonstration des Problems
- Erwartet wird keine vollständige Enterprise-Lösung, sondern ein Konzept
