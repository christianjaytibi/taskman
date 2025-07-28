from typing import Literal
from taskman.view import TaskView
from taskman.repository import TaskRepository
from taskman.model import Task


class TaskController:
    def __init__(self, view: TaskView, repo: TaskRepository):
        self.view = view
        self.repo = repo

    def add_task(self, task: Task):
        self.repo.add_task(task)
        self.view.display_random_msg(
            TaskView.MESSAGES__TASK_ADDED, task.id)

    def delete_task_by_id(self, id: int) -> None:
        if self.repo.task_exists(id):
            self.repo.delete_task_by_id(id)
            self.view.display_random_msg(TaskView.MESSAGES__TASK_DELETED, id)
        else:
            self.view.display_random_msg(TaskView.MESSAGES__TASK_NOT_FOUND, id)

    def update_task(self, id: int, description: str) -> None:
        if self.repo.task_exists(id):
            self.repo.update_task_by_id(id, description)
            self.view.display_random_msg(TaskView.MESSAGES__TASK_UPDATED, id)
        else:
            self.view.display_random_msg(TaskView.MESSAGES__TASK_NOT_FOUND, id)

    def mark_as_done(self, id: int) -> None:
        if self.repo.task_exists(id):
            self.repo.update_task_by_id(id, status="done")
            self.view.display_random_msg(TaskView.MESSAGES__TASK_DONE, id)
        else:
            self.view.display_random_msg(TaskView.MESSAGES__TASK_NOT_FOUND, id)

    def mark_as_in_progress(self, id: int) -> None:
        if self.repo.task_exists(id):
            self.repo.update_task_by_id(id, status="in-progress")
            self.view.display_random_msg(
                TaskView.MESSAGES__TASK_IN_PROGRESS, id)
        else:
            self.view.display_random_msg(TaskView.MESSAGES__TASK_NOT_FOUND, id)

    def list_tasks(self, status: Literal["todo", "in-progress", "done", "all"] = "all") -> None:
        list_of_tasks = self.repo.get_list_of_tasks(status)
        self.view.list_items(list_of_tasks)
