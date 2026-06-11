# Submission Checklist

## 1. Code

Included.

- `generate_combined_predictions.py`
- `bhume-starter-kit/bhume/baseline.py`
- `bhume-starter-kit/quickstart.py`
- `bhume-starter-kit/compare_methods.py`
- `bhume-starter-kit/pyproject.toml`
- `bhume-starter-kit/uv.lock`

Runnable command:

```bash
cd bhume-starter-kit
uv sync
cd ..
.\bhume-starter-kit\.venv\Scripts\python.exe generate_combined_predictions.py
```

## 2. Predictions

Included.

- `Malatavadi/predictions.geojson`
- `Vadnerbhairav/predictions.geojson`
- `predictions.geojson`

Validation summary:

- `4965` total combined features
- `2508` Malatavadi features
- `2457` Vadnerbhairav features
- all `corrected`
- CRS `EPSG:4326`

## 3. AI Transcripts

Included.

- `transcripts/README.md`
- `transcripts/codex-session.md`

Add any external web-chat share links to `transcripts/README.md` if used.

## 4. Video

Manual item.

Record a roughly 5-minute screen video covering:

- what was tried
- what worked
- what broke
- how the final method was chosen
- what would be improved next

Paste the public video link into the Google Form.

## 5. Google Form

Manual item.

Submit:

- name
- email
- phone
- GitHub repo URL
- video link
- resume

