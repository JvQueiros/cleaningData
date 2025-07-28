import pandas as pd
import numpy as np
import datetime as dt

# Creating client.csv

df = pd.read_csv('bank_marketing.csv')

dfcl = df[["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]]

dfcl['job'] = dfcl['job'].replace(".", "_")
dfcl['education'] = dfcl['education'].str.replace('.', '_')
dfcl['education'] = dfcl['education'].replace('unknown', np.NaN, regex = False)
dfcl['credit_default'] = dfcl['credit_default'].replace({'no': 0, 'unknown': 0, 'yes': 1}).astype("bool")
dfcl['mortgage'] = dfcl['mortgage'].replace({'no': 0, 'unknown': 0, 'yes': 1}).astype("bool")

dfcl.to_csv('client.csv', index= False)


# Creating campaing.csv

dfc = df[["client_id", "number_contacts", "contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome"]]

dfc["previous_outcome"] = dfc["previous_outcome"].replace({'success': True, 'failure': False, 'nonexistent': False}).astype("bool")
dfc["campaign_outcome"] = dfc["campaign_outcome"].map({'yes': True, 'no': False}).astype("bool")

map_month = {dt.datetime(2022, i, 1).strftime('%b').lower(): i for i in range(1, 13)}

dfc["last_contact_date"] = pd.to_datetime({'year': 2022,
                                             'month': df["month"].map(map_month),
                                             'day': df["day"]})\
                                             .dt.strftime("%Y-%m-%d")

dfc.to_csv('campaign.csv', index= False)


# Creating economics.csv
dfe = df[["client_id", "cons_price_idx", "euribor_three_months"]]

dfe.to_csv('economics.csv', index= False)