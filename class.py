# Class vs Instance Attributes in Python

class Website:
  def __init__(self, title):
    self.title = title

# instance attributes

ws = Website('My Website Title')
print(ws.__dict__)

ws_two = Website('My Second Title')
print(ws_two.__dict__)

# class attributes

class DifferentWebsite:
  title = 'My Class Title'

dw = DifferentWebsite()
print(dw.title)

dw_two = DifferentWebsite()
print(dw_two.title)


# Introduction to Inheritance in Python

class User:
  def __init__(self, email, first_name, last_name):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name

  def greeting(self):
    return f'Hi {self.first_name} {self.last_name}'

class AdminUser(User):
  def active_users(self):
    return '500'


tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')

kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')

print(tiffany.active_users())
print(tiffany.greeting())
print(kristine.greeting())
# print(kristine.active_users())


# Using Polymorphism to Build an HTML Generator in Python
# if you have shared custom behaviours use this

class Html:
    def __init__(self, content):
        self.content = content

    def render(self):             
        raise NotImplementedError("Subclass must implement render method")


class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'


class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'


tags = [Div('Some content'), Heading('My Amazing Heading'), Div('Another div')]

for tag in tags:
    print(str(tag) + ': ' + tag.render())
    print(tag.render())


# Building Polymorphic Functions in Python
# if you don't have a lot of shared behaviour use this

class Heading:
    def __init__(self, content):
      self.content = content

    def render(self):
      return f'<h1>{self.content}</h1>'

class Div:
  def __init__(self, content):
    self.content = content

  def render(self):
    return f'<div>{self.content}</div>'

div_one = Div('Some content')
heading = Heading('My Amazing Heading')
div_two = Div('Another div')

def html_render(tag_object):
  print(tag_object.render())

html_render(div_one)
html_render(div_two)
html_render(heading)