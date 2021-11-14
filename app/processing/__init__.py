from .pipeline import get_queries


def process_query(query: str) -> list[str]:
    return get_queries(query, 3)


def normalize_tag(tag: str) -> list[str]:
    return [tag, tag[::-1]]
