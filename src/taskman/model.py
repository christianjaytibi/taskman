from __future__ import annotations
from dataclasses import dataclass
from typing import Literal, ClassVar
from datetime import datetime


@dataclass
class Task:
    """Structure that defines a task.
    """
    id: int
    description: str
    status: Literal["todo", "in-progress", "done"] = "todo"
    createdAt: datetime = datetime.now()
    updatedAt: datetime = datetime.now()
    DATETIME_FORMAT: ClassVar[str] = "%b %d, %Y (%a %I:%M %p)"

    def to_dict(self) -> dict:
        """Converts the Task object into a serializable dictionary.

        Returns:
            dict: key-value pairs of the properties from the Task object.
        """
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt.strftime(Task.DATETIME_FORMAT),
            "updatedAt": self.updatedAt.strftime(Task.DATETIME_FORMAT)
        }
