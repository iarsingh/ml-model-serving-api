# ML Model Serving API

Level: 11 — ML engineering

Skills: Python, FastAPI, a versioned weight file

Load `models/house-price-v1.json` and score square feet and bedrooms. A missing feature is rejected. The endpoint does not retrain.

```bash
pip install -r requirements.txt
pytest -q
```
