pipeline {
    agent {
        label 'python'
    }
    stages {
        stage('Entorno') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pip3 install pytest'
            }
        }
        stage('Descarga') {
            steps {
                git url: 'https://github.com/ThailyAguilar/Jenkins-python.git', branch: 'main'
            }
        }
        stage('Ejecutar') {
            steps {
                sh 'python3 conversor.py'
            }
        }
        stage('Probar') {
            steps {
                sh 'python -m pytest --junitxml=reports/results.xml'
            }
            post {
                always {
                    junit 'reports/results.xml'
                }
            }
        }
    }
}
