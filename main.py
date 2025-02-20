nome = "Luca"
cognome = "Gemma"
nome_completo = nome + " " + cognome

print(f"{nome = }")
print(f"{cognome = }")
print(f"{nome_completo = }")

nome_file = "output.txt"
stringa_da_scrivere = "Hello world!\n"

# Aggiungo la stringa "Hello world" al file output.txt
with open(nome_file, mode = "a") as file:
    file.writ(stringa_da_scrivere)

print(f"\nStringa '{stringa_da_scrivere}' scritta sul file '{nome_file}' correttament.")