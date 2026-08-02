import ollama

history = []
model = "phi3:latest"

while True:
    prompt = input("You: ").strip()

    if prompt.lower() in ("exit", "bye"):
        print("have a nice day")
        break

    message = {"role": "user", "content": prompt}
    history.append(message)

    response = ollama.chat(model=model, messages=history)

    reply = response["message"]["content"]
    print(f"Bot: {reply}")

    history.append({"role": "assistant", "content": reply})