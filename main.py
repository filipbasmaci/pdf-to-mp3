import PyPDF2
from gtts import gTTS
import tkinter as tk
from tkinter import filedialog, messagebox


def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)

            text = ""
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text()

            return text
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while reading the PDF: {e}")
        return None


def save_audio(text, output_path):
    try:
        tts = gTTS(text)
        tts.save(output_path)
        messagebox.showinfo("Success", f"Audio saved successfully to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the audio: {e}")


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        text = read_pdf(file_path)
        if text:
            output_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
            if output_path:
                save_audio(text, output_path)


def setup_gui(root):
    root.title("PDF to MP3 Converter")
    root.geometry("400x200")
    root.resizable(False, False)

    frame = tk.Frame(root, bg="#2c3e50")
    frame.place(relwidth=1, relheight=1)

    label = tk.Label(frame, text="PDF to MP3 Converter", font=("Arial", 18), bg="#2c3e50", fg="#ecf0f1")
    label.pack(pady=20)

    btn_open = tk.Button(frame, text="PDF Dosyası Aç", font=("Arial", 14), bg="#3498db", fg="#ecf0f1", relief="flat",
                         command=open_file)
    btn_open.pack(pady=10)

    btn_exit = tk.Button(frame, text="Çıkış", font=("Arial", 14), bg="#e74c3c", fg="#ecf0f1", relief="flat",
                         command=root.quit)
    btn_exit.pack(pady=10)


root = tk.Tk()
setup_gui(root)
root.mainloop()
