<div align="center">
  <img src="utils/assets/Sentinel.png" alt="Sentinel Logo" width="300"/>
</div>

# Sentinel - Leak Detection System

`Sentinel` é um sistema desenvolvido para detectar credenciais vazadas monitorando fontes diversas. O projeto permite o envio de alertas via Slack e e-mail sempre que uma credencial monitorada for encontrada em uma lista de dados vazados.

## Funcionalidades
- Detectar credenciais vazadas em fontes externas.
- Enviar alertas via Slack e/ou e-mail quando uma credencial monitorada for detectada.
- Fácil configuração via arquivo YAML.

## Estrutura do Projeto

```
├── main.py               # Script principal que inicia o sistema
├── leaksentinel.py        # Módulo responsável pela detecção de credenciais vazadas
├── envia_alerta.py        # Módulo responsável pelo envio de alertas
├── utils
│   ├── logs.py            # Configuração do sistema de logging
│   └── config.py          # Classe para carregar as configurações do arquivo YAML
└── config.yml             # Arquivo de configuração (não incluído no repositório)
```

## Instalação e Configuração

1. **Clone o repositório**
    ```bash
    git clone https://github.com/seuusuario/sentinel.git
    cd sentinel
    ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

3. **Instale as dependências**
    Utilize o [Poetry](https://python-poetry.org/) para gerenciar as dependências:
    ```bash
    poetry install
    ```

4. **Configure o arquivo `config.yml`**
    Crie um arquivo `config.yml` dentro da pasta `utils` com as informações de configuração, por exemplo:
    ```yaml
    leaked_credentials:
      - email: "email_vazado@example.com"
        password: "password123"
        source: "dark web"
    
    monitored_credentials:
      - email: "email_monitorado@example.com"

    config_slack:
      - webhook_url: "https://hooks.slack.com/services/SEU_WEBHOOK_URL"
    ```

## Utilização

Para iniciar o sistema de detecção, execute o arquivo `main.py` com o argumento `--engine` para selecionar o tipo de ação que deseja executar. Exemplo:

```bash
python main.py --engine leaksentinel
```

Esse comando inicializa o módulo de detecção de credenciais vazadas.

## Envio de Alertas

O sistema envia alertas automaticamente nas seguintes condições:
- **Slack**: Se o webhook estiver configurado no arquivo `config.yml`.
- **E-mail**: Chame o método `send_email_alert` da classe `SendAlert` com as credenciais apropriadas.

### Exemplo de Alerta no Slack
```json
{
  "text": "🚨 *Alerta de Credenciais Vazadas* 🚨\nE-mail: email_vazado@example.com\nSenha: password123\nFonte: dark web"
}
```

## Logger

O sistema de logs foi configurado para registrar informações detalhadas sobre as operações realizadas, incluindo a validação das credenciais e os alertas enviados.

### Exemplo de Log:
```plaintext
🔎 Validando: email_vazado@example.com - Fonte: dark web
⚠️  Credencial vazada encontrada: email_vazado@example.com - Fonte: dark web
```

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch: `git checkout -b minha-branch`.
3. Faça suas alterações e commit: `git commit -m 'Minha nova feature'`.
4. Envie as alterações: `git push origin minha-branch`.
5. Abra um pull request.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Autor**: [Seu Nome](https://github.com/seuusuario)
