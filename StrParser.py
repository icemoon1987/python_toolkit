
class StrParser(object):
	'A simple parser that helps you to parse a string.'

	version = "0.1" # module version information

	def __init__(self):

		self.input_coding = "utf-8"
		self.output_coding = "utf-8"
		self.delimiter = "\t"
		self.trim_on_process = True
		self.throw_exception_on_process = False
		self.fields = "all"

		return

	def print_params(self):

		print "input_coding		=	", self.input_coding
		print "output_coding	=	", self.output_coding
		print "delimiter		=	\"%s\"" % self.delimiter
		print "trim_on_process	=	", self.trim_on_process
		print "throw_exception_on_process  =   ", self.throw_exception_on_process
		print "fields  =   ", self.fields

		return

	
	def parse_str(self, str_in):
		'Parse an input str'

		if len(self.fields) == 0:
			print "Warning: no fields specified!"
			return []

		try:
			str_decode = str_in.decode(self.input_coding)

			if self.trim_on_process:
				str_tmp = str_decode.strip()
			else:
				str_tmp = str_decode

			if str_tmp == "":
				return []

			tmp_list = str_tmp.split(self.delimiter)

			result = []

			if self.fields == "all" or self.fields == "All" or self.fields == "ALL":
				for item in tmp_list:
					if self.trim_on_process:
						field = item.strip()
					else:
						field = item 

					result.append(field.encode(self.output_coding))
					
			else:
				for field_num in self.fields:
					if self.trim_on_process:
						field = tmp_list[field_num].strip()
					else:
						field = tmp_list[field_num]

					result.append(field.encode(self.output_coding))

		except Exception, ex:
			if self.throw_exception_on_process:
				raise 
			else:
				print "Exception: ", str(ex)
				return False

		return result

