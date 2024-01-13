import logging
from thefuzz import process
from qa.parse import QuestionItem


logger = logging.getLogger(__name__)


def get_answer(
    query: str, question_items: list[QuestionItem]
) -> tuple[str | None, float]:
    def calculate_score(question_item: QuestionItem) -> float:
        choices = question_item.questions
        res = process.extractOne(query, choices)
        if not res:
            return 0
        score = res[1]
        return score

    scores = list(zip(question_items, map(calculate_score, question_items)))
    logger.debug(scores)

    if not scores:
        return None, 0
    best_match, best_score = sorted(scores, key=lambda s: s[1], reverse=True)[0]
    return best_match.answer, best_score
