from pathlib import Path

def load_prompt_template(filename: str) -> str:
    """
    Loads a prompt template file from the same directory.
    
    Args:
        filename (str): The name of the prompt file (e.g., 'message_classification.txt')
        
    Returns:
        str: The content of the prompt file as a string.
    """
    current_dir = Path(__file__).parent
    file_path = current_dir / filename
    
    if not file_path.exists():
        raise FileNotFoundError(f"Prompt template '{filename}' not found in {current_dir}")
    
    return file_path.read_text(encoding="utf-8")
