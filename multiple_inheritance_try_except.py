class IT_Department:
    def number_of_employes(self):
        print("50")

class Dev:
    def number_of_dev(self):
        print("40")

class QA:
    def number_of_qa(self):
        print("5")

class BA:
    def number_of_ba(self):
        print("3")

class PM:
    def number_of_pm(self):
        print("2")


class Service_Associate(Dev, QA, BA):
    def making_coffee(self):
        print("Coffee")

orlando = Service_Associate()
orlando.number_of_dev()
orlando.number_of_ba()
orlando.number_of_qa()

try:
    orlando.number_of_PM()

except Exception:
    print("orlando dont like to support PM")

finally:
    print("Close the test")