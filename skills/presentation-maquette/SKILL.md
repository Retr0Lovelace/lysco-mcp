---
name: presentation-maquette
description: Présenter une maquette de site au fondateur puis au client avec le gabarit interne. À utiliser quand une maquette (desktop et mobile) est prête à être montrée : copie du gabarit, captures, titre et badge, puis fil de validation.
variables:
  entreprise: Nom de l'entreprise (badge) | @entreprise
  dossier_gabarit: Dossier du gabarit de présentation | 03_PROJETS_INTERNE/Templates/Maquette | dossier
  dossier_clients: Dossier des projets clients | 02_CLIENTS | dossier
---

# Présentation de maquette

Gabarit : `{{dossier_gabarit}}/` (`index.html` + `desktop.png` + `mobile.png`). S'il est vide, demande-le au fondateur (fil `hq/inbox`) au lieu d'en inventer un.

## Étapes

1. Copier le gabarit dans le dossier maquette du client, par exemple `{{dossier_clients}}/<Client>/05_Maquette/presentation/`.
2. Remplacer `desktop.png` et `mobile.png` par les captures pleine page de la maquette (largeur ordinateur et largeur téléphone).
3. Dans `index.html`, ne changer que :
   - le `<title>` : `Présentation maquette — <Client>` ;
   - le badge : `{{entreprise}} x <Client>`.
   Ne pas modifier le reste du gabarit.
4. Ouvrir un fil de validation (skill `fil-question-fondateur`) avec la page de présentation dans `files`.

## Règles

- Photos fournies par le client uniquement ; jamais de reprise de son Instagram sans accord explicite.
- Aucun texte inventé (chiffres, avis, références) : laisser `[À FOURNIR]`.
- Ordre de validation : **le fondateur d'abord, puis le client**. Les retouches continuent jusqu'à la validation.
- Aucun prénom d'agent visible : face au client, {{entreprise}} = le fondateur.
