import configparser
from pathlib import Path


class ConfigReader:
    def __init__(self, config_file="playwright/config/settings.ini"):
        self.config = configparser.ConfigParser()

        root_dir = Path(__file__).parents[2]  # adjust if needed
        full_path = root_dir / config_file

        print("CONFIG FULL PATH:", full_path)  # debug
        if not full_path.exists():
            raise FileNotFoundError(f"Config file not found: {full_path}")

        self.config.read(full_path, encoding="utf-8")

        print("CONFIG SECTIONS:", self.config.sections())

    def getUserName(self):
        return self.config["user"]["username"]
    def getBaseUrl(self, ):
        return self.config["environment"]["base_url"]
    def getPassword(self ):
        return self.config["user"]["password"]