all-tests:
	docker run --rm --mount type=bind,src=/home/nva/git/LearnQA_PythonAPI,target=/tests_project/ pytest_runner

allure_report:
	allure serve test_results/