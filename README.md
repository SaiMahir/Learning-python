# Learning Python

A repository for learning Python fundamentals and best practices.

## Setting Up a Virtual Environment

You must create a virtual environment for your Python code to run in.

### Why Use Virtual Environments?

If you don't create a virtual environment, all Python packages will be installed globally. This means they are not separated or isolated between projects.

This won't be a problem for basic code since we won't be installing any libraries or different versions of the same libraries. However, if we need to install libraries in the future, they may conflict. For example:
- One project needs **Django 3.0**
- Another project needs **Django 4.0**

If both are running globally, installing one version will break the other project.

### Commands

**Create a virtual environment:**
```powershell
python -m venv EnvironmentName
```

**Activate the environment (Windows PowerShell):**
```powershell
.\EnvironmentName\Scripts\Activate.ps1
```

**Activate the environment (Command Prompt):**
```cmd
.\EnvironmentName\Scripts\activate.bat
```

**Deactivate the environment:**
```powershell
deactivate
```

> **Note:** If you get an execution policy error when activating, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```