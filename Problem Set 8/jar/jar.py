class Jar:
    def __init__(self, capacity=12): # capacity is an attrivute which will be returned in the getter
        self._capacity = capacity # capacity is the maximum number of cookies a jar can take
        self._size = 0 # size is how many cookies there are in the jar (an attribute which will be returned in the getter)
        if capacity < 0:
            raise ValueError



    def __str__(self):
        return '🍪' * self._size



    def deposit(self, n = int):
        # if we try to add more that 12 cookies (jar capacity)
        if n > self.capacity:
            raise ValueError('Too much cookies, the jar capacity is 12...Try to take less cookies')
        # if the cookies already in the jar plus the onews we add are more than 12 (jar capacity)
        if self.size + n > self.capacity:
            raise ValueError('Too much cookies, the jar capacity is 12...Try to take less cookies')
        # add cookies to the jar
        # it has to come at the end, because if we put before the if condition, and deposit more cookies than those available, python
        # raises an error as it does't get to the if condition before
        self._size += n




    def withdraw(self, n = int):
        # if I want to remove more cookies that those already in the jar
        if self.size < n:
            raise ValueError('Not enough cookies in the jar...Try to take less cookies')
        # if all well...deduct cookies from the jar...it has to come at the end, because if we put before the if condition, and deduct
        # more cookies than those available python raises an error as it does't get to the if condition before
        self._size -= n



# The getter methods are used to retrieve the values of the private attributes in a controlled manner, without exposing the private
# attributes directly to the external user of the class.
# By using getter and setter methods, we can expose only the necessary properties of an object to the outside world

# Bellow we have 2 getters...
# A setter would be defined using the @propertyname.setter decorator, and would allow to set the value of an attribute

# Getters can also be used to perform some additional computation or validation before returning the value, but here just return a value

# Getter
    @property
    def capacity(self):
        return self._capacity


# Getter
    @property
    def size(self):
        return self._size

