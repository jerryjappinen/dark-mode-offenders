"""Build new README based on data.json."""

import os
from utils import generate_readme, write_to_readme

data_path = os.path.join(os.path.dirname(__file__), "../data.json")
base_readme_path = os.path.join(os.path.dirname(__file__), "readme_base.md")
target_readme_path = os.path.join(os.path.dirname(__file__), "../README.md")

if __name__ == "__main__":
    print("\n" + "✔️ Generating new README...")
    write_to_readme(
        target_readme_path,
        generate_readme(data_path, base_readme_path)
    )
    print(f"✔️ README.md updated ({ os.path.normpath(target_readme_path)})" + "\n")
