# 🧪 Understanding Python Virtual Environments (venv)

## 👶🏼 What’s a Virtual Environment?

A virtual environment in Python is like a tiny isolated bubble where you can install packages, dependencies, and run your Python code—without messing up your system’s main Python setup.

Think of it like this:

> 🧑🏼‍🍳 You’re cooking a specific recipe. A virtual environment is your clean kitchen counter. You bring only the ingredients you need. No interference from that expired jar in the back of your fridge.

## 🧩 Why Use a Virtual Environment?

Here’s why Python developers (including Goblin’s creator 😎) always use venv:

- Isolation: Keeps project dependencies separate
- Avoid Conflicts: One project may need Flask==1.1.2, another may need Flask==2.0.0. Without venv, you’re toast.
- Professional Practice: All real-world Python projects use venv, including open-source tools and production apps.
- Safe Experimentation: Want to try breaking things without consequences? Go ahead.

## ⚙️ How to Create and Use a Virtual Environment

1.  Create the virtual environment

```bash
python3 -m venv venv
```

This creates a folder named venv/ with a clean Python interpreter and no packages.

2.  Activate it

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Now your shell should look like this:

```bash
(venv) your-computer:unit-test-goblin$
```

3.  Install your packages

```bash
pip install -r requirements.txt
```

4.  Run your project

```bash
python python src/cli.py analyze examples/ analyze examples/
```

5.  Deactivate when done

```bash
deactivate
```

You’ll exit the virtual world and return to the real one.

### ❌ .gitignore It!

Never commit the venv/ folder to Git. Add this to your .gitignore:

```
venv/
__pycache__/
```
