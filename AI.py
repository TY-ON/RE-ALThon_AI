import google.generativeai as genai
f = open("API-Key.txt", "r")

genai.configure(api_key=f.read())
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)