import openai  # pip install openai
import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx4  # pip install pyttsx4
import configparser
import json
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')

# Key da openai para utilizar o chatgpt
openai.api_key = config.get('openai', 'api_key')

noKeyWord = False
chat_input = False

# user settings
username = "Aluno"
context = """Você é meu assistente virtual chamado MecChat, você foi desenvolvido pelo laboratório de tecnologia da empresa Mecânica Total Brasil, baseado em uma tecnologia proprietária e é um assistente de suporte técnico especializado em serviços 
    e ferramentas de mecânica industrial, hidraulica industrial, vulcanização industrial, lubrificação industrial. Responda de forma objetiva e clara sempre que possível.
    Não responda a absolutamente nada que não tenha conexão ou relação com o contexto industrial, conduza a conversa para o contexto correto.
    Forneça soluções, orientações e sugestões para resolução de problemas."""

if chat_input:
    noKeyWord = True

def generate_answer(prompt):  # cria a instância da api do chatgpt
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Meu nome é {0} e {1}".format(
            username, context)}, {"role": "user", "content": "{0}".format(prompt)}],
        max_tokens=1000,
        temperature=0.5,
    )

    return [response.choices[0].message.content]

def talk(texto):  # função para sintese de voz
    engine.say(texto)
    engine.runAndWait()
    engine.stop()

# variaveis para controlar o reconhecimento de voz
r = sr.Recognizer()
mic = sr.Microphone()

# variaveis de controle de sintese de voz
try:
    engine =  pyttsx4.init() #Padrão selecionado
except:
    engine =  pyttsx4.init('dummy')

# ==================== LISTAGEM DE VOZES  ====================
voices = engine.getProperty('voices')

# ==================== CONFIGURAÇOES DE VOZ  ====================
engine.setProperty('rate', 60)  # velocidade 120 = lento
engine.setProperty("volume", 1.) # Volume da voz 0-1

# ==================== SELEÇÃO DE VOZES  ====================
for i, voice in enumerate(voices):
    if voice.languages == ['pt-BR']:
        engine.setProperty('voice', voices[i].id)
        talk("Olá, sou Méqui-Chét, seu assistente virtual")

while True:
    question = ""

    if chat_input:
        question = input(">  (\"sair\"): ")
    else:
        # start voice recognition
        with mic as source:
            try:
                r.adjust_for_ambient_noise(source)
                print("Escutando..")
                audio = r.listen(source)
                question = r.recognize_google(audio, language="pt-BR")
            except Exception:
                continue

    if question.lower().startswith("assistente") or noKeyWord:
        if ("desligar" in question.lower()):
            talk("Desligando.")
            exit(0)

        print("f'{0}:".format(username), question)

        answer = generate_answer(question)

        # Save the current interaction on memory database (json file)
        with open('logs/memory_data.json', 'r') as f:
            interactions = json.load(f)

        interactions.append({
            'usuario': question,
            'assistente': answer[0]
        })

        with open(f'logs/memory_data.json', 'w') as f:
            json.dump(interactions, f)

        print("f'MecChat > ", answer[0])
        talk(answer[0])
    else:
        print(question)
        continue
