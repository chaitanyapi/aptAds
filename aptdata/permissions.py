from rest_framework.permissions import BasePermission

class CanViewThisPage(BasePermission):
	"""docstring for CanViewThisPage"""
	def __init__(self, arg):
		super (CanViewThisPage, self).__init__()
		self.arg = arg
