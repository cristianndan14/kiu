import unittest


class Airline:
    def __init__(self):
        self.packages = []
        self.price_per_package = 10

    def add_package(self, package):
        self.packages.append(package)

    def generate_report(self, date):
        total_packages = 0
        total_revenue = 0
        for package in self.packages:
            if package.date == date:
                total_packages += 1
                total_revenue += self.price_per_package
        return (total_packages, total_revenue)


class Package:
    def __init__(self, date):
        self.date = date


class TestAirline(unittest.TestCase):
    def test_add_package(self):
        airline = Airline()
        package1 = Package("2023-09-01")
        package2 = Package("2023-09-01")
        package3 = Package("2023-09-02")
        airline.add_package(package1)
        airline.add_package(package2)
        airline.add_package(package3)
        self.assertEqual(len(airline.packages), 3)

    def test_generate_report(self):
        airline = Airline()
        package1 = Package("2023-09-01")
        package2 = Package("2023-09-01")
        package3 = Package("2023-09-02")
        airline.add_package(package1)
        airline.add_package(package2)
        airline.add_package(package3)
        report = airline.generate_report("2023-09-01")
        self.assertEqual(report, (2, 20))


if __name__ == "__main__":
    unittest.main()