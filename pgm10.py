import requests

# Replace with the IP you got from Step 4
WINDOWS_HOST_IP = "172.27.80.1"

response = requests.post(
    f"http://{WINDOWS_HOST_IP}:11434/api/generate",
    json={
        "model": "phi3:mini",
        "prompt": "Explain the A* algorithm briefly.",
        "stream": False
    }
)

print(response.json()["response"])