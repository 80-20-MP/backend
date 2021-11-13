def process_query(query: str) -> list[str]:
    return query.split()


def normalize_tag(tag: str) -> list[str]:
    return [tag, tag[::-1]]
