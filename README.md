> Eurovision self-provided voting votes calculator for me and my friends.
    <details>
        <summary>Motivation</summary>
        Me and my friends provide our own voting for every Eurovision contest basing on only our votes. 
        To automate the process of votes processing I create this python-script.
    </details>

# Installation

Note: python 3.10+ is required. Follow the [INSTALL.md](INSTALL.md) to prepare your code.

# Get-started:

1. Replace `answers` with your answers inside of [main.py](main.py). Also you can specify the `top_n` value there for 
   limit the number of result value.


2. Move to folder with the repository, run in your terminal:
    ```shell
    pipenv run main.py
    ```

3. See results. Example of the output (while `top_n=10`):
    ```text
   10) Швеция: 10
   9) Румыния: 12
   8) Азербайджан: 14
   7) Нидерланды: 14
   6) Молдавия: 17
   5) Испания: 23
   4) Великобритания: 28
   3) Италия: 30
   2) Норвегия: 40
   1) Финляндия: 42
    ```

# Developing and TODOs

Follow the [DEVELOPING.md](DEVELOPING.md) for further developing.