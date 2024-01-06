from art import tprint
from rich.console import Console
from rich.prompt import Prompt

console = Console()

EXIT_KEY = '6'


def main():
    task_list = []

    tprint('To-Do List')
    console.print('Welcome to the To-Do List!', style='italic')

    console.print('[red]1. [/red] Add new task')
    console.print('[red]2. [/red] Show task list')
    console.print('[red]3. [/red] Complete task')
    console.print('[red]4. [/red] Delete task')
    console.print('[red]5. [/red] Sort task list')
    console.print('[red]6. [/red] Exit')

    input_key = Prompt.ask('Please, choose menu item (1-6)',
                           choices=['1', '2', '3', '4', '5', '6'], show_choices=False)

    while input_key != EXIT_KEY:
        match input_key:
            case '1':
                task_name = Prompt.ask('Enter a task name')
                task_list.append({
                    'name': task_name,
                    'is_done': False
                })
                console.print('f[green]The "{task}" task has been added[/green]', task_name)

    console.print('Thanks for using To-Do List!')


if __name__ == '__main__':
    main()
