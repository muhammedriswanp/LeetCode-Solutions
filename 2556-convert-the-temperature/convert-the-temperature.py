class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        Fahrenheit = celsius * 1.80 + 32.00
        Kelvin = celsius + 273.15

        return Kelvin,Fahrenheit