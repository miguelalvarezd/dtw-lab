from src.dtw_lab.lab2 import calculate_statistic, get_statistic
from src.dtw_lab.lab1 import encode_categorical_vars
import pandas as pd

def test_calculate_statistic():
    """
    Test the calculate_statistic function.
    We create a DataFrame with some values and check if the function returns the expected values.
    """
    df = pd.DataFrame({"Charge_Left_Percentage": [39, 60, 30, 30, 41]})
    assert calculate_statistic("mean", df["Charge_Left_Percentage"]) == 40
    assert calculate_statistic("median", df["Charge_Left_Percentage"]) == 39
    assert calculate_statistic("mode", df["Charge_Left_Percentage"]) == 30

def test_encode_categorical_vars():
    """
    Test the encode_categorical_vars function.
    We create a DataFrame with some categorical variables and check if the function returns the expected
    DataFrame.
    """
    df = pd.DataFrame({
        "Manufacturer": ["Sony", "Panasonic", "Sony"],
        "Battery_Size": ["AAA", "AA", "C"],
        "Discharge_Speed": ["Slow", "Medium", "Fast"]
    })

    df_result = pd.DataFrame({
        "Battery_Size": [1, 2, 3],
        "Discharge_Speed": [1, 2, 3],
        "Manufacturer_Panasonic": [False, True, False],
        "Manufacturer_Sony": [True, False, True]
    })

    print(encode_categorical_vars(df))

    for i in range(len(df_result.columns)):
        for j in range(len(df_result)):
            assert encode_categorical_vars(df)[df_result.columns[i]][j] == df_result[df_result.columns[i]][j]

def test_get_statistic(mocker):
    """
    Test the get_statistic function. 
    We mock the read_csv_from_google_drive function to return a DataFrame with the expected values.
    We then check if the function returns the expected result.
    """
    mock_get = mocker.patch("src.dtw_lab.lab2.read_csv_from_google_drive")
    mock_get.return_value = pd.DataFrame({
        "Charge_Left_Percentage": [39, 60, 30, 30, 41],
        "Serial_Number": [1, 2, 3, 4, 5],
        "Voltage_Cutoff": [1, 1, 1, 1, 1],
        "Nominal_Voltage": [3.5, 4.5, 5.5, 6.5, 7.5],
        "Avg_Operating_Temperature": [20, 30, 40, 50, 60],
        "Days_Since_Production": [1, 2, 3, 4, 5],
        "Current_Voltage": [1, 1, 1, 1, 1],
        "Battery_Size": ["AAA", "AA", "C", "D", "AAA"],
        })

    result = get_statistic("mean", "Charge_Left_Percentage")

    assert result == {"message": "The mean for the Charge_Left_Percentage column is 40.0"}
    assert mock_get.called
    mock_get.assert_called_once()

