pipeline {
    agent any

    triggers {
        cron('H 22 * * *')
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/omkarawaregithub/aws-ec2-automation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install boto3
                '''
            }
        }

        stage('Stop EC2 Instances') {
            steps {
                sh 'python3 stop_ec2.py'
            }
        }
    }
}