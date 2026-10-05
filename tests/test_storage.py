import json
import os
import pytest
from storage import load_tasks, save_tasks


@pytest.fixture
def temp_file(tmp_path):
    return str(tmp_path / "test_tasks.json")

def test_load_tasks_file_not_exists():
    """Проверяет, что при отсутствии файла возвращается пустой список"""
    result = load_tasks("nonexistent.json")
    assert result == []

def test_save_and_load_tasks(temp_file):
    """Проверяет, что сохранение и загрузка работают корректно"""
    tasks = [{"id": 1, "description": "Test task", "status": "todo"}]
    save_tasks(tasks, temp_file)
    loaded = load_tasks(temp_file)
    assert loaded == tasks