from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
app = Flask(__name__)

# Load the pre-trained GPT model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.json.get("input_text", "")
    inputs = tokenizer.encode(input_text, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=150,
        num_return_sequences=1,
        no_repeat_ngram_size=2,  # Prevents repeating n-grams
        temperature=0.7,         # Controls randomness: lower is less random
        top_k=50,                # Limits sampling pool to top_k tokens
        top_p=0.95               # Limits sampling pool to top_p cumulative probability
    )
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": text})

if __name__ == '__main__':
    app.run(debug=True)
