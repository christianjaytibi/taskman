import json
import jsonschema
from taskman import config
from taskman.model import Task
from datetime import datetime
from pathlib import Path
from typing import Literal


class TaskRepository:
    def __init__(self, db_path: Path | str) -> None:
        self.db_path = db_path

        if isinstance(self.db_path, str):
            self.db_path = Path(self.db_path)

        if not self.db_path.exists():
            with open(self.db_path, "w", encoding="utf-8") as file:
                json.dump({"tasks": []}, file, indent=2)

        self.data = self.load()
        self.tasks = self.data["tasks"]

    def load(self) -> dict[str, list[dict[str, str | int]]]:
        """Loads the content of the JSON file where the tasks are stored.

        Returns:
            dict[str,list[dict[str,str|int]]]: the "tasks" property is set to an empty list if the JSON file does not fit the schema.
        """
        with open(self.db_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        try:
            jsonschema.validate(data, config.DB_SCHEMA)
        except jsonschema.ValidationError:
            data = {"tasks": []}

        return data

    def add_task(self, task: Task) -> None:
        """Add a new task to the database.

        Args:
            task (Task): Task object to be added
        """
        self.tasks.append(task.to_dict())
        if task.id != len(self.tasks):
            self.tasks.sort(key=lambda x: x["id"])
        self.save()

    def delete_task_by_id(self, id: int) -> None:
        """Delete the task at the specified ID.

        Args:
            id (int): The ID of the task to delete.
        """
        self.tasks = [
            task for task in self.tasks if task["id"] != id]
        self.save()

    def update_task_by_id(
            self, id: int,
            description: str | None = None,
            status: Literal["todo", "in-progress", "done"] | None = None) -> None:
        """Update the description of an existing task.

        Args:
            id (int): The ID of the task to update.
            description (str | None, optional): The new description for the task. Defaults to None.
            status (Literal[&quot;todo&quot;, &quot;in-progress&quot;, &quot;done&quot;], optional): The new status of the task. Defaults to None.
        """
        for task in self.tasks:
            if task["id"] != id:
                continue

            if description:
                task["description"] = description
            if status:
                task["status"] = status

            task["updatedAt"] = datetime.now().strftime(Task.DATETIME_FORMAT)

        self.save()

    def get_next_id(self) -> int:
        """Get the next id for a new task.

        Returns:
            int: new id
        """
        for index, task in enumerate(self.tasks, start=1):
            if index != task["id"]:
                return index

        return len(self.tasks) + 1

    def get_list_of_tasks(self, status: Literal["todo", "in-progress", "done", "all"] = "all") -> list[dict[str, str | int]]:
        """Retrieve a list of tasks based on status.

        Args:
            status (Literal[&quot;todo&quot;, &quot;in-progress&quot;, &quot;done&quot;], optional): Defaults to "all".

        Returns:
            list[dict[str,str|int]]: list of tasks
        """
        if status == "all":
            return self.tasks
        else:
            return [task for task in self.tasks if task["status"] == status]

    def task_exists(self, id: int) -> bool:
        return any(task["id"] == id for task in self.tasks)

    def save(self) -> None:
        """Save changes to the database.
        """
        self.data["tasks"] = self.tasks
        with open(self.db_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=2)
