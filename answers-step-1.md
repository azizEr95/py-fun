# Step 1: Questions for Python Project-Setup

1. **What is the project scaffold?**
    - The basic directory and file structure of a project (`src`, `tests`, `docs`, `makefile`, `requirements.txt`, ...).

1. **What is a software build process?**
    - An automated, reproducible sequence of steps that turns source code into a deliverable artifact.

1. **When does the build process start and when does it end?**
    - Starts when the source code is present and ready to be compiled.
    - Ends when the executable artifact is created (e.g. `py-fun-SNAPSHOT-0.1.0.tar`).

1. **What are the steps and what is the result of the build process?**
    - Steps: fetch dependencies, compile, run tests, build docs, package.
    - Result: a versioned, distributable artifact (e.g. `.tar.gz`, `.whl`).

1. **What is make?**
    - A build tool that runs targets (and their dependencies) defined in a `makefile`.

1. **What is the purpose of requirements.txt? How is it used?**
    - Lists the external packages (and versions) the project depends on.
    - Used with `pip install -r requirements.txt` (here: `make install`).

1. **What is a Build Server? What does it mean for Python?**
    - A central (CI) server that builds and tests automatically in a clean environment, e.g. on every push.
    - For Python: the environment must be fully defined (`requirements.txt`, Python version), and tests are essential because errors only show up at runtime.

1. **What are Nightly Builds?**
    - Automated builds of the latest code that run on a schedule, usually every night.

1. **Differences between Scripts, Modules, Packages and Libraries?**
    - Script: a `.py` file you run directly. Module: a `.py` file you import.
    - Package: a directory of modules with `__init__.py`. Library: a distributed collection of packages (e.g. from PyPI).

1. **What is `__init__.py` used for?**
    - Marks a directory as a package and runs when the package is first imported.
    - Defines what the package exports (e.g. `from .calculator import Calculator`).
