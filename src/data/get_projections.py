import src.config

import pandas as pd
import pyswagger.contrib.client.requests
import pprint


config  = src.config.load()


# load Swagger resource file into App object
app = pyswagger.App._create_('https://fantasydata.com/downloads/swagger/nfl-v3-projections.json')

auth = pyswagger.Security(app)

auth.update_with('apiKeyHeader', config['fantasydata']['primary_key']) # api key
auth.update_with('apiKeyQuery', config['fantasydata']['secondary_key']) # api key

# init swagger client
client = pyswagger.contrib.client.requests.Client(auth)

req, resp = app.op['ProjectedFantasyDefenseGameStatsWDfsSalaries'](format='JSON', season='2015REG', week='1')
defense_stats = client.request((req, resp)).data

pprint.pprint(defense_stats)

pd.DataFrame(defense_stats)
