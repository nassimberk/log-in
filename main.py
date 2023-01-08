from tkinter import *




# Personnalisation de la fenêtre:

app = Tk()
app.title("Ma Première Fenêtre.")
app.minsize(480, 360)
app.config(background="#4174E1")

# Création de la frame:

frame = Frame(app, bg="#4174E1")

# Ajout le contenu de la frame:
text = "Identifiez-vous SVP!"
label_title = Label(frame, text=text, font=("", 18), bg="#4174E1", fg="white")
entry_id = Entry(frame, fg="#4174E1")
label_id = Label(frame, text= "Entrer votre identifiant :", bg="#4174E1" ,fg="white")
entry_pw = Entry(frame, show="*", fg="#4174E1")
label_pw = Label(frame, text="Entrer votre mot de passe :", bg="#4174E1", fg="white")
button_connexion = Button(frame, text="connexion",bg="#1044E1", fg="white", width= 17)
check_widget = Checkbutton(frame, text="Mémoirisez mon identifiant", bg="#4174E1", fg="White")
button_pw_oublie = Button(frame, text="Mot de passe oublié ?", bg="#4174E1", fg="white", border=0)
button_new_member = Button(frame, text="Créer nouveau compte", bg="#1044E1", fg="white")


# Afficher le contenu de fenêtre :
label_title.grid(row=0, column=1)
label_id.grid(row=1, column=0)
entry_id.grid(row=1, column=1)
label_pw.grid(row=2, column=0)
entry_pw.grid(row=2, column=1)
check_widget.grid(row=3, column=1)
button_pw_oublie.grid(row=5, column=1)
button_connexion.grid(row=4, column=1)
button_new_member.grid(row=6, column=1)


frame.pack(expand="YES")


app.mainloop()

