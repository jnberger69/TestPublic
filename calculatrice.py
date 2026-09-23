"""Petite calculatrice fenêtrée avec mise à jour du résultat en direct."""
import tkinter as tk


def calculer(*_args):
    op1_texte = entree1.get().strip().replace(",", ".")
    op2_texte = entree2.get().strip().replace(",", ".")
    operateur = operateur_var.get()

    try:
        op1 = float(op1_texte)
        op2 = float(op2_texte)
    except ValueError:
        resultat_var.set("Résultat : ?")
        return

    if operateur == "+":
        resultat = op1 + op2
    elif operateur == "-":
        resultat = op1 - op2
    else:  # "x"
        resultat = op1 * op2

    if resultat == int(resultat):
        resultat = int(resultat)

    resultat_var.set(f"Résultat : {resultat}")


fenetre = tk.Tk()
fenetre.title("Calculatrice")
fenetre.resizable(False, False)

cadre = tk.Frame(fenetre, padx=15, pady=15)
cadre.pack()

entree1 = tk.Entry(cadre, width=10, justify="center")
entree1.grid(row=0, column=0, padx=5)

operateur_var = tk.StringVar(value="+")
menu_operateur = tk.OptionMenu(cadre, operateur_var, "+", "-", "x", command=calculer)
menu_operateur.grid(row=0, column=1, padx=5)

entree2 = tk.Entry(cadre, width=10, justify="center")
entree2.grid(row=0, column=2, padx=5)

resultat_var = tk.StringVar(value="Résultat : ?")
label_resultat = tk.Label(cadre, textvariable=resultat_var, font=("Arial", 14))
label_resultat.grid(row=1, column=0, columnspan=3, pady=(15, 0))

entree1.bind("<KeyRelease>", calculer)
entree2.bind("<KeyRelease>", calculer)

fenetre.mainloop()
