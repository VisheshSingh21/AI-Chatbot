<!DOCTYPE html>
<html>
<head>
   
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
<hr>

<h2>Difficulties Faced During Development</h2>

<p>
While building this chatbot, I faced several practical issues related to
token handling, model generation, warnings, and Git workflow.
Solving these problems helped me understand the internal working of
Transformer-based language models.
</p>

<ul>

<li>
<b>Difficulty 1 — Model giving random / nonsense output</b><br>
Reason: Default generation parameters were not suitable for conversation.<br>
Fix: Tuned temperature, top_k, top_p, and repetition_penalty.<br>
Learning: Text generation quality depends heavily on sampling parameters.
</li>

<br>

<li>
<b>Difficulty 2 — Repeated words in response</b><br>
Reason: Model was generating same tokens again and again.<br>
Fix: Used no_repeat_ngram_size and repetition_penalty.<br>
Learning: GPT models predict next token greedily without constraints.
</li>

<br>

<li>
<b>Difficulty 3 — Warning about attention_mask</b><br>
Reason: pad_token_id and eos_token_id were same.<br>
Fix: Added attention_mask manually.<br>
Learning: Attention mask tells transformer which tokens are valid.
</li>

<br>

<li>
<b>Difficulty 4 — Context length overflow</b><br>
Reason: Chat history kept increasing every turn.<br>
Fix: Limited tokens to 512 using slicing.<br>
Learning: All transformer models have max context length.
</li>

<br>

<li>
<b>Difficulty 5 — Full history printed in output</b><br>
Reason: Decoding entire token sequence.<br>
Fix: Decoded only new tokens after input length.<br>
Learning: Must track input vs generated tokens.
</li>

<br>

<li>
<b>Difficulty 6 — Git push error (refspec main)</b><br>
Reason: Branch not created before push.<br>
Fix: Commit → rename branch → push.<br>
Learning: Git requires commit before pushing.
</li>

<br>

<li>
<b>Difficulty 7 — Model unstable responses</b><br>
Reason: Small model (DialoGPT small) has limited understanding.<br>
Fix: Optimized generation parameters and history handling.<br>
Learning: Model size affects response quality.
</li>

<br>

<li>
<b>Difficulty 8 — Understanding how GPT actually works</b><br>
Reason: Initially treated model as black box.<br>
Fix: Studied tokenization, transformer, attention, sampling.<br>
Learning: LLM engineering requires understanding pipeline.
</li>

</ul>

<hr>

<h2>What This Project Taught Me</h2>

<ul>

<li>How LLM generates text step by step</li>
<li>How tokens are stored in memory</li>
<li>Why context limit matters</li>
<li>How transformer attention works</li>
<li>How to debug AI errors</li>
<li>How to optimize generation</li>
<li>How real chatbots manage history</li>
<li>How to structure AI projects</li>

</ul>

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
