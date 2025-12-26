import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

sheets = pd.read_excel("UserUsageData.xlsx", sheet_name=None)
app_items = list(sheets.items())

colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

fig, axes = plt.subplots(2, 2, figsize=(18, 12))
axes = axes.flatten()

for i, (app_name, df) in enumerate(app_items):
    ax = axes[i]
    
    df['Hour_dt'] = pd.to_datetime(df['Hour'].astype(str))
    df['Time_12hr'] = df['Hour_dt'].dt.strftime('%I:%M %p').str.lstrip('0')
    
    peak_row = df.loc[df['Active Users (Millions)'].idxmax()]
    
    sns.lineplot(
        x='Time_12hr',
        y='Active Users (Millions)',
        data=df,
        marker='o',
        ax=ax,
        color=colors[i % len(colors)]
    )
    
    ax.scatter(
        peak_row['Time_12hr'],
        peak_row['Active Users (Millions)'],
        s=140,
        color=colors[i % len(colors)],
        zorder=5
    )
    
    ax.annotate(
        f"Peak Usage\n{peak_row['Time_12hr']}",
        xy=(peak_row['Time_12hr'], peak_row['Active Users (Millions)']),
        xytext=(0, 14),
        textcoords='offset points',
        ha='center',
        fontsize=9,
        fontweight='bold'
    )
    
    ax.set_title(app_name, fontsize=12, fontweight='bold')
    ax.set_xlabel("Time of Day")
    ax.set_ylabel("Active Users (Millions)")
    ax.tick_params(axis='x', rotation=45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

for j in range(i + 1, 4):
    axes[j].axis('off')

fig.suptitle(
    "Social Media Usage Time – Hourly Format",
    fontsize=20,
    fontweight='bold'
)

plt.subplots_adjust(hspace=0.45, wspace=0.25)
plt.show()
