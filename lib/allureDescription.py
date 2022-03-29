import allure

@allure.step('{Step}')
def use_allure_step(Step):
	pass


class AllureDescription:

	@staticmethod
	def add_step(title):
		use_allure_step(title)
