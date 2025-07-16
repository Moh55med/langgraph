import pandas as pd
import matplotlib.pyplot as plt

# Agent 1: Get total number of tourists (2020-2025)
def agent_total_tourists(state):
    df = pd.read_csv('tourism_saudi_2020_2025.csv')
    total = df['total_tourists'].sum()
    print(f"Total tourists (2020-2025): {total}")
    state['df'] = df
    state['total_tourists'] = total
    return state

# Agent 2: Divide into ordinary and religious tourists
def agent_divide_tourists(state):
    df = state['df']
    ordinary = df['ordinary_tourists'].sum()
    religious = df['religious_tourists'].sum()
    print(f"Ordinary tourists: {ordinary}")
    print(f"Religious tourists: {religious}")
    state['ordinary_tourists'] = ordinary
    state['religious_tourists'] = religious
    return state

# Agent 3: Chart by nation (pie chart)
def agent_nation_chart(state):
    df = state['df']
    nation_counts = {}
    for nations in df['top_nations']:
        for pair in nations.split(','):
            name, count = pair.split(':')
            nation_counts[name.strip()] = nation_counts.get(name.strip(), 0) + int(count)
    # Pie chart
    plt.figure(figsize=(7,7))
    plt.pie(list(nation_counts.values()), labels=list(nation_counts.keys()), autopct='%1.1f%%', startangle=140)
    plt.title('Tourists by Nation (2020-2025)')
    plt.savefig('tourists_by_nation.png')
    plt.close()
    print("Saved chart: tourists_by_nation.png")
    state['nation_counts'] = nation_counts
    state['nation_chart'] = 'tourists_by_nation.png'
    return state

# Agent 4: Chart by month (bar chart)
def agent_month_chart(state):
    df = state['df']
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_totals = df.groupby('month')['total_tourists'].sum().reindex(month_order).fillna(0)
    plt.figure(figsize=(10,5))
    month_totals.plot(kind='bar')
    plt.title('Total Tourists by Month (2020-2025)')
    plt.ylabel('Number of Tourists')
    plt.xlabel('Month')
    plt.tight_layout()
    plt.savefig('tourists_by_month.png')
    plt.close()
    print("Saved chart: tourists_by_month.png")
    state['month_chart'] = 'tourists_by_month.png'
    return state 