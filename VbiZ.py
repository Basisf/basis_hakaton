def proverkluch(x,y):
    for i in range(len(x)):
        if x[i] not in y: return False #проверка ключей осуществляется в формате "и"
    return True

def parsing(kluch):
    import requests
    from bs4 import BeautifulSoup
    urlmas = ["https://mbkuban.ru/documents/gosudarstvennaya-programma/",
              "https://xn--90aifddrld7a.xn--p1ai/anticrisis/", "https://admkrai.krasnodar.ru/*https://moibiz93.ru/",
              "https://mbkuban.ru/", "https://dirmsp.krasnodar.ru/activity/msp"]

    for url in urlmas:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title
        links = soup.find_all("a")
        for link in links:
            try:
                if "http" in (link.get("href")):
                    url1 = f'{link.get("href")}'
                    response1 = requests.get(url1)
                    bit = BeautifulSoup(response1.text, "html.parser")
                    text = bit.get_text(strip=True)
                if (k == 1) and proverkluch(kluch, text):
                    with open(r'data.txt', 'a', encoding='utf-8') as data:
                        data.write("$" + f"{text}" + "$")
                elif proverkluch(kluch, text):
                    with open(r'data.txt', 'w', encoding='utf-8') as data:
                        data.write("$" + f"{text}" + "$")
                        k = 1
            except:
                ...
    try:
        data = open('data.txt','r')
        inf = data.read()
        if data=="":
            print("Ошибка! Данных по вашим ключам не найдено!")
        else: return inf
    except:
        print("Ошибка! Данных по вашим ключам не найдено!")



import customtkinter as ctk
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.page = 1

        self.Tags = []


        self.geometry("800x600")
        self.title("Vbiz")
        self.resizable(False, False)

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
            'Микро бизнес', 'Малый бизнес', 'Средний бизнес'
        ]
        self.TypeBusinessList = [
            'Индивидуальный предприниматель',
            'Полное товарищество',
            'Коммандитное товарищество',
            'Общество с ограниченной ответственностью',
            'Акционерное общество',
            'Публичное акционерное общество',
            'Кооператив'
        ]
        self.ListIDunno = [
            'Денежная поддержка',
            'Недвижимость',
            'Обучение',
            'Маркетинг и продвижение',
            'Консультирование',
            'Поддержка экспорта',
            'Регистрация, разрешения, экспертиза',
            'Выставка и ярмарки',
            'Обеспечение хозяйственной деятельности'
        ]

        self.create_what_do_you_want()

    def create_welcome_widgets(self):
        self.clear_widgets()
        self.text_welcome = ctk.CTkLabel(self, text='Привет. Введи свой регион:', text_color='gray')
        self.region_select = ctk.CTkComboBox(self, values=self.RegionList)
        self.region_done = ctk.CTkButton(self, text='Готово', command=self.on_done)

        self.text_welcome.grid(row=1, column=2, padx=10, pady=(10, 5), sticky='nsew')
        self.region_select.grid(row=2, column=2, padx=10, pady=5, sticky='nsew')
        self.region_done.grid(row=3, column=2, padx=10, pady=(15, 10), sticky='nsew')

    def create_another_widgets(self):
        self.clear_widgets()
        self.choose_size_text = ctk.CTkLabel(self, text='Теперь выберите свой размер бизнеса', text_color='gray')
        self.size_select = ctk.CTkComboBox(self, values=self.SizeList,state='readonly')

        self.choose_size_text.grid(row=1, column=2, sticky='nsew')
        self.size_select.grid(row=2, column=2, pady=10, sticky='nsew')
        self.region_done.grid(row=3, column=2, pady=10, sticky='nsew')

    def chosen_news(self):
        self.clear_widgets()
        self.text_in_progress = ctk.CTkLabel(self, text='В процессе...\n\n Обратная связь - BaziS@mail.ru', font=("Arial", 20, 'bold') )
        self.text_in_progress.grid(row=2, column=2)

    def create_what_do_you_want(self):
        self.clear_widgets()
        self.text_question = ctk.CTkLabel(self, text='Что вы хотите?', font=("Arial", 16, "bold"))
        self.button_news = ctk.CTkButton(self, text='Хочу\nновости!', font=("Arial", 14, 'bold'), command=self.chosen_news)
        self.button_recs = ctk.CTkButton(self, text='Хочу\nрекомендации!', font=("Arial", 14, 'bold'), command=self.create_welcome_widgets)

        self.text_question.grid(row=1, column=2, pady=10)
        self.button_news.grid(row=2, column=1,padx=10,pady=10,sticky='nsew')
        self.button_recs.grid(row=2, column=3,padx=10,pady=10,sticky='nsew')


    def create_main_menu(self):
        self.clear_widgets()

        for i in range(10):
            self.grid_rowconfigure(i, weight=1)
        for j in range(5):
            self.grid_columnconfigure(j, weight=1)

        self.third_que = ctk.CTkEntry(self, width=300, height=30, placeholder_text='Производство бытовой электроники')
        self.next_step= ctk.CTkButton(self, text='Готово', command=self.third_que_done)

        self.fourth_que = ctk.CTkSwitch(self, text='Нет действующего бизнеса', font=("Arial", 20) )

        ctk.CTkLabel(self, text='Ещё парочку вопросов...', font=("Arial", 30, 'bold')).grid(row=0, column=2)
        ctk.CTkLabel(self, text='Какова ваша отрасль деятельности бизнеса?\n(не обязательно)', font=("Arial", 20)).grid(row=1, column=2)
        self.third_que.grid(row=2, column=2)
        self.next_step.grid(row=8, column=2)

        self.fourth_que.grid(row=7, column=2)

    def create_fourth_page(self):
        self.clear_widgets()


    def on_done(self):
        if self.page == 1:
            selected_region = self.region_select.get();
            self.Tags.append(selected_region)
            self.page += 1
            self.create_another_widgets()



        elif self.page == 2:
            selected_size = self.size_select.get()
            self.Tags.append(selected_size)
            self.page += 1
            self.create_main_menu()
    def third_que_done(self):
        self.Tag_text = self.third_que.get()

        if (self.Tag_text != '') and (self.Tag_text not in self.Tags):
            self.Tags.append(self.Tag_text)
            self.next_step.configure(state='disabled', text='Введено!', fg_color='#247087')
            self.chosen_news()
            inf = parsing(self.Tags)

        else:
            self.create_fourth_page()
            self.chosen_news()

            inf = parsing(self.Tags)


    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.grid_forget()
    def ydal(self):
        self.clear_widgets()


if __name__ == "__main__":
    app = App()
    app.mainloop()