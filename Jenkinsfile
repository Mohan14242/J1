@Library('mohan') _

pipeline {
    agent any
    
    parameters{
        booleanParam(name: 'ENABLE_DEBUG', defaultValue: false, description: 'Enable debug mode')
        string(name: 'ENVIRONMENT', defaultValue: 'production', description: 'Select environment: production, staging, or testing')
        choice(name: 'BROWSER', choices: ['Chrome', 'Firefox', 'Safari'], description: 'Select browser for testing')
        password(name: 'DB_PASSWORD', defaultValue: 'mohan123', description: 'Enter database password')
    }

    
    stages {
        stage('Example') {
            steps {
                script {
                    def prod_deply=params.ENABLE_DEBUG
                    def environment=params.ENVIRONMENT
                    def choice=params.BROWSER
                    def password=params.DB_PASSWORD
                    def maps=[prod_deply=${prod_deply},environment=${environment},choice=${BROWSER},password=${DB_PASSWORD}] 
                    mohan.names(maps)
                  
                    // Call the 'names' function from the 'mohan' shared library
                }
            }
        }
    }
}
