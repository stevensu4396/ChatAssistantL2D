import openai
openai.api_key = "sk-qwer1234"
openai.api_base = "http://127.0.0.1:8000"
openai.api_version = "2023-05-15"
model_engine = "rwkv"
message = []
def chatgpt(question):
    message.append({"role": "user", "content": question})

    print("user's question: %s" % question)
    # get reply from ChatGPT
    completions = openai.ChatCompletion.create(
        model=model_engine,
        # temperature=1.0,
        # max_tokens=4024,
        # top_p=0.3,
        messages=message
    )
    print("chatgpt resp: %s" % completions)
    message.append({"role": completions.choices[0].message.role, "content": completions.choices[0].message.content})
    return completions.choices[0].message.content