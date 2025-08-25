def main():
    print("Hello World")
if __name__ == "__main__":
    main()

class Doniko:
    def __init__(self, name):
        self.name = name

    def Get_info(self):
        return self.name
D = Doniko('Daniel')
print(D.Get_info())