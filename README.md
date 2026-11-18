# devstudio9082-kit

Sort a folder of files into per-type subfolders.

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m devstudio9082_kit.cli --help
```

```python
from devstudio9082_kit.core import Devstudio9082Tool

tool = Devstudio9082Tool()
print(tool)
```

## Layout

```
devstudio9082_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 devstudio9082
