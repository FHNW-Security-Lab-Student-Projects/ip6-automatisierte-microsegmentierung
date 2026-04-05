# Modell des Netzwerks

- Segmente (implizit, nicht vorgegeben!)
- User / Clients
- Application Services
- Core Infrastructure
- Security / Management
- Data Layer

##  Rollen

- Identity (AD)
- DNS
- Fileservices
- Mail
- Monitoring
- Backup
- Security

## Kommunikationsmuster

- Users → viele Services
- Apps → DB
- Infra → alle
- zentrale Dienste (DNS, AD)

##  Erwartete Segmente

- User Cluster
- App Cluster
- DB Cluster
- Infra evtl. separat oder verteilt

```mermaid
---
config:
  layout: elk
---
flowchart LR
 subgraph U["User Segment"]
        U1["Clients"]
  end
 subgraph A["Application Segment"]
        A1["App Services"]
  end
 subgraph D["Database Segment"]
        D1["Databases"]
  end
 subgraph I["Core Infrastructure"]
        I1["Identity AD"]
        I2["DNS"]
        I3["Mail"]
        I4["File Services"]
  end
 subgraph M["Security & Management"]
        M1["Monitoring / Logging"]
        M2["Backup"]
  end
 subgraph V["Internet & External"]
        V1["Internet"]
        V2["VPN"]
  end
    U -- DNS (UDP 53) --> I
    U -- SMB (TCP 445) --> I
    U -- IMAP (TCP 993) --> I
    U -- WEB (TCP 443) --> A & V
    A -- SQL (TCP 5432) --> D
    A -- API (TCP 8080) --> A
    A -- DNS (UDP 53) --> I
    A -- LDAP (TCP 389) --> I
    M -- Management (DIV) --> U & A & D & I
    V2 -- Uplink --> V1

     U1:::user
     A1:::application
     D1:::database
     I1:::infra
     I2:::infra
     I3:::infra
     I4:::infra
     M1:::mgmt
     M2:::mgmt
     V1:::external
     V2:::external
    classDef user fill:lightblue,stroke:#333
    classDef application fill:lightgreen,stroke:#333
    classDef database fill:orange,stroke:#333
    classDef infra fill:violet,stroke:#333
    classDef mgmt fill:grey,stroke:#333
    classDef external fill:#FFCDD2,stroke:#333
```