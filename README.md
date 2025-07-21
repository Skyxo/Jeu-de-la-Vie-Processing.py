# Jeu-de-la-Vie ★ Processing.py

Un éditeur interactif du **Jeu de la Vie** (Conway) écrit en **Processing 3 – mode Python**.  
Il combine un moteur maison (algorithmes d’évolution, export, comptage) et une interface graphique temps-réel avec boutons, zoom, rotation, symétries et dépôt de figures pré-enregistrées.

[![Demo YouTube](https://img.youtube.com/vi/4Upv88OFJC8/0.jpg)](https://www.youtube.com/watch?v=4Upv88OFJC8)

---

## ✨ Fonctionnalités

* Interface glisser-déposer fluide pour placer des patterns  
* **Zoom / dézoom** dynamique et navigation dans le temps (⏮ / ⏭)  
* Transformation des figures : rotations ±90°, symétries X-Y  
* **Export** d’un état dans `export.txt` (tableau Python)  
* Compteur de cellules vivantes et affichage des coordonnées  
* Bibliothèque de patterns incluse (`data.py`)  
* Moteur d’évolution optimisé (deux algos au choix)

---

## 📦 Installation

| Pré-requis | Version conseillée |
| ---------- | ----------------- |
| **Processing 3.x** | ≥ 3.5.4 |
| **Python Mode**     | installé via le *Contribution Manager* |
| **ControlP5**       | idem (*Libraries → Install*) |
| **Java**            | JDK 8 ou 11 |

```bash
# 1. Cloner le dépôt
git clone https://github.com/Skyxo/Jeu-de-la-Vie-Processing.py.git
cd Jeu-de-la-Vie-Processing.py

# 2. Ouvrir Processing, passer en Python Mode
# 3. Ouvrir le fichier  jeu_de_la_vie.pyde  puis ► Run
