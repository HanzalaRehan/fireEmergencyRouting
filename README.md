
# Fire Emergency Routing

Fire Emergency Routing is a Python-based application that calculates the optimal routes for fire trucks to respond to emergencies in a metropolitan area. The program uses the **A\* search algorithm** to determine the shortest path between fire stations and emergency locations while accounting for traffic conditions at specific times.

---

## Features

- **A\* Search Algorithm**: Implements A* to find the most time-efficient routes.
- **Traffic-Aware Routing**: Considers road conditions and speeds at specific times.
- **Multiple Fire Stations**: Supports routing from two predefined fire stations.
- **Emergency Call Handling**: Processes a list of emergency calls with time-stamped locations.
- **Detailed Results**: Outputs emergency details, response times, and preferred fire station in a tabular format.
- **CSV Export**: Saves results as a CSV file for further analysis.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/HanzalaRehan/fireEmergencyRouting.git
   cd fireEmergencyRouting
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that Python 3.11 or later is installed on your system.

---

## Usage

1. **Prepare Traffic Data**:
   - Ensure the `roads.csv` file contains traffic data with columns for `Start`, `End`, `Time`, and `Speed`.

2. **Edit Emergency Calls**:
   - Modify the `EMERGENCY_CALLS` list in the `main.py` file to include emergency locations and times:
     ```python
     EMERGENCY_CALLS = [
         ((2, 9), '12:00'),  # Example emergency at location (2, 9) at 12:00 PM
         ((5, 5), '15:00'),  # Another emergency at (5, 5) at 3:00 PM
     ]
     ```

3. **Run the Program**:
   ```bash
   python main.py
   ```

4. **View Results**:
   - The program will print the results in the terminal and save them to `emergency_calls_summary.csv`.

---

## Example Output

### Terminal Output:
```
Call: ((2, 9), '12:00'), Time1: 4.32, Time2: Traffic Blocked
Emergency Location    Time Preferred Station Time from Station 1 Time from Station 2
(2, 9)                12:00 Fire Station 1    4.32               Traffic Blocked
```

### CSV Output:
| Emergency Location | Time   | Preferred Station | Time from Station 1 | Time from Station 2 |
|---------------------|--------|-------------------|----------------------|----------------------|
| (2, 9)             | 12:00 | Fire Station 1    | 4.32                | Traffic Blocked      |

---

## Project Structure

```plaintext
fireEmergencyRouting/
├── main.py             # Main entry point for the application
├── road.py             # Handles road and traffic data
├── search.py           # Implements A* search algorithm
├── roads.csv           # Traffic data (user-provided)
├── requirements.txt    # Python dependencies
└── emergency_calls_summary.csv  # Output file (generated)
```

---

## Contributing

Contributions are welcome! If you have suggestions or find a bug, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

- **Author**: Hanzala B. Rehan
- **GitHub**: [HanzalaRehan](https://github.com/HanzalaRehan)
