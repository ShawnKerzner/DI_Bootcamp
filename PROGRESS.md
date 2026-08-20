# Progress Log

This is the running, human-readable log kept by the Student Progress Coach. Each daily review adds a new dated entry at the **top** of this file (newest first), covering commits since the last review, what changed, and any recommendations. See `CLAUDE.md` for the full behavior contract.

## 2026-08-20

*Catch-up review — no run happened on 2026-08-19, so this covers three days of work (2026-08-18 evening through this morning).*

**Since yesterday:** 7 commits, 22 files — javascript fundamentals, loops, switch statements, string methods, DOM manipulation, input validation, npm packages

**What I saw:** Big jump this week: you moved from Python into JavaScript (`week-3/day-1`), working through `course-notes` on switch statements, short-circuit evaluation (`short-circuiting-js.js`), string methods (`string-split-method-in-js.js`, `index-of-method-in-js.js`), and a small DOM exercise wiring `script.js` up to `exercise-1-html.html`. In `exercise-xp/exercises-xp.js` you kept the same habit from `warmup.py` last time — commenting out each finished exercise instead of deleting it — so Exercise 1's array methods and Exercise 2's loop-with-suffix logic are still sitting there above Exercise 3. Exercise 3's `do...while` loop does real input validation: it checks `isNaN(user_number)` and prints a message before looping again instead of crashing on bad input, which carries the error-handling instinct forward from the `Pagination` class you built last time. One thing worth knowing: that same commit pulled the whole `readline-sync` package into git — `node_modules/readline-sync/` is now checked in (2,500+ lines) because there's no `.gitignore` in the repo yet. Also noticed `claude-course/day-3/2students.zip` is sitting untracked and unopened — looks like tomorrow's material, not started yet.

**Recommendations:**
- Add a `.gitignore` at the repo root with `node_modules/`, `__pycache__/`, and `__MACOSX/` in it — right now `week-3/day-1/exercise-xp/node_modules/` is fully committed, and there are stray `__pycache__`/`__MACOSX` files untracked under `claude-course/day-2/sample-project/` from unzipping that project.
- In `exercises-xp.js` line 52, swap `while (1)` for `while (true)` — same behavior, but `true` says what you mean instead of relying on truthy-number trivia.
- Two recommendations from 2026-08-18 are still open and now three days old: `Pagination.__init__`'s `if items == None` (should be `is None`) and the pagination bonus step. Worth a quick pass before they get buried under this week's JS work.

**Streak:** 3 days in a row

## 2026-08-18

**Since yesterday:** 1 commit, 1 file — pagination, object-oriented programming, error handling

**What I saw:** Your `Pagination` class in `week-2/day-2/daily-challenge-pagination/daily-challenge-pagination.py` is doing real OOP: `go_to_page`, `next_page`, and `previous_page` raise `ValueError` with actual messages instead of failing silently, and `next_page`/`previous_page`/`first_page`/`last_page` all `return self`, so calls like `p.next_page().next_page()` chain cleanly. You flagged the commit itself as "minus the bonus step," so the challenge isn't fully wrapped yet. Separately (still uncommitted, so not counted above), `week-2/day-4/warmup/warmup.py` writes the factorial result with a `with open(...)` block and leaves an old `try/finally` version commented out right below it — good instinct to keep the earlier pattern visible for comparison instead of just deleting it.

**Recommendations:**
- In `Pagination.__init__`, swap `if items == None` for `if items is None` — `is` is the idiomatic way to check for `None` in Python and avoids surprises with objects that override `__eq__`.
- Circle back and finish the bonus step on the pagination challenge — you're one step from a fully complete exercise, not a fresh one.
- Commit the `week-2/day-4/warmup/` work (and the `claude-course` reorg into `day-2/`) once you're happy with it — it's sitting uncommitted right now, so it won't factor into tomorrow's review until it lands.

**Streak:** 1 day in a row
