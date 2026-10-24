# Repository utilities

Run the structure and relative Markdown-link check from the repository root:

```text
python scripts/check_repository.py
```

This uses only the Python standard library. It checks that reserved directories and .gitkeep markers exist, verifies internal Markdown links, and rejects unresolved Git conflict markers. It does not run application or prototype tests.
