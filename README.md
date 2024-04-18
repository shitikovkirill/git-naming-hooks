# Git naming hooks

## Example of pattern 

```yaml
repos:
-   repo: https://git.webwave.work/Common/git-naming-hooks.git
    rev: v0.1.0
    hooks:
    -   id: check-git-commit
        args: [-r, '^HOOK\-[0-9]+\: .+']
    -   id: check-git-branch
        args: [-r, '^(HOOK|Hook|hook)-[0-9]+((_|\/)[\w\-_]+)?']
```

## Install pre-commit
```bash
pre-commit install --install-hooks -t pre-commit -t commit-msg
```