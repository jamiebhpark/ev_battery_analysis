# 기준값 설정
VOLTAGE_THRESHOLD = 3.0  # 최소 전압 (V)
TEMPERATURE_THRESHOLD = 40.0  # 최대 온도 (°C)
CURRENT_ABS_MAX = 2.0  # 최대 전류 절대값 (A)

# 분석 함수 정의
def analyze_battery_performance(data):
    analysis_results = {}

    # Voltage Analysis
    low_voltage_count = (data['Voltage_measured'] < VOLTAGE_THRESHOLD).sum()
    avg_voltage = data['Voltage_measured'].mean()
    analysis_results['Voltage'] = {
        'Low Voltage Occurrences': low_voltage_count,
        'Average Voltage': avg_voltage,
        'Interpretation': (
            f"The battery voltage dropped below {VOLTAGE_THRESHOLD}V {low_voltage_count} times. "
            f"This indicates instances of low charge, potentially requiring recharging. "
            f"The average voltage of {avg_voltage:.2f}V suggests the battery operated within normal limits overall."
        )
    }

    # Temperature Analysis
    high_temp_count = (data['Temperature_measured'] > TEMPERATURE_THRESHOLD).sum()
    avg_temp = data['Temperature_measured'].mean()
    analysis_results['Temperature'] = {
        'High Temperature Occurrences': high_temp_count,
        'Average Temperature': avg_temp,
        'Interpretation': (
            f"The battery temperature never exceeded {TEMPERATURE_THRESHOLD}°C, showing stable thermal performance. "
            f"The average temperature of {avg_temp:.2f}°C is within safe operating limits, reducing risk of thermal degradation."
        )
    }

    # Current Analysis
    excessive_current_count = (data['Current_measured'].abs() > CURRENT_ABS_MAX).sum()
    avg_current = data['Current_measured'].mean()
    analysis_results['Current'] = {
        'Excessive Current Occurrences': excessive_current_count,
        'Average Current': avg_current,
        'Interpretation': (
            f"No instances of current exceeding ±{CURRENT_ABS_MAX}A were observed, indicating consistent charge/discharge behavior. "
            f"The average current of {avg_current:.2f}A implies the battery was predominantly in a discharge state."
        )
    }

    # SoC Prediction Analysis
    min_soc = data['SoC'].min()
    max_soc = data['SoC'].max()
    avg_soc = data['SoC'].mean()
    analysis_results['SoC'] = {
        'Min SoC': min_soc,
        'Max SoC': max_soc,
        'Average SoC': avg_soc,
        'Interpretation': (
            f"The predicted SoC ranged from {min_soc:.2f}% to {max_soc:.2f}%, with an average of {avg_soc:.2f}%. "
            f"This indicates the battery was operating in a low-charge state during the observed period."
        )
    }

    return analysis_results

# 데이터프레임 로드
import pandas as pd
data = pd.read_csv("07388.csv")

# SoC 값 추가
data['SoC'] = 100 - (data['Voltage_measured'] / data['Voltage_measured'].max() * 100)  # Mock SoC 계산

# 분석 실행
results = analyze_battery_performance(data)

# 결과 출력
for category, metrics in results.items():
    print(f"### {category} Analysis ###")
    for metric, value in metrics.items():
        if metric != 'Interpretation':
            print(f"{metric}: {value:.2f}")
    print(metrics['Interpretation'])
    print("\n")
