from tkinter import *
from tkinter import messagebox
from math import isqrt


class MainWindow():


    def __init__(self, app):

        self.expression = ""


        entry_font = ("Times", 15)
        butt_font = ("Verdana", 20)
        active_bg = "slategrey"
        num_bg = "lightgrey"
        op_bg = "darkgrey"
        f_bg = "white"

        frame = Frame(app, bg=f_bg, padx=4, pady=4)
        frame.pack()

        self.entry = Entry(frame, width=20, font=entry_font, bd=5)
        self.entry.grid(row=0, column=0, columnspan=3, pady=2)

        num_7 = Button(frame, text="7", font=butt_font,
            command=lambda: self.pressed("7"), bg=num_bg,
            activebackground=active_bg)
        num_8 = Button(frame, text="8", font=butt_font,
            command=lambda: self.pressed("8"), bg=num_bg,
            activebackground=active_bg)
        num_9 = Button(frame, text="9", font=butt_font,
            command=lambda: self.pressed("9"), bg=num_bg,
            activebackground=active_bg)
        num_4 = Button(frame, text="4", font=butt_font,
            command=lambda: self.pressed("4"), bg=num_bg,
            activebackground=active_bg)
        num_5 = Button(frame, text="5", font=butt_font,
            command=lambda: self.pressed("5"), bg=num_bg,
            activebackground=active_bg)
        num_6 = Button(frame, text="6", font=butt_font,
            command=lambda: self.pressed("6"), bg=num_bg,
            activebackground=active_bg)
        num_1 = Button(frame, text="1", font=butt_font,
            command=lambda: self.pressed("1"), bg=num_bg,
            activebackground=active_bg)
        num_2 = Button(frame, text="2", font=butt_font,
            command=lambda: self.pressed("2"), bg=num_bg,
            activebackground=active_bg)
        num_3 = Button(frame, text="3", font=butt_font,
            command=lambda: self.pressed("3"), bg=num_bg,
            activebackground=active_bg)
        num_0 = Button(frame, text="0", font=butt_font,
            command=lambda: self.pressed("0"), bg=num_bg,
            activebackground=active_bg)

        num_7.grid(row=1, column=0, padx=1, pady=1, sticky="we")
        num_8.grid(row=1, column=1, padx=1, pady=1, sticky="we")
        num_9.grid(row=1, column=2, padx=1, pady=1, sticky="we")

        num_4.grid(row=2, column=0, padx=1, pady=1, sticky="we")
        num_5.grid(row=2, column=1, padx=1, pady=1, sticky="we")
        num_6.grid(row=2, column=2, padx=1, pady=1, sticky="we")

        num_1.grid(row=3, column=0, padx=1, pady=1, sticky="we")
        num_2.grid(row=3, column=1, padx=1, pady=1, sticky="we")
        num_3.grid(row=3, column=2, padx=1, pady=1, sticky="we")

        num_0.grid(row=4, column=1, padx=1, pady=1, sticky="we")


        plus = Button(frame, text="+", font=butt_font,
            command=lambda: self.pressed("+"),bg=op_bg, fg="blue",
            activebackground=active_bg, activeforeground="blue")
        minus = Button(frame, text="-", font=butt_font,
            command=lambda: self.pressed("-"),bg=op_bg, fg="blue",
            activebackground=active_bg, activeforeground="blue")
        divide = Button(frame, text="/", font=butt_font,
            command=lambda: self.pressed("/"),bg=op_bg, fg="blue",
            activebackground=active_bg, activeforeground="blue")
        multiply = Button(frame, text="*", font=butt_font,
            command=lambda: self.pressed("*"),bg=op_bg, fg="blue",
            activebackground=active_bg, activeforeground="blue")
        equal = Button(frame, text="=", font=butt_font,
            command=lambda: self.equalpressed(),bg=op_bg, fg="green",
            activebackground=active_bg, activeforeground="green")

        clear = Button(frame, text="C", font=butt_font,
            command=lambda: self.clear_entry(),bg=op_bg,
            fg="red", activebackground=active_bg, activeforeground="red")
        del_last_num = Button(frame, text="CE", font=("Verdana", 9, "bold"),
            command=lambda: self.delete_last(), width=7,bg=op_bg, fg="red",
            activebackground=active_bg, activeforeground="red" )

        plus.grid(row=1, column=3, padx=1, pady=1, sticky="we")
        minus.grid(row=2, column=3, padx=1, pady=1, sticky="we")
        divide.grid(row=3, column=3, padx=1, pady=1, sticky="we")
        multiply.grid(row=4, column=3, padx=1, pady=1, sticky="we")
        equal.grid(row=4, column=2, padx=1, pady=1, sticky="we")

        clear.grid(row=4, column=0, padx=1, pady=1, sticky="we")
        del_last_num.grid(row=0, column=3, padx=2)

        more = Button(frame, text="Viac", font=("Verdana", 10),
            command=lambda: self.show_more(), bg=op_bg, fg="blue",
            activebackground=active_bg, activeforeground="blue")
        more.grid(row=5, column=0, columnspan=4, padx=1, pady=1, sticky="ew")




    def pressed(self, num):

        self.expression += num
        self.entry.delete(0, END)
        self.entry.insert(END, self.expression)



    def equalpressed(self):

        self.entry.delete(0, END)
        result = str(eval(self.expression))
        self.entry.insert(0, result)
        self.expression = result



    def clear_entry(self):

        self.expression = ""
        self.entry.delete(0, END)



    def delete_last(self):

        self.expression = self.expression[0:-1]
        self.entry.delete(0, END)
        self.entry.insert(0, self.expression)



# Second window
#---------------------------------------------------------------------------#
    def show_more(self):
    
        try:
            self.win.destroy()
        except:
            print("Excepted")

        self.text_one = StringVar()
        self.text_two = StringVar()
        self.text_three = StringVar()
        self.selection_tag = StringVar()

        self.text_one.set("x")
        self.text_two.set("x")
        self.text_three.set("x")
        self.selection_tag.set("Vybrane: nezvolene")

        self.win = Toplevel()


        top_f = Frame(self.win)
        top_f.pack(padx=10, pady=5, fill="both")
        bot_f = LabelFrame(self.win, text="Hodnoty") 
        bot_f.pack(padx=10, pady=10, fill="both")
        very_bot_f = Frame(self.win)
        very_bot_f.pack(fill="both")

        self.select = Button(top_f, text="Vybrat", command=lambda: self.selected_item(), bg="lightgrey")
        self.select.grid(row=0, column=0, sticky="ew", columnspan=2, padx=5, pady=5)

        self.list_func = Listbox(top_f, height=4, selectmode="single", font=("Verdana", 15))
        self.list_func.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.list_func.insert(0, "Kvadraticka rovnica")
        self.list_func.insert(0, "Pytagorova veta")
        self.list_func.insert(0, "Objem a obsah kvadra")
        self.list_func.insert(0, "Obvod a obsah kruhu")


        self.selection_view = Label(bot_f, textvariable=self.selection_tag, font=("Verdana", 15))
        self.selection_view.grid(row=2, column=0, columnspan=2, sticky="we", ipadx=15)

        self.label_one = Label(bot_f, textvariable=self.text_one, font=("Verdana", 10))
        self.label_one.grid(row=3, column=0, padx=20)

        self.entry_one = Entry(bot_f, state="disabled", font=("Verdana", 10))
        self.entry_one.grid(row=3, column=1, padx=5, pady=1)


        self.label_two = Label(bot_f, textvariable=self.text_two, font=("Verdana", 10))
        self.label_two.grid(row=4, column=0, padx=20)

        self.entry_two = Entry(bot_f, state="disabled", font=("Verdana", 10))
        self.entry_two.grid(row=4, column=1, padx=5, pady=1)


        self.label_three = Label(bot_f, textvariable=self.text_three, font=("Verdana", 10))
        self.label_three.grid(row=5, column=0, padx=20)

        self.entry_three = Entry(bot_f, state="disabled", font=("Verdana", 10))
        self.entry_three.grid(row=5, column=1, padx=5, pady=1)

        self.calculate = Button(bot_f, text="Vypocitaj", command=lambda: self.calculate_result(), font=("Verdana", 10), state="disabled")
        self.calculate.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.info_label = Label(very_bot_f, text="Ak je to potrebne, zadavaj hodonty v cm.")
        self.info_label.pack()


#### Second window methods ####
#-----------------------------#

    def selected_item(self):

        self.entry_one.delete(0, END)
        self.entry_two.delete(0, END)
        self.entry_three.delete(0, END)

        self.text_one.set(" ")
        self.text_two.set(" ")
        self.text_three.set(" ")

        try:
            selected = self.list_func.curselection()
            self.current = self.list_func.get(selected)
            print(self.current)

            if self.current == "Objem a obsah kvadra":

                self.selection_tag.set("Vybrane: V a S kvader")

                self.calculate["state"] = "normal"
                self.entry_one.configure(state="normal")
                self.entry_two.configure(state="normal")
                self.entry_three.configure(state="normal")
                self.text_one.set("a:")
                self.text_two.set("b:")
                self.text_three.set("c:")

                self.current = "Objem a obsah kvadra"


            elif self.current == "Obvod a obsah kruhu":

                self.selection_tag.set("Vybrane: S a o kruhu")

                self.calculate["state"] = "normal"
                self.entry_one["state"] = "normal"
                self.entry_two["state"] = "disabled"
                self.entry_three["state"] = "disabled"

                self.text_one.set("r:")

                self.current = "Obvod a obsah kruhu"


            elif self.current == "Kvadraticka rovnica":

                self.selection_tag.set("Vybrane: Kvadrar. r.")

                self.calculate["state"] = "normal"
                self.entry_one["state"] = "normal"
                self.entry_two["state"] = "normal"
                self.entry_three["state"] = "normal"

                self.text_one.set("a:")
                self.text_two.set("b:")
                self.text_three.set("c:")

                self.current = "Kvadraticka rovnica"


            elif self.current == "Pytagorova veta":

                self.selection_tag.set("Vybrane: Pytag. veta")

                self.calculate["state"] = "normal"
                self.entry_one["state"] = "normal"
                self.entry_two["state"] = "normal"
                self.entry_three["state"] = "disabled"

                self.text_one.set("a:")
                self.text_two.set("b:")

                self.current = "Pytagorova veta"


        except:
            messagebox.showwarning("Chyba", "Nebola vybraná žiadna možnosť.")



    def calculate_result(self):


        # Objem a obsah kvádra
        if self.current == "Objem a obsah kvadra":

            if self.entry_one != "" or self.entry_two != "" or self.entry_three != "":
                try:
                    a = float(self.entry_one.get())
                    b = float(self.entry_two.get())
                    c = float(self.entry_three.get())

                    V = round((a*b*c), 2)
                    S = round((2 * (a*b + b*c + a*c)),2)

                    messagebox.showinfo("Výsledok", f"Kváder pri rozmeroch: a={a}cm; b={b}cm; c={c}cm\n-->V = {V}cm kubických\n-->S = {S}cm štvorcových")

                except ValueError:
                    messagebox.showwarning("Chyba", "Zadané hodnoty nie su akceptovateľné.\nProsím, skontrolujte vaše zadané hodnoty.")

            else:
                messagebox.showwarning("Chyba", "Skontrolujte, či sú všetky polia zaplnené.")


        # Obvod a obsah kruhu
        elif self.current == "Obvod a obsah kruhu":

            if self.entry_one != "":
                try:
                    r = float(self.entry_one.get())

                    S = round(3.14 * (r*r), 2)
                    o = round(3.14 * (2*r), 2)
                    
                    messagebox.showinfo("Výsledok", f"Kruh pri polomere {r}cm\n-->S = {S}cm štvorcových\n-->o = {o}cm")

                except ValueError:
                    messagebox.showwarning("Chyba", "Zadané hodnoty nie su akceptovateľné.\nProsím, skontrolujte vaše zadané hodnoty.")

            else:
                messagebox.showwarning("Chyba", "Skontrolujte, či sú všetky polia zaplnené.")


        # Pytagorova veta
        elif self.current == "Pytagorova veta":

            try:
                a = float(self.entry_one.get())
                b = float(self.entry_two.get())

                c = ((a**2 + b**2)**(1/2))

                messagebox.showinfo("Výsledok", f"Pri odvesnách a={a}cm a b={b}cm\n-->c = {c}cm")

            except ValueError:
                messagebox.showwarning("Chyba", "Zadané hodnoty nie su akceptovateľné.\nProsím, skontrolujte vaše zadané hodnoty.")


        # Kvadraticka rovnica
        elif self.current == "Kvadraticka rovnica":

            try:
                a = int(self.entry_one.get())
                b = int(self.entry_two.get())
                c = int(self.entry_three.get())

                D = ((b**2) - 4*a*c)

                if D == 0:
                    x = (-b / (2*a))
                    messagebox.showinfo("Výsledok", f"Pre hodnoty: a={a}; b={b}; c={c}\n-->x = {x}")

                elif D < 0:
                    messagebox.showinfo("Výsledok", f"Pre hodnoty: a={a}; b={b}; c={c}\n-->Rovnica nemá riešenie")

                elif D > 0:
                    x1 = (-b + (isqrt(D)) / 2*a)
                    x2 = (-b - (isqrt(D)) / 2*a)

                    messagebox.showinfo("Výsledok", f"Pre hodnoty: a={a}; b={b}; c={c}\n-->x1 = {x1}\n-->x2 = {x2}")

            except ValueError:
                messagebox.showwarning("Chyba", "Zadané hodnoty nie su akceptovateľné.\nProsím, skontrolujte vaše zadané hodnoty.")





if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    app = MainWindow(root)

    root.mainloop()
