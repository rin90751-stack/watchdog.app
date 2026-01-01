import re
from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = [
    "verify", "password", "login", "security", "update",
    "free", "gift", "bonus", "bank", "account"
]

def is_ip_address(host):
    return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", host) is not None

def check_url(url):
    parsed = urlparse(url)

    host = parsed.netloc.lower()
    path = parsed.path.lower()

    score = 0
    reasons = []

    # 1) IP address instead of domain
    if is_ip_address(host):
        score += 2
        reasons.append("Uses IP address instead of domain")

    # 2) Too many subdomains
    if host.count(".") >= 3:
        score += 1
        reasons.append("Many subdomains")

    # 3) Suspicious keywords
    if any(k in url.lower() for k in SUSPICIOUS_KEYWORDS):
        score += 1
        reasons.append("Contains phishing‑related keywords")

    # 4) HTTP not HTTPS
    if parsed.scheme != "https":
        score += 1
        reasons.append("Not using HTTPS")

    # 5) Very long URL
    if len(url) > 120:
        score += 1
        reasons.append("Unusually long URL")

    if score >= 3:
        verdict = "Likely Phishing"
    elif score == 2:
        verdict = "Suspicious"
    else:
        verdict = "Probably Safe"

    return verdict, reasons