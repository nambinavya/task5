import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("USD Currency Converter")
        self.create_widgets()

    def create_widgets(self):
        self.usd_label = tk.Label(self.root, text="Amount in USD:")
        self.usd_label.grid(column=0, row=0, padx=10, pady=10)
        self.usd_entry = tk.Entry(self.root)
        self.usd_entry.grid(column=1, row=0, padx=10, pady=10)

        self.currency_label = tk.Label(self.root, text="Convert to:")
        self.currency_label.grid(column=0, row=1, padx=10, pady=10)
        self.currency_var = tk.StringVar(self.root)
        self.currency_dropdown = ttk.Combobox(self.root, textvariable=self.currency_var)
        self.currency_dropdown.grid(column=1, row=1, padx=10, pady=10)

        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert)
        self.convert_button.grid(column=0, row=2, columnspan=2, pady=10)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(column=0, row=3, columnspan=2, pady=10)

        self.load_currencies()

    def load_currencies(self):
        self.rates = get_exchange_rates()
        self.currency_dropdown['values'] = list(self.rates.keys())

    def convert(self):
        try:
            amount = float(self.usd_entry.get())
            currency = self.currency_var.get()
            if currency:
                rate = self.rates[currency]
                converted_amount = convert_currency(amount, rate)
                self.result_label.config(text=f"{amount} USD = {converted_amount:.2f} {currency}")
            else:
                messagebox.showerror("Error", "Please select a currency")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
