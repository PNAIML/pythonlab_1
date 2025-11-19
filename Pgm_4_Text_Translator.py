from googletrans import Translator
translator= Translator()
ME= 'posso parlare ingelese. '
OUTPUT=translator.translate( ME,dest='en')
print(OUTPUT)
