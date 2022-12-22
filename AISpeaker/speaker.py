import time, os 
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# 음성 인식 (듣기, STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[크리스]' + text)
        answer(text)
    except sr.UnknownValueError:            # 음성 인식 실패를 대비하기 위한 예외처리 구문
        print('인식 실패')
    except sr.RequestError as e:            # 인터넷 오류 포함 다양한 이유
        print('요청 실패 : {0}' .format(e))   # API Key 오류, 네트워크 단절 등

# 대답
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요? 반갑습니다.'
    elif '날씨' in input_text:
        answer_text = '오늘의 서울 기온은 영하 10도 입니다. 맑은 하늘이 예상됩니다.'
    elif '환율' in input_text:
        answer_text = '원 달러 환율은 1300원 입니다.'
    elif '고마워' in input_text:
        answer_text = '도와드릴 수 있어 영광입니다'
    elif '종료' in input_text:
        answer_text = '다음에도 또 뵙겠습니다'
        stop_listening(wait_for_stop=False) # 더 이상 듣지 않음
    else: 
        answer_text = '다시 한 번 말씀해주시겠어요?'
    speak(answer_text)

# 소리내어 읽기 (TTS)
def speak(text):
    print('[인공지능]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):   # voice.mp3 파일 삭제 (AI가 처음 인사말 하고 생긴 파일을 지워줌)
        os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen) 
# stop_listening(wait_for_stop=False) # 더 이상 듣지 않음

while True:
    time.sleep(0.1)

