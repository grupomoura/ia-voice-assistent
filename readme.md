# IA - Assistente Virtual para Suporte Técnico

Bem-vindo ao repositório do ADD-ON AI Voice Assistente Virtual Especializado.

## Pré-requisitos

Antes de começar a usar o ADD-ON IA Voice Assistente, certifique-se de que você possui os seguintes pré-requisitos instalados:

- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- Bibliotecas Python: `openai`, `speech_recognition`, `pyttsx4`, `configparser`, `json`, `webbrowser`, `datetime`

Você pode instalar essas bibliotecas usando o `pip`:

```
pip install openai speech_recognition pyttsx4
```

## Configuração

Antes de executar o IA, é necessário configurar o arquivo `config.ini` com a chave da API da OpenAI. Certifique-se de que a chave esteja corretamente configurada no arquivo `config.ini`.

```ini
[openai]
api_key = SUA_CHAVE_DA_API_AQUI
```

## Uso

O IA é um assistente virtual de suporte técnico que pode ser usado de duas maneiras:

### Interface de Linha de Comando

Você pode usar o IA a partir da linha de comando. Para isso, defina a variável `chat_input` como `True` no código e execute o assistente. Você pode iniciar uma conversa digitando perguntas ou comandos diretamente na linha de comando. Para encerrar a conversa, digite "sair".

### Reconhecimento de Voz

O IA também oferece suporte ao reconhecimento de voz. Para usar essa funcionalidade, você precisa de um microfone configurado em seu sistema. Certifique-se de que o microfone esteja funcionando corretamente.

Quando a variável `chat_input` estiver definida como `False`, o IA usará o reconhecimento de voz para ouvir suas perguntas e comandos. Após falar uma pergunta ou comando, o IA fornecerá uma resposta por meio de síntese de voz.

## Comandos de voz Disponíveis

O IA responde a comandos específicos que podem ser ditos em voz alta ou digitados na linha de comando. Alguns comandos úteis incluem:

- "Assistente, "Qualquer coisa que queira perguntar": Isso acionará a resposta direta do ChatGpt com o prompt configurado.
- "Assistente, desligar": Isso encerrará o Assistente IA.
- "Assistente, já entendi": Isso interrompe a resposta do Assistente IA.
- "Assistente, pode parar": Isso interrompe a resposta do Assistente IA.
- "Assistente, abrir área do aluno": Isso abrirá a área do aluno em um navegador.
- "Assistente, abrir plataforma": Isso abrirá a plataforma especialista em um navegador.

## Logs de Conversa

O IA armazena as interações em um arquivo JSON chamado `logs/memory_data.json`. Cada interação entre o usuário e o assistente é registrada nesse arquivo, incluindo a pergunta do usuário e a resposta do assistente.

## Síntese de Voz

O IA é capaz de sintetizar voz para fornecer respostas por meio da biblioteca `pyttsx4`. Você pode configurar a velocidade e o volume da voz no código.

## Notas Adicionais

- O IA usa o modelo de linguagem GPT-3.5-turbo da OpenAI para fornecer respostas às perguntas.
- A linguagem de comunicação padrão é o português do Brasil (pt-BR).
- O IA detecta automaticamente a hora do dia e cumprimenta o usuário apropriadamente (bom dia, boa tarde ou boa noite).

## Contribuições

Agradecemos por usar o IA! Esperamos que ele seja útil para fornecer suporte técnico em sua área de expertise. Se tiver alguma dúvida ou problema, não hesite em entrar em contato conosco.

**Desenvolvido por Mecânica Total Brasil**
Website: [https://www.mecanicatotalbrasil.com.br](https://www.mecanicatotalbrasil.com.br)

**OpenAI - Modelo GPT-3.5-turbo**
Website: [https://openai.com](https://openai.com)

---

*Nota: Este README.md é uma descrição detalhada do projeto ADD-ON IA Voice Assistente e fornece informações sobre como configurar e usar o assistente virtual. Certifique-se de manter as dependências atualizadas e configurar a chave da API da OpenAI antes de usar o IA.*
