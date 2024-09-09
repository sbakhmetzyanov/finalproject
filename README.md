# Final project
## Запуск тестов:

** Необходимо, чтобы контейнеры докера opencart и jenkins работали в одной сети - selenoid 
### 1. Запуск opencart:

docker compose up -d

### 2. Запуск selenoid:

./cm selenoid start

### 3. Настройки jenkins: 

python3 -m venv venv

chmod +x venv/bin/activate

venv/bin/activate

venv/bin/pip3 install jsonschema 
venv/bin/pip3 install Faker
venv/bin/pip3 install -r requirements.txt
chown -R jenkins:jenkins /var/jenkins_home/workspace/jenkins/tests
chmod -R 755 /var/jenkins_home/workspace/jenkins/tests
./venv/bin/pytest tests_api
./venv/bin/pytest tests
