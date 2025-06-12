import pandas as pd
import json

def load_event_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return pd.json_normalize(data)
