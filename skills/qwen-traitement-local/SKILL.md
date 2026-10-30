---
name: qwen-traitement-local
description: Confier un traitement de texte en masse au modèle local qwen (Ollama) pour économiser les tokens Claude. À utiliser pour résumer un long document, classer ou trier une liste, extraire des champs, traduire, reformuler ou faire un premier jet de messages répétitifs, au lieu de lire le contenu en entier dans le contexte.
---

# Traitement local avec qwen

Outil : `03_PROJETS_INTERNE/Outils/qwen.py` (modèle `qwen3.5:9b` par défaut, sans token Claude, autorisé sans confirmation).

```sh
python3 -I 03_PROJETS_INTERNE/Outils/qwen.py "consigne" fichier1 fichier2
cat liste.txt | python3 -I 03_PROJETS_INTERNE/Outils/qwen.py "consigne"
```

## Quand l'utiliser

- Résumer un long document, puis ne garder que le résumé.
- Classer ou trier une liste de prospects (ex. « pas de site / Linktree / site existant », réponse en CSV).
- Extraire des champs, traduire, reformuler, premier jet de messages répétitifs.

## Bonnes pratiques

- Consigne courte et précise, avec le **format de sortie** attendu (CSV, puces, JSON).
- Ne pas relire le fichier source dans le contexte : seul le résultat de qwen compte.
- Vérifier un échantillon du résultat. S'il est faible, monter d'**un seul** cran (Haiku), jamais directement à un modèle plus cher.
- Mémoire : qwen occupe environ 7,6 Go de RAM ; éviter de le lancer en même temps que toute la stack Docker sans surveiller.
- Ne jamais envoyer à qwen de document légal ou RH, ni de secret.
