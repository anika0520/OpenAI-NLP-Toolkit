# GPT-3/4 NLP & Code Tasks Mini Project

<p align="center">
  <img src="banner.png" alt="GPT-3 NLP Tasks Banner" width="80%">
</p>

---

## Overview

<p>
This mini project demonstrates the power of OpenAI’s <strong>GPT-4</strong> model to automate a variety of <strong>Natural Language Processing (NLP)</strong> and data science tasks. Using the OpenAI API, this project generates Python code, creates resumes from experience paragraphs, formulates interview questions, and summarizes meeting notes — all with minimal manual effort — via an <strong>interactive Streamlit web interface</strong>!
</p>

---

## Features

<ul>
  <li>💻 Generate Python code for <strong>Exploratory Data Analysis (EDA)</strong> using <code>pandas</code> and <code>matplotlib</code></li>
  <li>📊 Create data visualizations with <code>matplotlib</code> and <code>seaborn</code></li>
  <li>📝 Convert plain text about your skills & experience into a professional resume summary</li>
  <li>❓ Automatically generate programming interview questions in your preferred language</li>
  <li>🗒️ Summarize meeting notes into concise action points</li>
  <li>🌐 Interactive Streamlit web UI, works locally or on Google Colab with ngrok</li>
</ul>

---

## Technologies Used

<table>
  <tr>
    <td>🐍 Python 3.x</td>
    <td>🤖 OpenAI GPT-4 / GPT-4o-mini API</td>
    <td>🔐 python-dotenv for environment variable management</td>
  </tr>
  <tr>
    <td>📊 pandas, matplotlib, seaborn</td>
    <td>🌐 Streamlit</td>
    <td>🔗 pyngrok (Colab hosting)</td>
  </tr>
</table>

---

## Getting Started

### Prerequisites

<ul>
  <li>Python 3.6+ installed</li>
  <li>OpenAI API key — <a href="https://platform.openai.com/account/api-keys" target="_blank" rel="noopener noreferrer">Get your API key here</a></li>
  <li>ngrok AuthToken (for running on Google Colab) — <a href="https://dashboard.ngrok.com/get-started/your-authtoken" target="_blank" rel="noopener noreferrer">Get your ngrok AuthToken</a></li>
</ul>

### Setup

<pre><code>
git clone https://github.com/annahunn20/gpt3-nlp-tasks.git
cd gpt3-nlp-tasks
pip install -r requirements.txt
</code></pre>

<p>Create a <code>.env</code> file in the root folder and add your OpenAI API key:</p>

<pre><code class="language-ini">
OPENAI_API_KEY=your_openai_api_key_here
</code></pre>

---

### Run Locally

<pre><code>streamlit run app.py</code></pre>

---

### Run on Google Colab

<ol>
  <li>Install dependencies:
<pre><code>!pip install openai streamlit pyngrok python-dotenv</code></pre>
  </li>
  <li>Set your OpenAI API key:
<pre><code>import os
os.environ["OPENAI_API_KEY"] = "YOUR_REAL_OPENAI_KEY"</code></pre>
  </li>
  <li>Configure ngrok auth token:
<pre><code>from pyngrok import ngrok
!ngrok config add-authtoken "YOUR_NGROK_AUTH_TOKEN"</code></pre>
  </li>
  <li>Run the Streamlit app and get a public URL:
<pre><code>!streamlit run app.py &>/dev/null &
url = ngrok.connect(8501)
print("Streamlit App URL:", url)</code></pre>
  </li>
</ol>

<p>Click the generated URL to open the interactive app.</p>

---

## Usage

<ul>
  <li>Select a task from the sidebar in the Streamlit app.</li>
  <li>Provide input where required (paragraphs, notes, or parameters).</li>
  <li>Click "Generate" to get results instantly.</li>
  <li>Optionally, download the outputs (code as <code>.py</code>, summaries as <code>.txt</code>).</li>
</ul>

---

## Important Notes

<ul>
  <li>🔐 Keep your API key secure. <strong>Never commit your <code>.env</code> file</strong> to public repositories.</li>
  <li>⚙️ Adjust <code>temperature</code> and <code>max_tokens</code> in the script for creativity vs length.</li>
  <li>💡 Streamlit + ngrok is intended for development/demo purposes. For production, deploy on Streamlit Cloud or Hugging Face Spaces.</li>
</ul>

---

## Contribution

<p>Feel free to fork this repository, improve the scripts, or add new AI tasks. Pull requests and suggestions are highly appreciated!</p>

---

## License

<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

---

## Acknowledgements

<p>Thanks to <a href="https://openai.com/">OpenAI</a> for providing powerful GPT APIs.</p>
<p>Inspired by Infosys’ initiatives on AI and Automation.</p>

---

## About the Author

<p>👩‍🎓 <strong>Anika Gangwar</strong> — 3rd Year B.Tech CSE Student</p>
<p>📧 <a href="mailto:anikagangwar2005@gmail.com">anikagangwar2005@gmail.com</a> | 🔗 <a href="https://www.linkedin.com/in/anika-gangwar-3a10772b1/">LinkedIn</a> | 🐙 <a href="https://github.com/anika0520">GitHub</a></p>

<p style="text-align:center;"><em>Empowering automation and AI for the next generation of developers!</em></p>

---

