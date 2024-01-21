pipeline {
    agent any

    stages {
        stage('Build') {
            agent {
                label 'ansible'
            }
            steps {
                script {
                    git url: 'https://github.com/Mohan14242/jenkins2.git'
                    dir('jenkins2') {
                        // Add more Ansible commands or other build steps here if needed
                    }
                }
            }
        }

        stage("Testing Stage") {
            steps {
                script {
                    echo "This is Chiru. Who are you?"
                }
            }
        }
    }
}
