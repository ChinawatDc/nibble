# nibble bench — how to run (agy 1.4.3, headless)

No answers in this package. Grading is done separately by QA Bot.

## Sandbox
- Unpack into an isolated folder: `mkdir -p ~/nibble-sandbox && tar xzf nibble-tasks.tgz -C ~/nibble-sandbox`
- No real repos, no .env, no credentials inside ~/nibble-sandbox. Do NOT use --dangerously-skip-permissions.
- Confirm flags once with `agy --help` (headless prompt flag + `--output-format json`).

## Variants
- none: prompt = contents of prompt.txt
- with-skill: prompt = SKILL.md + modes/*.md + prompt.txt
  SK=~/workspace/Chinawatdev/projects/personal/skill-lab/nibble

## Loop (3 runs per task per variant, fresh copy of workspace each run)
```bash
cd ~/nibble-sandbox
SK=~/workspace/Chinawatdev/projects/personal/skill-lab/nibble
for v in none with-skill; do mkdir -p out/$v; done
for t in tasks/*/; do id=$(basename $t)
  for v in none with-skill; do for n in 1 2 3; do
    rm -rf run && cp -R "$t/workspace" run && cd run
    P="$(cat ../$t/prompt.txt)"
    [ $v = with-skill ] && P="$(cat $SK/SKILL.md $SK/modes/*.md)

$P"
    agy -p "$P" --output-format json > ../out/$v/${id}_r$n.json 2> ../out/$v/${id}_r$n.err
    cd ..
  done; done
done
```
- Token numbers must come from agy's JSON usage fields; never estimate.
- Send the whole out/ folder back (plus `agy --version`, model name used).
