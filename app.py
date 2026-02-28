import json
import os
from openai import OpenAI

def run_test():
    print("--- Pipeline Started ---")

    # Load notes to convert into flashcards
    notes_path = "notes.txt"
    if not os.path.exists(notes_path):
        print(f"Error: {notes_path} not found")
        return

    with open(notes_path, "r") as f:
        notes_content = f.read().strip()

    if not notes_content:
        print("Error: notes.txt is empty")
        return

    # Load API key from .env file or environment
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        env_path = os.path.join(os.path.dirname(__file__), ".env")
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, val = line.split("=", 1)
                        if key.strip() == "OPENAI_API_KEY":
                            api_key = val.strip().strip("'\"")
                            break
    if not api_key:
        print("Error: Set OPENAI_API_KEY in .env or your environment")
        return

    client = OpenAI(api_key=api_key)

    # Ask OpenAI to generate flashcards from the notes
    prompt = f"""Convert the following study notes into flashcards. Return a JSON array of objects, each with "question" and "answer" keys. Create 2-5 flashcards that capture the key concepts.

Notes:
{notes_content}

Return ONLY valid JSON, no other text. Example format:
[{{"question": "...", "answer": "..."}}, {{"question": "...", "answer": "..."}}]"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    raw_content = response.choices[0].message.content.strip()

    # Extract JSON (handle markdown code blocks if present)
    if raw_content.startswith("```"):
        raw_content = raw_content.split("```")[1]
        if raw_content.startswith("json"):
            raw_content = raw_content[4:]
        raw_content = raw_content.strip()

    flashcard_data = json.loads(raw_content)

    with open("output.json", "w") as f:
        json.dump(flashcard_data, f, indent=2)

    print(f"Generated {len(flashcard_data)} flashcard(s)")
    print("--- Pipeline Completed ---")

if __name__ == "__main__":
    run_test()
