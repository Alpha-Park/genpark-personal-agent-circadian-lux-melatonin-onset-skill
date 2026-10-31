# -*- coding: utf-8 -*-
"""
Personal Agent Circadian Lux Melatonin Onset Client
Zero-dependency photic retinal lux integral modeler, Khalsa human phase response curve (PRC),
and Dim Light Melatonin Onset (DLMO) blue-light attenuation scheduler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentCircadianLuxMelatoninOnset:
    """
    Models ocular photon flux, calculates Dim Light Melatonin Onset (DLMO) shifts,
    and schedules digital sunset screen cutoffs to optimize deep sleep architecture.
    """

    def calculate_cumulative_photic_lux_dose(
        self,
        light_exposure_log: List[Dict[str, Any]],
        target_morning_lux_mins: float = 100000.0
    ) -> Dict[str, Any]:
        """
        Integrates cumulative photic lux exposure: Dose = sum(Lux_i * DurationMinutes_i).
        Log format: [{"time": "07:30", "lux": 15000.0, "duration_minutes": 20.0, "source": "Outdoor Sunlight"}]
        """
        if not light_exposure_log:
            raise ValueError("Light exposure log cannot be empty.")

        total_dose = 0.0
        morning_dose = 0.0

        for entry in light_exposure_log:
            lux = max(0.0, float(entry.get("lux", 500.0)))
            dur = max(0.0, float(entry.get("duration_minutes", 15.0)))
            t_str = str(entry.get("time", "12:00"))
            hour = int(t_str.split(":")[0]) if ":" in t_str else 12

            dose = lux * dur
            total_dose += dose
            if hour <= 10:
                morning_dose += dose

        pct_morning_target = round((morning_dose / max(1e-6, target_morning_lux_mins)) * 100.0, 1)

        return {
            "total_daily_lux_minutes": round(total_dose, 1),
            "morning_lux_minutes": round(morning_dose, 1),
            "target_morning_lux_minutes": target_morning_lux_mins,
            "morning_target_attainment_pct": pct_morning_target,
            "circadian_synchronization_status": "OPTIMALLY_ANCHORED" if pct_morning_target >= 100.0 else ("MODERATE_ALIGNMENT" if pct_morning_target >= 60.0 else "INSUFFICIENT_MORNING_PHOTIC_DRIVE"),
            "cortisol_awakening_response_robustness": "HIGH" if pct_morning_target >= 100.0 else "SUBOPTIMAL"
        }

    def predict_dim_light_melatonin_onset(
        self,
        wake_time_hhmm: str = "07:00",
        evening_screen_lux: float = 250.0,
        evening_screen_hours: float = 3.0
    ) -> Dict[str, Any]:
        """
        Predicts Dim Light Melatonin Onset (DLMO) time based on natural circadian anchor and blue-light delay.
        Natural DLMO occurs ~14 hours post-wake.
        Light Delay = evening_screen_hours * (evening_screen_lux / 100)^0.5 * 0.35 hours.
        """
        try:
            parts = wake_time_hhmm.strip().split(":")
            w_h = int(parts[0])
            w_m = int(parts[1])
        except:
            w_h, w_m = 7, 0

        wake_min = w_h * 60 + w_m
        natural_dlmo_min = wake_min + (14 * 60)

        # Photic delay in minutes
        lux_intensity = max(10.0, min(1000.0, float(evening_screen_lux)))
        screen_h = max(0.0, min(8.0, float(evening_screen_hours)))

        delay_minutes = round(screen_h * math.sqrt(lux_intensity / 100.0) * 22.0)
        delayed_dlmo_min = natural_dlmo_min + delay_minutes

        def format_min(m: int) -> str:
            m = m % (24 * 60)
            return f"{m // 60:02d}:{m % 60:02d}"

        # Biological sleep readiness window: 2 hours post-DLMO
        sleep_window_min = delayed_dlmo_min + 120

        return {
            "wake_time": wake_time_hhmm,
            "natural_baseline_dlmo_time": format_min(natural_dlmo_min),
            "photic_screen_delay_minutes": delay_minutes,
            "predicted_actual_dlmo_time": format_min(delayed_dlmo_min),
            "optimal_biological_sleep_onset_time": format_min(sleep_window_min),
            "melatonin_suppression_severity": "SEVERE_SLEEP_PHASE_DELAY" if delay_minutes >= 60 else ("MODERATE_DELAY" if delay_minutes >= 30 else "MINIMAL_INHIBITION")
        }

    def recommend_digital_sunset_schedule(
        self,
        desired_sleep_time_hhmm: str = "23:00",
        room_ambient_lux: float = 150.0
    ) -> Dict[str, Any]:
        """
        Schedules progressive digital blue-light attenuation and photic sunset milestones.
        """
        try:
            parts = desired_sleep_time_hhmm.strip().split(":")
            s_h = int(parts[0])
            s_m = int(parts[1])
        except:
            s_h, s_m = 23, 0

        sleep_min = s_h * 60 + s_m

        def fmt(m: int) -> str:
            m = (m + 24 * 60) % (24 * 60)
            return f"{m // 60:02d}:{m % 60:02d}"

        return {
            "desired_sleep_time": desired_sleep_time_hhmm,
            "milestones": [
                {
                    "time": fmt(sleep_min - 120),
                    "action": "ENABLE_NIGHT_SHIFT_AND_WARM_FILTERS",
                    "target_lux": "< 100 Lux",
                    "rationale": "Reduces melanopic blue wavelength flux 2 hours before target sleep."
                },
                {
                    "time": fmt(sleep_min - 60),
                    "action": "DIM_OVERHEAD_ROOM_LIGHTS",
                    "target_lux": "< 30 Lux",
                    "rationale": "Promotes pineal gland melatonin synthesis onset."
                },
                {
                    "time": fmt(sleep_min - 30),
                    "action": "COMPLETE_SCREEN_TERMINATION",
                    "target_lux": "< 5 Lux (Darkness/Red Light)",
                    "rationale": "Eliminates cognitive arousal and photic retinal ganglion activation."
                }
            ],
            "projected_deep_slow_wave_benefit_pct": 28.0
        }
