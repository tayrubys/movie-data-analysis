import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Veri yükleniyor ve analiz ediliyor...")

# veri okuma ve temizleme
df = pd.read_csv("movies_metadata.csv", low_memory=False)
df = df[['title', 'vote_average', 'vote_count']].dropna()
df['vote_count'] = pd.to_numeric(df['vote_count'], errors='coerce')
df['vote_average'] = pd.to_numeric(df['vote_average'], errors='coerce')
df = df.dropna()

# veri analizi
populer_filmler = df[df['vote_count'] > 1000]
en_iyiler = populer_filmler.sort_values(by='vote_average', ascending=False).head(10)

# veri gorsellestirme
sns.set_theme(style="whitegrid", context="talk")
plt.figure(figsize=(12, 7), dpi=300)

# grafik ayarlari
ax = sns.barplot(
    x='vote_average',
    y='title',
    data=en_iyiler,
    hue='title',
    palette='mako',
    legend=False,
    edgecolor=".2" # Çubuklara çok ince, şık bir kenarlık ekler
)
for i in ax.containers:
    ax.bar_label(i, fmt='%.1f', padding=5, fontsize=12, color='#333333', fontweight='bold')

#baslik ve eksen isimlendirme
plt.title('En Beğenilen 10 Film\n(En az 1000 oylama baz alınmıştır)',
          fontsize=18, fontweight='bold', pad=20, color='#222222')
plt.xlabel('Ortalama Puan (10 Üzerinden)', fontsize=14, labelpad=15, color='#555555')
plt.ylabel('') # Y ekseni adını siliyoruz çünkü film isimleri zaten kendini açıklıyor

plt.xlim(0, 10)

# Gereksiz çerçeve çizgilerini kaldirma
sns.despine(left=True, bottom=True)

ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
ax.yaxis.grid(False)

plt.tight_layout()
plt.savefig('en_iyi_filmler_pro.png', bbox_inches='tight')
plt.show()
print("Grafik başarıyla oluşturuldu ve 'en_iyi_filmler_pro.png' olarak kaydedildi")