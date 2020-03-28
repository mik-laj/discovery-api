def md_link(title: str, target: str) -> str:
    return f"[{title}]({target})"


def md_header(title: str) -> str:
    return "\n".join([title, "=" * len(title), ""])
