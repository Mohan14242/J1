@Library('mohan') _ // Load the shared library

pipeline {
    agent any

    stages {
        stage('Example') {
            steps {
                script {
                    def message = myFunction() // Calling the function from the shared library
                    echo message
                }
            }
        }
    }
}
