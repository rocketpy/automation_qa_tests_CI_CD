#  A list with examples of solved problems
# https://automated-testing.info/t/allure-podborka-tipichnyh-problem-voznikayushhih-v-proczesse-ispolzovaniya-i-ih-resheniya/20759


#  How creating a HTML report
"""
run Allure with command:  py.test EW.py --alluredir directory-with-results

В директории allure-commandline/bin/ выполняете allure generate directory-with-results/
Отчет в виде index.html сгенерится в allure-commandline/bin/allure-report/
Если же хочется поместить этот index.html куда-то в другое место, то выполняем
allure generate directory-with-results/ -o directory-where-u-want-indexhtmlreport-to-be-generated/

Нужно очищать папку allure-results

"""

#  Creating allure report with allure-cli and pytest
"""
# base command
allure serve path/to/allure-results

Локально вот так лучше сделать

py.test --alluredir reports
allure serve reports
Можно сделать вот так

py.test --alluredir reports
allure generate reports



Откройте отчет в Firefox
"""
