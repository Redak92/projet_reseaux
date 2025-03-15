# Projet de Communication Client-Serveur avec TCP/UDP et Streaming Vidéo

Ce projet est divisé en deux phases distinctes, chacune illustrant une méthode de communication entre un client et un serveur. La première phase utilise les protocoles TCP et UDP pour l'échange de messages textuels, tandis que la deuxième phase met en œuvre un système de streaming vidéo en utilisant UDP.

---

## Phase 1 : Communication TCP/UDP

### Description

La première phase du projet consiste en un serveur capable de gérer à la fois des connexions TCP et UDP. Les clients peuvent se connecter au serveur via l'un de ces protocoles pour envoyer des messages textuels. Le serveur répond aux clients TCP avec un accusé de réception, tandis que les messages UDP sont simplement affichés sur le serveur.

### Fichiers

- **`client_tcp.py`** : Client TCP qui se connecte au serveur et envoie des messages.
- **`client_udp.py`** : Client UDP qui envoie des messages au serveur.
- **`server.py`** : Serveur qui gère les connexions TCP et UDP.

### Exécution

1. **Lancer le serveur** :

   ```bash
   py server.py

   ```

   Le serveur écoutera sur les ports 8080 (TCP) et 8081 (UDP).

2. **Lancer le client TCP** :

   ```bash
   py client_tcp.py

   ```

Le client se connectera au serveur TCP et permettra d'envoyer des messages.

3. **Lancer le client UDP** :
   ```bash
   py client_udp.py
   ```
   Le client enverra des messages au serveur UDP.

## Phase 2 : Streaming Vidéo avec UDP

### Description

La deuxième phase du projet implémente un système de streaming vidéo en utilisant UDP. Le client capture des images à partir d'une webcam, les encode en JPEG, et les envoie au serveur par paquets. Le serveur reçoit ces paquets, les réassemble, et affiche les images.

### Fichiers

- **`client.py`** : Client qui capture les images de la webcam et les envoie au serveur.
- **`server.py`** : Serveur qui reçoit et affiche les images envoyées par le client.

### Exécution

1. **Lancer le serveur** :

   ```bash
   py server.py

   ```

   Le serveur écoutera sur le port 5000.

2. **Lancer le client** :

   ```bash
   py client.py

   ```

   Le client commencera à capturer les images de la webcam et à les envoyer au serveur.

## Dépendances

Assurez-vous d'avoir installé les dépendances nécessaires en exécutant cette commande à la racine du projet:

```bash
pip install -r requirements.txt
```

### Les dépendances

- numpy
- opencv-python
