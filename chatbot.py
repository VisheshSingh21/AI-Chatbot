from model_loader import load_model
import torch

tokenizer, model = load_model()

chat_history_ids = None

print("Chatbot ready! Type 'exit' to stop.")

for step in range(1000):

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # encode input
    new_input_ids = tokenizer.encode(
        user_input + tokenizer.eos_token,
        return_tensors="pt"
    )

    # append history correctly
    if chat_history_ids is not None:
        bot_input_ids = torch.cat(
            [chat_history_ids, new_input_ids],
            dim=-1
        )
    else:
        bot_input_ids = new_input_ids

    # limit history (IMPORTANT)
    if bot_input_ids.shape[-1] > 512:
        bot_input_ids = bot_input_ids[:, -512:]

    # generate response
    chat_history_ids = model.generate(
        bot_input_ids,
        max_new_tokens=60,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=40,
        top_p=0.9,
        temperature=0.7,
        repetition_penalty=1.1
    )

    # decode only new tokens
    bot_output = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1]:][0],
        skip_special_tokens=True
    )

    print("Bot:", bot_output)