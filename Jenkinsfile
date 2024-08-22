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
                sh 'python3 -m venv venv'
                sh '. $WORKSPACE/venv/bin/activate'
                sh 'pip install -r $WORKSPACE/requirements.txt'
            }
        }
        stage('Tests') {
            steps {
                sh 'python3 -m pytest --junitxml=$WORKSPACE/report.xml'
                junit 'report.xml'
            }
        }
    }
}