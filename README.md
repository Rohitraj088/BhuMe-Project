# BhuMe Boundary Prediction Submission

This repository contains the code, predictions, and AI transcript materials for the BhuMe boundary take-home.

## Run The Method

Install dependencies once from the starter-kit folder:

```bash
cd bhume-starter-kit
uv sync
cd ..
```

From the repository root:

```bash
.\bhume-starter-kit\.venv\Scripts\python.exe generate_combined_predictions.py
```

This regenerates:

- `Malatavadi/predictions.geojson`
- `Vadnerbhairav/predictions.geojson`
- `predictions.geojson`

The method is implemented in:

- `generate_combined_predictions.py`
- `bhume-starter-kit/bhume/baseline.py`

## Approach

The final boundary predictions are generated using an automated method that selects the best all-corrected village-wide transform based on the public example truths. The evaluated methods include:
- **Tuned Global Median Shift**: Evaluates translation adjustments over a local grid based on median offsets.
- **Centroid Affine Transform**: Fits an affine transformation (accounting for mild scale, rotation, and shear) from public truth centroids.

This ensures that the official boundaries are shifted to match the ground truth accurately while remaining robust across both `Malatavadi` and `Vadnerbhairav`.

## Predictions

Village prediction files:

- `Malatavadi/predictions.geojson`
- `Vadnerbhairav/predictions.geojson`

Combined prediction file:

- `predictions.geojson`

Final validated output:

- `4965` total features
- all features marked `corrected`
- CRS `EPSG:4326`

## AI Transcripts

AI transcript materials are in:

- `transcripts/README.md`
- `transcripts/codex-session.md`
- Note: Both Codex and Gemini Code Assist were used during the completion of this task.

## Manual Submission Items

The Google Form still needs:

- GitHub repo URL
- 5-minute video link
- resume upload
- contact details
