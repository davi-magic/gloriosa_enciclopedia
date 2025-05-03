def transform_data(rows):
    transformed_data = []
    
    for row in rows:
        player = row[0]
        goals = int(row[1]) if row[1].isdigit() else 0
        assists = int(row[2]) if row[2].isdigit() else 0
        participations = goals + assists
        
        transformed_data.append({
            'player': player,
            'goals': goals,
            'assists': assists,
            'participations': participations
        })
    
    return transformed_data
