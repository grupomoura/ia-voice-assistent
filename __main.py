import openai  # pip install openai
import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3

# Key da openai para utilizar o chatgpt
openai.api_key = "YOUR_API_KEY"

noKeyWord = False
chat_input = False

# user settings
username = "Twilight Moon"
context = "você é meu assistente virtual chamado zeus"

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
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 180)  # velocidade 120 = lento

# ==================== LISTAGEM DE VOZES  ====================
# for i, all_voices in enumerate(voices):
# print(i, all_voices)

# ==================== SELEÇÃO DE VOZES  ====================
voice = 2  # Seleciona a voz do RICARDO IVONA
engine.setProperty('voice', voices[voice].id)

while True:
    question = ""

    if chat_input:
        question = input(">  (\"sair\"): ")
    else:
        # start voice recognition
        with mic as source:
            try:
                r.adjust_for_ambient_noise(source)

                audio = r.listen(source)

                question = r.recognize_google(audio, language="pt-BR")
                print("Listening..")
            except:
                continue

    if question.lower().startswith("zeus") or noKeyWord:
        if ("desligar" in question.lower()):
            talk("Desligando.")
            exit(0)

        print("{0}:".format(username), question)

        answer = generate_answer(question)

        print("Zeus > ", answer[0])
        talk(answer)
    else:
        print("Não entendi..")
