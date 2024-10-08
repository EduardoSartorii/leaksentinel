from utils.logs import logger_instance

class Sentinel:
    def __init__(self,leaked_data,monitored_data):
        self.leaked_data = leaked_data
        self.monitored_data = monitored_data

    def detect_leaked_credentials(self):
        for leaked in self.leaked_data:
            for monitored in self.monitored_data:
                logger_instance.info(f"🔎Validando: {leaked.email} - Fonte: {leaked.source} ")                
                if leaked.email == monitored.email:
                    logger_instance.warning(f"Credencial vazada encontrada: {leaked.email} - Fonte: {leaked.source}")                    
                    slack_data = {
                    'text': f"🚨 *Alerta de Credencial Vazadas* 🚨\nE-mail: {leaked.email}\nSenha: {leaked.password}\nFonte: {leaked.source}"
                    }
                    return {
                        'leaked': leaked,
                        'slack_data': slack_data,
                    }                
        return None
                    