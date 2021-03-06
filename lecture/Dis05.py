class Instructor:
    degree = "PhD (Magic)" # this is a class attribute
    def __init__(self, name):
        self.name = name # this is an instance attribute
    def lecture(self, topic):
        print("Today we're learning about " + topic)
dumbledore = Instructor("Dumbledore")
class Student:
    instructor = dumbledore
    def __init__(self, name, ta):
        self.name = name
        self.understanding = 0
        ta.add_student(self)
    def attend_lecture(self, topic):
        Student.instructor.lecture(topic)
        if Student.instructor == dumbledore:
            print(Student.instructor.name + " is awesome!")
        else:
            print("I miss Dumbledore.")
        self.understanding += 1
    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)
class TeachingAssistant:
    def __init__(self, name):
        self.name = name
        self.students = {}
    def add_student(self, student):
        self.students[student.name] = student
    def assist(self, student):
        student.understanding += 1

def test():
    """
    >>> snape = TeachingAssistant("Snape")
    >>> harry = Student("Harry", snape)
    >>> harry.attend_lecture("potions")
    Today we're learning about potions
    Dumbledore is awesome!
    >>> hermione = Student("Hermione", snape)
    >>> hermione.attend_lecture("herbology")
    Today we're learning about herbology
    Dumbledore is awesome!
    >>> hermione.visit_office_hours(TeachingAssistant("Hagrid"))
    Thanks, Hagrid
    >>> harry.understanding
    1
    >>> snape.students["Hermione"].understanding
    2
    >>> Student.instructor = Instructor("Umbridge")
    >>> Student.attend_lecture(harry, "transfiguration")
    Today we're learning about transfiguration
    I miss Dumbledore.
    """
    return None

#2
class Email:
    """
    Every email object has 3 instance attributes:
    the message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.message = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Mailman:
    """Each Mailman has an instance attribute clients,
    which is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}
    def send(self, email):
        """
        Take an email and put it in the inbox of the client it is addressed to.
        """
        self.clients[email.recipient_name].receive(email)


    def register_client(self, client, client_name):
        """
        Takes a client object and client_name and adds it to the clients instance attribute.
        """
        self.clients[client_name] =  client

class Client:
    """Every Client has instance attributes name
    (which is used for addressing emails to the client),
    mailman (which is used to send emails out to other clients),
    and inbox (a list of all emails the client has received).
    """
    def __init__(self, mailman, name):
        self.inbox = []
        self.mailman = mailman
        self.name = name
        mailman.register_client(self, self.name)
    def compose(self, msg, recipient_name):
        """
        Send an email with the given message msg to the given recipient client.
        """
        return Email(msg,self.name, recipient_name)


    def receive(self, email):
        """
        Take an email and add it to the inbox of this client.
        """
        self.inbox.append(email)
        return

#3
class Dog(object):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name + " says woof!")
class Cat(object):
    def __init__(self, name, owner, lives=9):
        self.name = name
        self.owner = owner
        self.lives = lives
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name + " says meow!")


class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

class Dog(Pet):
    def __init__(self, name, owner):
        Pet.__init__(self, name, owner)
    def talk(self):
        print(self.name + ' says woof!')

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives
    def talk(self):
        """A cat says meow! when asked to talk."""
        print(self.name + ' says meow!')
    def lose_life(self):
        """A cat can only lose a life if they have at
        least one life. When lives reaches zero, 'is_alive' becomes False.
        """
        if self.lives >= 1:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print('the cat is already died!')

class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        Cat.__init__(self, name, owner, lives)

    def talk(self):
        """Repeat what a Cat says twice."""
        Cat.talk(self)
        Cat.talk(self)

#4
class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)
class B(A):
    def f(self):
        return 4

#2.4

class Yolo:
    def __init__(self, n):
        self.motto = n
    def g(self, n):
        return n+self.motto

def test():
    """
    >>> x = Yolo(1)
    >>> x.g(3)
    4
    >>> x.g(5)
    6
    >>> x.motto = 5
    >>> x.g(5)
    10
    """
    return
