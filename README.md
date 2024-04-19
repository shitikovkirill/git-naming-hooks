# Git naming hooks

This hooks  which check branch name format and commit name format in git.

## Example of usage

```yaml
repos:
-   repo: https://github.com/shitikovkirill/git-naming-hooks.git
    rev: v0.1.2
    hooks:
    -   id: check-git-commit
        args: [-r, '^HOOK\-[0-9]+\: .+']
    -   id: check-git-branch
        args: [-r, '^(HOOK|Hook|hook)-[0-9]+((_|\/)[\w\-_]+)?']
```

## Install commit-msg hook

NOTE: For running check commit message hook need run this command.

```bash
pre-commit install --install-hooks -t commit-msg
```
