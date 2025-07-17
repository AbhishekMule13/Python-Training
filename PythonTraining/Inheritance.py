class person:
    def __init__(self, name, address, qulification):
        self.name=name
        self.address=address
        self.qulification= qulification

    def display_info(self):
        print("-----Personal Info-----")
        print(f"Name = {self.name}")
        print(f"Address = {self.address}")
        print(f"Qulification = {self.qulification}")


class employee(person):
    def __init__(self, name, address, qulification, employee_id):
        super().__init__(name, address, qulification)
        self.employee_id=employee_id

    def display_employee(self):
         self.display_info()
         print(f"Employee_id = {self.employee_id}")


def main():
    a= employee('Abhishek', 'Kavalapur', '12th', 'E5454' )
    a.display_employee()

if __name__=="__main__":
    main()

                  
    


        