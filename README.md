# MESOP - SHOWCASE

## What's MESOP?
Please read the Introduction of Medium: [](../Intr0_by_Medium.md)

## Getting Started

### Pre-requisites
Make sure you have Python version 3.10 or later installed by running:
```shell
python --version
```

### Create a venv environment
1. __Open the terminal__ and navigate to a directory: 
    ```shell
    cd foo
    ```
2. __Create a virtual environment__ by using venv, which will avoid Python environment issues. Run:
    ```shell
    python -m venv .venv
    ```
3. __Activate your virtual environment__:
    macOS and Linux
    ```shell
    source .venv/bin/activate
    ```
    Windows command prompt
    ```shell
    .venv\Scripts\activate.bat
    ```
    Windows PowerShell
    ```shell
    .venv\Scripts\Activate.ps1
    ```
    Once you've activated the virtual environment, you will see ".venv" at the start of your terminal prompt.
.
4. __Install mesop__:
    ```shell
    pip install mesop
    ```

5. __Upgrading__
    To upgrade Mesop, run the following command:
    ```shell
    pip install --upgrade mesop
    ```

If you are using __requirements.txt__ or __pyproject.toml__ to manage your dependency versions, then you should update those.

## Demo Apps

* [Starter Kit](../mesop/main.py)
* [helloworld.py](../mesop/helloworld.py)
* [counter.py](../mesop/counter.py)

## Mesop DuoChat Codelab
* 1 - Overview & Setup: [DuoChat 1](../mesop/Mesop-DuoChat/DuoChat-Codelab-Part-1.md)
* 2 - Building the basic UI: [DuoChat 2](../mesop/Mesop-DuoChat/DuoChat-Codelab-Part-2.md)
* 3 - Managing state & dialogs: [DuoChat 3](../mesop/Mesop-DuoChat/DuoChat-Codelab-Part-3.md)
* 4 - Integrating AI APIs: [DuoChat 4](../mesop/Mesop-DuoChat/DuoChat-Codelab-Part-4.md)
* 5 - Wrapping it up: [DuoChat 5](../mesop/Mesop-DuoChat/DuoChat-Codelab-Part-5.md)  
