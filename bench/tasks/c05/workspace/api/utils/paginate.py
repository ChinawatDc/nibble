def paginate(items, page, size=20):
    """page is 1-based."""
    offset = page * size
    return items[offset:offset + size]
