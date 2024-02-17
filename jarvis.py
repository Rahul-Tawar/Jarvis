import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyjokes
import smtplib

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("User said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error processing the request.")
        return ""

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I'm Jarvis. How can I help you today?")

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def open_website(url):
    webbrowser.open(url)

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def send_email(recipient, subject, body):
    # Configure your email settings here
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email, recipient, message)
    server.quit()

if __name__ == "__main__":
    wish_me()
    while True:
        command = take_command()

        if "time" in command:
            get_time()
        elif "open website" in command:
            website = command.split("open website ")[1]
            open_website(website)
        elif "joke" in command:
            tell_joke()
        elif "send email" in command:
            speak("Who do you want to send the email to?")
            recipient = take_command()
            speak("What is the subject of the email?")
            subject = take_command()
            speak("What should I write in the email?")
            body = take_command()
            send_email(recipient, subject, body)
            speak("Email sent successfully!")
        elif "exit" in command:
            speak("Goodbye!")
            break
