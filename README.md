# Unit Test Goblin 🧪👹

A CLI tool that analyzes your unit tests and codebase to detect weak test coverage, redundant cases, and untested logic paths. Because your tests *aren’t as good as you think*.

## Why?
Most test suites lie. They pass when they shouldn't, cover when they shouldn't, and leave edge cases to die in the cold. Goblin helps you:

- Spot meaningless tests
- Identify missing assertions
- Catch untested edge cases

## MVP Features
- Parse code and test files
- Detect empty or redundant tests
- Identify missing logical branches
- Suggest better coverage

## Usage (soon)
```bash
$ goblin analyze ./path/to/your/code
```

## Devlog
All progress will be logged in `/devlog`. Follow the journey or contribute!

### 📁 Folder Overview

| Folder       | Purpose                                                 |
|--------------|---------------------------------------------------------|
| `goblin/`    | Core logic: parsing, detecting, and shaming bad tests  |
| `cli/`       | CLI entry point – run the Goblin from your terminal     |
| `tests/`     | Unit tests *for the Goblin itself*                      |
| `docs/`      | Design plans, roadmap, architecture decisions           |
| `devlog/`    | Daily journal of progress, chaos, and existential dread |

---

👋 Created by [gpapachr](https://github.com/gpapachr) – fueled by sarcasm, caffeine, and a deep hatred for fragile test suites.