import openai  # pip install openai
import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx4  # pip install pyttsx4
import configparser
import os
import json
import webbrowser
import threading
import pytz
from datetime import datetime

interrupt_speech = False
config = configparser.ConfigParser()
config.read('config.ini')

# Key da openai para utilizar o chatgpt
openai.api_key = config.get('openai', 'api_key')
prompt_default = config.get('prompts', 'default')
<<<<<<< Updated upstream
mic_sensibility = config.get('configs', 'mic_sensibility')
speed_voice = config.get('configs', 'speed_voice')
ia_volume = config.get('configs', 'ia_volume')

def clear_console():
    try:
        os.system("clear")
    except:
        try:
            os.system("cls")
        except:
            pass
=======
username = config.get('user', 'username')
mic_sensibility = int(config.get('configs', 'mic_sensibility'))
speed_voice = int(config.get('configs', 'speed_voice'))
if sistema_operacional.lower() == 'windows':
    speed_voice = speed_voice*3
ia_volume = float(config.get('configs', 'ia_volume'))

# variaveis para controlar o reconhecimento de voz
r = sr.Recognizer()
mic = sr.Microphone()
>>>>>>> Stashed changes

def print_timer():
    # Define o fuso horário de Brasília
    brasilia_tz = pytz.timezone('America/Sao_Paulo')

    # Obtém a hora atual de Brasília
    brasilia_time = datetime.now(brasilia_tz)

    # Formata a hora de Brasília e imprime
    formatted_time = brasilia_time.strftime("%H:%M:%S")
    return("[" + formatted_time + "]")
    
def print_ts_log(text=""):
    # Define o fuso horário de Brasília
    brasilia_tz = pytz.timezone('America/Sao_Paulo')

    # Obtém a hora atual de Brasília
    brasilia_time = datetime.now(brasilia_tz)

    # Formata a hora de Brasília e imprime
    formatted_time = brasilia_time.strftime("%H:%M:%S")
    print("[" + formatted_time + "] " + text)

# variaveis de controle de sintese de voz
try:
    engine =  pyttsx4.init() #Padrão selecionado
except:
    engine =  pyttsx4.init('dummy')

# ==================== LISTAGEM DE VOZES  ====================
voices = engine.getProperty('voices')

# ==================== CONFIGURAÇOES DE VOZ  ====================
engine.setProperty('rate', speed_voice)  # velocidade 120 = lento
engine.setProperty("volume", ia_volume) # Volume da voz 0-1

def talk(texto):  # função para sintese de voz
    global interrupt_speech
    # Verifica se a síntese de voz deve ser interrompida
    if interrupt_speech:
        engine.stop()
        interrupt_speech = False
    else:
        engine.say(texto)
        engine.runAndWait()
        engine.stop()

def wishme():    # função para reconhecer qual momendo do dia, manhã, tarde, noite.
    hour=int(datetime.now().hour)
    if hour>=0 and hour<12:
        talk('Bom dia! ')
    elif hour>=12 and hour<18:   
        talk('Boa tarde! ')
    else:
        talk('Boa noite! ')

# ==================== SELEÇÃO DE VOZES  ====================
for i, voice in enumerate(voices):
    if voice.languages == ['pt-BR'] or voice.name == 'Microsoft Maria Desktop - Portuguese(Brazil)':
        engine.setProperty('voice', voices[i].id)
        print()
        print_ts_log("Olá! Sou seu assistente pessoal")
        talk("Olá")
        wishme()
        talk("Sou seu assistente pessoal")
        break

def clear_console():
    try:
        os.system("clear")
    except:
        pass
    try:
        os.system("cls")
    except:
        pass

clear_console()
print_ts_log('MecChat Voice Assistent 0.1')
print('_________________________________________')

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
        messages=[{"role": "system", "content": "Você esta falando com {0} e {1}".format(
            username, context)}, {"role": "user", "content": "{0}".format(prompt)}],
        max_tokens=1000,
        temperature=0.5,
    )
    return [response.choices[0].message.content]

def navegator(url):
    try:
        webbrowser.get(using='chrome').open(url)
    except:
        try:
            webbrowser.get(using='google-chrome').open(url)
        except:
            webbrowser.open(url)

<<<<<<< Updated upstream
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
engine.setProperty('rate', speed_voice)  # velocidade 120 = lento
engine.setProperty("volume", ia_volume) # Volume da voz 0-1

# ==================== SELEÇÃO DE VOZES  ====================
for i, voice in enumerate(voices):
    if voice.languages == ['pt-BR']:
        engine.setProperty('voice', voices[i].id)
        print()
        print_ts_log("Olá! Sou seu assistente pessoal")
        talk("Olá,")
        wishme()
        talk("Sou seu assistente pessoal")
        break

=======
>>>>>>> Stashed changes
while True:
    question = ""

    if chat_input:
        question = input(f"> {username}: ")
    else:
        # start voice recognition
        with mic as source:
            try:
                r.adjust_for_ambient_noise(source)
                r.energy_threshold = mic_sensibility
                r.pause_threshold = 1
                print("Escutando..")
                audio = r.listen(source)
                question = r.recognize_google(audio, language="pt-BR")
            except Exception:
                continue

    if question.lower().startswith("assistente") or noKeyWord:
        if ("desligar" in question.lower() or "sair" in question.lower()):
            print_ts_log("Desligando..")
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

        elif ("já entendi" in question.lower() or "pode parar" in question.lower()):
            interrupt_speech = True
            print("MecChat > Ok!")
            stop_signal.set()
            talk("Ok!")
            continue
        
        if not chat_input:
            print("{0}:".format(username), question)

        answer = generate_answer(question)

        try:
            # Save the current interaction on memory database (json file)
            with open('logs/memory_data.json', 'r') as f:
                interactions = json.load(f)
        except:
            interactions = []
            pass

        interactions.append({
                'timer': print_timer(),
                'usuario': question,
                'assistente': answer[0]
            })

        with open(f'logs/memory_data.json', 'w') as f:
            json.dump(interactions, f)

        print("MecChat > ", answer[0])
        # talk(answer[0])

        # Salve a resposta atual na variável de controle para interromper
        current_response = answer[0]
        # Inicie uma nova thread para síntese de voz
        response_thread = threading.Thread(target=talk, args=(current_response,))
        response_thread.start()
        stop_signal = threading.Event()

        # Continue a execução do loop
        continue

    else:
        print(question)
        continue
