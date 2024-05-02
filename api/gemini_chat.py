import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyAjKBYbaEpuSAszNIZ_gnFwoqgD2q6DjEU"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

def gemini(promt):
    return model.generate_content(promt).text



if __name__ == '__main__':
    result = gemini('What is the best AI chat bot ?')
    print(result)