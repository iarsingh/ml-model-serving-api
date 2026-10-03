import json
from pathlib import Path

MODEL = json.loads((Path(__file__).resolve().parents[2] / "models" / "house-price-v1.json").read_text())

def predict(features):
    missing = [name for name in MODEL["weights"] if name not in features]
    if missing:
        return None
    price = sum(MODEL["weights"][name] * features[name] for name in MODEL["weights"])
    return {"price": price, "model": MODEL["name"], "version": MODEL["version"]}
