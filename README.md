# taskman

## Description

A simple CLI tool for tracking and managing your to-do list. This is a sample solution for the [Task Tracker project on **roadmap.sh**](https://roadmap.sh/projects/task-tracker). The tasks are stored in a JSON file.

## Key Features

- **Add a Task**
- **Update the Description of a Task**
- **Mark a Task** as _"in progress"_ or _"done"_
- **List all Tasks**
  - status-based filter:
    - todo
    - in-progress
    - done
    - all (default)
- **Delete a Task by ID**

## Usage

- **Add a task**

  - Sample command:
    ```bash
    $ taskman add "Clean my workplace."
    ```
  - Sample output:
    ```
    The task fairies have received your offering. (ID: 1)
    ```

- **Update a task**

  - Sample command:
    ```bash
    $ taskman update 1 "Study for at least 3 hours."
    ```
  - Sample output:
    ```
    Refreshed like a cold lemonade on a hot day. (ID: 1)
    ```

- **Mark a task as _"in progress"_.**

  - Sample command
    ```bash
    $ taskman mark-in-progress 1
    ```
  - Sample output
    ```
    Putting the 'do' in 'to-do'. (ID: 1)
    ```

- **Mark a task as _"done"_.**

  - Sample command:
    ```bash
    $ taskman mark-done 1
    ```
  - Sample output:
    ```
    Give yourself a high-five. You earned it! (ID: 1)
    ```

- **List tasks**
  - Sample command:
    ```bash
    $ taskman list --status done
    ```
  - Sample output:
    ```
    ╭──────┬─────────────────────────────┬──────────┬─────────────────────────────┬─────────────────────────────╮
    │   id │ description                 │ status   │ createdAt                   │ updatedAt                   │
    ├──────┼─────────────────────────────┼──────────┼─────────────────────────────┼─────────────────────────────┤
    │    1 │ Study for at least 3 hours. │ done     │ Jul 28, 2025 (Mon 01:42 PM) │ Jul 28, 2025 (Mon 01:49 PM) │
    ╰──────┴─────────────────────────────┴──────────┴─────────────────────────────┴─────────────────────────────╯
    ```
