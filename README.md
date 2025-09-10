# OkayGarmin

OkayGarmin est un assistant vocal en français qui permet d'exécuter des commandes vocales simples sur Windows. Inspiré par Garmin Connect.

## Fonctionnalités

- **Reconnaissance vocale** : Détection du mot "ok garmin" et traitement des commandes en français
- **Synthèse vocale** : Réponses audio en français
- **Commandes système** : Ouverture d'applications Windows
- **Informations temporelles** : Annonce de l'heure actuelle
- **Interface simple** : Fonctionnement en ligne de commande

## Commandes disponibles

| Commande  | Action |
|-----------|--------|
| `ok garmin ouvre notepad` | Ouvre le Bloc-notes |
| `ok garmin ouvre la calculatrice` | Ouvre la Calculatrice |
| `ok garmin quelle heure est-il` | Annonce l'heure actuelle |
| `ok garmin arrête-toi` | Ferme l'assistant |

## Prérequis

- Python 3.7 ou supérieur
- Windows
- Microphone fonctionnel

## Installation

1. Clonez ou téléchargez ce projet
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez l'assistant :
   ```bash
   python main.py
   ```

2. Attendez le message "Assistant vocal démarré. Parlez maintenant..."

3. Dites "ok garmin" suivi de votre commande

4. L'assistant émettra un bip sonore pour confirmer la détection du mot de réveil

5. Pour quitter, dites "ok garmin arrête-toi" ou utilisez Ctrl+C

## Structure du projet

```
OkayGarmin/
├── main.py              # Script principal
├── requirements.txt     # Dépendances Python
├── LICENSE             # Licence du projet
└── README.md           # Documentation
```

## Dépendances

- `speech_recognition` : Reconnaissance vocale
- `pyttsx3` : Synthèse vocale
- `sounddevice` : Capture audio
- `numpy` : Traitement des données audio

## Licence

Voir le fichier [LICENSE](LICENSE) pour plus de détails.