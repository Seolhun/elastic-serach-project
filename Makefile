# Variable
project_server := "app.py"
project_path := $(shell pwd)

# Target : Dependency
# 		Command
clean:
		find . -name \*.pyc -delete

db:
		python import_data.py

first-install:
		pip install -r requirements.txt && \
		cd $(project_path)/templates && npm install

first-run:
		mkdir $(project_path)/logs && python $(project_server) && cd $(project_path)/templates && npm run dev


back-install:
		pip install -r requirements.txt

back:
		python $(project_server)

front-install:
		cd $(project_path)/templates && npm install

front:
		cd $(project_path)/templates && npm run dev