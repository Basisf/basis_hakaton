import customtkinter as ctk
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.page = 1

        self.RegionInfo = ''
        self.SizeInfo = ''

        with open(r'datap.txt', 'w', encoding='utf-8') as data:
            data.write(f"-r-{self.RegionInfo}\n")
            data.write(f"-s-{self.SizeInfo}\n")

        self.geometry("500x500")
        self.title("Привет")
        self.resizable(False, False)

        # Конфигурация сетки
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        for j in range(5):
            self.grid_columnconfigure(j, weight=1)

        self.RegionList = [
            "Республика Алтай", "Республика Башкортостан", "Республика Бурятия",
            "Карачаево-Черкесская Республика", "Республика Карелия", "Республика Коми",
            "Республика Марий Эл", "Республика Мордовия", "Республика Саха (Якутия)",
            "Республика Татарстан", "Республика Тыва", "Республика Хакасия",
            "Удмуртская Республика", "Чувашская Республика", "Алтайский край",
            "Забайкальский край", "Камчатский край", "Краснодарский край",
            "Красноярский край", "Пермский край", "Приморский край", "Хабаровский край",
            "Амурская область", "Архангельская область", "Белгородская область",
            "Брянская область", "Владимирская область", "Волгоградская область",
            "Вологодская область", "Воронежская область", "Ивановская область",
            "Иркутская область", "Калужская область", "Кемеровская область",
            "Кировская область", "Костромская область", "Курганская область",
            "Курская область", "Ленинградская область", "Липецкая область",
            "Магаданская область", "Московская область", "Мурманская область",
            "Нижегородская область", "Новгородская область", "Новосибирская область",
            "Омская область", "Оренбургская область", "Орловская область",
            "Пензенская область", "Псковская область", "Ростовская область",
            "Рязанская область", "Самарская область", "Саратовская область",
            "Сахалинская область", "Свердловская область", "Смоленская область",
            "Тамбовская область", "Тверская область", "Томская область",
            "Тульская область", "Тюменская область", "Ульяновская область",
            "Челябинская область", "Ярославская область", "Москва",
            "Санкт-Петербург", "Еврейская автономная область", "Ненецкий автономный округ",
            "Ханты-Мансийский автономный округ - Югра", "Чукотский автономный округ",
            "Ямало-Ненецкий автономный округ"
        ]
        self.SizeList = [
            'Малый', 'Средний', 'Большой', 'Микро'
        ]

        self.create_welcome_widgets()

    def create_welcome_widgets(self):
        self.text_welcome = ctk.CTkLabel(self, text='Привет. Введи свой регион:', text_color='gray')
        self.region_select = ctk.CTkComboBox(self, values=self.RegionList)
        self.region_done = ctk.CTkButton(self, text='Готово', command=self.on_done)

        self.text_welcome.grid(row=1, column=2, padx=10, pady=(10, 5), sticky='nsew')
        self.region_select.grid(row=2, column=2, padx=10, pady=5, sticky='nsew')
        self.region_done.grid(row=3, column=2, padx=10, pady=(15, 10), sticky='nsew')

    def create_another_widgets(self):
        self.choose_size_text = ctk.CTkLabel(self, text='Теперь выберите свой размер', text_color='gray')
        self.size_select = ctk.CTkComboBox(self, values=self.SizeList)

        self.choose_size_text.grid(row=1, column=2, sticky='nsew')
        self.size_select.grid(row=2, column=2, pady=10, sticky='nsew')
        self.region_done.grid(row=3, column=2, pady=10, sticky='nsew')

    def create_custom_tags(self):
        self.text_existing_tags = ctk.CTkLabel(self, text='Ваши теги:')
        self.tag_region = ctk.CTkButton(self, text=f'{self.RegionInfo}', state='disabled')
        self.tag_size = ctk.CTkButton(self, text=f'{self.SizeInfo}', state='disabled')
        self.all_done = ctk.CTkButton(self, text='Готово', command=self.on_done)

        self.text_existing_tags.grid(row=1, column=2, pady=10, sticky='nsew')
        self.tag_region.grid(row=2,column=1,pady=10,sticky='nsew')
        self.tag_size.grid(row=2,column=3,pady=10,sticky='nsew')
        self.all_done.grid(row=3,column=2,pady=10)

    def show_me_reccomendations(self):
        ...
    def on_done(self):
        if self.page == 1:
            self.RegionInfo = self.region_select.get()
            # with open(r'datap.txt',encoding='utf-8') as data:
            #     for i in data:
            #         if "-r-" in i:
            #             self.RegionInfo = i[3:]

            self.page += 1
            self.clear_widgets()
            self.create_another_widgets()

        elif self.page == 2:
            self.SizeInfo = self.size_select.get()
            # with open(r'datap.txt',encoding='utf-8') as data:
            #     for i in data:
            #         if "-s-" in i:
            #             self.SizeInfo = i[3:]
            self.page += 1
            self.clear_widgets()
            self.create_custom_tags()

        elif self.page == 3:
            #pars pars pars
            self.page += 1
            self.clear_widgets()
            self.create_custom_tags()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.grid_forget()


if __name__ == "__main__":
    app = App()
    app.mainloop()
"""
region = "Кубань"
napravlen = "Средний бизнес"
otras = "Машины"
with open(r'data.txt', 'w', encoding='utf-8') as data:
   data.write(f"-r-{region}\n")
   data.write(f"-n-{napravlen}\n")
   data.write(f"-o-{otras}\n")
with open(r'data.txt', encoding='utf-8') as data:
   for i in data:
      if "-r-" in i:
         print(f"Регион {i[3:]}")
      if "-n-" in i:
         print(f"Направление {i[3:]}")
      if "-o-" in i:
         print(f"Отрасль {i[3:]}")
"""