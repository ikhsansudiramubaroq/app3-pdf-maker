from fpdf import FPDF  # Mengimpor kelas FPDF dari pustaka fpdf untuk membuat file PDF
import pandas as pd  # Mengimpor pustaka pandas untuk manipulasi dan analisis data

# Inisialisasi objek PDF dengan orientasi portrait, unit mm, dan format A4
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)  # Menonaktifkan pemisahan halaman otomatis dan mengatur margin menjadi 0

# Membaca data dari file CSV dan menyimpannya dalam DataFrame
df = pd.read_csv("topics.csv")

# Iterasi melalui setiap baris dalam DataFrame
for index, row in df.iterrows():
    pdf.add_page()  # Menambahkan halaman baru untuk setiap baris data

    # Mengatur font untuk header
    pdf.set_font(family="Times", style="B", size=24)  # Mengatur font menjadi Times, tebal, ukuran 24
    pdf.set_text_color(50, 200, 20)  # Mengatur warna teks menjadi hijau
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)  # Menambahkan sel dengan teks dari kolom "Topic" dan posisi kiri
    pdf.line(10, 21, 200, 21)  # Menggambar garis horizontal di bawah header

    # Mengatur footer
    pdf.ln(265)  # Menambahkan jarak vertikal untuk footer
    pdf.set_font(family="Times", style="I", size=8)  # Mengatur font menjadi italic (I) dengan ukuran 8
    pdf.set_text_color(180, 180, 100)  # Mengatur warna teks footer menjadi kuning keabu-abuan
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")  # Menambahkan sel footer dengan teks dari kolom "Topic" dan posisi kanan

    # Menambahkan halaman tambahan berdasarkan nilai di kolom "Pages"
    for i in range(row["Pages"] - 1):  # Loop untuk setiap halaman tambahan
        pdf.add_page()  # Menambahkan halaman baru

        # Mengatur footer untuk halaman tambahan
        pdf.ln(277)  # Menambahkan jarak vertikal untuk footer
        pdf.set_font(family="Times", style="I", size=8)  # Mengatur font menjadi italic (I) dengan ukuran 8
        pdf.set_text_color(180, 180, 100)  # Mengatur warna teks footer menjadi kuning keabu-abuan
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")  # Menambahkan sel footer dengan teks dari kolom "Topic" dan posisi kanan

# Menyimpan PDF yang telah dibuat dengan nama "output.pdf"
pdf.output("output.pdf")
