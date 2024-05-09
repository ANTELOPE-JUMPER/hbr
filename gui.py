import customtkinter
import ujson
import dbs

db = dbs.DatabaseManager('./hbr.db')

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


root = customtkinter.CTk()
root.title('Habr News (Python)')
root.geometry('1400x800')


links = []


def prt(url):
    db.create_tables()
    id, title, body, link, date = db.fetchone('SELECT * FROM news WHERE link = ?', (url,))
    textbox = customtkinter.CTkTextbox(master=root, width=800, height=500, corner_radius=0)
    textbox.grid(row=0, column=1, padx=(20, 0), pady=(40, 0), sticky="nsew")
    textbox.insert("0.0", body)


sframe = customtkinter.CTkScrollableFrame(
    master=root,
    height=500,
    width=300,
    corner_radius=10)
sframe.grid(sticky="nsew", row=0, column=0, padx=20, pady=40)


def show_news():
    with open('title_link.json') as file:
        src = ujson.load(file)
    k = 0
    for i, v in src.items():
        if v in links:
            continue
        else:
            if k == 101:
                break
            bt = customtkinter.CTkButton(
                master=sframe,
                text=i,
                command=lambda url=v: prt(url),
                width=20,
                height=20,
                anchor='left')
            bt.pack()
            links.append(v)
            k += 1


bt = customtkinter.CTkButton(
    master=root,
    text='Далее',
    command=lambda: show_news(),
    width=30,
    height=30,
    anchor='left')
bt.grid(row=3)


if __name__ == "__main__":
    root.mainloop()
    show_news()
