from pydantic import BaseModel
from typing import List


class ConceptOut(BaseModel):
    name: str


class ChapterOut(BaseModel):
    name: str
    concepts: List[ConceptOut]


class TopicOut(BaseModel):
    name: str
    chapters: List[ChapterOut]


class SubjectOut(BaseModel):
    name: str
    topics: List[TopicOut]
