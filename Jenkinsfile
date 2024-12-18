pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/eduszabolcsfule/devops_CEVLCW.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest --maxfail=1 --disable-warnings -q'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('streamlit-app')
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.image('streamlit-app').run('-d -p 8501:8501')
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline futtatása befejeződött.'
        }
        success {
            echo 'Build sikeresen befejeződött!'
        }
        failure {
            echo 'A build során hiba történt!'
        }
    }
}

