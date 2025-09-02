from dataclasses import dataclass


@dataclass
class EmailMeta:
    template_name: str
    subject: str
    cc: list[str] | None = None
    bcc: list[str] | None = None
