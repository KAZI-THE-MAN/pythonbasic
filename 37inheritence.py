#vdo 55
#inheritence

class phone:
    def call(self):
        print("you can call")
    def message(self):
        print("you can message")
class samsung(phone):
    def photo(self):
        print("you can take photo")

s=samsung()
s.call()
s.message()
s.photo()

