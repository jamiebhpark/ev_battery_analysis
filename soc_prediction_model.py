import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from pre_processing import data

# SoC를 예측 목표로 설정 (임의의 계산식 사용)
# 실제 SoC 데이터를 사용할 수 없는 경우 대체 계산
data['SoC'] = 100 - (data['Voltage_measured'] / data['Voltage_measured'].max() * 100)

# 입력(X)과 출력(y) 정의
X = data[['Voltage_measured', 'Current_measured']]
y = data['SoC']

# 학습용/테스트용 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 회귀 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 모델 예측
y_pred = model.predict(X_test)

# 결과 평가
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# 예측 결과 시각화
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel('Actual SoC')
plt.ylabel('Predicted SoC')
plt.title('Actual vs Predicted SoC')
plt.show()

# 온도 변화에 따른 SoC 시뮬레이션
temperature_profiles = [0, 25, 50]  # 다양한 온도 시나리오
for temp in temperature_profiles:
    # 온도 변화에 따른 전류 조정
    temp_adjusted_current = data['Current_measured'] * (1 + temp * 0.01)
    soc_simulated = model.predict(pd.DataFrame({
        'Voltage_measured': data['Voltage_measured'],
        'Current_measured': temp_adjusted_current
    }))
    plt.plot(data['Time_minutes'], soc_simulated, label=f'Temperature: {temp}°C')

plt.xlabel('Time (minutes)')
plt.ylabel('Simulated SoC')
plt.title('SoC under Different Temperature Scenarios')
plt.legend()
plt.show()
