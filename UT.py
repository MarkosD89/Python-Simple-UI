#############################################################################################
# This code is property of the individual created:
# All rights to the code are reserved
# Unothorized use, disctrubution or any adaptation of the code will result in ligal actions
#############################################################################################

#region ----------------------- Imports -------------------------

import Dependencies.DataHandler as DH
import Dependencies.UIModule as UI
import Dependencies.PlottingData as PTD

# Unit Test Imports
import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
#endregion

class TestDevice(unittest.TestCase):

    def test_device_initialization(self):
        # Mock the `Device.Get_data` and `Device.Get_x_y` methods
        with patch.object(DH.Device, 'Get_data', return_value=pd.DataFrame({'test': [1, 2, 3]})) as mock_get_data, \
             patch.object(DH.Device, 'Get_x_y', return_value=(100, 200)) as mock_get_xy:
            
            device = DH.Device(Filepath="Data.csv", index=1, passed=True)

            # Ensure that the methods are being called during initialization
            mock_get_data.assert_called_once_with("Data.csv")
            mock_get_xy.assert_called_once_with("Data.csv")
            
            # Check if the attributes are correctly set
            self.assertEqual(device.index, 1)
            self.assertEqual(device.locationxy, (100, 200))
            self.assertTrue(device.passed)
    
    def test_repr(self):
        # Create a device object
        device = DH.Device(Filepath="Data.csv", index=2, passed=False)
        
        # Check the string representation
        self.assertEqual(str(device), "Device index: 2 located: (100, 200) and device passed the test False")

    def test_passed_property_setter(self):
        # Test the setter of the 'passed' property
        device = DH.Device(Filepath="Data.csv", index=3, passed=False)
        
        # Set to true with admin rights
        device.passed = (True, True)
        self.assertTrue(device.passed)

        # Set to false without admin rights
        device.passed = (True, False)
        self.assertFalse(device.passed)

        # Set with wrong input (tuple with one value)
        device.passed = (True,)  # Should print error message
        self.assertFalse(device.passed)

    def test_invalid_file_format(self):
        # Test handling invalid file format in `Get_data`
        with patch.object(DH.Device, 'Get_data', side_effect=Exception("Data not in the correct format")):
            device = DH.Device(Filepath="invalid_file.csv", index=4, passed=False)
            self.assertIsNone(device.df)

    def test_get_xy_invalid(self):
        # Test invalid file path handling in `Get_x_y`
        with patch.object(DH.Device, 'Get_x_y', return_value=("N/a", "N/a")):
            device = DH.Device(Filepath="invalid_file.csv", index=5, passed=False)
            self.assertEqual(device.locationxy, ("N/a", "N/a"))

if __name__ == '__main__':
    unittest.main()
