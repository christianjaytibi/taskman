from tabulate import tabulate
from taskman.model import Task
import random


class TaskView:
    MESSAGES__NO_ADDED_TASKS = [
        "You don't have any added task yet.",
        "Look at you, productivity master! The list is clear and the day is yours.",
        "No tasks ahead! Maybe it's time to make some mischief?",
        "Your list is so empty, it's practically a zen garden.",
        "Zero tasks. Infinite possibilities. What's next, genius?"
    ]

    MESSAGES__TASK_ADDED = [
        "Task added. You're on fire!",
        "The to-do list just got cooler.",
        "Added! Because future-you will thank present-you.",
        "Task secured. Time to pretend we're organized!",
        "Just fed your to-do list. It's growing...",
        "The task fairies have received your offering."
    ]

    MESSAGES__TASK_DELETED = [
        "Poof! That task is history.",
        "Task yeeted into the void.",
        "Task deleted. One less thing to worry about!",
        "The to-do gods have accepted your sacrifice.",
        "Task vanished like a magician's rabbit."
    ]

    MESSAGES__TASK_UPDATED = [
        "Nice edit. The to-do list approves.",
        "You just gave that task a makeover.",
        "Update complete. You're clearly the boss.",
        "Refreshed like a cold lemonade on a hot day.",
        "Just a little tweakeroo."
    ]

    MESSAGES__TASK_DONE = [
        "Give yourself a high-five. You earned it!",
        "Another one for the victory pile!",
        "That task didn't stand a chance!",
        "Done and dusted!",
        "Stamp it: DONE."
    ]

    MESSAGES__TASK_IN_PROGRESS = [
        "You've started. Now make it epic!",
        "Putting the 'do' in 'to-do'.",
        "Taking the first bite of the productivity sandwich.",
        "Progress has entered the chat.",
        "You touched it — now you gotta finish it."
    ]

    MESSAGES__TASK_NOT_FOUND = [
        "Oops! This task must've gone on vacation. Try another!",
        "Task not found — maybe it's hiding under your bed?",
        "This task ghosted you — it's nowhere to be seen!",
        "Looks like this task took a day off. Care to create a new one?",
        "We asked the task politely to show itself. It declined.",
    ]

    def display_random_msg(self, choices: list[str], id: int) -> None:
        print(random.choice(choices), f"(ID: {id})")

    def display_task_details(self, task: Task) -> None:
        print(tabulate([task.to_dict()],
              headers="keys", tablefmt="rounded_grid"))

    def list_items(self, data: list[dict[str, str | int]]) -> None:
        """Display a list of tasks in a table format.

        Args:
            data (list[dict[str,str|int]]): data containing list of tasks
        """
        print(tabulate(data, headers="keys",
              tablefmt="rounded_grid") or random.choice(TaskView.MESSAGES__NO_ADDED_TASKS))
