pipeline {

    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Stop EC2 Instances') {
            steps {
                withCredentials([
                    [$class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'awscreds']
                ]) {
                sh '~/ec2-venv/bin/python stop_ec2.py'
                   }
            }
        }
    }
    post {

        success {
            echo 'EC2 stop process completed successfully.'
        }

        failure {
            echo 'EC2 stop process failed.'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}