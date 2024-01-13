from pathlib import Path

from pydantic import BaseModel, TypeAdapter


class QuestionItem(BaseModel):
    questions: list[str]
    answer: str


ta = TypeAdapter(list[QuestionItem])


def parse_questions(json_path: Path) -> list[QuestionItem]:
    text = json_path.read_text()
    items = ta.validate_json(text)
    return items
