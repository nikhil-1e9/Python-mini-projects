import tkinter as tk
from googletrans import Translator

translator = Translator()

class TranslatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Language Translator")
        self.master.geometry("500x350")
        self.master.resizable(0, 0)

        self.source_label = tk.Label(self.master, text="Source Language", font=("Helvetica", 12))
        self.source_label.grid(row=0, column=0, padx=10, pady=10)

        self.source_var = tk.StringVar()
        self.source_var.set("English")

        self.source_menu = tk.OptionMenu(self.master, self.source_var, "English", "Spanish", "French", "German")
        self.source_menu.grid(row=0, column=1, padx=10, pady=10)

        self.target_label = tk.Label(self.master, text="Target Language", font=("Helvetica", 12))
        self.target_label.grid(row=1, column=0, padx=10, pady=10)

        self.target_var = tk.StringVar()
        self.target_var.set("Spanish")

        self.target_menu = tk.OptionMenu(self.master, self.target_var, "English", "Spanish", "French", "German")
        self.target_menu.grid(row=1, column=1, padx=10, pady=10)

        self.source_text_label = tk.Label(self.master, text="Source Text", font=("Helvetica", 12))
        self.source_text_label.grid(row=2, column=0, padx=10, pady=10)

        self.source_text = tk.Text(self.master, height=3, width=30, font=("Helvetica", 12))
        self.source_text.grid(row=2, column=1, padx=10, pady=10)

        self.target_text_label = tk.Label(self.master, text="Target Text", font=("Helvetica", 12))
        self.target_text_label.grid(row=3, column=0, padx=10, pady=10)

        self.target_text = tk.Text(self.master, height=3, width=30, font=("Helvetica", 12))
        self.target_text.grid(row=3, column=1, padx=10, pady=10)

        self.translate_button = tk.Button(self.master, text="Translate", font=("Helvetica", 12), command=self.translate)
        self.translate_button.grid(row=4, column=1, padx=10, pady=10)

    def translate(self):
        source_lang = self.source_var.get()
        target_lang = self.target_var.get()
        source_text = self.source_text.get("1.0", tk.END)
        translation = translator.translate(source_text, src=source_lang.lower(), dest=target_lang.lower())
        self.target_text.delete("1.0", tk.END)
        self.target_text.insert(tk.END, translation.text)

root = tk.Tk()
app = TranslatorGUI(root)
root.mainloop()
