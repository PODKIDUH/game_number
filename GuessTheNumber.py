from customtkinter import *
import random

set_appearance_mode("dark")
set_default_color_theme("blue")

window = CTk()
window.title("Guess The Number")
window.geometry("400x450")

secret_number = random.randint(1,100)
attemps = 0

# Функція перевірки введеного числа
def check_guess():
    global attemps

    user_input = entry.get()

    if not user_input.isdigit():
        label_info.configure(text="веди число від 1 до 100")
        return

    guess = int(user_input)
    attemps += 1

    label_attempts.configure(text=f"Спроб: {attemps}")

    if guess < secret_number:
        label_info.configure(text="Загадане число більше", text_color="lightblue")
    elif guess > secret_number:
        label_info.configure(text="Загадане число менше", text_color="red")
    else:
        label_info.configure(text=f"ВГАДАВ! Число: {secret_number}", text_color="gold")
        button_check.configure(state="disabled")

# Функція перезапуску гри
def reset_game():
    global attemps, secret_number

    secret_number = random.randint(1, 100)
    attemps = 0

    label_info.configure(text="від 1 до 100", text_color="white")
    label_attempts.configure(text="Спроб: 0")
    button_check.configure(state="normal")
    entry.delete(0, "end")

# Заголовок. Шрифт  font=("Arial", 28, "bold")
label_title = CTkLabel(window,
                       text="вгадай число",
                       font=("Arial", 28, "bold"),
                       text_color="#3B8ED0",
                       )
label_title.pack(pady=20)

# Підказка. Шрифт  font=("Arial", 16)
label_info = CTkLabel(window,
                       text="від 1 до 100",
                       font=("Arial", 20),
                       )
label_info.pack(pady=20)


# Лічильник спроб. Шрифт  font=("Arial", 14)
label_attempts = CTkLabel(window,
                       text="Спроб: 0",
                       font=("Arial", 16),
                       )
label_attempts.pack(pady=5)


# Поле введення
entry = CTkEntry(window,
                 placeholder_text="Твоя здогадка",
                 width=200,
                 height=40,
                 justify="center",
                 )
entry.pack(pady=10)

# Кнопка перевірки. Шрифт  font=("Arial", 14, "bold")
button_check = CTkButton(window,
                         text="Перевірити",
                         width=200,
                         font=("Arial", 14, "bold"),
                         command=check_guess,
                         )
button_check.pack(pady=10)

# Кнопка рестарту. Колір при наведенні hover_color="#555555"
button_reset = CTkButton(window,
                         text="Нова гра",
                         width=200,
                         font=("Arial", 14, "bold"),
                         command=reset_game,
                         fg_color="green",
                         hover_color="darkgreen"
                         )
button_reset.pack(pady=10)


# Запуск
window.mainloop()