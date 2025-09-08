

import requests

def main():
	url = "https://catfact.ninja/fact"
	try:
		response = requests.get(url)
		response.raise_for_status()
		data = response.json()
		print(data.get('fact', 'No fact found.'))
	except Exception as e:
		print(f"Error: {e}")

if __name__ == "__main__":
	main()


