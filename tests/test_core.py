import tempfile
from pathlib import Path

from devstudio9082_kit.core import Devstudio9082Tool


def test_plan_empty_dir():
    with tempfile.TemporaryDirectory() as tmp:
        assert Devstudio9082Tool(tmp).plan() == []


def test_category_of_known_and_unknown():
    sorter = Devstudio9082Tool(".")
    assert sorter.category_of("a.png") == "images"
    assert sorter.category_of("a.unknown") == "other"


def test_apply_moves_files():
    with tempfile.TemporaryDirectory() as tmp:
        Path(tmp, "note.md").write_text("hi", encoding="utf-8")
        moved = Devstudio9082Tool(tmp).apply()
        assert moved == [("note.md", "docs")]
        assert Path(tmp, "docs", "note.md").is_file()
