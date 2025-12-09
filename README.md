# Meta Ads Insights Automation

This small Python script automatically connects to the Meta (Facebook) Ads API and pulls campaign data for the last 7 days. It basically grabs all the important stuff like:

- Campaign name
- Impressions (how many times the ad was shown)
- Clicks (how many times someone clicked)
- Spend (how much money was spent)
- CTR (% of clicks)

## What the script does:

- Connects to the Meta API and fetches data from your ad account
- Uses the access token that you put in the script
- Converts everything into a pandas DataFrame
- Finally, saves it all into a file called meta_campaign_insights.csv

## How it works:

1. Put your token and ad account ID into the script (without them, nothing works)
2. The script builds the request URL:
   https://graph.facebook.com/v23.0/<AD_ACCOUNT_ID>/insights
3. You define which fields you want to pull:
   "fields": "campaign_name,impressions,clicks,spend,ctr"
4. Meta API returns the data in JSON format
5. The script converts it into a DataFrame
6. And saves the CSV file, ready for further analysis

## What you need:

- Python libraries:
  pip install requests pandas

## How to run it:

1. Open the script in VS Code, PyCharm, or any IDE
2. Replace the token and account ID with your own
3. Run:
   python meta_ads_export.py
4. Check the folder, there should be a file:
   meta_campaign_insights.csv

## Security notes:

- Don’t share your token with anyone
- Don’t upload it to GitHub
- If you want, you can keep it in a .env file or as an environment variable

## Why it’s useful:

- You don’t have to manually export reports from Meta Ads Manager anymore
- You always get fresh data every time you run the script
- You can also send data to Google Sheets, create charts, or do further analysis

## Extra:

- Right now it pulls data from the last 7 days, but you can change it in the script:
  "date_preset": "last_30d"
