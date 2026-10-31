# -*- coding: utf-8 -*-
import json
from client import PersonalAgentCircadianLuxMelatoninOnset

chronobiology = PersonalAgentCircadianLuxMelatoninOnset()

print("=" * 64)
print("DEMO: Personal Circadian Lux & Melatonin Onset Architect")
print("=" * 64)

# 1. Photic Lux Integral
exposure = [
    {"time": "07:30", "lux": 25000.0, "duration_minutes": 20.0, "source": "Morning Sunlight Walk"},
    {"time": "09:00", "lux": 600.0, "duration_minutes": 180.0, "source": "Office Desk"},
    {"time": "20:00", "lux": 300.0, "duration_minutes": 120.0, "source": "Laptop / Phone Screens"}
]
dose = chronobiology.calculate_cumulative_photic_lux_dose(exposure)
print(f"\n1. Photic Lux Dose:")
print(f"   Morning Lux Dose: {dose['morning_lux_minutes']:,} lux-mins ({dose['morning_target_attainment_pct']}% of target)")
print(f"   Circadian Anchor: {dose['circadian_synchronization_status']}")

# 2. Predict DLMO shift
dlmo = chronobiology.predict_dim_light_melatonin_onset(wake_time_hhmm="07:00", evening_screen_lux=350.0, evening_screen_hours=3.5)
print(f"\n2. Melatonin Onset Prediction:")
print(f"   Natural DLMO: {dlmo['natural_baseline_dlmo_time']} -> Actual Delayed DLMO: {dlmo['predicted_actual_dlmo_time']}")
print(f"   Photic Delay: +{dlmo['photic_screen_delay_minutes']} min ({dlmo['melatonin_suppression_severity']})")
print(f"   Optimal Sleep Window: {dlmo['optimal_biological_sleep_onset_time']}")

# 3. Progressive Digital Sunset
sunset = chronobiology.recommend_digital_sunset_schedule("23:30")
print(f"\n3. Digital Sunset Protocol for {sunset['desired_sleep_time']} Bedtime:")
for m in sunset["milestones"]:
    print(f"   [{m['time']}] {m['action']} ({m['target_lux']})")
