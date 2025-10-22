import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types



def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    print("Hello from ai-code-agent!")
    script_name = sys.argv[0]
    if '-v' in sys.argv or '--verbose' in sys.argv:
        verbose_mode = True
    else:
        verbose_mode = False
    if len(sys.argv) > 1:
        user_prompt = " ".join(sys.argv[1:])
    else:
        print("Error: No prompt entered")
        sys.exit(1)
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
    response = client.models.generate_content(
    model='gemini-2.0-flash', contents=messages
    )
    print(response.text)
    if verbose_mode == True:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
 

if __name__ == "__main__":
    main()
