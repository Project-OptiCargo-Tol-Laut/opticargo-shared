from scripts.check_compatibility import compare_schema


def test_compatibility_checker_detects_breaking_changes() -> None:
    old = {
        "type": "object",
        "properties": {"id": {"type": "string"}, "name": {"type": "string"}},
        "required": ["id"],
    }
    new = {
        "type": "object",
        "properties": {"id": {"type": "integer"}},
        "required": ["id", "new_field"],
    }
    problems = compare_schema(old, new)
    assert any("newly required" in problem for problem in problems)
    assert any("removed property" in problem for problem in problems)
    assert any("type changed" in problem for problem in problems)
