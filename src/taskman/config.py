import os
import json
from pathlib import Path


# Path of the the project root folder
ROOT_FOLDER = Path(__file__).resolve().parents[2]

# JSON file as a database containing the tasks
DB_PATH = ROOT_FOLDER / "tasks.json"

# Positional arguments for the CLI tool
COMMANDS = {
    "add": {
        "help": "Add a new task.",
        "args": {
            "description": {
                "help": "The description of the task you want to add.",
                "type": str
            }
        }
    },
    "update": {
        "help": "Update the description of an existing task.",
        "args": {
            "id": {
                "help": "The ID of the task to update.",
                "type": int
            },
            "description": {
                "help": "The new description for the task.",
                "type": str
            }
        }
    },
    "delete": {
        "help": "Delete the task at the specified ID.",
        "args": {
            "id": {
                "help": "The ID of the task to delete.",
                "type": int
            }
        }
    },
    "mark-in-progress": {
        "help": "Mark the task at the specified ID as \"in progress\".",
        "args": {
            "id": {
                "help": "The ID of the task to mark as \"in progress\".",
                "type": int
            }
        }
    },
    "mark-done": {
        "help": "Mark the task at the specified ID as \"done\".",
        "args": {
            "id": {
                "help": "The ID of the task to mark as \"done\".",
                "type": int
            }
        }
    },
    "list": {
        "help": "Lists all tasks (filter by status).",
        "args": {
            "--status": {
                "help": "The ID of the task to mark as \"done\".",
                "type": str.lower,
                "choices": ["done", "todo", "in-progress"],
                "default": "all"
            }
        }
    }
}

# JSON schema for validating the JSON file
DB_SCHEMA = {
    "type": "object",
    "properties": {
        "tasks": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "id",
                    "description",
                    "status",
                    "createdAt",
                    "updatedAt"
                ],
                "properties": {
                    "id": {
                        "type": "integer",
                        "minimum": 1
                    },
                    "description": {
                        "type": "string"
                    },
                    "status": {
                        "type": "string",
                        "enum": [
                            "done",
                            "todo",
                            "in-progress"
                        ],
                        "default": "todo"
                    },
                    "createdAt": {
                        "type": "string"
                    },
                    "updatedAt": {
                        "type": "string"
                    },
                    "additionalProperties": False
                }
            }
        },
        "additionalProperties": False
    }
}
