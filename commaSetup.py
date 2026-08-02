import ollama


def fix_punctuation(text_from_user):
    model_name = 'llama3.2:3b'

    system_prompt = (
        "You are a tool for correcting punctuation and spelling in Russian text."
        "Your only task is to place missing commas, periods, and other punctuation marks, and capitalize letters where needed"
        "DO NOT change words, DO NOT edit style, DO NOT add any comments, greetings, or explanations. Do not translate the text."
        "Output ONLY the corrected text and nothing else."
    )

    response = ollama.chat(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text_from_user}
        ],
        options={
            "temperature": 0.1  # limited the temperature
        }
    )



    return response['message']['content'].strip()