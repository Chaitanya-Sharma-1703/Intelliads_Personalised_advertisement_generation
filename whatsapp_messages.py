import pywhatkit as pwk

def send_whatsapp_message(to_whom, message):
    pwk.sendwhats_text(to_whom, message)
    print('Whatsapp message sent successfully!')