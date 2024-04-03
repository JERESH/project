import re
from urllib.parse import urlparse

class FeatureExtractor:
    def __init__(self, url):
        self.url = url

    def extract(self):
        features = {
            'has_https': self.has_https(),
            'has_at_symbol': self.has_at_symbol(),
            'has_dash_or_ip': self.has_dash_or_ip(),
            'url_length': len(self.url),
        }

        return self.determine_phishing(features)

    def has_https(self):
        return 'https' in self.url

    def has_at_symbol(self):
        return '@' in self.url

    def has_dash_or_ip(self):
        # Check for dashes or if the host is an IP address
        parsed_url = urlparse(self.url)
        host = parsed_url.netloc
        return '-' in host or re.match(r'\d+\.\d+\.\d+\.\d+', host)

    def determine_phishing(self, features):
        # Simple rule-based phishing detection
        # Adjust these rules based on your specific requirements
        phishing_score = 0

        if features['has_https']:
            phishing_score += 1

        if features['has_at_symbol']:
            phishing_score += 1

        if features['has_dash_or_ip']:
            phishing_score += 1

        if features['url_length'] > 50:
            phishing_score += 1

        # Threshold for phishing detection (adjust based on your needs)
        threshold = 2

        if phishing_score >= threshold:
            return "Phishing Detected", f"Phishing Score: {phishing_score}/4"
        else:
            return "Not a Phishing URL", f"Phishing Score: {phishing_score}/4"
