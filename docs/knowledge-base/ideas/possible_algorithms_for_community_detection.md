# Mögliche Ansätze für Community Detection

## Algorithmen

###  1. Louvain Algorithmus

<https://en.wikipedia.org/wiki/Louvain_method>

#### Grundidee

Der Louvain-Algorithmus maximiert die Modularity des Netzwerks.

####  Modularity

Maß dafür, wie stark ein Netzwerk in Communities aufgeteilt ist.

####  Ablauf

Der Algorithmus arbeitet iterativ in zwei Phasen:

1. Lokale Optimierung
    - Jeder Knoten startet als eigene Community.
    - Knoten werden zu Nachbar-Communities verschoben, wenn dadurch die Modularity steigt.

2. Community-Aggregation
    - Communities werden zu Superknoten zusammengefasst.
    - Der Prozess beginnt erneut auf dem reduzierten Netzwerk.

Dieser Prozess wiederholt sich, bis keine Modularity-Verbesserung mehr möglich ist.

#### Typische Anwendungen

- große Social Networks
- Webgraphen
- biologische Netzwerke
- Millionen Knoten möglich

####  Kurz

Sehr effizienter Standardalgorithmus für große Graphen.

### 2. Label Propagation

####  Grundidee

Communities entstehen durch Mehrheitsentscheidung der Nachbarn.

#### Ablauf

1. Jeder Knoten bekommt ein eigenes Label.
2. Iterativ:
    - Ein Knoten übernimmt das häufigste Label seiner Nachbarn.
3. Dieser Prozess läuft, bis sich Labels nicht mehr ändern.

####  Nachteile

- Ergebnis kann instabil sein
- unterschiedliche Runs → unterschiedliche Communities
- kann große Communities verschmelzen

####  Typische Anwendungen

- sehr große Graphen
- Streaming / dynamische Netzwerke
- schnelle Approximation

#### Kurz

Einfachster und schnellster Community-Algorithmus, aber weniger stabil.

### 3. Girvan–Newman

####  Grundidee

Communities werden gefunden, indem Brücken zwischen Gruppen entfernt werden.

Der Algorithmus nutzt Edge Betweenness Centrality.

#### Edge Betweenness

Wie viele kürzeste Pfade durch eine Kante laufen.

Kanten zwischen Communities haben oft hohe Betweenness.

#### Ablauf

1. Berechne Edge Betweenness für alle Kanten.
2. Entferne die Kante mit der höchsten Betweenness.
3. Berechne Betweenness erneut.
4. Wiederhole den Prozess.

Das Netzwerk zerfällt schrittweise in Communities.

####  Typische Anwendungen

- kleine Netzwerke
- Lehrzwecke
- Analyse sozialer Strukturen

####  Kurz

Sehr anschaulich, aber nicht skalierbar.

## Direktvergleich

| Eigenschaft               | Louvain                | Label Propagation | Girvan–Newman |
| ------------------------- | ---------------------- | ----------------- | ------------- |
| Methode                   | Modularity Optimierung | Label Diffusion   | Edge Removal  |
| Geschwindigkeit           | schnell                | extrem schnell    | sehr langsam  |
| Skalierbarkeit            | sehr gut               | sehr gut          | schlecht      |
| Stabilität                | gut                    | niedrig           | hoch          |
| Hierarchische Communities | ja                     | nein              | ja            |

---

| Algorithmus           | Eignung  | Begründung                      |
| --------------------- | -------- | ------------------------------- |
| **Louvain**           | sehr gut | stabile Communities, skalierbar |
| **Label Propagation** | mittel   | schnell, aber instabil          |
| **Girvan–Newman**     | schlecht | zu langsam für reale Netzwerke  |

---

**Louvain scheint die beste Wahl zu sein.**

Warum gut für Mikrosegmentierung:

- erkennt dichte Kommunikationscluster
- funktioniert gut mit gewichteten Kanten (Traffic-Volumen, Verbindungsanzahl)
- skaliert auf tausende oder Millionen Nodes
- erzeugt hierarchische Communities
  → ideal für Segment → Subsegment Struktur

Typisches Modell:

```bash
Node = Host / Container / VM / Service
Edge = Netzwerkkommunikation
Weight = Traffic oder Verbindungshäufigkeit
```

Beispiel:

```bash
DB Server  <--->  Backend Services
Backend    <--->  API Layer
API        <--->  Frontend
```

Louvain erkennt automatisch diese funktionalen Gruppen.

```bash
Traffic Logs
      ↓
Communication Graph
      ↓
Louvain / Leiden
      ↓
Segment Candidates
      ↓
Policy Engine
```

### Leiden Algorithmus

<https://en.wikipedia.org/wiki/Leiden_algorithm>

<https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.leiden.leiden_communities.html>

#### Grundidee

Der Leiden-Algorithmus ist eine Verbesserung des Louvain-Algorithmus zur Community Detection.
Er optimiert ebenfalls Modularity, stellt aber zusätzlich sicher, dass Communities intern zusammenhängend und gut verbunden sind.

Das löst ein Problem von Louvain: Dort können Communities entstehen, die intern schlecht verbunden oder sogar getrennt sind.

####  Ablauf

Der Algorithmus arbeitet in drei Phasen:

1. Local Moving
    - Knoten werden zu Nachbar-Communities verschoben, wenn dadurch die Qualitätsfunktion (z. B. Modularity) steigt.

2. Refinement Phase
    - Communities werden überprüft und ggf. in kleinere Subcommunities aufgeteilt, damit sie intern gut verbunden bleiben.

3. Aggregation
    - Communities werden zu Superknoten zusammengefasst und der Prozess wiederholt sich.

Studien zeigen, dass Leiden oft bessere Community-Strukturen und gleichzeitig kürzere Laufzeiten als Louvain liefert.

#### Vorteile

- Communities sind garantiert zusammenhängend
- bessere Modularity-Optimierung
- oft 2–20× schneller als Louvain auf großen Netzwerken
- funktioniert gut bei sehr großen Graphen

#### Nachteile

- etwas komplexer zu implementieren
- erzeugt harte Partitionen
  → ein Knoten kann nur zu einer Community gehören
- benötigt ggf. Resolution-Parameter (γ) zur Kontrolle der Granularität

#### Typische Anwendungen

- große Social-Network-Graphen
- Bioinformatik (z. B. Single-Cell-Clustering)
- Wissensgraphen
- Netzwerk-Traffic-Cluster
- Graph-Analytics Plattformen
