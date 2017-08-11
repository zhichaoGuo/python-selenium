import logging,os,time

class log_message:
	def __init__(self,title):
		self.day=time.strftime("%Y%m%d",time.localtime(time.time()))
		self.logger=logging.getLogger(title)
		self.logger.setLevel(logging.INFO)
		self.logfile=logging.FileHandler(r'C:\Users\Administrator\Desktop\te_blogf\lo\%s.log'%self.day)
		self.logfile.setLevel(logging.INFO)
		self.control=logging.StreamHandler()
		self.control.setLevel(logging.INFO)
		self.formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
		self.logfile.setFormatter(self.formatter)
		self.control.setFormatter(self.formatter)
		self.logger.addHandler(self.logfile)
		self.logger.addHandler(self.control)
	def debug_log(self,message):
		self.logger.debug(message)
	def info_log(self,message):
		self.logger.info(message)
	def ware_log(self,message):
		self.logger.ware(message)
	def error_log(self,message):
		self.logger.error(message)