from typing import Dict
import gdown
from pathlib import Path


ZEMBEREK_FILES: Dict[str, Dict[str, str]] = {
    'bin': {'zemberek-full.jar': '1RRuFK43JqcHcthB3fV2IEpPftWoeoHAu'},
    'data/classification': {
        'news-title-category-set': '13d6TjKSk8Uy0FNHrbqJQv1hHalKUg1l5',
        'news-title-category-set.lemmas': '1VP-DcPDY423cU48CP675yT6RS_hygtpX',
        'news-title-category-set.tokenized': '1xt81joeOA7nOTYNUKdxKBOeDtLGMCwNO',
    },
    'data/lm': {'lm.2gram.slm': '1JZG0I8jUS511lFVg0M-QAA4QRqydlCiX'},
    'data/normalization': {
        'ascii-map': '1ptbPoGZrKxXS5PNr5kpGfHziGdIUP-n7',
        'lookup-from-graph': '1ko31lO1yrYf1twjZOl_vHikmsGkQGKt5',
        'split': '1X8UpIE0ifYF1_tpMQp7o5PLEqms3Ew5Q',
    },
}


def download_drive_files(
    file_map: Dict[str, Dict[str, str]], skip_if_exists: bool = True
) -> None:
    """
    Downloads the files from Google Drive.

    Args:
        file_map (Dict[str, Dict[str, str]]): Mapping of directories to install
            to, with the file names and Google Drive ID's.
        skip_if_exists (bool): Skips the download if the target file already
            exists on the local filesystem.
    """

    base_path: Path = Path(__file__).parent

    for folder in file_map:

        for file_name, drive_id in file_map[folder].items():

            target_path: Path = base_path.joinpath(
                folder, file_name
            ).absolute()

            if skip_if_exists and target_path.exists():
                print(f'Target already exists, skipping: {target_path}')
                continue

            gdown.download(
                url=f'https://drive.google.com/u/0/uc?id={drive_id}',
                output=str(target_path),
            )


if __name__ == '__main__':
    download_drive_files(ZEMBEREK_FILES)
