from dataclasses import dataclass

@dataclass
class PostElement:
    user_id: int
    id: int
    title: str
    body: str