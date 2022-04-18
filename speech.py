import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('speak now')
    audio = r3.listen(source)
if 'edureka' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.edureka.co/'
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)
        try:
            wb.get().open_new(url)
            print("Done")
        except sr.UnknownValueError:
            print('Error')
        except sr.RequestError as e:
            print('failed'.format(e))

elif 'khanacademy' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.khanacademy.org/'
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)
        try:
            wb.get().open_new(url)
            print("Done")
        except sr.UnknownValueError:
            print('Error')
        except sr.RequestError as e:
            print('failed'.format(e))

elif 'outlook' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://outlook.live.com/owa/'
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)
        try:
            wb.get().open_new(url)
            print("Done")
        except sr.UnknownValueError:
            print('Error')
        except sr.RequestError as e:
            print('failed'.format(e))

elif 'youtube' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.youtube.com/'
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)
        try:
            wb.get().open_new(url)
            print("Done")
        except sr.UnknownValueError:
            print('Error')
        except sr.RequestError as e:
            print('failed'.format(e))

elif 'mail' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://mail.google.com/mail/u/0/#inbox'
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)
        try:
            wb.get().open_new(url)
            print("Done")
        except sr.UnknownValueError:
            print('Error')
        except sr.RequestError as e:
            print('failed'.format(e))

elif 'grammarly' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://app.grammarly.com/'
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)
        try:
            wb.get().open_new(url)
            print("Done")
        except sr.UnknownValueError:
            print('Error')
        except sr.RequestError as e:
            print('failed'.format(e))

elif 'slack' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://app.slack.com/client/T02L8AXLZ2L/C02KLTCKX1S/thread/C02KLTCKX1S-1642706405.196800'
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)
        try:
            wb.get().open_new(url)
            print("Done")
        except sr.UnknownValueError:
            print('Error')
        except sr.RequestError as e:
            print('failed'.format(e))

elif 'facebook' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.facebook.com/'
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)
        try:
            wb.get().open_new(url)
            print("Done")
        except sr.UnknownValueError:
            print('Error')
        except sr.RequestError as e:
            print('failed'.format(e))

elif 'LinkedIn' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.linkedin.com/login'
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)
        try:
            wb.get().open_new(url)
            print("Done")
        except sr.UnknownValueError:
            print('Error')
        except sr.RequestError as e:
            print('failed'.format(e))

elif 'Zoom' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://zoom.us/'
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)
        try:
            wb.get().open_new(url)
            print("Done")
        except sr.UnknownValueError:
            print('Error')
        except sr.RequestError as e:
            print('failed'.format(e))

elif 'tesla' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.tesla.com/'
    with sr.Microphone() as source:
        print('Search your query')
        audio = r2.listen(source)
        try:
            wb.get().open_new(url)
            print("Done")
        except sr.UnknownValueError:
            print('Error')
        except sr.RequestError as e:
            print('failed'.format(e))
