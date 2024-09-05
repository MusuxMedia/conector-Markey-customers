from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MARKEY_URL: str = "https://australQA.markey.com.ar/APIMarkeyV2/obtener"
    MARKEY_TOKEN: str = 'UZN9291llgxWJ93uzilrmantG6t20r0v8kwrihYXmZl1EO8irdhT0gFK0tFAlv3m'
    MARKEY_API_KEY: str = "933ec3bb-91c7-4ca5-bcdd-5220778c0f36"
    CUSTOMERTYPE: int = 829
    NO_CUSTOMERTYPE: int = 799
