"""Common constants for the examples."""
import os
from pathlib import Path
from typing import Dict, List, Optional, Union
from jpype import getDefaultJVMPath

__all__: List[str] = ['ZEMBEREK_PATH', 'DATA_PATH', 'JVM_KWARGS', 'JAVA_PATH']

ZEMBEREK_PATH: Path = (
    Path(__file__).parents[1].joinpath('bin', 'zemberek-full.jar').absolute()
)

DATA_PATH: Path = Path(__file__).parents[1].joinpath('data').absolute()

JVM_KWARGS: Dict[str, Union[str, bool]] = {
    'jvmpath': getDefaultJVMPath(),
    'classpath': str(ZEMBEREK_PATH),
    'convertStrings': False,
    'interrupt': True,
}

_JAVA_HOME: Optional[str] = os.getenv('JAVA_HOME')

if _JAVA_HOME is None:
    raise EnvironmentError(
        'Install Java and make sure the JAVA_HOME environment variable is set.'
    )

JAVA_PATH: Path = Path(_JAVA_HOME, 'bin', 'java')
