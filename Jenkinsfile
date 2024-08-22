pipeline {
    agent any

    stages {
        stage('Clone source') {
            steps {
                git url: 'https://github.com/alex-pancho/aqa_py_290424', branch: 'main'
            }
        }
        stage('Build and activate venv') {
            steps {
                sh 'pip3 install -r $WORKSPACE/requirements.txt'
            }
        }
        stage('Tests') {
            steps {
                sh 'pytest -s --junitxml=$WORKSPACE/report.xml'
                junit 'report.xml'
            }
        }
    }
}