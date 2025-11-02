"""
LLM Reasoner module for generating natural language responses about hospital appointments.
"""
import json
import subprocess
import logging
from config import LLM_CONFIG
from typing import Optional

class LLMReasoner:
    """Handles LLM-based response generation with error handling and retries."""
    
    def __init__(self):
        """Initialize the LLM reasoner with configuration."""
        self.config = LLM_CONFIG
        self.setup_logging()
    
    def setup_logging(self):
        """Configure logging for the module."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def _run_ollama(self, prompt: str, retry_count: int = 0) -> Optional[str]:
        """Run Ollama with retry mechanism."""
        try:
            result = subprocess.run(
                ["ollama", "run", self.config["model"], prompt],
                capture_output=True,
                timeout=30
            )
            return result.stdout.decode("utf-8", errors="ignore").strip()
        except subprocess.TimeoutExpired:
            if retry_count < 2:
                logging.warning(f"Ollama timeout, retrying ({retry_count + 1}/3)...")
                return self._run_ollama(prompt, retry_count + 1)
            else:
                logging.error("Ollama timeout after 3 attempts")
                return None
        except Exception as e:
            logging.error(f"Error running Ollama: {str(e)}")
            return None

    def generate_response(self, entities: dict, question: str = None) -> str:
        """Generate a response using the LLM based on provided entities."""
        try:
            prompt = self.config["prompt_template"].format(
                entities=json.dumps(entities, indent=2)
            )
            
            response = self._run_ollama(prompt)
            
            if not response:
                return "I apologize, but I couldn't generate a response at this time."
            
            return response.strip()
        except Exception as e:
            logging.error(f"Error generating response: {str(e)}")
            return f"Error generating response: {str(e)}"

# Create a singleton instance
llm_reasoner = LLMReasoner()

def generating_response(entities: dict, question: str) -> str:
    """Generate a response about a hospital appointment using the provided entities."""
    return llm_reasoner.generate_response(entities, question)

if __name__ == "__main__":
    # Example test data
    test_entities = {
        "PATIENT": "John Doe",
        "DOCTOR": "Dr. Smith",
        "DEPARTMENT": "Cardiology",
        "DATE": "02-Nov-2025",
        "TIME": "10:30 AM",
        "HOSPITAL": "CityCare Hospital",
        "TOKEN": "14"
    }
    question = "Create a short summary of the patient's appointment."
    print("\n🤖 Testing LLM Reasoner...\n")
    result = generating_response(test_entities, question)
    print("Generated Response:\n", result)