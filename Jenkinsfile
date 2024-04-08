pipeline {
    agent {
        label 'agent1'
    }
    stages {
        stage("Test Stage") {
            steps {
                script {
                    // Install npm dependencies
                    sh 'npm install'
                }
            }
        }
        stage("SonarQube Scanner") {
            steps {
                script {
                    // Run SonarQube scanner
                    withSonarQubeEnv('SonarQube') {
                        sh 'sonar-scanner'
                    }
                }
            }
        }
    }
}
