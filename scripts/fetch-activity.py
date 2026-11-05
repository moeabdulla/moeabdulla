"""Refresh aggregate calendar data using an already-authenticated gh CLI. No source code is fetched."""
import json,subprocess
from pathlib import Path
query='query { user(login:"moe1011") { contributionsCollection { contributionCalendar { totalContributions weeks { contributionDays { date contributionCount contributionLevel } } } } } }'
data=subprocess.check_output(['gh','api','graphql','-f',f'query={query}'])
parsed=json.loads(data)
if parsed.get('errors') or 'data' not in parsed:
    raise RuntimeError('GitHub did not return a valid contribution calendar')
root=Path(__file__).resolve().parents[1]
(root/'data/activity.json').write_text(json.dumps(parsed,indent=2)+'\n')
print('Saved contribution-calendar snapshot. Rebuild with scripts/build-all.py.')
