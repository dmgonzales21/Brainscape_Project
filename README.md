AI Flashcard Migration & Validation Engine
Project Overview
This is a specialized Python utility developed to streamline the migration of unstructured educational notes into high-fidelity, "atomic" flashcard datasets. The engine uses GPT-4o-mini to transform raw text into structured JSON arrays, adhering to specific pedagogical standards required for digital active-recall platforms.

Core Features
Atomic Design Enforcement: The system prompt is engineered to ensure each flashcard covers exactly one discrete concept to optimize cognitive load.

Automated JSON Formatting: Bridges the gap between natural language notes and machine-readable data structures.

Contextual Ingestion: Reads directly from local .txt files, allowing for bulk processing of complex subject matter (e.g., Legal Writing, Humanities, or Linguistics).

Validation Ready: Outputs standardized JSON schemas ready for import into platforms like Brainscape or Anki.

Technical Stack
IDE: Cursor (AI-Native Development)

Language: Python 3.x

API: OpenAI (GPT-4o-mini)

Version Control: Git / GitHub

How to Use
Prepare Notes: Place your raw study notes into notes.txt.

Set API Key: Ensure your OpenAI API key is configured in app.py.

Execute Pipeline: Run the command python3 app.py in your terminal.

Review Output: The validated flashcards will appear in output.json.

Pedagogical Philosophy
This tool is built on the Minimum Redundancy Principle. By treating the Prompt Layer and the Logic Layer as distinct entities, the engine allows for rapid iteration of "learning personas" without altering the underlying data pipeline.

Author: Darrin Gonzales
Role: Linguistic Architect & AI Prompt Engineer
