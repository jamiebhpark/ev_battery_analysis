import matplotlib.pyplot as plt

from pre_processing import data

# 데이터 시각화
plt.figure(figsize=(14, 8))

# Voltage over Time
plt.subplot(3, 1, 1)
plt.plot(data['Time_minutes'], data['Voltage_measured'], label='Voltage Measured')
plt.xlabel('Time (minutes)')
plt.ylabel('Voltage (V)')
plt.title('Voltage over Time')
plt.legend()

# Current over Time
plt.subplot(3, 1, 2)
plt.plot(data['Time_minutes'], data['Current_measured'], label='Current Measured', color='orange')
plt.xlabel('Time (minutes)')
plt.ylabel('Current (A)')
plt.title('Current over Time')
plt.legend()

# Temperature over Time
plt.subplot(3, 1, 3)
plt.plot(data['Time_minutes'], data['Temperature_measured'], label='Temperature Measured', color='green')
plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature over Time')
plt.legend()

plt.tight_layout()
plt.show()
