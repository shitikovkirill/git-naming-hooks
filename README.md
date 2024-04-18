# Git naming hooks

## Example of pattern 

```yaml
args: [-r, '^HOOK\-[0-9]+\: .+']
```
```yaml
args: [-r, '^(HOOK|Hook|hook)-[0-9]+((_|\/)[\w\-_]+)?']
```

## Install pre-commit
```bash
pre-commit install --install-hooks -t pre-commit -t commit-msg
```