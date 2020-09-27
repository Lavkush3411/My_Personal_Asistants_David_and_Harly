import pyttsx3
import datetime
import speech_recognition
import wikipedia
import requests, json
import pywhatkit
import webbrowser
def David(str,speed=180):
    david=pyttsx3.init("sapi5")
    devid_voice=david.getProperty("voices")
    david.setProperty("voice",devid_voice[0].id)
    david.setProperty("rate",speed)
    david.say(str)
    david.runAndWait()
def Harly(str,speed=180):
    harly=pyttsx3.init("sapi5")
    harly_voice=harly.getProperty("voices")
    harly.setProperty("voice",harly_voice[1].id)
    harly.setProperty("rate",speed)
    harly.say(str)
    harly.runAndWait()

def user_words_recognizing():
    words = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('listning...')
        words.pause_threshold = 1
        words.energy_threshold = 1000
        a = words.listen(source)
    try:
        print("recognizing....")
        output = words.recognize_google(a, language="en-in")
    except:
        print("Try again..")
        return "None"
    return output
print("hello sir, i am david. Do you want me as you personal assistant.")
David("hello sir, i am david. Do you want me as you personal assistant.")
print("if you want Harly as your personal assistant press any number, else enter any Alphabet")
David("if you want Harly as your personal assistant press any number, else enter any Alphabet")
choose_assitant=input("press any number or Alphabet = ")
def c_a():
    if choose_assitant.isnumeric():
        Harly("hello sir , Thank you for choosing me. I am Harly in your service.")
    elif choose_assitant.isalpha():
        David("Thank you for continuing with me sir.")
    else:
        David("sorry sir you have to run the programme again")
        quit()
def wish():
    hour=datetime.datetime.now().hour
    if choose_assitant.isnumeric():
        if hour>0 and hour<12:
            Harly("Good Morning sir")
        elif hour>=12 and hour<17:
            Harly("Good Afternoon sir")
        else:
            Harly("Good Evening sir")
    elif choose_assitant.isalpha():
        if hour>0 and hour<12:
            David("Good Morning sir")
        elif hour>=12 and hour<17:
            David("Good Afternoon sir")
        else:
            David("Good Evening sir")
if __name__=="__main__" :
    c_a()
    wish()
    if choose_assitant.isnumeric():
        Harly("do you want me to give u top 10 news of today")
        Harly("say yes or no")
        print("yes or no")
        a = user_words_recognizing().lower()
        if "yes" in a:
            web_data=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=191cf1fb38894e32b6df4ee4e7b9d319").text
            web_data=json.loads(web_data)
            web_data=web_data["articles"]
            for data in web_data:
                print(data["title"])
                Harly(data["title"])
                quit = a
                i = 1
                if i < len(web_data):
                    Harly("press q to stop reading or press enter")
                    quit = input().lower()
                    Harly("and the next thing is")
                    if quit == "q":
                        break
                    else:
                        Harly("Okay sir")
                        pass
                i+=1
        else:
            Harly("Okay sir")
            pass
    elif choose_assitant.isalpha():
        David("sir , do You want me to give you top 10 news of today")
        David("say yes or no")
        print("yes or no")
        a=user_words_recognizing().lower()
        if "yes" in a:
            web_data=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=191cf1fb38894e32b6df4ee4e7b9d319").text
            web_data=json.loads(web_data)
            web_data=web_data["articles"]
            quit=a
            i=1
            for data in web_data:
                print(data["title"])
                David(data["title"])
                if i<len(web_data):
                    David("press q to stop reading or press enter")
                    quit=input().lower()
                    David("and the next news is")
                    if quit=="q":
                        David("Okay sir")
                        break
                    else:pass
                i+=1
        else:
            David("Okay sir")
            pass
    if choose_assitant.isnumeric():
        Harly("These are following other things that i can do for you")
        n="i can"
        print(f"{n} send whatsapp message \n {n} play music \n {n} give weather  details \n {n} Wikipedia , Google , youtube anything\n {n} open Gmail, Facebook, Instagram , Twitter \n {n} print tasks that i can do")
        Harly(f"{n} send whatsapp message \n {n} play music \n {n} give weather  details \n {n} Wikipedia Google youtube anything\n {n} open Gmail,Facebook,Instagram,twitter \n {n} print tasks that i can do")
        Harly("I am listning ... ")
    elif choose_assitant.isalpha():
        David("These are following other things that i can do for you")
        n = "i can"
        print(f"{n} send whatsapp message \n {n} play music \n {n} give weather  details \n {n} Wikipedia Google youtube anything\n {n} open Gmail,Facebook,Instagram,twitter \n {n} print tasks that i can do")
        David(f"{n} send whatsapp message \n {n} play music \n {n} give weather  details \n {n} Wikipedia Google youtube anything\n {n} open Gmail,Facebook,Instagram,twitter \n {n} print tasks that i can do")
        David("I am listning ...")
    while True:
        output=user_words_recognizing().lower()
        print(output)
        try:
            if "wikipedia" in output:
                try:
                    if choose_assitant.isnumeric():
                        Harly("Searching in wikipedia")
                        output=output.replace("wikipedia","")
                        print(output)
                        results=wikipedia.summary(output,sentences=2)
                        print(output)
                        Harly(results)
                    elif choose_assitant.isalpha():
                        output=output.replace("wikipedia", "")
                        output=wikipedia.summary(output,sentences=2)
                        print(output)
                        David(output)
                except:
                    David("Sorry did not find anything")
                    pass
            if "youtube" in output:
                try:
                    if choose_assitant.isalpha():
                        David("what do you want to search on youtube")
                        search=user_words_recognizing().lower()
                        webbrowser.open("https://www.youtube.com/results?search_query="+search)
                    elif choose_assitant.isnumeric():
                        Harly("what do you want to search on youtube")
                        search=user_words_recognizing().lower()
                        webbrowser.open("https://www.youtube.com/results?search_query="+search)
                except:
                    Harly("someting went wrong")
                    pass
            elif "google" in output:
                if choose_assitant.isalpha():
                    David("what do you want to search on google")
                    search=user_words_recognizing().lower()
                    webbrowser.open("https://www.google.com/search?q="+search)
                elif choose_assitant.isnumeric():
                    Harly("what do you want to search on google")
                    search=user_words_recognizing().lower()
                    webbrowser.open("https://www.google.com/search?q="+search)
            if "open gmail" in output:
                webbrowser.open("https://mail.google.com/")
            elif "facebook" in output:
                webbrowser.open("https://www.facebook.com/")
            elif "instagram" in output:
                webbrowser.open("https://www.instagram.com/")
            elif "twitter" in output:
                webbrowser.open("https://twitter.com/")
            elif "play music" in output:
                David("what do want to listen")
                top=user_words_recognizing()
                pywhatkit.playonyt(top)
            elif "weather" in output:
                if choose_assitant.isalpha():
                    David("enter the city name for knowing weather")
                    city_name=user_words_recognizing()
                    weather=requests.get("http://api.openweathermap.org/data/2.5/weather?&appid=00817d3ccfafa3c6cc2fc4ec0342fd1a&q="+city_name)
                    weather = json.loads(weather.text)
                    weather_des = weather["weather"][0]["description"]
                    weather_mintemp = weather["main"]["temp_min"]
                    weather_maxtemp = weather["main"]["temp_max"]
                    print(weather_des)
                    David(f"today's weather of {city_name} is {weather_des}")
                    m_t=round(weather_maxtemp - 273.16, 2)
                    print(m_t)
                    David(f"Maximum temperature of today will go around {m_t}")
                    m_m_t=round(weather_mintemp - 273.16, 2)
                    print(m_m_t)
                    David(f"Maximum temperature of today will go around {m_m_t}")
                if choose_assitant.isnumeric():
                    Harly("enter the city name for knowing weather")
                    city_name = user_words_recognizing()
                    weather = requests.get(
                        "http://api.openweathermap.org/data/2.5/weather?&appid=00817d3ccfafa3c6cc2fc4ec0342fd1a&q=" + city_name)
                    weather = json.loads(weather.text)
                    weather_des = weather["weather"][0]["description"]
                    weather_mintemp = weather["main"]["temp_min"]
                    weather_maxtemp = weather["main"]["temp_max"]
                    print(weather_des)
                    Harly(f"today's weather of {city_name} is {weather_des}")
                    m_t = round(weather_maxtemp - 273.16, 2)
                    print(m_t)
                    Harly(f"Maximum temperature of today will go around {m_t}")
                    m_m_t = round(weather_mintemp - 273.16, 2)
                    print(m_m_t)
                    Harly(f"Maximum temperature of today will go around {m_m_t}")
            elif "whatsapp message" in output:
                print("you will need to familier with whatsapp web for sending mssages on whatsapp")
                if choose_assitant.isalpha():
                    David("sir , enter 10 digit mobile  number to whom u want to send message")
                if choose_assitant.isnumeric():
                    Harly("sir , enter 10 digit mobile number to whom u want to send message")
                mo_no=input("Enter mobile number to send message = ")
                if choose_assitant.isalpha():
                    David("say what message should i send ")
                if choose_assitant.isnumeric():
                    Harly("say what message should i send")
                msg=user_words_recognizing()
                if choose_assitant.isalpha():
                    David("Enter time in 24 hour format")
                if choose_assitant.isnumeric():
                    Harly("Enter time in 24 hour format")
                time=input("Time as (hour:minute)".split(":"))
                try:
                    pywhatkit.sendwhatmsg("+91"+mo_no,msg,int(time[0]),int(time[1]))
                except:
                    David("Something went wrong please try again")
                    pass
            elif "None" in output:
                if choose_assitant.isnumeric():
                    Harly("I was not able to hear please try again")
                if choose_assitant.isalpha():
                    David("I was not able to hear please try again")
            elif 'tasks' in output:
                n="I can"
                print(f"{n} send whatsapp message \n {n} play music \n {n} give weather  details \n {n} Wikipedia Google youtube anything\n {n} open Gmail,Facebook,Instagram,twiter \n {n} print tasks that i can do")

            elif 'what u can do' in output:
                n="I can"
                print(f"{n} send whatsapp message \n {n} play music \n {n} give weather  details \n {n} Wikipedia Google youtube anything\n {n} open Gmail,Facebook,Instagram,twiter \n {n} print tasks that i can do")

            elif "exit program" in output:
                Harly("okay sir , Have a good day")
                break
            elif "quit program" in output:
                Harly("okay sir , Have a good day")
                break
            elif "stop program" in output:
                Harly("okay sir , Have a good day")
                break
            elif "close program" in output:
                Harly("okay sir , Have a good day")
                break
        except:
            pass


input("press enter to close window")