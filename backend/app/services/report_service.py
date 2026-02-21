from app.data.campaign_data import campaigns

def generate_report(creator=None, platform=None):
    filtered = campaigns

    if creator:
        filtered = [c for c in filtered if c["content_creator"] == creator]

    if platform:
        filtered = [c for c in filtered if c["platform"] == platform]

    for c in filtered:
        roi = ((c["revenue"] - c["investment"]) / c["investment"]) * 100
        c["roi"] = f"{roi:.2f}%"

    return filtered