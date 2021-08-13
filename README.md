# test_fabrica

```docker-compose up```  для запуска проекта, настроен 8000-ый порт

- для доступа ко всем активным опросам ```/survey/?active=True/```
- для доступа к вопросом одного опроса ```/question/?survey=.../```
- для доступа к пройденным опросам ```/survey/?interviewees=.../```
- для доступа к ответам на вопросы на опроса ```/passed_surveys/?survey=...&interviewee=.../```
