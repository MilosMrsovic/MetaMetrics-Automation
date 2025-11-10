import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file containing fake Meta API data
df = pd.read_csv('meta_api_fake_call.csv')

# Convert values to numeric (invalid values become NaN)
df['Impressions'] = pd.to_numeric(df['Impressions'], errors='coerce')
df['Clicks'] = pd.to_numeric(df['Clicks'], errors='coerce')
df['Spend'] = pd.to_numeric(df['Spend'], errors='coerce')
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')

# Calculate campaign performance metrics
df['CTR (%)'] = (df['Clicks'] / df['Impressions']) * 100
df['CPC ($)'] = df['Spend'] / df['Clicks']
df['ROAS'] = df['Revenue'] / df['Spend']

# Create summary grouped by campaign name
campaign_summary = df.groupby('CampaignName').agg({
    'Impressions': 'sum',
    'Clicks': 'sum',
    'Spend': 'sum',
    'Revenue': 'sum'
}).reset_index()

campaign_summary['CTR (%)'] = (campaign_summary['Clicks'] / campaign_summary['Impressions']) * 100
campaign_summary['CPC ($)'] = campaign_summary['Spend'] / campaign_summary['Clicks']
campaign_summary['ROAS'] = campaign_summary['Revenue'] / campaign_summary['Spend']

# Create summary grouped by date
daily_summary = df.groupby('Date').agg({
    'Impressions': 'sum',
    'Clicks': 'sum',
    'Spend': 'sum',
    'Revenue': 'sum'
}).reset_index()

daily_summary['CTR (%)'] = (daily_summary['Clicks'] / daily_summary['Impressions']) * 100
daily_summary['CPC ($)'] = daily_summary['Spend'] / daily_summary['Clicks']
daily_summary['ROAS'] = daily_summary['Revenue'] / daily_summary['Spend']

# Export data into Excel and generate charts
with pd.ExcelWriter('ad_report.xlsx', engine='xlsxwriter') as writer:
    campaign_summary.to_excel(writer, sheet_name='Campaign Summary', index=False)
    daily_summary.to_excel(writer, sheet_name='Daily Summary', index=False)

    workbook = writer.book
    campaign_sheet = writer.sheets['Campaign Summary']
    daily_sheet = writer.sheets['Daily Summary']

    # Chart: Compare spend and revenue for each campaign
    chart1 = workbook.add_chart({'type': 'column'})
    chart1.add_series({
        'name': 'Spend',
        'categories': ['Campaign Summary', 1, 0, len(campaign_summary), 0],
        'values': ['Campaign Summary', 1, 2, len(campaign_summary), 2],
    })
    chart1.add_series({
        'name': 'Revenue',
        'categories': ['Campaign Summary', 1, 0, len(campaign_summary), 0],
        'values': ['Campaign Summary', 1, 3, len(campaign_summary), 3],
    })
    chart1.set_title({'name': 'Spend vs Revenue per Campaign'})
    chart1.set_x_axis({'name': 'Campaign'})
    chart1.set_y_axis({'name': 'USD'})
    campaign_sheet.insert_chart('H2', chart1)

    # Chart: Daily spending trend
    chart2 = workbook.add_chart({'type': 'line'})
    chart2.add_series({
        'name': 'Daily Spend',
        'categories': ['Daily Summary', 1, 0, len(daily_summary), 0],
        'values': ['Daily Summary', 1, 2, len(daily_summary), 2],
    })
    chart2.set_title({'name': 'Daily Spend Trend'})
    chart2.set_x_axis({'name': 'Date'})
    chart2.set_y_axis({'name': 'USD'})
    daily_sheet.insert_chart('H2', chart2)

print("Reports with charts generated successfully")
