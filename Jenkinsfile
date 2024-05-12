pipeline {
    agent {node { label '54.92.201.154'}}
    stages {
        stage("installing snyk") {
            steps {
                sh '''
                sudo yum install nodejs npm -y
                sudo curl https://static.snyk.io/cli/latest/snyk-linux -o snyk
                sudo chmod +x ./snyk 
                sudo mv ./snyk /usr/local/bin/ 
                sudo npm install -g snyk
                '''
            }
        }
        stage('snyk stage') {
            steps {
                withCredentials([string(credentialsId: 'snyk-auth', variable: 'SNYK_TOKEN')]) {
                    sh "snyk test --all-projects --json --org=mohan14242"
                }
            }
        }
    }
}
