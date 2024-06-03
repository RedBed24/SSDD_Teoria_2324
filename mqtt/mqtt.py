import json
import paho.mqtt.client as mqtt

SERVER = "93.189.90.58"

def callback(client, userdata, message):
    token = message.payload.decode()

    print(f"Received token: {token}")

    client.publish("students",
        json.dumps({
            "token": token,
            "fullname": "Samuel Espejo Gil",
            "identifier": "05735354M"
        })
    )

    # para que sólo obtengamos un un token
    client.disconnect()


def main():
    subscriber = mqtt.Client()
    subscriber.on_message = callback
    subscriber.connect(SERVER)
    subscriber.subscribe('tokens')

    try:
        subscriber.loop_forever()
    except KeyboardInterrupt:
        print("Execution interrupted by the user")

if __name__ == "__main__":
    main()

