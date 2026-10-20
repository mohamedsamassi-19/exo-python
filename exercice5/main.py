from outil import convertir_note, moyenne, mention

notes_brutes = ["12,5", "15", "abc", "9", "18,25"]

notes_valides = []
for texte in notes_brutes:
    note = convertir_note(texte)
    if note is not None:
        notes_valides.append(note)

ignorees = len(notes_brutes) - len(notes_valides)
moy = moyenne(notes_valides)

print(f"Notes ignorées : {ignorees}")
print(f"Moyenne : {moy:.2f}")
print(f"Mention : {mention(moy)}")