---
name: handoff
description: Passation de session. À utiliser quand le fondateur arrête pour la journée (« on arrête », « pour ce soir », « handoff », « on reprend demain ») pour écrire une note de passation, et en début de session (« on reprend », « où on en était ») pour la relire et repartir sans tout réexpliquer.
variables:
  entreprise: Nom de l'entreprise | @entreprise
  dossier_notes: Dossier des notes de passation | 05_DOCUMENTATION/Handoffs | dossier
  dossier_clients: Dossier des projets clients | 02_CLIENTS | dossier
---

# Handoff : clôturer ou reprendre une session de {{entreprise}}

Les notes vivent dans `{{dossier_notes}}/`, une par session : `AAAA-MM-JJ-HHMM.md`.
Objectif : la session suivante repart en lisant **un seul fichier court**, sans relire tout le projet. Économie de tokens.

## Clôturer (fin de session)

1. Rassemble l'état **sans lire de gros fichiers** :
   - fils de questions : statut de chaque `hq/inbox/*.json` (champ `status`, titre, agent) ;
   - missions du QG en cours ou en attente (page Missions) ;
   - livrables : `ls` des dossiers d'étape de chaque projet en cours dans `{{dossier_clients}}/` ;
   - décisions prises dans la session : déjà dans la conversation, ne relis pas les fichiers.
2. Écris `{{dossier_notes}}/AAAA-MM-JJ-HHMM.md`, **une page maximum**, avec ces sections :
   - **Où on en est** : 3 lignes maximum, par projet ;
   - **Fait dans cette session** : puces courtes ;
   - **Décisions du fondateur** : à reporter aussi dans `ENTREPRISE.md` si elles sont durables ;
   - **En attente du fondateur** : fils ouverts du QG, validations de mission, actions manuelles ;
   - **Prochaine étape** : l'agent à lancer et son brief en une phrase ;
   - **Pour relancer** : commandes exactes ;
   - **Points d'attention** : risques, dette, éléments sensibles.
3. N'y mets **aucun secret** (token, mot de passe) ni aucune donnée personnelle.
4. Réponds au fondateur avec un résumé de 5 lignes maximum et le chemin de la note.

## Reprendre (début de session)

1. Lis la note la plus récente de `{{dossier_notes}}/` (tri par nom), et elle seule.
2. Vérifie en 1 commande les éléments qui ont pu bouger : statut des fils `hq/inbox`, missions en attente.
3. Résume au fondateur en 5 lignes : où on en est, ce qui l'attend, la prochaine étape proposée. Attends son feu vert avant de lancer un agent.
