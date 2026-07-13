import pandas as pd
from textblob import TextBlob

# Fungsi untuk menentukan sentimen
def get_sentiment(text):
    if pd.isna(text):
        return "Neutral"
    
    analysis = TextBlob(str(text))
    
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

print("Membaca data dan menganalisis sentimen, mohon tunggu beberapa detik...")

# Membaca file CSV mentah
df = pd.read_csv("laptop_online_review.csv")

# Membuat kolom baru bernama 'Sentiment'
df['Sentiment'] = df['Review'].apply(get_sentiment)

# Menampilkan 5 baris pertama di terminal agar bisa dilihat
print("\n--- HASIL 5 BARIS PERTAMA ---")
print(df[['Review', 'Sentiment']].head())

# Menyimpan hasil ke file CSV baru
df.to_csv("hasil_sentimen_pelanggan.csv", index=False)
print("\nSukses! File 'hasil_sentimen_pelanggan.csv' berhasil dibuat.")