class Car:
    #クラス変数
    maker = "PEACE" #自動車メーカ
    count = 0 #台数

    @classmethod
    def countup(cls):
        cls.count += 1
        print(f"出荷台数:{cls.count}")

    def __init__(self, color = "white"):
        Car.countup()
        self.mynumber = Car.count
        self.color = color
        self.mileage = 0
    
    def drive(self, km):
        self.mileage += km
        msg = f"{km}kmドライブしました。総距離は{self.mileage}kmです。"
        print(msg)