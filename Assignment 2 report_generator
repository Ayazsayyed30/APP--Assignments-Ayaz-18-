import datetime

def add_border(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        line = "=" * 40
        return f"{line}\n{res}\n{line}"
    return wrapper

def make_upper(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

class Report:
    count = 0

    def __init__(self, title, created_by):
        self.title = title
        self.created_by = created_by
        self.data = []
        self.date = datetime.datetime.now()
        Report.count += 1

    def __iadd__(self, text):
        self.data.append(text)
        return self

    def __len__(self):
        return len(self.data)

    def __str__(self):
        body = ""
        for item in self.data:
            body += f" -> {item}\n"
        
        return f"Title: {self.title}\nBy: {self.created_by}\nDate: {self.date.strftime('%d-%m-%Y')}\n\nContent:\n{body}"

    @classmethod
    def create_sales_report(cls, created_by):
        rep = cls("Monthly Sales", created_by)
        rep += "Revenue report"
        rep += "Expenses report"
        rep += "Profit calculation"
        return rep

    @classmethod
    def total_reports(cls):
        return cls.count

    @add_border
    @make_upper
    def generate(self):
        return str(self)

if __name__ == "__main__":
    r1 = Report("Audit Report", "Rahul")
    r1 += "Checked all systems"
    r1 += "Updated security"
    
    print(r1.generate())
    print("Total lines:", len(r1))
    print("\n")

    r2 = Report.create_sales_report("Amit")
    r2 += "Added next month targets"
    print(r2.generate())
    print("Total lines:", len(r2))
    
    print("\nTotal reports made:", Report.total_reports())
