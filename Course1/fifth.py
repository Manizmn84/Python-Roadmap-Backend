class Drug:
    def __init__(self, name: str, amount: int, price: int):
        self.name = name 
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name: str):
        self.name = name
        self.drugs = []
        self.employees = []

    def add_drug(self, drug: Drug):
        self.drugs.append(drug)

    def add_employee(self, first_name: str, last_name: str, age: int):
        self.employees.append({
            "first_name" : first_name,
            "last_name" : last_name,
            "age" : age
        })

    def total_value(self) -> int:
        return sum([drug.price * drug.amount for drug in self.drugs ])

    def employees_summary(self) -> str:
        return "Employees:\n" + "\n".join([
            f"The employee number {index + 1} is {employee['first_name']} {employee['last_name']} who is {employee['age']} years old."
            for index, employee in enumerate(self.employees)
        ]) + "\n"

class ExceptionProxy(Exception):
    def __init__(self, message, function):
      self.message = message
      self.function = function
      super().__init__(message)


def transform_exceptions(func_ls: list) -> list[ExceptionProxy]:
    listProxy = []
    for func in func_ls :
        try:
            func()
            objectExceptionProxy = ExceptionProxy("ok!",func)
            listProxy.append(objectExceptionProxy)
        except Exception as err:
            objectExceptionProxy = ExceptionProxy(str(err),func)
            listProxy.append(objectExceptionProxy)
    return listProxy
            
            
