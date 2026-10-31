# genpark-personal-agent-circadian-lux-melatonin-onset-skill

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Personal Agent Circadian Lux Melatonin Onset applies ocular photobiology and human circadian phase response curves to optimize personal light hygiene and sleep readiness.

```mermaid
flowchart TD
    A[Ocular Lux Exposure Log & Sources] --> B[Photic Integral Dose Integrator]
    B --> C[Morning Circadian Anchoring Status]
    D[Evening Screen Brightness & Duration] --> E[Khalsa Human DLMO Delay Model]
    E --> F[Actual Biological Melatonin Onset Window]
    F --> G[Progressive Digital Sunset Protocol]
```

## Features
- **Photic Dose Integration**: Tracks cumulative photon flux and verifies morning anchor thresholds.
- **DLMO Delay Forecaster**: Models pineal gland melatonin suppression from digital screens.
- **Digital Sunset Milestones**: Prescribes timed 120-min, 60-min, and 30-min lighting transitions.

## Quickstart

```python
from client import PersonalAgentCircadianLuxMelatoninOnset

chronobiology = PersonalAgentCircadianLuxMelatoninOnset()
res = chronobiology.recommend_digital_sunset_schedule("23:00")
print("First Sunset Action:", res["milestones"][0]["action"])
```

## FastMCP Integration

```bash
python -m genpark-personal-agent-circadian-lux-melatonin-onset-skill.mcp_server
```

## License
MIT
