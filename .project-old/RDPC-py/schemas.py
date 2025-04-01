from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Literal


class UserCreator(BaseModel):
    model_config = ConfigDict(
        error_messages={
            "name": "The name must contain at least two names separated by space, and each name must have at least two letters.",
            "email": "The email is mandatory and must be valid.",
            "pswd": "The password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character (@#$%^&*!).",
            "type": "The type value must be one of the following: 'editor', 'author' or 'reviewer'.",
        }
    )

    name: str = Field(..., regex=r"^\b[A-Za-zÀ-ÖØ-öø-ÿ]{2,}\s+[A-Za-zÀ-ÖØ-öø-ÿ]{2,}\b$")
    email: EmailStr = Field(...)
    pswd: str = Field(
        ..., min_length=8, regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*!]).+$"
    )
    type: Literal["editor", "author", "reviewer"]


class ArticleCreator(BaseModel):
    model_config = ConfigDict(
        error_messages={
            "summary_pt": "The text exceeds the 300-word limit. Please reduce the number of words to meet the requirement.",
            "summary_en": "The text exceeds the 300-word limit. Please reduce the number of words to meet the requirement.",
            "summary_es": "The text exceeds the 300-word limit. Please reduce the number of words to meet the requirement.",
            "two_phrase_summary_pt": "The text must contain a maximum of two sentences. Remove extra sentences or adjust the punctuation.",
            "two_phrase_summary_en": "The text must contain a maximum of two sentences. Remove extra sentences or adjust the punctuation.",
            "two_phrase_summary_es": "The text must contain a maximum of two sentences. Remove extra sentences or adjust the punctuation.",
        }
    )

    title_pt: str = Field(..., max_length=150)
    title_en: str = Field(..., max_length=150)
    title_es: str = Field(..., max_length=150)
    summary_pt: str = Field(..., regex=r"^(\S+\s*){1,300}$")
    summary_en: str = Field(..., regex=r"^(\S+\s*){1,300}$")
    summary_es: str = Field(..., regex=r"^(\S+\s*){1,300}$")
    two_phrase_summary_pt: str = Field(..., regex=r"^([^.!?]+[.!?]\s*){1,2}$")
    two_phrase_summary_en: str = Field(..., regex=r"^([^.!?]+[.!?]\s*){1,2}$")
    two_phrase_summary_es: str = Field(..., regex=r"^([^.!?]+[.!?]\s*){1,2}$")
    key_word_pt: str = Field(
        ..., regex=r"^([\wÀ-ÿ-]+(?:\s[\wÀ-ÿ-]+)*(?:,\s*[\wÀ-ÿ-]+(?:\s[\wÀ-ÿ-]+)*)*)?$"
    )
    key_word_en: str = Field(
        ..., regex=r"^([\wÀ-ÿ-]+(?:\s[\wÀ-ÿ-]+)*(?:,\s*[\wÀ-ÿ-]+(?:\s[\wÀ-ÿ-]+)*)*)?$"
    )
    key_word_es: str = Field(
        ..., regex=r"^([\wÀ-ÿ-]+(?:\s[\wÀ-ÿ-]+)*(?:,\s*[\wÀ-ÿ-]+(?:\s[\wÀ-ÿ-]+)*)*)?$"
    )
    full_article_pt: str
    full_article_en: str
    full_article_es: str
    doc_full_article: bytes
