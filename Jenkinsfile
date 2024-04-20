@Library('mohan') _

pipeline {
    agent any
    
    parameters {
        booleanParam(name: 'ENABLE_DEBUG', defaultValue: false, description: 'Enable debug mode')
        string(name: 'ENVIRONMENT', defaultValue: 'production', description: 'Select environment: production, staging, or testing')
        choice(name: 'BROWSER', choices: ['Chrome', 'Firefox', 'Safari'], description: 'Select browser for testing')
        password(name: 'DB_PASSWORD', defaultValue: 'mohan123', description: 'Enter database password')
    }

    stages {
        stage('Example') {
            steps {
                script {
                    def prod_deploy = params.ENABLE_DEBUG
                    def environment = params.ENVIRONMENT
                    def choice = params.BROWSER
                    def password = params.DB_PASSWORD
                    def maps = [prod_deploy: prod_deploy, environment: environment, choice: choice, password: password]
                    chiru.names() // Call the 'names' function from the shared library
                }
            }
        }
    }
}
