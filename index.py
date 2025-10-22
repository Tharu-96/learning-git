from dotenv import load_dotenv as world
import os
world()


url = os.getenv("Project_url")
key = os.getenv("anon_key")
print("URL:",url)
print("key:",key[:10]+"......")