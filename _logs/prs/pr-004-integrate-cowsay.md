# PR 004: Integrate Cowsay into Main

**Branch**: `feat/integrate-cowsay`
**Target**: `main`

## Description
This PR integrates the `cowsay_demo.py` module into `main.py`.
It updates `main()` to directy call `cowsay()` from the demo module, demonstrating internal module imports and usage.

## Changes
- [x] Modified `main.py`
    - Added `from cowsay_demo import cowsay`
    - Added call `cowsay("Hello from main!")`

## Verification
- Ran `python main.py` in worktree.
- Output confirmed:
    ```
    Hello from gitsample-project!
     ------------------
    < Hello from main! >
     ------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
    ```
