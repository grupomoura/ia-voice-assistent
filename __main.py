import openai  # pip install openai
import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx4  # pip install pyttsx4
import configparser
import json
import webbrowser
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')

# Key da openai para utilizar o chatgpt
openai.api_key = config.get('openai', 'api_key')
prompt_default = config.get('prompts', 'default')

while True:
    option = input("""\n\nSelecione uma opção:
    1. Conversar digitando
    2. Conversar falando (Microfone)
    Resposta: """)
    if option == "1":
        noKeyWord = True
        chat_input = True
        break
    elif option == "2":
        noKeyWord = False
        chat_input = False
        break
    else:
        print("\n\naOpção inválida!")

# user settings
username = "Aluno"
context = prompt_default

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

def wishme():                                   #for wishyou good morning ,evening and night
    hour=int(datetime.now().hour)
    if hour>=0 and hour<12:
        talk('Bom dia! ')
    elif hour>=12 and hour<18:   
        talk('Boa tarde! ')
    else:
        talk('Boa noite! ')

def navegator(url):
    try:
        webbrowser.get(using='chrome').open(url)
    except:
        try:
            webbrowser.get(using='google-chrome').open(url)
        except:
            webbrowser.open(url)

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
        talk("Olá,")
        wishme()
        talk("Sou seu assistente virtual")
        break

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
        if ("desligar" in question.lower() or "sair" in question.lower()):
            talk("Desligando.")
            exit(0)

        elif ("área do aluno" in question.lower()):
            talk("Ok! Abrindo a área do aluno.")
            navegator("https://app.mecanicatotalacademy.com.br/lessons")
            continue

        elif ("abrir plataforma" in question.lower()):
            talk("Ok! Abrindo a plataforma especialista.")
            navegator("https://app.mecanicatotalacademy.com.br")
            continue

        print("f'{0}:".format(username), question)

        answer = generate_answer(question)

        try:
            # Save the current interaction on memory database (json file)
            with open('logs/memory_data.json', 'r') as f:
                interactions = json.load(f)
        except:
            interactions = []
            pass

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
