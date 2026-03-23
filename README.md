<!DOCTYPE html>
<html>
<head>
    <title>AI Chatbot using Transformers</title>
</head>

<body>

<h1>AI Chatbot using HuggingFace Transformers</h1>

<p>
This project is a conversational AI chatbot built using Python, PyTorch, and HuggingFace Transformers.
The goal of this project was to understand how Large Language Models work internally,
how tokens are processed, how generation happens, and how context is managed.
</p>

<hr>

<h2>Architecture Diagram</h2>

<pre>

User Input
   │
   ▼
Tokenizer
   │
   ▼
Token IDs
   │
   ▼
Add Chat History
   │
   ▼
Limit Tokens (512)
   │
   ▼
Transformer Model (DialoGPT / GPT2)
   │
   ▼
Text Generation
   │
   ▼
Decode Tokens
   │
   ▼
Bot Response

</pre>

<hr>

<h2>Token Flow Diagram</h2>

<pre>

Text → Tokenizer → Tokens → Append History → Model → New Tokens → Decoder → Text

Example:

Hello
 ↓
[15496, 995]
 ↓
[history + new tokens]
 ↓
model.generate()
 ↓
[502, 345, 99]
 ↓
"Hi, how are you?"

</pre>

<hr>

<h2>Generation Pipeline</h2>

<pre>

1. User types message
2. Convert to tokens
3. Append previous tokens
4. Trim to max length
5. Create attention mask
6. Generate new tokens
7. Decode only new tokens
8. Print response

</pre>

<hr>

<h2>How Transformer Works</h2>

<p>
Transformer is a neural network architecture used in modern NLP models.
It uses self-attention to understand relationships between words.
</p>

<pre>

Input Tokens
   │
   ▼
Embedding Layer
   │
   ▼
Self Attention
   │
   ▼
Feed Forward Network
   │
   ▼
Multiple Layers
   │
   ▼
Output Probabilities

</pre>

<p>

Key concepts learned:

</p>

<ul>

<li>Self Attention</li>
<li>Multi Head Attention</li>
<li>Positional Encoding</li>
<li>Feed Forward Layers</li>
<li>Layer Normalization</li>

</ul>

<hr>

<h2>How GPT Works Internally</h2>

<pre>

Input Text
   │
   ▼
Tokenizer
   │
   ▼
Token IDs
   │
   ▼
Embedding
   │
   ▼
Transformer Blocks
   │
   ▼
Next Token Prediction
   │
   ▼
Sampling (top_k, top_p, temperature)
   │
   ▼
Generated Text

</pre>

<p>

GPT predicts the next word repeatedly until response is complete.

</p>

<hr>

<h2>Concepts I Understood</h2>

<ul>

<li>Tokenization</li>
<li>Context handling</li>
<li>Token limit</li>
<li>Sampling parameters</li>
<li>Attention mask</li>
<li>Decoding logic</li>
<li>Generation control</li>

</ul>

<hr>

<h2>Problems Faced</h2>

<ul>

<li>attention_mask warning → fixed by mask</li>

<li>Repeated output → fixed by repetition_penalty</li>

<li>Bad responses → tuned temperature</li>

<li>Context overflow → limited to 512</li>

<li>Git push error → fixed branch</li>

<li>Model unstable → optimized parameters</li>

</ul>

<hr>

<h2>Optimizations</h2>

<ul>

<li>max_new_tokens</li>
<li>top_k</li>
<li>top_p</li>
<li>temperature</li>
<li>repetition_penalty</li>
<li>no_repeat_ngram_size</li>
<li>attention_mask</li>

</ul>

<hr>

<h2>Why This Project Is Important For Me</h2>

<p>

This project helped me understand how real AI chat systems work internally.

Instead of using APIs, I learned:

</p>

<ul>

<li>How LLM generates text</li>
<li>How tokens are processed</li>
<li>How transformer works</li>
<li>How GPT predicts next token</li>
<li>How to debug AI errors</li>
<li>How to optimize generation</li>

</ul>

<p>

This gives strong foundation for:

</p>

<ul>

<li>Generative AI</li>
<li>NLP</li>
<li>LLM engineering</li>
<li>AI backend</li>
<li>Model deployment</li>

</ul>

<hr>

<h2>Future Improvements</h2>

<ul>

<li>Mistral / LLaMA</li>
<li>Vector DB memory</li>
<li>API</li>
<li>GUI</li>
<li>Cloud deploy</li>
<li>RAG chatbot</li>

</ul>

<hr>

<h2>Run</h2>

<pre>

pip install -r requirements.txt
python chatbot.py

</pre>

<hr>

<h2>Author</h2>

<p>

Vishesh Singh  
AI / ML / GenAI Learner  
Project built to understand LLM internals

</p>

</body>
</html>
