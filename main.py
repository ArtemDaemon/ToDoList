from art import tprint
from rich.console import Console
from rich.prompt import Prompt

console = Console()

EXIT_KEY = '6'


def str_task(task):
    return f'[{"X" if task["is_done"] else " "}] {task["name"]}'


def input_task_index(task_list):
    while True:
        value = Prompt.ask(f'Enter task index (1-{len(task_list)})')
        try:
            value = int(value)
            if 1 <= value <= len(task_list):
                return value
            print('Value must be task list element index. Please try again.')
        except ValueError:
            print(f'"{value}" is not a valid integer value. Please try again.')


def main():
    task_list = []

    tprint('To-Do List')
    console.print('Welcome to the To-Do List!\n', style='italic')

    console.print('[red]1.[/red] Add new task')
    console.print('[red]2.[/red] Show task list')
    console.print('[red]3.[/red] Complete task')
    console.print('[red]4.[/red] Delete task')
    console.print('[red]5.[/red] Sort task list')
    console.print('[red]6.[/red] Exit')

    input_key = ''

    while input_key != EXIT_KEY:
        input_key = Prompt.ask('\nPlease, choose menu item (1-6)',
                               choices=['1', '2', '3', '4', '5', '6'], show_choices=False)

        match input_key:
            case '1':
                task_name = Prompt.ask('Enter a task name')
                task_list.append({
                    'name': task_name,
                    'is_done': False
                })
                console.print(f'The [green]"{task_name}"[/green] task has been added!')
            case '2':
                console.print('Task list:')
                for index, task in enumerate(task_list):
                    console.print(f'[red]{index + 1}.[/red] {str_task(task)}')
            case '3':
                if len(task_list) == 0:
                    console.print('[red]Task list has no tasks![/red]')
                    continue
                task_index = input_task_index(task_list)
                task = task_list[task_index - 1]
                task["is_done"] = True
                console.print(f'The [green]"{task["name"]}"[/green] task is done!')

    console.print('Thanks for using To-Do List!')


if __name__ == '__main__':
    main()
