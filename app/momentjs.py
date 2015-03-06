from jinja2 import Markup

class momentjs(object):
	def __init__(self, timestamp):
		self.timestamp = timestamp

	def render(self, format):
		script = "<script>\ndocument.write(moment(\"{}\")).{};\n</script>"
		return Markup(
			script.format(self.timestamp.strftime("%Y-%m-%dT%H:%M:%S Z"), format)
		)

	def format(self, fmt):
		return self.render("format(\"{}\")".format(fmt))

	def calendar(self):
		return self.render("calendar()")

	def fromNow(self):
		return self.render("fromNow()")

