pipeline {
    agent {
       node { label 'agent1' }
    }
    stages {
        stage("Test Stage") {
            steps {
                script {
                    // Install npm dependencies
                    sh 'zip -r ./* --exculde=.git '
                }
            }
        }
        stage("SonarQube Scanner") {
            steps {
                script {
        
                        sh 'sonar-scanner'
                    }
                }
            }
        }
    }

