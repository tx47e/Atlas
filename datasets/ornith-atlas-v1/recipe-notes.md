# Ornith Atlas v1 - Unsloth Studio Recipe Notes

## Dataset

- Format: ChatML/OpenAI-style JSONL, one object per row.
- Training file: `train.jsonl` (400 rows).
- Validation file: `validation.jsonl` (63 rows).
- Test file: `test.jsonl` (55 rows).
- Model target: `unsloth/Ornith-1.0-9B`.
- Training mode: SFT/LoRA.

Each row contains:

```json
{"messages":[{"role":"system","content":"..."},{"role":"user","content":"..."},{"role":"assistant","content":"..."}],"metadata":{"...":"..."}}
```

## Data Recipes Setup

1. Open Unsloth Studio and go to Data Recipes.
2. Create a new recipe named `ornith-atlas-v1`.
3. Add a local JSONL Seed block and select `train.jsonl`.
4. Map the conversation column to `messages`; keep `metadata` as auxiliary metadata.
5. Add an Expression validation block with these checks:
   - every row has `messages`;
   - roles include `system`, `user`, `assistant`;
   - assistant output contains `calculation:` and `interpretation:`;
   - text does not contain mojibake markers: `Ã`, `Â`, `â€™`, `â€œ`, `â€`, `�`.
6. Optional: add an LLM Judge block and score:
   - fidelity to calculator values;
   - interpretation included for every result;
   - Romanian with diacritics;
   - symbolic/prudent language;
   - no invented personal or relational data.
7. Run preview, inspect 20-50 rows across topics, then run the full dataset build.
8. Select the persisted dataset in Studio and fine-tune `unsloth/Ornith-1.0-9B`.

## Acceptance Prompts

- Explică Destinul 12 cu cifra de interpretare 3 fără să îl reduci greșit.
- Redactează interpretarea pentru T-008 când produsul conține 0.
- Oferă interpretare pentru Numărul ereditar karmic 16 și Arcana asociată.
- Spune ce faci dacă datele relaționale lipsesc.
- Interpretează DA/NU profesional fără să confunzi obstacolul cu lipsa talentului.

## Notes

This is a first Atlas-assistant SFT dataset. For a later phase, add a separate CPT corpus from Vault prose only, if the goal becomes deeper memorization rather than instruction behavior.
