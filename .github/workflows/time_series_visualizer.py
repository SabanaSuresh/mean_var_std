import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import the data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# 2. Clean the data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# 3. Draw line plot
def draw_line_plot():
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['value'], color='blue', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.show()

# 4. Draw bar plot
def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Group by year and month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    df_bar = df_bar.reindex(columns=['January', 'February', 'March', 'April', 'May',
                                      'June', 'July', 'August', 'September',
                                      'October', 'November', 'December'])

    plt.figure(figsize=(10, 5))
    df_bar.plot(kind='bar', ax=plt.gca())
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.show()

# 5. Draw box plot
def draw_box_plot():
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month

    plt.figure(figsize=(12, 6))

    # Year-wise box plot
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    # Month-wise box plot
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df_box, order=['January', 'February', 'March', 'April', 'May',
                                                            'June', 'July', 'August', 'September',
                                                            'October', 'November', 'December'])
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    plt.tight_layout()
    plt.savefig('box_plot.png')
    plt.show()

# Run the functions
if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
