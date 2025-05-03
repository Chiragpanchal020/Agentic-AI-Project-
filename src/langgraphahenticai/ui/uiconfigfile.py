import os
from configparser import ConfigParser

class Config:
    def __init__(self, config_file=None):
        base_path = os.path.dirname(os.path.abspath(__file__))  # path to uiconfigfile.py
        config_file = config_file or os.path.join(base_path, "uiconfigfile.ini")

        self.config = ConfigParser()
        files_read = self.config.read(config_file)
        if not files_read:
            raise FileNotFoundError(f"❌ Config file not found: {config_file}")


    def _get_list(self, key):
        value = self.config["DEFAULT"].get(key)
        if not value:
            return []
        return [item.strip() for item in value.split(",")]

    def get_llm_options(self):
        return self._get_list("LLM_OPTIONS")

    def get_usecase_options(self):
        return self._get_list("USECASE_OPTIONS")

    def get_groq_model_options(self):
        return self._get_list("GROQ_MODEL_OPTIONS")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE") or "Untitled"



