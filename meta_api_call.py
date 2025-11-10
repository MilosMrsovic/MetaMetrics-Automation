import requests
import pandas as pd

# Meta access token (hidden for security)
meta_app_token = 'EAARUf***************'

# Ad account ID (hidden for security)
ad_account_id = '914***************'

# Facebook Graph API endpoint
url = f'https://graph.facebook.com/v23.0/{ad_account_id}/insights'

# Parameters sent to Meta API
params = {
    "fields": "campaign_name,impressions,clicks,spend,ctr",
    "level": "campaign",
    "date_preset": "last_7d",
    "access_token": meta_app_token
}

# Make a request to fetch campaign insights
response = requests.get(url, params=params)

if response.status_code == 200:
    # Extract data from JSON response
    data = response.json().get('data', [])

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Save results to CSV
    df.to_csv('meta_campaign_insights.csv', index=False)

    print('Data fetched and saved to meta_campaign_insights.csv')
else:
    # If API returns an error
    print(f"Error fetching data: {response.status_code} - {response.text}")
