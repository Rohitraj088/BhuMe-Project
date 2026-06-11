#!/usr/bin/env python3
"""Generate village predictions and combine them into one root predictions.geojson."""
import json
from pathlib import Path
import sys

# Resolve the absolute path to prevent ModuleNotFoundError or FileNotFoundError
root_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(root_dir / 'bhume-starter-kit'))

from bhume import load, write_predictions
from bhume.baseline import best_example_truth_transform

villages = ['Malatavadi', 'Vadnerbhairav']
required_properties = {'plot_number', 'status'}
valid_statuses = {'corrected', 'flagged'}

all_features = []

for village_name in villages:
    village_path = root_dir / village_name
    predictions_path = village_path / 'predictions.geojson'
    print(f'Generating {predictions_path}...')

    # Pass paths as strings to avoid TypeErrors in the underlying library
    village = load(str(village_path))
    predictions = best_example_truth_transform(village)
    write_predictions(str(predictions_path), predictions)

    with predictions_path.open(encoding='utf-8') as f:
        data = json.load(f)

    if data.get('type') != 'FeatureCollection':
        raise ValueError(f'{predictions_path} is not a GeoJSON FeatureCollection')

    features = data.get('features')
    if not isinstance(features, list):
        raise ValueError(f'{predictions_path} is missing a features list')

    for index, feature in enumerate(features, start=1):
        if feature.get('type') != 'Feature':
            raise ValueError(f'{predictions_path} feature {index} is not a GeoJSON Feature')

        properties = feature.get('properties')
        if not isinstance(properties, dict):
            raise ValueError(f'{predictions_path} feature {index} is missing properties')

        missing = required_properties - set(properties)
        if missing:
            raise ValueError(f'{predictions_path} feature {index} is missing {sorted(missing)}')

        status = properties.get('status')
        if status not in valid_statuses:
            raise ValueError(f'{predictions_path} feature {index} has invalid status {status!r}')

        if status == 'corrected':
            confidence = properties.get('confidence')
            if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
                raise ValueError(
                    f'{predictions_path} feature {index} has invalid confidence {confidence!r}'
                )

        feature['properties'] = dict(properties, village=village_name)
        all_features.append(feature)

    print(f'  added {len(features)} features')

# Write combined file at root
combined = {
    'type': 'FeatureCollection',
    'features': all_features
}

combined_path = root_dir / 'predictions.geojson'
with combined_path.open('w', encoding='utf-8') as f:
    json.dump(combined, f, separators=(',', ':'))

print(f'\nCombined {len(all_features)} predictions to {combined_path}')
