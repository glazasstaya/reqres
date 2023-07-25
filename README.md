# API-автотесты для reqres.in/
Учебный проект: API-тесты для песочницы https://reqres.in/

<!-- Технологии -->
## Использованы технологии:
<p  align="left">
  <code><img width="5%" title="Python" src="media/logo/python.png"></code>
  <code><img width="5%" title="Pycharm" src="media/logo/pycharm.png"></code>
  <code><img width="5%" title="Pytest" src="media/logo/pytest.png"></code>
  <code><img width="5%" title="Requests" src="media/logo/requests.png"></code>
  <code><img width="5%" title="Jenkins" src="media/logo/jenkins.png"></code>
  <code><img width="5%" title="Allure Report" src="media/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="media/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="media/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="media/logo/tg.png"></code>
</p>

<!-- Тест кейсы -->

## Автоматизировано тестирование API:
* get - single user
* get - list users
* post - create user
* put - update user
* delete - delete user

  Для всех API тестируется бизнес-логика, проверяются коды ответов и валидируется схема ответа.

## Запуск тестов в Jenkins
<p  align="left">
  <code><img width="5%" title="Jenkins" src="media/logo/jenkins.png"></code>
</p>

### [Jenkins](https://jenkins.autotests.cloud/job/005_tsgibneva_reqres_api_tests/)

#### Запуск тестов:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
  
##### При нажатии на "Собрать сейчас" тесты собираются из GitHub и начинается прохождение тестов.
<p  align="left">
  <code><img width="45%" title="Jenkins" src="media/screenshot/Jenkins.png"></code>
</p>

## В результате генерируется allure-отчет
<p  align="left">
  <code><img width="5%" title="Jenkins" src="media/logo/allure_report.png"></code>
</p>

### [Allure-report](https://jenkins.autotests.cloud/job/005_tsgibneva_reqres_api_tests/12/allure/)

##### Сводная информация по прогону тестов
<p  align="left">
  <code><img width="45%" title="Сводная информация в allure-report" src="media/screenshot/Allure_report1.png"></code>
</p>

##### Инфографика
<p  align="left">
  <code><img width="45%" title="Инфографика в allure-report" src="media/screenshot/Allure_report2.png"></code>
  <code><img width="45%" title="Инфографика в allure-report" src="media/screenshot/Allure_report3.png"></code>
</p>

##### Во вкладке Behavoirs тесты сгруппированы с точки зрения бизнес-логики, а attachments есть полная информация об отправленном запросе (время, curl, код ответа, дополнительные параметры) и ответ.
<p  align="left">
  <code><img width="45%" title="Результаты тестов в allure-report" src="media/screenshot/Allure_report4.png"></code>
</p>

## Настроена интеграция с Allure TestOps 
<p  align="left">
  <code><img width="5%" title="Allure TestOps" src="media/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="media/logo/jira.png"></code>
</p>

### [Allure TestOps](https://allure.autotests.cloud/project/3564/dashboards)
<p  align="left">
  <code><img width="45%" title="Дашборд в Allure Testops" src="media/screenshot/AllureTestOps1.png"></code>
  <code><img width="45%" title="Тест-кейсы в Allure Testops" src="media/screenshot/AllureTestOps2.png"></code>
</p>

### [Тикет в Jira](https://jira.autotests.cloud/browse/HOMEWORK-816)
<p  align="left">
  <code><img width="45%" title="Тикет в Jira" src="media/screenshot/jira.png"></code>
</p>



## По результату прогона отправляется уведомление в телеграм
<p  align="left">
  <code><img width="5%" title="Telegram" src="media/logo/tg.png"></code>
</p>

<p  align="left">
  <code><img width="30%" title="Telegram notification" src="media/screenshot/telegram-notification.png"></code>
</p>
