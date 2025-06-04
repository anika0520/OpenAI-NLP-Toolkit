# GPT-3 NLP Tasks Mini Project

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/OpenAI_Logo.svg/2560px-OpenAI_Logo.svg.png" alt="OpenAI Logo" width="300"/>
</p>

---

## Overview

<p>
This mini project demonstrates the power of OpenAI’s <strong>GPT-3</strong> model to automate various <strong>Natural Language Processing (NLP)</strong> tasks. Using GPT-3’s API, this project generates Python code for common data science tasks, creates resumes from experience paragraphs, formulates interview questions, and summarizes meeting notes — all with minimal manual effort!
</p>

---

## Features

<ul>
  <li>💻 Generate Python code for <strong>Exploratory Data Analysis (EDA)</strong> using <code>pandas</code></li>
  <li>📊 Create data visualizations with <code>matplotlib</code> and <code>seaborn</code></li>
  <li>📝 Convert plain text about your skills & experience into a professional resume</li>
  <li>❓ Automatically generate programming interview questions in your preferred language</li>
  <li>🗒️ Summarize meeting notes into concise action points</li>
</ul>

---

## Technologies Used

<table>
  <tr>
    <td>🐍 Python 3.x</td>
    <td>🤖 OpenAI GPT-3 API (Davinci engine)</td>
    <td>🔐 dotenv for environment variable management</td>
  </tr>
</table>

---

## Getting Started

### Prerequisites

<ul>
  <li>Python 3.6+ installed</li>
  <li>OpenAI API key — <a href="https://platform.openai.com/account/api-keys" target="_blank" rel="noopener noreferrer">Get your API key here</a></li>
</ul>

<h2>Setup</h2>
<pre><code>
git clone https://github.com/yourusername/gpt3-nlp-tasks.git
cd gpt3-nlp-tasks
pip install -r requirements.txt
</code></pre>

<p>Create a <code>.env</code> file in the root folder and add your OpenAI API key:</p>

<pre><code class="language-ini">
OPENAI_API_KEY=your_openai_api_key_here
</code></pre>

<h2>Run the script</h2>
<pre><code>python gpt3_nlp_tasks.py</code></pre>

<h2>Usage</h2>
<p>Inside the script, you will find example functions for each NLP task. Customize the GPT-3 prompts and parameters to suit your specific use case.</p>

<h2>Important Notes</h2>
<ul>
  <li>🔐 Keep your API key secure and <strong>never commit your <code>.env</code> file</strong> to public repositories.</li>
  <li>⚙️ Adjust the <code>temperature</code> and <code>max_tokens</code> parameters to balance creativity and output length.</li>
</ul>

<h2>Contribution</h2>
<p>Feel free to fork this repository, improve the scripts, and open pull requests. Your feedback and suggestions are highly appreciated!</p>

<h2>License</h2>
<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

<h2>Acknowledgements</h2>
<p>Thanks to <a href="https://openai.com/">OpenAI</a> for providing the powerful GPT-3 API.</p>
<p>Inspired by Infosys’ initiatives on AI and Automation.</p>

<h2>About the Author</h2>
<p>👨‍🎓 <strong>Anika Gangwar</strong> — 3rd Year B.Tech CSE Student</p>
<p>📧 <a href="mailto:anikagangwar2005@gmail.com">anikagangwar2005@gmail.com</a> | 🔗 <a href="https://www.linkedin.com/in/anika-gangwar-3a10772b1/">LinkedIn</a> | 🐙 <a href="https://github.com/annahunn20">GitHub</a></p>

<p style="text-align:center;"><em>Empowering automation and AI for the next generation of developers!</em></p>
