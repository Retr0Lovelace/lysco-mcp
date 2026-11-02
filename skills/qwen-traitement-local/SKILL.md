---
name: qwen-traitement-local
description: Confier un traitement de texte en masse au modèle local qwen (Ollama) pour économiser les tokens Claude. À utiliser pour résumer un long document, classer ou trier une liste, extraire des champs, traduire, reformuler ou faire un premier jet de messages répétitifs, au lieu de lire le contenu en entier dans le contexte.
variables:
  modele: Modèle Ollama | qwen3.5:9b
  url_ollama: Adresse d'Ollama | http://localhost:11434
---

# Traitement local avec qwen

Outil fourni avec ce skill : `.claude/skills/qwen-traitement-local/qwen.py` (modèle `{{modele}}`, Ollama sur `{{url_ollama}}`, sans token Claude).

```sh
python3 -I .claude/skills/qwen-traitement-local/qwen.py "consigne" fichier1 fichier2
cat liste.txt | python3 -I .claude/skills/qwen-traitement-local/qwen.py "consigne"
```

## Quand l'utiliser

- Résumer un long document, puis ne garder que le résumé.
- Classer ou trier une liste de prospects (ex. « pas de site / Linktree / site existant », réponse en CSV).
- Extraire des champs, traduire, reformuler, premier jet de messages répétitifs.

## Bonnes pratiques

- Consigne courte et précise, avec le **format de sortie** attendu (CSV, puces, JSON).
- Ne pas relire le fichier source dans le contexte : seul le résultat de qwen compte.
- Vérifier un échantillon du résultat. S'il est faible, monter d'**un seul** cran (Haiku), jamais directement à un modèle plus cher.
- Surveiller la mémoire : un modèle de 9 milliards de paramètres occupe plusieurs Go de RAM.
- Ne jamais envoyer à qwen de document légal ou RH, ni de secret.
