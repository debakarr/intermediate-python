from pathlib import Path
import subprocess
import sys


if __name__ == "__main__":
    file_path = Path(__file__).parent
    notebooks = file_path.parent.glob("*.ipynb")

    for notebook in notebooks:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "jupyter",
                "nbconvert",
                "--to",
                "webpdf",
                "--no-input",
                notebook,
            ]
        )
