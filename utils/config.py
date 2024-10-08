import os
from typing import List
from pydantic import BaseModel
import yaml

class EmailConfig(BaseModel):
    from_address: str
    to_address: str
    password: str

class SlackConfig(BaseModel):
    webhook_url: str

class LeakedCredential(BaseModel):
    email: str
    password: str
    source: str

class MonitoredCredential(BaseModel):
    email: str
    password: str

class Settings(BaseModel):
    app_name: str = "Geral"
    config_email: List[EmailConfig]
    config_slack: List[SlackConfig]
    leaked_credentials: List[LeakedCredential]
    monitored_credentials: List[MonitoredCredential]

    @classmethod
    def from_yaml(cls, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return cls(**data)  # Carrega os dados diretamente


