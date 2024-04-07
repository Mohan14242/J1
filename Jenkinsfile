pipeline {
    agent any
    environment {
        SSH_CREDENTIALS = credentials('ssh-auth')
        SERVER_HOST = '3.81.211.54'
        SERVER_USER = 'centos'
    }
    stages {
        stage('Connect to Server') {
            steps {
                script {
                    sshagent(credentials: [SSH_CREDENTIALS]) {
                        sh "ssh -o StrictHostKeyChecking=no ${SERVER_USER}@${SERVER_HOST} 'echo Connected'"
                    }
                }
            }
        }
        // Additional stages
    }
}
