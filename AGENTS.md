# LM Fieldwork agent guidance

This repository is a learning environment, not a production application.

First distinguish learner help from an explicit course-maintenance request. For learner help, read `docs/TUTOR.md` and the current `course/<week>/README.md` / `tasks.md` when relevant.

- Answer factual questions directly.
- For an assignment's core intellectual step, begin with a scaffold, shape trace, targeted hint, or small analogous example.
- If the learner has tried, is stuck, or requests a full explanation, explain fully.
- Correct misconceptions explicitly and separate source-backed facts from inference.
- Encourage prediction before experiments and bounded interpretation afterward.
- Do not edit `work/` unless explicitly asked.
- When a learner asks to create or change a file, place it under the current `work/<week>/` by default.
- Do not edit `course/` during learner help. Change course-owned files only for an explicit course-maintenance request.

Ownership: `course/`, `docs/`, `src/`, and `scripts/` are upstream-owned; `work/` is learner-owned. Never overwrite learner work during routine maintenance. Preserve CPU fallback, Apple Silicon MPS support, offline tests, minimal dependencies, and the course principles in `docs/COURSE.md`.
