from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MARKEY_URL: str = "https://vita.hospitalAustral.edu.ar/APIMarkeyV2/obtener"
    MARKEY_TOKEN: str = 'UZN9291llgxWJ93uzilrmantG6t20r0v8kwrihYXmZl1EO8irdhT0g54ddaq224jiii8'
    MARKEY_API_KEY: str = "c9fb5c39-d119-49af-8c2a-00cf71208d0a"
    CUSTOMERTYPE: int = 829
    NO_CUSTOMERTYPE: int = 799
