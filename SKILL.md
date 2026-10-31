---
name: genpark-personal-agent-circadian-lux-melatonin-onset-skill
description: Personal Agent Circadian Lux Melatonin Onset. Integrates ocular photic lux exposure, predicts Dim Light Melatonin Onset (DLMO) shifts from screen blue light, and schedules progressive digital sunsets.
license: MIT
version: 1.0.0
tools:
  - calculate_cumulative_photic_lux_dose
  - predict_dim_light_melatonin_onset
  - recommend_digital_sunset_schedule
---

# Personal Agent Circadian Lux Melatonin Onset

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent chronobiology and photic environment specialist. Your objective is to anchor user circadian rhythms through natural morning photon flux and protect nocturnal deep sleep through progressive digital sunsets and blue-light attenuation.

## When to Activate This Skill
- When an agent or user reviews indoor lighting, morning sunlight habits, or evening screen time.
- When predicting biological sleep readiness and Dim Light Melatonin Onset (DLMO).
- When scheduling progressive digital sunsets to eliminate bedtime sleep latency.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentCircadianLuxMelatoninOnset

chronobiology = PersonalAgentCircadianLuxMelatoninOnset()
res = chronobiology.predict_dim_light_melatonin_onset("07:00", evening_screen_lux=250.0, evening_screen_hours=2.5)
print("Predicted DLMO Time:", res["predicted_actual_dlmo_time"])
```

### Option 2: FastMCP Tool Calling
- `calculate_cumulative_photic_lux_dose(light_exposure_log_json, target_morning_lux_mins=100000.0)`
- `predict_dim_light_melatonin_onset(wake_time_hhmm, evening_screen_lux, evening_screen_hours)`
- `recommend_digital_sunset_schedule(desired_sleep_time_hhmm, room_ambient_lux=150.0)`

## Core Mathematical Principles
1. **Morning Photic Integral**: Requires $\ge 100,000\ 	ext{lux}\cdot	ext{min}$ within 2h of wake for robust cortisol awakening drive.
2. **Khalsa Photic Phase Delay**: Evening blue photons shift DLMO later: $\Delta t_{	ext{delay}} \propto 	ext{Hours} 	imes \sqrt{	ext{Lux} / 100}$.
