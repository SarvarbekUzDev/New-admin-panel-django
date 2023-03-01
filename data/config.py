from dotenv import load_dotenv, dotenv_values
import os

env = dotenv_values(".env")

# env data
COOKIE = env.get("COOKIE")


def read_env():
	# refresh .env
	env = dotenv_values(".env")

	data = {
		'ADMIN':env.get("ADMIN"), 
		'PASSWORD':env.get("PASSWORD"),
		'COOKIE':env.get("COOKIE")
		}
	
	return data