import random
import tkinter as tk
from PIL import Image, ImageTk

def generate_khodam():
    nama = entry.get()
    kata1 = ["Naga", 'Kuda', 'Gajah', 'Singa', 'Harimau', 'Tapir', "Monyet", 'Kucing', 'T-Rex', "Semut", 'Pohon', 'Kudanil', 'Kuman', 'Kelapa', 'Kutu', 'Babi', 'Koala', 'Panda']
    kata2 = ['Kawin', 'Hamil', 'Ngesot', 'Melahirkan', 'Main Catur', 'Raja Judi', 'Pembalap', 'Robux', 'Kayang', 'Ngaji', 'Umroh', 'Bakar', 'Rebus', 'Nge GYM', 'Gamers', 'Dagang']
    result = f"Khodam {nama} adalah {random.choice(kata1)} {random.choice(kata2)}"
    result_label.config(text=result)

root = tk.Tk()
root.title("Khodam Generator")
root.geometry("850x566")
root.configure(bg="grey")

image = Image.open("Umbrella Corps/dark night/Projek_KhodamGenerator/Harimau Seram.jpg")
image = image.resize((850, 566))
image_tk = ImageTk.PhotoImage(image)

# Create a canvas widget
canvas = tk.Canvas(root, width=850, height=566)
canvas.pack(fill="both", expand=True)

# Place the background image on the canvas
canvas.create_image(0, 0, image=image_tk, anchor="nw")

# Menggambar teks langsung pada canvas
canvas.create_text(425, 75, text="Masukkan nama yang ingin di cek:", fill="white", font=('Arial', 30, 'bold'), anchor="center")

entry = tk.Entry(root)
canvas.create_window(425, 125, width=425, height=25, window=entry)

generate_button = tk.Button(root, text="Cek", font=('Arial', 20, 'bold'), command=generate_khodam)
canvas.create_window(425, 200, window=generate_button)

result_label = tk.Label(root, text="", font=('Arial', 30), bg="white")
canvas.create_window(425, 275, window=result_label)

canvas.image = image_tk

root.mainloop()