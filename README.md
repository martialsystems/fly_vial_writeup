# fly_vial_writeup

Note on the fly_vial assortative IBD F split. Locks stay on the trees.

The argument is [NOTE.md](NOTE.md). The PDF is [docs/fly_vial_f_note.pdf](docs/fly_vial_f_note.pdf). The SHA index is gist [12835f74](https://gist.github.com/martialsystems/12835f747d6360781f3cc7f91f243178). Do not restamp `@e2e22b7` or F = 0.524 / 0.034. This git is not a finding-tree row.

## How to run

```
.venv/bin/python -m pytest
.venv/bin/python scripts/build_stack_fig.py
.venv/bin/python scripts/build_note_pdf.py
```

## Files

| Path | Role |
|------|------|
| `NOTE.md` | The argument |
| `docs/fly_vial_f_note.pdf` | Research-format PDF of the same argument |
| `figures/stack.png` | F versus generation on the seed-1 lock |
| `AGENTS.md` | Project rules |

[Fly research index](https://gist.github.com/martialsystems/12835f747d6360781f3cc7f91f243178)
