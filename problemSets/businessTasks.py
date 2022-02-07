##Business Tasks - SRM 236 Div 1 (SOLVED)
##https://www.topcoder.com/thrive/articles/How%20To%20Find%20a%20Solution
#the loop is actually NOT the length of the word but until the length of the list is equal to 1
#so the while loop is sufficient
#n is a counter and less an iterator through the word, that way the count is constand and not dependent on#the length or index of the list

class BusinessTasks: 
    
    def __init__(self, tasks, number, count = 0):
        self.tasks = tasks
        self.number = number
        self.count = count
    
    def getTask(self):
        t = self.tasks
        n = self.number
        c = self.count
        while len(t) > 1:
            for i in t:
                c += 1
                if c == (n):
                    c = 1
                    t.remove(i)
                    print('tasks now: ', t)
        return t[0]
                    

input_string = input('enter your list of strings: ')
userList = input_string.split()
print('userList: ', userList)
u_n = int(input('enter n: '))
finalTask = BusinessTasks(userList, u_n)
print(finalTask.getTask())
