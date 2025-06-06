# 🛣️ Roadmap - Unit Test Goblin

## 🧪 Overview

This roadmap breaks down the phases of building Unit Test Goblin: a CLI tool that analyzes Java unit tests, detects weak or missing coverage, and makes intelligent suggestions to improve test quality.

---

## 🚀 Phase 1: MVP Build

### Goal: Build a working CLI tool that:

- Accepts path to Java test files
- Detects @Test methods (JUnit)
- Flags methods with no assertions
- Flags duplicate/mock-only tests
- Prints suggestions in terminal

### 🔧 Deliverable:

- Working CLI (goblin analyze ./src)
- At least 3 test smell types detected
- Early feedback from friends/devs

---

## 🎯 Phase 2: Refine & Integrate

### Goal: Make the tool more useful, flexible, and fun

- Add customization via config file
- Add better output formatting (color, severity, confidence)
- Support more advanced smell detection (e.g. over-mocking, untested branches)
- Spock test support (Groovy)
- Collect feedback from open-source users

---

## 💻 Phase 3: Dev Tool Ecosystem

### Goal: Make it easy to integrate Goblin into daily dev life

- GitHub Action: auto-analyze test quality on PRs
- VS Code extension (if not a complete nightmare)
- Web dashboard (stretch goal)
- Possibly support more languages (Python, JS, etc.)

---

## **💰 Phase 4: Monetization Experiments**

### **Goal:** Explore if this tool could become a product

- Team dashboard for coverage trends
- CI integration with reports + Slack alerts
- Licensing or open-core model?
- Accept donations or GitHub Sponsors

---

## **🧠 Phase “What If…?”**

- AI-generated test suggestion assistant
- Meme output mode that roasts devs with gifs
- Integration with code review bots
- Test quality leaderboard (don’t tempt people tho)
