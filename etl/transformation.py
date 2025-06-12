import pandas as pd

def clean_event_data(df):
    df = df[df['type.name'].notna()]  # Remove rows with no event type
    df.fillna({'pass.outcome.name': 'Complete'}, inplace=True)
    return df

def calculate_kpis(df):
    kpis = {}

    # Passing Accuracy (per team)
    passes = df[df['type.name'] == 'Pass']
    total_passes = passes.groupby('team.name').size()
    completed_passes = passes[passes['pass.outcome.name'] == 'Complete'].groupby('team.name').size()
    kpis['passing_accuracy'] = (completed_passes / total_passes * 100).round(2).fillna(0)

    # Shot Conversion
    shots = df[df['type.name'] == 'Shot']
    total_shots = shots.groupby('team.name').size()
    goals = shots[shots['shot.outcome.name'] == 'Goal'].groupby('team.name').size()
    kpis['shot_conversion'] = (goals / total_shots * 100).round(2).fillna(0)

    # Possession estimation: count continuous events from same team
    df['team_shift'] = df['team.name'].ne(df['team.name'].shift())
    df['possession_id'] = df['team_shift'].cumsum()
    possession_counts = df.groupby(['team.name', 'possession_id']).size().reset_index()
    possession_counts = possession_counts.groupby('team.name').size()
    kpis['possession_count'] = possession_counts
    return kpis
