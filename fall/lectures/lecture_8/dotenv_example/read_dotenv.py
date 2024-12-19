# .env файл не надо закидывать в гитхаб
# здесь это сделано в образовательных целях

from dotenv import load_dotenv
import os
import pathlib


dotenv_path = pathlib.Path(".").absolute().parent / ".env"



if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    raise FileNotFoundError


api_token = os.getenv("API_TOKEN")
secret_key = os.getenv("SECRET_KEY")
print(f"API Token: {api_token}")
print(f"Secret Key: {secret_key}")