from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
    )
    API_V1_STR: str = "/api/v1"
    

    GROQ_MODEL_NAME: str
    GROQ_API_KEY: str

    VECTARA_AGENTIC_MAIN_LLM_PROVIDER: str
    VECTARA_AGENTIC_AGENT_TYPE: str
    VECTARA_AGENTIC_TOOL_LLM_PROVIDER: str

    


settings = Settings()
