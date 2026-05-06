# Constraint Solver Modell (Z3) – Microsegmentation v2

## Ziel

Dieses Dokument beschreibt das formale Modell zur automatisierten Microsegmentierung
mittels Constraint Solving (Z3).

Gegeben:

- Netzwerktopologie (Graph)
- High-Level Constraints (ALLOW, DENY)

Gesucht:

- VLAN-Zuweisung für alle Nodes

So dass:

- alle ALLOW-Constraints erfüllt sind
- alle DENY-Constraints eingehalten werden
- die Topologie korrekt berücksichtigt wird

# 1. Grundidee

Das Netzwerk wird als Graph modelliert:

- Nodes: Hosts, Switches
- Edges: physische Verbindungen

Die Segmentierung erfolgt über VLANs.

# 2. Variablen

Für jeden Node `n` und jedes VLAN `v`:

$$
V(n, v) \in \{0,1\}
$$

**Bedeutung:**

$$
V(n, v) = 1 \;\Leftrightarrow\; n \text{ gehört zu VLAN } v
$$

**Erklärung:**

Diese boolesche Entscheidungsvariable modelliert die VLAN-Zugehörigkeit eines Nodes.
Der Wertebereich ${0,1}$ stellt sicher, dass ein Node entweder Mitglied eines VLANs ist (1) oder nicht (0).
Damit wird das Problem in eine klassische SAT/SMT-Struktur überführt.

## 2.1 Gruppen (High-Level Abstraktion)

In realen Netzwerken werden Systeme häufig nicht einzeln, sondern in logischen Gruppen organisiert (z. B. _ICT_, _Office_, _Servers_).

Eine Gruppe wird definiert als:

$$
G = \{ n_1, n_2, \dots, n_k \}
$$

wobei jedes Element $ \ n_1\ $ ein Node im Netzwerk ist.

### Semantik von Gruppen

Gruppen haben im Modell folgende Bedeutung:

#### 1. Implizite Kommunikation innerhalb der Gruppe

Alle Nodes einer Gruppe dürfen miteinander kommunizieren:

$$
\forall a,b \in G,\; a \neq b:\quad ALLOW(a,b)
$$

Dies entspricht einem vollständig verbundenen Subgraphen (Clique).

#### 2. Verwendung in Constraints

Gruppen können in High-Level Constraints verwendet werden:

ALLOW ICT -> Office  
DENY Office -> Printer

Diese werden definiert als:

$$
ALLOW(G_1, G_2) \equiv \forall a \in G_1, \forall b \in G_2:\; ALLOW(a,b)
$$

$$
DENY(G_1, G_2) \equiv \forall a \in G_1, \forall b \in G_2:\; DENY(a,b)
$$

# 3. Host Constraint

Hosts dürfen genau ein VLAN haben:

$$
\forall h \in \text{Hosts}:\quad \sum_{v} V(h, v) = 1
$$

**Begründung:**

Hosts sind Endsysteme und können in der Regel nur einem Layer-2 Broadcast-Domain (VLAN) zugeordnet werden.
Die Summenbedingung erzwingt eine exklusive Zuordnung (Exactly-One) und verhindert:

- Mehrfachzuweisung (Sicherheitsproblem)
- fehlende Zuweisung (Undefinierter Zustand)

# 4. Switch Constraint

Switches dürfen mehrere VLANs haben:

$$
\forall s \in \text{Switches}:\quad \sum_{v} V(s, v) \geq 1
$$

**Begründung:**

Switches fungieren als Transportknoten und müssen mindestens ein VLAN tragen, um überhaupt Teil der Segmentierungsstruktur zu sein.
Die Ungleichung erlaubt gleichzeitig:

- Trunking (mehrere VLANs pro Switch)
- flexible Weiterleitung über mehrere Segmente

# 5. Topologie Constraint

VLANs müssen entlang eines Pfades existieren:

$$
\forall v,\; \forall n \in P:\quad V(n, v) = 1
$$

**Erklärung:**

Diese Bedingung stellt sicher, dass ein VLAN entlang eines gesamten Pfades konsistent existiert.
Ein Kommunikationspfad ist nur dann realisierbar, wenn alle beteiligten Knoten das VLAN führen.

Ohne diese Einschränkung könnte der Solver Lösungen erzeugen, die logisch korrekt wirken, aber physisch nicht routbar sind.

# 6. ALLOW Constraint

$$
\exists v:\;
\Big(
V(A, v) = 1 \;\wedge\; V(B, v) = 1 \;\wedge\;
\forall n \in \text{path}(A,B): V(n, v) = 1
\Big)
$$

**Erklärung:**

Ein ALLOW-Constraint verlangt, dass es mindestens ein gemeinsames VLAN gibt, über das zwei Nodes kommunizieren können.

Die drei Teile bedeuten:

1. Beide Endpunkte sind im selben VLAN
2. Es existiert ein durchgängiger Pfad
3. Alle Zwischenknoten tragen dieses VLAN

Damit wird Konnektivität als Existenz eines konsistenten VLAN-Pfades modelliert.

# 7. DENY Constraint

$$
\forall v:\;
\neg \Big(
V(A, v) = 1 \;\wedge\; V(B, v) = 1 \;\wedge\;
\forall n \in \text{path}(A,B): V(n, v) = 1
\Big)
$$

**Begründung:**

Hier wird das Gegenteil erzwungen:
Es darf kein VLAN existieren, das eine vollständige Verbindung zwischen den beiden Nodes ermöglicht.

Das ist stärker als nur „nicht gleiches VLAN“, weil:

1. auch indirekte Pfade ausgeschlossen werden
2. sämtliche möglichen VLANs berücksichtigt werden

Damit wird echte Netzwerkisolation garantiert.

# 8. VLAN Domain

$$
\text{VLANs} = \{10, 20, 30, \dots, K\}
$$

**Erklärung:**

Diese Menge definiert den Suchraum des Solvers.
Nur VLAN-IDs innerhalb dieser Domain dürfen verwendet werden.

Die Wahl von $K$ beeinflusst direkt:

Komplexität des Problems
Flexibilität der Segmentierung
Anzahl möglicher Lösungen

# 9. Encoding Strategy

- Bool V(node, vlan)
- ExactlyOne für Hosts
- Or/And für ALLOW
- Not für DENY

# 10. Mapping Python → Z3

```python
segmentation.node_to_vlans[node] = {10, 20}

V(node, 10) = True
V(node, 20) = True
```

# 11. Erweiterung: Optimierung

$$
\min \sum_{v} \mathrm{used}(v)
$$

Dabei ist $\mathrm{used}(v)$ eine Hilfsvariable, die angibt, ob ein VLAN $v$ von mindestens einem Node verwendet wird.

**Begründung:**

Neben der reinen Erfüllbarkeit wird hier ein Optimierungsziel eingeführt:
Die Anzahl der verwendeten VLANs soll minimiert werden.

Das führt zu:

einfacheren Konfigurationen
geringerer administrativer Komplexität
effizienterer Nutzung der VLAN-ID-Ressourcen

# 12. Zusammenfassung

- Boolesche Variablen pro (Node, VLAN)
- Constraints für ALLOW, DENY, Topologie
- direkt in Z3 umsetzbar
