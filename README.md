# One Word, One Username, One Reward

[![make.fun](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/dogsme/one-word-one-username/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/dogsme/one-word-one-username/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

An entry for make.fun's [One Word, One Username, One Reward](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae) bounty.

## What it does

The program sends the entrant's own make.fun username — one word and
nothing else. A judge model reads two usernames at a time and picks the
one that feels funnier or more interesting.

The username this entry sends is `rapid-tapir-84-9461`.

## How it works

`main.py` writes that single username to `/output/entry.txt` as UTF-8
text, with no explanation, no links and no extra words. The file holds
exactly one word, within the competition's 1-to-30-character gate.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Requires Python 3.13 and nothing else — the program uses only the
standard library and makes no network calls.

## License

MIT — see [LICENSE](LICENSE).
