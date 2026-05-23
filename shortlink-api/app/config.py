"""
Configuration Management.

This module handles all application settings using environment variables.
It uses Pydantic for validation and type safety.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    
    Pydantic will automatically:
    - Load values from .env file
    - Validate types (str, int, bool, etc.)
    - Provide default values
    - Raise errors if required values are missing
    """
    
    # Application Settings
    app_name: str = "ShortLink API"
    app_version: str = "0.1.0"
    debug: bool = True
    
    # API Settings
    api_v1_prefix: str = "/api/v1"
    
    # Database Settings
    database_url: str = "postgresql+psycopg2://postgres:changeme@localhost:5432/shortlink_db"
    
    # Security Settings
    secret_key: str = "change-this-to-a-random-string"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # CORS Settings (Cross-Origin Resource Sharing)
    allowed_origins: str = "http://localhost:3000"
    
    # Configure how Pydantic loads settings
    model_config = SettingsConfigDict(
        env_file=".env",           # Load from .env file
        env_file_encoding="utf-8", # File encoding
        case_sensitive=False,      # DATABASE_URL = database_url (flexible)
        extra="ignore"             # Ignore extra variables in .env
    )
    
    def get_allowed_origins_list(self) -> List[str]:
        """
        Convert comma-separated origins string to a list.
        Example: "http://localhost:3000,http://localhost:8000" 
                 -> ["http://localhost:3000", "http://localhost:8000"]
        """
        return [origin.strip() for origin in self.allowed_origins.split(",")]


# Create a single instance of settings
# This will be imported throughout the application
settings = Settings()


# Print loaded settings (for debugging - remove in production!)
if __name__ == "__main__":
    print("🔧 Configuration Loaded:")
    print(f"  App Name: {settings.app_name}")
    print(f"  Version: {settings.app_version}")
    print(f"  Debug Mode: {settings.debug}")
    print(f"  API Prefix: {settings.api_v1_prefix}")
    print(f"  Database URL: {settings.database_url[:30]}...")  # Don't print full URL!
    print(f"  Allowed Origins: {settings.get_allowed_origins_list()}")