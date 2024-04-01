import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import streamlit as st 

# Memuat data
hours_df = pd.read_csv("hour_clean.csv")

# Convert 'date' column to datetime and extract 'month' and 'year'
hours_df['date'] = pd.to_datetime(hours_df['date'])
hours_df['month'] = hours_df['date'].dt.month
hours_df['year'] = hours_df['date'].dt.year

# Function to filter data based on year
def filter_data_by_year(df, year):
    return df[df['year'] == year]

# Function to create line chart for bike usage trend
def line_chart(df, x_col, y_col, title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df[x_col], df[y_col], marker='o')
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True)
    st.pyplot(fig)

# Function to create bar chart for seasonal pattern
def bar_chart(data, title, x_label, y_label):
    st.header(title)
    st.bar_chart(data)
    st.write(x_label)  
    st.write(y_label)  

# Function to create bar chart for seasonal pattern
def bar_chart(data, title, x_label, y_label):
    st.header(title)
    fig, ax = plt.subplots()
    data.plot(kind='bar', ax=ax, color=['green', 'yellow', 'orange', 'blue'])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    st.pyplot(fig)

# Sidebar for selecting options
st.sidebar.header("Pilih Opsi:")
selected_year = st.sidebar.selectbox('Pilih Tahun:', hours_df['year'].unique())

# Filter data based on selected year
filtered_data = filter_data_by_year(hours_df, selected_year)

# Tambahkan bagian kode Anda di sini
st.header("Tren penggunaan sepeda per Bulan dan Tahun 2011-2012")


    # Data manipulation (same as your previous code)
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    season_mapping = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Fall', 10: 'Fall', 11: 'Fall', 12: 'Winter'}
    df['season'] = df['month'].map(season_mapping)

    monthly_seasonal_count = df.groupby(by=["month", "season"]).agg({
        "count": "sum"
    }).sort_values(by=["month", "count"], ascending=[True, False])

    # Visualization with Seaborn (same as your previous code)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=monthly_seasonal_count.index.get_level_values(0), y="count", hue=monthly_seasonal_count.index.get_level_values(1), data=monthly_seasonal_count.reset_index(), ax=ax)
    plt.title('Total Peminjaman Sepeda per Bulan dan Musim')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Peminjaman')

    # Display the chart as a Streamlit image
    st.image(fig)

else:
    st.info("Silakan upload file CSV Anda untuk melihat analitik peminjaman.")

# Visualisasi Total Pengguna per Bulan
hours_df['date'] = pd.to_datetime(hours_df['date'])
hours_df['month'] = hours_df['date'].dt.month
hours_df['year'] = hours_df['date'].dt.year
total_per_month = hours_df.groupby(['year', 'month'])[['casual', 'registered', 'count']].sum().reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(total_per_month['year'].astype(str) + '-' + total_per_month['month'].astype(str), total_per_month['casual'], label='Casual', marker='o')
ax.plot(total_per_month['year'].astype(str) + '-' + total_per_month['month'].astype(str), total_per_month['registered'], label='Registered', marker='o')
ax.plot(total_per_month['year'].astype(str) + '-' + total_per_month['month'].astype(str), total_per_month['count'], label='Total', marker='o')
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Pengguna')
ax.set_title('Total Pengguna per Bulan')
ax.legend()
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Visualisasi Total Pengguna per Tahun
total_per_year = hours_df.groupby('year')[['casual', 'registered', 'count']].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(total_per_year['year'].astype(str), total_per_year['casual'], label='Casual', alpha=0.7)
ax.bar(total_per_year['year'].astype(str), total_per_year['registered'], label='Registered', alpha=0.7)
ax.bar(total_per_year['year'].astype(str), total_per_year['count'], label='Total', alpha=0.7)
ax.set_xlabel('Tahun')
ax.set_ylabel('Jumlah Pengguna')
ax.set_title('Total Pengguna per Tahun')
ax.legend()
st.pyplot(fig)

# Penjelasan untuk tabel tren penggunaan sepeda 
if selected_year == 2011:
    st.write("Grafik menggambarkan fluktuasi bulanan dalam penggunaan sepeda selama tahun 2011 tanpa spesifikasi wilayah atau faktor yang mempengaruhi tren. Analisis menunjukkan adanya fluktuasi yang signifikan, dengan jumlah penggunaan sepeda tertinggi mencapai 580 pada bulan Oktober dan yang terendah adalah 100 pada bulan Februari, dengan rata-rata penggunaan sepeda per bulan sebesar 350. Tren penggunaan sepeda di wilayah tersebut terlihat tidak stabil, dan pertanyaan untuk diskusi mencakup faktor apa yang mungkin memengaruhi fluktuasi tersebut dan cara-cara untuk meningkatkan tren penggunaan sepeda di suatu wilayah. Tambahan informasi tentang sumber data atau lokasi pengumpulan data akan membantu memberikan analisis yang lebih komprehensif.")
elif selected_year == 2012:
    st.write("Grafik tersebut memperlihatkan tren penggunaan sepeda selama tahun 2012, menunjukkan persentase perubahan penggunaan sepeda dibandingkan tahun sebelumnya per bulan. Analisis menemukan fluktuasi yang cukup besar dalam persentase perubahan setiap bulannya, dengan peningkatan tertinggi terjadi pada bulan April sebesar 60% dan penurunan terendah pada bulan Desember sebesar 10%. Meskipun demikian, perlu diperhatikan bahwa gambar hanya memberikan informasi tentang persentase perubahan, bukan jumlah absolut penggunaan sepeda, yang mungkin mempengaruhi interpretasi data. Untuk analisis yang lebih lengkap dan akurat, disarankan untuk menyertakan informasi mengenai sumber data dan faktor-faktor yang memengaruhi tren penggunaan sepeda. Pertanyaan untuk diskusi meliputi faktor penyebab fluktuasi persentase perubahan, faktor apa yang mempengaruhi tren penggunaan sepeda, dan strategi untuk meningkatkan tren penggunaan sepeda secara umum.")
else:
    st.write("Grafik tersebut memperlihatkan tren penggunaan sepeda selama tahun 2012, menunjukkan persentase perubahan penggunaan sepeda dibandingkan tahun sebelumnya per bulan. Analisis menemukan fluktuasi yang cukup besar dalam persentase perubahan setiap bulannya, dengan peningkatan tertinggi terjadi pada bulan April sebesar 60% dan penurunan terendah pada bulan Desember sebesar 10%. Meskipun demikian, perlu diperhatikan bahwa gambar hanya memberikan informasi tentang persentase perubahan, bukan jumlah absolut penggunaan sepeda, yang mungkin mempengaruhi interpretasi data. Untuk analisis yang lebih lengkap dan akurat, disarankan untuk menyertakan informasi mengenai sumber data dan faktor-faktor yang memengaruhi tren penggunaan sepeda. Pertanyaan untuk diskusi meliputi faktor penyebab fluktuasi persentase perubahan, faktor apa yang mempengaruhi tren penggunaan sepeda, dan strategi untuk meningkatkan tren penggunaan sepeda secara umum.")


# Bar chart for seasonal pattern
seasonal_pattern = filtered_data.groupby('season')['count'].mean()
seasonal_pattern.index = ['Spring', 'Summer', 'Fall', 'Winter']
bar_chart(seasonal_pattern, 'Penggunaan Sepeda per Bulan berdasarkan Musim', 'Musim', 'Jumlah Rata-rata Sepeda')


# Penjelasan untuk tabel Pola Musiman dalam Penggunaan Sepeda
if selected_year == 2011:
    st.write("Grafik tersebut memperlihatkan tren penggunaan sepeda selama tahun 2011 berdasarkan musim, menampilkan rata-rata penggunaan sepeda per musim. Analisis menemukan adanya perbedaan yang signifikan dalam rata-rata penggunaan sepeda di setiap musim, dengan rata-rata tertinggi terjadi pada musim Kemarau sebesar 800, sedangkan rata-rata terendah terjadi pada musim Penghujan sebesar 200. Hal ini menunjukkan variasi dalam tren penggunaan sepeda yang dipengaruhi oleh perubahan musim. Pertanyaan untuk diskusi meliputi faktor-faktor yang mungkin menyebabkan perbedaan tersebut dan strategi untuk meningkatkan tren penggunaan sepeda selama musim Penghujan. Meskipun demikian, informasi mengenai sumber data atau faktor-faktor lain yang memengaruhi tren penggunaan sepeda tidak disertakan dalam gambar tersebut.")
elif selected_year == 2012:
    st.write("Gambar tersebut merupakan grafik garis yang menampilkan rata-rata penggunaan sepeda harian dari sistem berbagi sepeda selama tahun 2012. Dari grafik tersebut, terlihat bahwa penggunaan sepeda cenderung meningkat pada bulan-bulan musim panas dan menurun pada bulan-bulan musim dingin. Fluktuasi penggunaan sepeda terjadi sepanjang tahun, dipengaruhi oleh faktor-faktor seperti cuaca, musiman, acara khusus, dan ketersediaan sepeda. Analisis lebih lanjut mungkin diperlukan untuk memahami faktor-faktor yang memengaruhi tren penggunaan sepeda tersebut secara lebih mendalam.")
else:
    st.write("Gambar tersebut merupakan grafik garis yang menampilkan rata-rata penggunaan sepeda harian dari sistem berbagi sepeda selama tahun 2012. Dari grafik tersebut, terlihat bahwa penggunaan sepeda cenderung meningkat pada bulan-bulan musim panas dan menurun pada bulan-bulan musim dingin. Fluktuasi penggunaan sepeda terjadi sepanjang tahun, dipengaruhi oleh faktor-faktor seperti cuaca, musiman, acara khusus, dan ketersediaan sepeda. Analisis lebih lanjut mungkin diperlukan untuk memahami faktor-faktor yang memengaruhi tren penggunaan sepeda tersebut secara lebih mendalam.")

# Display data table
st.header("Tabel Data")
st.write(filtered_data)

# Display heatmap for hourly usage
st.header("Peta Panas Penggunaan Sepeda per Jam")
hourly_usage = filtered_data.pivot_table(values='count', index='season', columns='hour')
fig, ax = plt.subplots()
sns.heatmap(hourly_usage, cmap='viridis', ax=ax)
st.pyplot(fig)

st.text("Dibuat oleh: Maulidina Maulani")
