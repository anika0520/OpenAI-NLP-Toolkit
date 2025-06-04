import os
import openai

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code_for_eda():
    prompt = (
        "Write python code for Exploratory Data Analysis (EDA) using pandas library.\n\n"
        "import pandas as pd\n"
    )
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        temperature=0.3,
        max_tokens=150,
        stop=["#"]
    )
    return response.choices[0].text.strip()

def generate_code_for_visualization():
    prompt = (
        "Write python code for data visualization using matplotlib and seaborn libraries.\n\n"
        "import matplotlib.pyplot as plt\nimport seaborn as sns\n"
    )
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        temperature=0.3,
        max_tokens=150,
        stop=["#"]
    )
    return response.choices[0].text.strip()

def generate_resume(paragraph):
    prompt = (
        f"Generate a professional resume summary from this experience and skillset paragraph:\n\"\"\"\n{paragraph}\n\"\"\"\n\nResume Summary:"
    )
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=150,
        stop=["\n\n"]
    )
    return response.choices[0].text.strip()

def generate_interview_questions(language="Python"):
    prompt = (
        f"Generate a set of interview questions for {language} programming language."
    )
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        stop=["\n\n"]
    )
    return response.choices[0].text.strip()

def generate_meeting_summary(notes):
    prompt = (
        f"Summarize the following meeting notes:\n{notes}\n\nSummary:"
    )
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.3,
        max_tokens=100,
        stop=["\n\n"]
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # Example usage
    
    print("=== EDA Code ===")
    print(generate_code_for_eda())
    print("\n=== Visualization Code ===")
    print(generate_code_for_visualization())
    
    experience = ("I am a 3rd year BTech CSE student skilled in Python, "
                  "machine learning, data analysis, and software development.")
    print("\n=== Resume Summary ===")
    print(generate_resume(experience))
    
    print("\n=== Interview Questions (Python) ===")
    print(generate_interview_questions("Python"))
    
    meeting_notes = """Max: Profits up 50%
Ruby: New servers are online
Kyle: Need more time to fix software
Walker: Happy to help
Parkman: Beta testing almost done"""
    print("\n=== Meeting Summary ===")
    print(generate_meeting_summary(meeting_notes))
