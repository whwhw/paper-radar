from datetime import date
from typing import Literal

from pydantic import BaseModel, Field, computed_field
from slugify import slugify

Area = Literal["ai", "tech", "health", "cognition", "behavior", "complexity"]


class Paper(BaseModel):
    id: str
    title: str
    authors: list[str]
    abstract: str
    source: str
    url: str
    published: date
    primary_category: str

    @computed_field
    @property
    def slug(self) -> str:
        return slugify(self.title, max_length=60, word_boundary=True)


class Score(BaseModel):
    relevance: float = Field(ge=0, le=10, description="Domain match: AI/health/tech etc.")
    simplicity: float = Field(ge=0, le=10, description="How accessible to non-academic.")
    inspiration: float = Field(ge=0, le=10, description="Cross-domain takeaway potential.")
    reasoning: str = Field(min_length=1, description="Why these scores in 1-2 sentences.")

    @computed_field
    @property
    def total(self) -> float:
        return round(0.4 * self.relevance + 0.3 * self.simplicity + 0.3 * self.inspiration, 2)


class Summary(BaseModel):
    one_line_conclusion: str = Field(max_length=120)
    plain_explanation: str = Field(description="200 字内：背景→方法→发现→意义")
    key_method: str | None = Field(default=None, description="Optional simplified method")
    inspiration_programmer: str
    inspiration_investor: str
    inspiration_creator: str
