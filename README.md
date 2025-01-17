## EV Battery Data Analysis & BMS Simulation

---

### **1. Project Overview**

**Project Name**: EV Battery Data Analysis & BMS Simulation

**Objective**:
To analyze the charging and discharging behavior of EV batteries, predict State of Charge (SoC), and simulate the performance of a Battery Management System (BMS). The goal is to enhance battery performance, ensure safety, and develop insights into battery health through data-driven methods.

**Key Achievements**:
- Conducted a detailed analysis of EV battery data, including voltage, current, temperature, and SoC.
- Simulated charging/discharging scenarios and observed battery performance under various conditions.
- Built an interactive Streamlit dashboard to visualize results and provide actionable insights.

---

### **2. Data and Methodology**

**Data Source**:
- NASA Battery Dataset (via Kaggle)
- Data includes voltage (V), current (A), temperature (°C), and time (s).

**Analysis Approach**:
1. **Data Preprocessing**:
   - Cleaned and transformed raw CSV data.
   - Calculated State of Charge (SoC) using normalized voltage values.

2. **Exploratory Data Analysis**:
   - Visualized voltage, current, and temperature trends over time.
   - Identified anomalies and performance patterns.

3. **Modeling**:
   - Used regression models to predict SoC based on voltage and current.
   - Simulated battery behavior under various operational scenarios.

4. **Visualization**:
   - Built interactive graphs and dashboards to present key findings.

---

### **3. Key Findings**

#### **1) Voltage Analysis**
- **Low Voltage Occurrences**: 21 times
- **Average Voltage**: 3.41V

**Interpretation**:
- Voltage dropped below the threshold (3.0V) 21 times, indicating instances of low charge.
- The average voltage was within normal operating limits, ensuring safe operation.

---

#### **2) Temperature Analysis**
- **High Temperature Occurrences**: 0 times
- **Average Temperature**: 11.54°C

**Interpretation**:
- No instances of overheating (above 40°C) were observed, demonstrating excellent thermal stability.
- The average operating temperature was safe, reducing risks of thermal degradation.

---

#### **3) Current Analysis**
- **Excessive Current Occurrences**: 0 times
- **Average Current**: -1.61A

**Interpretation**:
- No excessive current events (±2A threshold) occurred, indicating stable charge/discharge cycles.
- Negative average current suggests the battery was primarily in a discharge state.

---

#### **4) SoC Analysis**
- **Min SoC**: 0.0%
- **Max SoC**: 40.97%
- **Average SoC**: 18.91%

**Interpretation**:
- The battery operated in a low-charge state, with an average SoC of 18.91%.
- Enhancements to charging strategies or BMS logic could optimize performance.

---

### **4. Dashboard Overview**

**Features**:
- **Data Upload**: Users can upload battery CSV files for analysis.
- **Interactive Visualization**:
  - Voltage, current, and temperature trends over time.
  - SoC predictions and their relationship with operational conditions.
- **Customizable Simulations**:
  - Analyze battery behavior under varying temperature and load conditions.

**Tools**:
- Built using Streamlit for real-time interactivity.

---

### **5. Tools and Technologies**

- **Programming Languages**: Python (pandas, numpy, matplotlib, scikit-learn, streamlit)
- **Development Environment**: PyCharm, Windows 11
- **Data Source**: NASA Battery Dataset

---

### **6. Conclusion and Future Work**

**Conclusion**:
This project successfully analyzed EV battery performance and demonstrated the potential for data-driven insights to improve BMS design. The findings provide actionable recommendations for enhancing battery safety, efficiency, and reliability.

**Future Work**:
1. **Advanced Modeling**:
   - Implement LSTM models for more accurate SoC and State of Health (SoH) predictions.
2. **Real-world Testing**:
   - Validate models using real-world battery data.
3. **Scenario Expansion**:
   - Simulate extreme conditions (e.g., rapid charging, deep discharge).

---

### **7. Repository and Deployment**

**GitHub Repository**: [Link to Project Repository]
- Contains all analysis code, documentation, and sample data.

**Live Dashboard**: [Link to Streamlit Deployment]
- Interactive dashboard for exploring analysis results.

---

This portfolio showcases my expertise in EV battery data analysis, machine learning modeling, and dashboard development, highlighting my ability to apply data-driven solutions to complex engineering challenges.

