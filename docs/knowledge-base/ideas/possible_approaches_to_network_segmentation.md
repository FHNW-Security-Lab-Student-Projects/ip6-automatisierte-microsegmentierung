# Mögliche Ansätze zur Netzwerksegmentierung

## 1. Rule Mining aus Traffic

Analyse von Netzwerkverkehr.

###  Methoden

- frequent communication
- dependency discovery

### Output

Host A -> Host B (Port 443)

###  Problem

- keine strukturelle Sicht
- schlecht für komplexe Netze

## 2. ML / Clustering Ansatz

Hosts werden gruppiert anhand:

- Traffic Pattern
- Role similarity
- Behavior

###  Methoden

- k-means
- hierarchical clustering
- DBSCAN

### Problem

- schwer erklärbar
- Admins vertrauen dem oft nicht

##  3. Policy Mining

Aus bestehenden Firewall Regeln.

###  Problem

- bestehende Regeln sind oft schlecht
- reproduziert Fehler

## 4. Graph-basierter Ansatz

Hier wird das Netzwerk als Graph modelliert.

###  Nodes

- Hosts
- VMs
- Containers
- Services

###  Edges

- Communication
- Dependencies
- Protocol
- Ports

###  Beispiel

- WebServer → AppServer → Database

Dann kann man Graph-Algorithmen verwenden:

- Community Detection
- Centrality
- Path Analysis
- Dependency Chains
