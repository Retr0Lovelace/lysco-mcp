---
name: fil-question-fondateur
description: Poser une question au fondateur LYSCO depuis un agent. À utiliser dès qu'un agent a besoin d'une décision, d'une validation ou d'une information du fondateur : il écrit ou met à jour un fil JSON dans hq/inbox/ au lieu d'un Question.md ou d'une question dans son rapport.
---

# Fil de questions au fondateur

Référence complète : `hq/INBOX.md`. Ne jamais poser de question ailleurs (ni `Question.md`, ni seulement dans le rapport).

## Créer ou mettre à jour le fil

1. Nom du fichier : `hq/inbox/<projet>-<etape>-<agent>.json`, en minuscules, chiffres et tirets (ex. `lysco-05-maquette-ui-ux-designer-chloe.json`).
2. **Un seul fil par agent et par étape** : s'il existe déjà, le relire et y ajouter messages et questions, sans en créer un second.
3. Champs : `id` (= nom du fichier sans `.json`), `agent`, `project`, `step`, `title`, `status: "open"`, `files` (livrables à relire, chemins relatifs à la racine), `next` (étape suivante proposée), `messages`, `questions`.
4. Chaque question : `id` (`q1`, `q2`…), `text`, `answer: null`, et facultativement `options` (choix proposés) et `see` (**seulement** avec une ancre qui montre précisément l'élément, ex. `…/index.html#hero`).

## Bonnes questions

- Une décision par question, formulée pour qu'on puisse répondre en un clic quand c'est possible (`options`).
- Donner le contexte utile dans un message `from: "agent"` avant les questions, en 2 ou 3 phrases.
- Ne rien inventer pour combler un manque : demander.

## Quand l'agent est relancé

1. Lire les `answer` et les messages `from: "founder"`.
2. Les appliquer aux livrables.
3. Ajouter un message `from: "agent"` qui résume les changements.
4. Conclure par `status: "validated"` (dernier message = résumé + `next`) ou reposer des questions (`status: "open"`, les anciennes gardent leur réponse).
