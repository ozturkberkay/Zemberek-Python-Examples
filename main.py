import argparse
import importlib
from pathlib import Path
from typing import List

from jpype import shutdownJVM, startJVM

from examples import JVM_KWARGS


def get_runnable_modules() -> List[str]:
    """
    Returns a list of scripts which implement the run function.

    Returns:
        List[str]: List of script names in 'module.submodule.script' format.
    """
    runnable_modules: List[str] = []
    for script in Path('examples').glob('**/*.py'):
        if script.name == '__init__.py':
            continue
        module_name: str = (
            f'{script.parents[0].name}.{script.name.split(".")[0]}'
        )
        if hasattr(importlib.import_module(f'examples.{module_name}'), 'run'):
            runnable_modules.append(module_name)
    return runnable_modules


if __name__ == '__main__':

    startJVM(**JVM_KWARGS)

    parser = argparse.ArgumentParser(
        description=(
            'Run a Zemberek example. Example usage: python -m main'
            ' morphology.word_analysis kelime'
        )
    )
    parser.add_argument(
        'example',
        type=str,
        help='The run() function from the chosen script will be invoked.',
        choices=get_runnable_modules(),
    )
    parser.add_argument(
        'args',
        type=str,
        default=[],
        nargs='*',
        help='Arguments to pass to the run function.',
    )

    args = parser.parse_args()

    example = importlib.import_module(f'examples.{args.example}')

    print(example.run.__doc__)

    example.run(*args.args)

    shutdownJVM()
