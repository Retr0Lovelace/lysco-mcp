#!/usr/bin/env python3
"""Envoie une tâche de texte au modèle local qwen (Ollama) : zéro token Claude.

Usage :
  .claude/skills/qwen-traitement-local/qwen.py "consigne" [fichier ...]      # la consigne s'applique au contenu des fichiers
  cat notes.txt | .claude/skills/qwen-traitement-local/qwen.py "consigne"    # ou au texte reçu sur l'entrée standard

Exemples :
  .claude/skills/qwen-traitement-local/qwen.py "Résume en 5 puces" 05_DOCUMENTATION/compte-rendu.md
  .claude/skills/qwen-traitement-local/qwen.py "Classe chaque compte : pas de site / Linktree / site existant. Réponds en CSV" liens.txt
"""
import json
import os
import sys
import urllib.error
import urllib.request

MODEL = os.environ.get("QWEN_MODEL", "{{modele}}")
URL = os.environ.get("OLLAMA_URL", "{{url_ollama}}") + "/api/generate"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    instruction, files = sys.argv[1], sys.argv[2:]

    parts = []
    for path in files:
        with open(path, encoding="utf-8", errors="replace") as f:
            parts.append(f"--- {path} ---\n{f.read()}")
    if not files and not sys.stdin.isatty():
        parts.append(sys.stdin.read())

    prompt = instruction + ("\n\n" + "\n\n".join(parts) if parts else "")
    body = json.dumps({
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "think": False,  # pas de raisonnement : plus rapide pour des corvées
        "options": {"num_ctx": 16384, "temperature": 0.2},
    }).encode()

    req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            print(json.load(r)["response"].strip())
    except urllib.error.URLError as e:
        sys.exit(f"Ollama injoignable ({e}). Lance l'app Ollama ou `ollama serve`.")


if __name__ == "__main__":
    main()
