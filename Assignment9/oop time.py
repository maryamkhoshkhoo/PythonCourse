class time():

    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def sum(self, mehman):
        result = time(None, None, None)
        result.second = self.second + mehman.second
        result.minute = self.minute + mehman.minute
        result.hour = self.hour + mehman.hour
        
        if result.second >= 60:
            result.second -= 60
            result.minute += 1
        
        if result.minute >= 60:
            result.minute -= 60
            result.hour += 1
            
        return result

    def sub(self, mehman):
        result = time(None, None, None)
        result.hour = self.hour - mehman.hour
        result.minute = self.minute - mehman.minute
        result.second = self.second - mehman.second
        
        if result.second < 0 :
            result.second += 60
            result.minute -= 1

        if result.minute < 0 :
            result.minute += 60
            result.hour -= 1    

        return result
        

    def sec_to_time(self):
        result = time(None, None, None)
        result.hour = self.second // 3600
        result.minute = (self.second % 3600) // 60
        result.second = (self.second % 3600) % 60
        return result

    def time_to_sec(self):
        result = time(None, None, None)
        result.hour = 0
        result.minute = 0
        result.second = self.second + self.minute * 60 + self.hour * 3600
        return result

    def show(self):
        print(self.hour, ':', self.minute, ':', self.second)

        
a = time(2, 30, 55)
b = time(3, 40, 10)
    
        
c = a.sum(b)
c.show()


d = b.sub(a)
d.show()


e = a.time_to_sec()
e.show()

f = e.sec_to_time()
f.show() 


    