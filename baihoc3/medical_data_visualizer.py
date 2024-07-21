
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Nhập dữ liệu
df = pd.read_csv('medical_examination.csv')

# Thêm cột 'overweight'
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# Chuẩn hóa dữ liệu
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    # Tạo DataFrame cho biểu đồ phân loại
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Nhóm và định dạng lại dữ liệu
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size().rename(columns={'size': 'total'})

    # Vẽ biểu đồ phân loại
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    # Làm sạch dữ liệu
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Tính toán ma trận tương quan
    corr = df_heat.corr()

    # Tạo mặt nạ cho tam giác trên
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Thiết lập matplotlib hình ảnh
    fig, ax = plt.subplots(figsize=(10, 8))

    # Vẽ ma trận tương quan bằng seaborn
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', ax=ax, cmap='coolwarm', center=0, vmin=-1, vmax=1)
    
    fig.savefig('heatmap.png')
    return fig
