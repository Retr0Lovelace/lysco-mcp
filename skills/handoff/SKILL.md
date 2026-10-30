---
name: handoff
description: Passation de session LYSCO. À utiliser quand le fondateur arrête pour la journée (« on arrête », « pour ce soir », « handoff », « on reprend demain ») pour écrire une note de passation, et en début de session (« on reprend », « où on en était ») pour la relire et repartir sans tout réexpliquer.
---

# Handoff : clôturer ou reprendre une session LYSCO

Les notes vivent dans `05_DOCUMENTATION/Handoffs/`, une par session : `AAAA-MM-JJ-HHMM.md`.
Objectif : la session suivante repart en lisant **un seul fichier court**, sans relire tout le projet. Économie de tokens.

## Clôturer (fin de session)

1. Rassemble l'état **sans lire de gros fichiers** :
   - fils de questions : statut de chaque `hq/inbox/*.json` (champ `status`, titre, agent) ;
   - livrables : `ls` des dossiers d'étape de chaque projet client en cours, par exemple `02_CLIENTS/Lysco/` ;
   - serveurs : `lsof -iTCP:4317 -iTCP:4400 -sTCP:LISTEN`. Arrête ceux qu'on a lancés si le fondateur arrête pour la journée ;
   - décisions prises dans la session : déjà dans la conversation, ne relis pas les fichiers.
2. Écris `05_DOCUMENTATION/Handoffs/AAAA-MM-JJ-HHMM.md`, **une page maximum**, avec ces sections :
   - **Où on en est** : 3 lignes maximum, par projet ;
   - **Fait dans cette session** : puces courtes ;
   - **Décisions du fondateur** : à reporter aussi dans `CLAUDE.md` si elles sont durables ;
   - **En attente du fondateur** : fils ouverts du QG, actions manuelles (commandes `!`, comptes à créer…) ;
   - **Prochaine étape** : l'agent à lancer et son brief en une phrase ;
   - **Pour relancer** : commandes exactes (relais QG, site local…) ;
   - **Points d'attention** : risques, dette, éléments sensibles.
3. N'y mets **aucun secret** (token, mot de passe) ni aucune donnée personnelle du fondateur.
4. **Scan du dépôt avec graphify** (toujours, après avoir écrit la note, pour que le graphe reflète l'état final de la session) :
   - Invoque le skill `graphify` avec `. --update` (mise à jour incrémentale : seuls les fichiers nouveaux, modifiés ou supprimés depuis le dernier scan sont retraités). Si `graphify-out/graph.json` n'existe pas, lance le scan complet `.`.
   - Interpréteur : utilise celui de `graphify-out/.graphify_python` (Python 3.11 de Homebrew). Le `python3` du système (3.9) est trop ancien.
   - Même périmètre que le premier scan : exclus `assets/vendor/`, les images et `hq/inbox/` (filtre le résultat de la détection, comme au premier passage).
   - Si seuls des fichiers de code ont changé, l'extraction se fait sans modèle (gratuite). Pour des documents modifiés, extraction sémantique par des sous-agents `general-purpose` en `model: sonnet` (jamais Opus), regroupés par lots de 20 à 25 fichiers.
   - S'il n'y a aucun changement depuis le dernier scan, dis-le en une ligne et passe à l'étape suivante.
   - Le scan ne doit jamais bloquer la clôture : en cas d'erreur, note-la dans « Points d'attention » de la note de passation et continue.
   - `graphify-out/` est ignoré par git. Ne le commite pas.
5. Réponds au fondateur avec un résumé de 5 lignes maximum, le chemin de la note et une ligne sur le graphe (nombre de nœuds et de liens, fichiers retraités, ou « inchangé »).

## Reprendre (début de session)

1. Lis la note la plus récente de `05_DOCUMENTATION/Handoffs/` (tri par nom), et elle seule.
2. Vérifie en 1 commande les éléments qui ont pu bouger : statut des fils `hq/inbox`, serveurs actifs.
3. Si `graphify-out/graph.json` existe (mis à jour à la dernière clôture), il sert de carte du dépôt : pour une question sur le code ou la documentation, interroge-le avec `graphify query` avant de parcourir des fichiers.
4. Résume au fondateur en 5 lignes : où on en est, ce qui l'attend, la prochaine étape proposée. Attends son feu vert avant de lancer un agent.
