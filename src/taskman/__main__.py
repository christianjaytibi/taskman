import argparse
from taskman import config
from taskman.controller import TaskController
from taskman.repository import TaskRepository
from taskman.view import TaskView
from taskman.model import Task


def main() -> None:
    args = parse_arguments()

    view = TaskView()
    repository = TaskRepository(config.DB_PATH)
    controller = TaskController(view, repository)

    match args.command:
        case "add":
            controller.add_task(Task(
                id=repository.get_next_id(),
                description=args.description
            ))
        case "delete":
            controller.delete_task_by_id(args.id)
        case "update":
            controller.update_task(args.id, args.description)
        case "mark-in-progress":
            controller.mark_as_in_progress(args.id)
        case "mark-done":
            controller.mark_as_done(args.id)
        case "list":
            controller.list_tasks(status=args.status)


def parse_arguments() -> argparse.Namespace:
    """Parse the arguments in the command line.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(
        prog="taskman",
        description="A CLI tool for tracking and managing your to-do list."
    )

    subparser = parser.add_subparsers(dest="command", required=True)
    for cmd_name, property in config.COMMANDS.items():
        command = subparser.add_parser(cmd_name, help=property["help"])
        for arg, arg_values in property["args"].items():
            command.add_argument(arg, **arg_values)

    return parser.parse_args()


if __name__ == "__main__":
    main()
