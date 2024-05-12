pipeline {
    agent any  
    stages {
        stage("installing snyk") {
            steps {
                sh '''
                sudo yum install nodejs npm -y
                sudo npm install -g snyk
                '''
            }
        }
        stage('snyk stage') {
            steps {
                withCredentials([string(credentialsId: 'snyk-api-token', variable: 'SNYK_TOKEN')]) {
                    sh "snyk test --all-projects --json --org=mohan14242"
                }
            }
        }
    }
}
