import argparse
import time
import os
from utils.logs import logger_instance
from utils.config import Settings
from envia_alerta import SendAlert

class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(
            prog='Sentinel',
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)        
        
        parser.add_argument("--engine",
                            dest="engine",
                            choices=[
                                'leaksentinel',
                            ],
                            help="Informe qual ação que gostaria de executar")
        
        
        logger_instance.info("Inicializando arquivo de cofigurações...")
        self.settings = Settings.from_yaml(os.path.join(os.path.dirname(__file__), 'utils', 'config.yml'))
        args = parser.parse_args()
        Engines(args,self.settings).start()

class Engines:
    def __init__(self, args: object,settings):
        self.args = args
        self.settings= settings
        self.send_alert = SendAlert()
    
    def start(self,):
        if self.args.engine == 'leaksentinel':
            self.leaksentinel()
    
    def leaksentinel(self):
        from leaksentinel import Sentinel
        logger_instance.info("Inicializando Leak Sentinel...")
        sentinel = Sentinel(self.settings.leaked_credentials,self.settings.monitored_credentials)
        alert_data = sentinel.detect_leaked_credentials()
        if alert_data:
            slack_webhooks = [slack_config.webhook_url for slack_config in self.settings.config_slack]
        for webhook_url in slack_webhooks:
            self.send_alert.send_slack_alert(webhook_url, alert_data['slack_data'])
            

Main()