# -*- coding: utf-8 -*-
"""
Personal Agent Circadian Lux Melatonin Onset FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentCircadianLuxMelatoninOnset

mcp = FastMCP("genpark-personal-agent-circadian-lux-melatonin-onset-skill")
chronobiology = PersonalAgentCircadianLuxMelatoninOnset()

@mcp.tool()
def calculate_cumulative_photic_lux_dose(
    light_exposure_log_json: str,
    target_morning_lux_mins: float = 100000.0
) -> str:
    """
    Integrates daily ocular photic lux exposure and evaluates morning circadian anchoring.
    """
    log = json.loads(light_exposure_log_json)
    res = chronobiology.calculate_cumulative_photic_lux_dose(log, target_morning_lux_mins)
    return json.dumps(res, indent=2)

@mcp.tool()
def predict_dim_light_melatonin_onset(
    wake_time_hhmm: str = "07:00",
    evening_screen_lux: float = 250.0,
    evening_screen_hours: float = 3.0
) -> str:
    """
    Predicts Dim Light Melatonin Onset (DLMO) and optimal biological sleep window.
    """
    res = chronobiology.predict_dim_light_melatonin_onset(wake_time_hhmm, evening_screen_lux, evening_screen_hours)
    return json.dumps(res, indent=2)

@mcp.tool()
def recommend_digital_sunset_schedule(
    desired_sleep_time_hhmm: str = "23:00",
    room_ambient_lux: float = 150.0
) -> str:
    """
    Schedules progressive digital sunset lighting milestones to optimize deep sleep.
    """
    res = chronobiology.recommend_digital_sunset_schedule(desired_sleep_time_hhmm, room_ambient_lux)
    return json.dumps(res, indent=2)

def main():
    print("Testing Circadian Lux Melatonin Onset FastMCP Server:")
    print(predict_dim_light_melatonin_onset("07:00", 200.0, 2.5))

if __name__ == "__main__":
    main()
